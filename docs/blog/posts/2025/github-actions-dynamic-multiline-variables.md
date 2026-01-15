---
title: Supporting dynamic multiline variables in GitHub Actions
description: >
  How to use dynamic multiline variables in GitHub Actions
icon: simple/json
status: new
draft: false
date:
  created: 2025-10-30
  updated: 2025-11-10
authors:
  - rwaight
categories:
  - GitHub Actions
  - CI/CD
  - DevOps
slug: github-actions-dynamic-multiline-variables
tags:
  - automation
  - coding
  - GitHub
  - JSON
  - Workflows
links:
  # All relative links are resolved from the docs directory.
  - resources/coding/jq-updating-json-objects.md
  - blog/posts/2025/jq-updating-json-objects.md
---

<!---  # Supporting dynamic multiline variables in GitHub Actions  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

One of the challenges when building reusable GitHub Actions workflows is handling multiline variables that need to be passed from configuration files to actions. This is particularly common when working with actions that require formatted input strings, like the `hashicorp/vault-action` which expects secrets in a specific multiline format.

In this post, I plan to store multiline variables in JSON arrays and dynamically load them in GitHub Actions workflows with support for prefixes to reduce duplication.

<!-- more -->

<!--- keep the 'more' entry above in place, the text above will become an 'excerpt' on the blog site
https://squidfunk.github.io/mkdocs-material/setup/setting-up-a-blog/#adding-an-excerpt --->


## What are we trying to solve?

Some GitHub Actions require multiline input in a specific format. For example:

```
path/to/resource1 key1 | OUTPUT_VAR1 ;
path/to/resource2 key2 | OUTPUT_VAR2 ;
path/to/resource3 key3 | OUTPUT_VAR3
```

When building reusable workflows, hardcoding these values directly in the workflow YAML creates several problems:

- ❌ **Not reusable** - Different projects need different values
- ❌ **Hard to maintain** - Changes require workflow modifications
- ❌ **Repetitive** - Common path prefixes are duplicated
- ❌ **Not project-specific** - Each project should define its own configuration


## A Possible Solution

A possible solution is to store these values in a JSON configuration file and dynamically load them at runtime. Additionally, we can support an optional prefix to reduce duplication when all entries share a common base path.

### Configuration Structure

We'll use a JSON structure with two fields:

1. **`prefix`** (optional) - A common base path prepended to all entries
2. **`entries`** (required) - An array of path strings

**With Prefix (Recommended):**
```json
{
  "config": {
    "prefix": "path/to/common/base/",
    "entries": [
      "service1/resource key1 | OUTPUT_VAR1",
      "service2/resource key2 | OUTPUT_VAR2",
      "service3/resource key3 | OUTPUT_VAR3"
    ]
  }
}
```

**Without Prefix (Full Paths):**
```json
{
  "config": {
    "entries": [
      "path/to/service1/resource key1 | OUTPUT_VAR1",
      "path/to/service2/resource key2 | OUTPUT_VAR2",
      "different/base/path/resource key3 | OUTPUT_VAR3"
    ]
  }
}
```

### Benefits of This Approach

✅ **Cleaner configuration** - No repeated paths when using prefix  
✅ **Project-specific** - Each project defines its own configuration  
✅ **Version controlled** - Configuration tracked in git  
✅ **Easy to maintain** - Change config file, not workflow  
✅ **Flexible** - Works with or without prefix  

## Implementation

### Step 1: Create Your Configuration File

Create a file like `project-config.json`:

```json
{
  "project_name": "my-project",
  "version": "1.0.0",
  "config": {
    "prefix": "path/to/common/base/",
    "entries": [
      "service1/resource key1 | SERVICE1_VAR",
      "service2/resource key2 | SERVICE2_VAR",
      "service3/resource key3 | SERVICE3_VAR",
      "api/endpoint key | API_KEY"
    ]
  }
}
```

### Step 2: Add Preparation Step to Your Workflow

Before using the multiline variable, add a step to read and format it:

```yaml
- name: Prepare multiline variable from config
  id: prepare-config
  env:
    CONFIG_FILE: ${{ inputs.CONFIG_FILE || './project-config.json' }}
    JSON_PATH_ENTRIES: '.config.entries'
    JSON_PATH_PREFIX: '.config.prefix'
  run: |
    echo "Reading configuration from: $CONFIG_FILE"
    
    # Check if entries exist in the config file
    if jq -e "${JSON_PATH_ENTRIES}" "$CONFIG_FILE" > /dev/null 2>&1; then
      echo "✓ Found entries at ${JSON_PATH_ENTRIES}"
      
      # Check if a prefix is defined
      PREFIX=""
      if jq -e "${JSON_PATH_PREFIX}" "$CONFIG_FILE" > /dev/null 2>&1; then
        PREFIX=$(jq -r "${JSON_PATH_PREFIX}" "$CONFIG_FILE")
        if [[ -n "$PREFIX" && "$PREFIX" != "null" ]]; then
          echo "✓ Using prefix: $PREFIX"
        fi
      fi
      
      # Build the multiline variable with or without prefix
      if [[ -n "$PREFIX" && "$PREFIX" != "null" ]]; then
        # Prepend prefix to each entry
        FORMATTED_OUTPUT=$(jq -r "${JSON_PATH_ENTRIES} | map(\"${PREFIX}\" + .) | join(\" ;\\n\")" "$CONFIG_FILE")
      else
        # Use entries as-is
        FORMATTED_OUTPUT=$(jq -r "${JSON_PATH_ENTRIES} | join(\" ;\\n\")" "$CONFIG_FILE")
      fi
      
      # Ensure it ends with a semicolon
      if [[ ! "$FORMATTED_OUTPUT" =~ \;[[:space:]]*$ ]]; then
        FORMATTED_OUTPUT="${FORMATTED_OUTPUT} ;"
      fi
    else
      echo "✗ Error: entries not found at ${JSON_PATH_ENTRIES}"
      exit 1
    fi
    
    # Store in output using multiline heredoc
    echo "output<<EOF" >> $GITHUB_OUTPUT
    echo "$FORMATTED_OUTPUT" >> $GITHUB_OUTPUT
    echo "EOF" >> $GITHUB_OUTPUT
```

### Step 3: Use the Dynamic Output

Now you can use the formatted multiline variable in your action:

```yaml
- name: Use the multiline variable
  uses: some-action/that-needs-multiline@v1
  with:
    formatted_input: ${{ steps.prepare-config.outputs.output }}
```

## How It Works

### Transformation Process

The workflow step uses `jq` (JSON processor) to:

1. **Read the prefix** (if defined) from the JSON file
2. **Read the entries array** from the JSON file
3. **Prepend the prefix** to each entry using `jq`'s `map()` function
4. **Join entries** with semicolons and newlines
5. **Store as multiline output** using GitHub Actions heredoc syntax

### Visual Flow

```
JSON Configuration
├── prefix: "path/to/common/base/"
└── entries: [
    "service1/resource key | VAR1",
    "service2/resource key | VAR2"
]

↓ [jq processes the JSON]

Step 1: Extract prefix
├── PREFIX = "path/to/common/base/"

Step 2: Map prefix to each entry
├── jq: map("${PREFIX}" + .)

Step 3: Join with semicolons
├── jq: join(" ;\n")

↓ [Output formatted string]

path/to/common/base/service1/resource key | VAR1 ;
path/to/common/base/service2/resource key | VAR2
```

## Other Features

### Configurable JSON Paths

You can customize where entries are stored by setting environment variables:

```yaml
env:
  JSON_PATH_ENTRIES: '.custom.path.to.entries'
  JSON_PATH_PREFIX: '.custom.path.to.prefix'
```

This allows you to store configuration anywhere in your JSON structure:

```json
{
  "custom": {
    "path": {
      "to": {
        "prefix": "common/base/",
        "entries": ["item1", "item2"]
      }
    }
  }
}
```

### Backward Compatibility

You can add fallback logic to support multiple configuration formats:

```yaml
run: |
  # Try new format
  if jq -e '.config.entries' "$CONFIG_FILE" > /dev/null 2>&1; then
    # Process new format
    ...
  # Try legacy format
  elif jq -e '.legacy_entries' "$CONFIG_FILE" > /dev/null 2>&1; then
    # Process legacy format
    FORMATTED_OUTPUT=$(jq -r '.legacy_entries | join(" ;\n")' "$CONFIG_FILE")
  else
    # Use hardcoded defaults
    FORMATTED_OUTPUT="default/path key | DEFAULT"
  fi
```

### Workflow Inputs for Testing

Add workflow inputs to test different configurations easily:

```yaml
on:
  workflow_dispatch:
    inputs:
      config_file:
        description: 'Path to configuration file'
        default: './project-config.json'
        required: false
        type: string
      json_path_entries:
        description: 'JSON path to entries array'
        default: '.config.entries'
        required: false
        type: string
      json_path_prefix:
        description: 'JSON path to optional prefix'
        default: '.config.prefix'
        required: false
        type: string
```

## Complete Working Example

Here's a complete reusable workflow example:

```yaml
name: Reusable Workflow with Dynamic Config

on:
  workflow_call:
    inputs:
      CONFIG_FILE:
        description: 'Path to JSON configuration file'
        default: './project-config.json'
        required: true
        type: string

jobs:
  process-dynamic-config:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Prepare multiline variable from config
        id: prepare-config
        env:
          CONFIG_FILE: ${{ inputs.CONFIG_FILE }}
          JSON_PATH_ENTRIES: '.config.entries'
          JSON_PATH_PREFIX: '.config.prefix'
        run: |
          echo "Reading configuration from: $CONFIG_FILE"
          
          if jq -e "${JSON_PATH_ENTRIES}" "$CONFIG_FILE" > /dev/null 2>&1; then
            echo "✓ Found entries at ${JSON_PATH_ENTRIES}"
            
            PREFIX=""
            if jq -e "${JSON_PATH_PREFIX}" "$CONFIG_FILE" > /dev/null 2>&1; then
              PREFIX=$(jq -r "${JSON_PATH_PREFIX}" "$CONFIG_FILE")
              if [[ -n "$PREFIX" && "$PREFIX" != "null" ]]; then
                echo "✓ Using prefix: $PREFIX"
              fi
            fi
            
            if [[ -n "$PREFIX" && "$PREFIX" != "null" ]]; then
              FORMATTED_OUTPUT=$(jq -r "${JSON_PATH_ENTRIES} | map(\"${PREFIX}\" + .) | join(\" ;\\n\")" "$CONFIG_FILE")
            else
              FORMATTED_OUTPUT=$(jq -r "${JSON_PATH_ENTRIES} | join(\" ;\\n\")" "$CONFIG_FILE")
            fi
            
            [[ ! "$FORMATTED_OUTPUT" =~ \;[[:space:]]*$ ]] && FORMATTED_OUTPUT="${FORMATTED_OUTPUT} ;"
          else
            echo "✗ Error: entries not found"
            exit 1
          fi
          
          echo "output<<EOF" >> $GITHUB_OUTPUT
          echo "$FORMATTED_OUTPUT" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: Display formatted output
        run: |
          echo "Formatted multiline variable:"
          echo "${{ steps.prepare-config.outputs.output }}"

      - name: Use with an action
        uses: hashicorp/vault-action@v3
        with:
          # Example: the vault-action expects this specific format
          secrets: ${{ steps.prepare-config.outputs.output }}
```

### Calling the Reusable Workflow

```yaml
name: My Project Build

on:
  push:
    branches: [main]

jobs:
  build:
    uses: ./.github/workflows/reusable-workflow.yml
    with:
      CONFIG_FILE: './my-project-config.json'
```

## Key Techniques

### Multiline Output in GitHub Actions

GitHub Actions uses heredoc syntax for multiline outputs:

```bash
echo "output<<EOF" >> $GITHUB_OUTPUT
echo "$MULTILINE_CONTENT" >> $GITHUB_OUTPUT
echo "EOF" >> $GITHUB_OUTPUT
```

This preserves newlines and special characters in the output.

### JQ Map Function

The `map()` function in `jq` transforms each element in an array:

```bash
# Input: ["item1", "item2"]
jq -r '.entries | map("PREFIX" + .) | join(" ;\n")'
# Output: PREFIXitem1 ;
#         PREFIXitem2
```

### JSON Processing with jq

Key `jq` operations used:

- `jq -e` - Exit with status based on expression result (for testing existence)
- `jq -r` - Raw output (without JSON quotes)
- `map()` - Transform each array element
- `join()` - Concatenate array elements with separator

## Testing and Debugging

### Enable Debug Mode

Add a debug step to see the formatted output:

```yaml
- name: Debug - Show formatted output
  if: runner.debug == '1'
  run: echo "${{ steps.prepare-config.outputs.output }}"
```

Run with debug logging:

```bash
gh workflow run my-workflow.yml --debug
```

### Validate Configuration Locally

Test your JSON transformation locally before running in CI:

```bash
# Test reading entries
jq '.config.entries' project-config.json

# Test with prefix
jq -r '.config.entries | map("PREFIX" + .) | join(" ;\n")' project-config.json

# Full test
PREFIX=$(jq -r '.config.prefix' project-config.json)
jq -r ".config.entries | map(\"${PREFIX}\" + .) | join(\" ;\\n\")" project-config.json
```

## Best Practices

1. **Use prefix for cleaner configs** - If most entries share a common base path, use the prefix feature
2. **Validate JSON syntax** - Use a JSON validator or `jq` to verify your config files
3. **Add error handling** - Include fallbacks for missing configuration
4. **Document your format** - Add comments in your JSON explaining the structure
5. **Test locally first** - Validate transformations with `jq` before running in CI
6. **Use workflow inputs** - Make paths configurable for flexibility
7. **Version your configs** - Track configuration changes in git

## Use Cases

This pattern is useful when you need to:

- Pass formatted lists to GitHub Actions that require specific input formats
- Maintain project-specific configurations for reusable workflows
- Reduce duplication in configuration files
- Support multiple projects with different requirements
- Keep workflows DRY (Don't Repeat Yourself)
- Version control your workflow configurations

## Conclusion

By storing multiline variables in JSON arrays and processing them with `jq`, you can build highly flexible and reusable GitHub Actions workflows. The optional prefix feature significantly reduces duplication and makes configurations easier to read and maintain.

This approach is particularly powerful for:

- **Reusable workflows** - One workflow, many projects
- **Configuration-driven pipelines** - Change config, not code
- **Maintainability** - Centralized, version-controlled configuration
- **Flexibility** - Works with or without prefixes

The key takeaways:

1. Store configuration in JSON for easy parsing
2. Use `jq` to transform and format data
3. Leverage GitHub Actions heredoc for multiline outputs
4. Add prefix support to reduce duplication
5. Include fallbacks for backward compatibility

With this pattern, your GitHub Actions workflows become more maintainable, flexible, and easier to reuse across multiple projects.

---

### References

**Resources**:

- [GitHub Actions: Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [jq Manual](https://stedolan.github.io/jq/manual/)
- [GitHub Actions: Reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [GitHub Actions: Setting outputs](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#multiline-strings)


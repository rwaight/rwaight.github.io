---
title: Multi-line strings in YAML
description: >
  There are many different ways to write multi-line strings in YAML
date:
  created: 2025-07-23
  updated: 2025-07-23
authors:
  - rwaight
tags:
  - YAML
  - coding
  - Resource
---

<!---  # Multi-line strings in YAML  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

!!! quote "Content Source" 

    This content is from [this _wonderful answer_ from stackoverflow](https://stackoverflow.com/a/21699210).


There are <s>5</s> *<s>6</s>* ***NINE*** (or 63\*, depending how you count) different ways to write multi-line strings in YAML.

### TL;DR

- Use `>` if you want to break a string up for readability but for it to still be treated as a single-line string: interior line breaks will be stripped out, there will only be one line break at the end:

```yml
        key: >
          Your long
          string here.
```

- Use `|` if you want those line breaks to be preserved as `\n` (for instance, embedded markdown with paragraphs).

```yml
        key: |
          ### Heading
      
          * Bullet
          * Points
```

- Use `>-` or `|-` instead if you don't want a line break appended at the end.

- Use `""` if you need to split lines in the middle of words or want to literally type line breaks as `\n`:

```yml
        key: "Antidisestab\
         lishmentarianism.\n\nGet on it."
```

- YAML is crazy.

### Block scalar styles (`>`, `|`)

These allow characters such as `\` and `"` without escaping, and add a new line (`\n`) to the end of your string.

`>` [_Folded style_](https://yaml.org/spec/1.2.2/#813-folded-style) removes single newlines within the string (but adds one at the end, and converts double newlines to singles):

```yml
    Key: >
      this is my very very very
      long string
```

→ `this is my very very very long string\n`

Extra leading space is retained and causes extra newlines. See note below.

Advice: Use this. Usually this is what you want.

`|` [_Literal style_](https://yaml.org/spec/1.2.2/#literal-style)
turns every newline within the string into a literal newline, and adds one at the end:

```yml
    Key: |
      this is my very very very 
      long string
```

→ `this is my very very very\nlong string\n`

Here's the official definition from the [YAML Spec 1.2.2](https://yaml.org/spec/1.2.2/#23-scalars)

> Scalar content can be written in block notation, using a literal style (indicated by “|”) where all line breaks are significant. Alternatively, they can be written with the folded style (denoted by “\>”) where each line break is folded to a space unless it ends an empty or a more-indented line.

Advice: Use this for inserting *formatted text* (especially Markdown) as a value.

### Block styles with block chomping indicator (`>-`, `|-`, `>+`, `|+`)

You can control the handling of the final new line in the string, and any trailing blank lines (`\n\n`) by adding a [block chomping indicator](https://yaml.org/spec/1.2.2/#8112-block-chomping-indicator) character:

- `>`, `|`: "clip": keep the line feed, remove the trailing blank lines.
- `>-`, `|-`: "strip": remove the line feed, remove the trailing blank lines.
- `>+`, `|+`: "keep": keep the line feed, keep trailing blank lines.

### "Flow" scalar styles (` `, `"`, `'`)

These have limited escaping, and construct a single-line string with no new line characters. They can begin on the same line as the key, or with additional newlines first, which are stripped. Doubled newline characters become one newline.

[_plain style_](https://yaml.org/spec/1.2.2/#733-plain-style) (no escaping, no ` #` or `: ` combinations, first character can't be `"`, `'` or many other punctuation characters ):

```yml
    Key: this is my very very very 
      long string
```

Advice: Avoid. May look convenient, but you're liable to shoot yourself in the foot by accidentally using forbidden punctuation and triggering a syntax error.

[_double-quoted style_](https://yaml.org/spec/1.2.2/#double-quoted-style) (`\` and `"` must be escaped by `\`, newlines can be inserted with a literal `\n` sequence, lines can be concatenated without spaces with trailing `\`):

```yml
    Key: "this is my very very \"very\" loooo\
      ng string.\n\nLove, YAML."
```

→ `"this is my very very \"very\" loooong string.\n\nLove, YAML." `

Advice: Use in very specific situations. This is the only way you can break a very long token (like a URL) across lines without adding spaces. And maybe adding newlines mid-line is conceivably useful.

[_single-quoted style_](https://yaml.org/spec/1.2.2/#single-quoted-style) (literal `'` must be doubled, no special characters, possibly useful for expressing strings starting with double quotes):

```yml
    Key: 'this is my very very "very"
      long string, isn''t it.'
```

→ `"this is my very very \"very\" long string, isn't it."`

Advice: Avoid. Very few benefits, mostly inconvenience.

### Block styles with indentation indicators

Just in case the above isn't enough for you, you can add a "[block indentation indicator](https://yaml.org/spec/1.2.2/#8111-block-indentation-indicator)" (after your block chomping indicator, if you have one):

```yml
    - >8
            My long string
            starts over here
    - |+1
     This one
     starts here
```

### Note: Leading spaces in Folded style (`>`)

If you insert extra spaces at the start of not-the-first lines in Folded style, they will be kept, with a bonus newline. (This doesn't happen with flow styles.) [Section 6.5](https://yaml.org/spec/1.2.2/#65-line-folding) says:

> In addition, folding does not apply to line breaks surrounding text lines that contain leading white space. Note that such a more-indented line may consist only of such leading white space.

```yml
    - >
        my long
          string
                        
        many spaces above
    - my long
          string
                        
        many spaces above
```

→ `["my long\n  string\n                \nmany spaces above\n","my long string\nmany spaces above"]`

## Summary

In this table: `_` means `space character`, `\n` means "newline character" except were noted. "Leading space" refers to an additional space character on the second line, when the first is only spaces (which establishes the indent).

|                          | `>`  | `|`  | `>-` | `|-` | `>+` | `|+` |     | `"` | `'` |
|--------------------------|------|------|-----|-----|-----|------|------|------|------|  
| **Spaces/newlines converted to:**
| Trailing space →        | \_    | \_    | \_    | \_    | \_    | \_    |     |     |     |
| Leading space  →        | \\n\_  | \\n\_  | \\n\_  | \\n\_  | \\n\_  | \\n\_  |     |     |     |
| Single newline →        | \_    | \\n   | \_    | \\n   |  \_   | \\n   | \_   | \_   | \_   |
| Double newline →        | \\n   | \\n\\n | \\n   | \\n\\n |  \\n  | \\n\\n | \\n  | \\n  | \\n  |
| Final newline  →        | \\n   | \\n   |      |      |  \\n  | \\n   |     |     |     |
| Final double newline →  | \\n   | \\n   |      |      | \\n\\n | \\n\\n |     |     |     |
| **How to create a literal:**
| Single quote             | '    | '    | '    | '    | '    | '    | '   | '   | ''  |
| Double quote             | "    | "    | "    | "    | "    | "    | "   | \\" | "   |
| Backslash                | \\    | \\    | \\    | \\    | \\    | \\    | \\   | \\\\ | \\   |
| **Other features**
| In-line newlines with literal `\n` | 🚫 | 🚫   | 🚫   | 🚫   | 🚫   | 🚫   | 🚫  | ✅ | 🚫  |
| Spaceless newlines with `\`| 🚫 | 🚫   | 🚫   | 🚫   | 🚫   | 🚫   | 🚫  | ✅ | 🚫  |
| ` #` or `: ` in value    | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | 🚫  | ✅  | ✅  |
| Can start on same  
line as key | 🚫   | 🚫   | 🚫   | 🚫   | 🚫   | 🚫 | ✅ | ✅ | ✅ |

## Examples

*Note the trailing spaces on the line before "spaces."*

```yml
    - >
      very "long"
      'string' with
    
      paragraph gap, \n and        
      spaces.
    - | 
      very "long"
      'string' with
    
      paragraph gap, \n and        
      spaces.
    - very "long"
      'string' with
    
      paragraph gap, \n and        
      spaces.
    - "very \"long\"
      'string' with
    
      paragraph gap, \n and        
      s\
      p\
      a\
      c\
      e\
      s."
    - 'very "long"
      ''string'' with
    
      paragraph gap, \n and        
      spaces.'
    - >- 
      very "long"
      'string' with
    
      paragraph gap, \n and        
      spaces.
    
    [
      "very \"long\" 'string' with\nparagraph gap, \\n and         spaces.\n", 
      "very \"long\"\n'string' with\n\nparagraph gap, \\n and        \nspaces.\n", 
      "very \"long\" 'string' with\nparagraph gap, \\n and spaces.", 
      "very \"long\" 'string' with\nparagraph gap, \n and spaces.", 
      "very \"long\" 'string' with\nparagraph gap, \\n and spaces.", 
      "very \"long\" 'string' with\nparagraph gap, \\n and         spaces."
    ]
```

_`*`2 block styles, each with 2 possible block chomping indicators (or none), and with 9 possible indentation indicators (or none), 1 plain style and 2 quoted styles: 2 x (2 + 1) x (9 + 1) + 1 + 2 = 63_

Some of this information has also been summarised [here](https://yaml-multiline.info/).

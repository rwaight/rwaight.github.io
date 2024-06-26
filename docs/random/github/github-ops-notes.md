---
title: GitHub Ops Notes
date:
  created: 2023-10-03
  updated: 2024-06-25
authors:
  - rwaight
#slug: github-ops-notes
tags:
  - GitHub
  - GitHub/Actions
  - GitHub/cli
---

# GitHub Ops Notes


### Deleting Workflow Runs

https://docs.github.com/en/actions/managing-workflow-runs/deleting-a-workflow-run

using the command line, `cd` to the repo folder, then issue `gh run list` to see the last 20 workflows

Also the following:
- See a specific workflow: `gh run list -w workflow_file.yml`
- Specific workflow, date, and event: 
    - `gh run list -w pk-ami-builder.yml --created 2023-10-02 -e pull_request`
    - `gh run list -w pk-ami-builder.yml --created 2023-10-02 --event pull_request`

```bash
gh run list -w workflow_file.yml --json databaseId  -q '.[].databaseId' |
  xargs -IID gh api \
    "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/ID" \
    -X DELETE
```

Also see https://blog.oddbit.com/post/2022-09-22-delete-workflow-runs/:
```bash
gh run list --json databaseId  -q '.[].databaseId' |
  xargs -IID gh api \
    "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/ID" \
    -X DELETE
```


### GitHub Actions actions/script

- Pass parameters to script: https://github.com/actions/github-script/issues/56
- Multiline comment: https://github.com/actions/github-script/issues/401
- Create workflowDispatch: https://github.com/actions/github-script/issues/298


#### Multiline comments

Option 1: 
- See https://stackoverflow.com/questions/70628889/get-github-rest-issues-createcomment-to-use-an-environment-variable-for-multi

```yaml
name: GitHub Actions Test Multi-line
on:
  pull_request:
    branches:
      - Dev
jobs:
  Run-check-references:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0

      - run: |
          SCRIPT_OUTPUT=$(cat << EOF
          first line
          second line
          third line
          EOF
          )
          echo "SCRIPT_OUTPUT<<EOF" >> $GITHUB_ENV
          echo "$SCRIPT_OUTPUT" >> $GITHUB_ENV
          echo "EOF" >> $GITHUB_ENV

      - run: |
          echo "${{env.SCRIPT_OUTPUT}}"
          echo $SCRIPT_OUTPUT

      - uses: actions/github-script@v5
        with:
          github-token: ${{secrets.GITHUB_TOKEN}}
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `${{env.SCRIPT_OUTPUT}}`
            })

```

Option 2:
- See https://github.com/actions/github-script/issues/220#issuecomment-1045972871

```yaml
  - name: Plan Output
    uses: actions/github-script@v6
    if: github.event_name == 'pull_request'
    env:
      PLAN: "terraform\n${{ steps.plan.outputs.stdout }}"
    with:
      github-token: ${{ secrets.GITHUB_TOKEN }}
      script: |
        const output = `## Terraform Prod Infra Plan
        #### Terraform Initialization \`${{ steps.init.outcome }}\`
        #### Terraform Validation \`${{ steps.validate.outcome }}\`
        #### Terraform Plan \`${{ steps.plan.outcome }}\`
        
        <details><summary>Show Plan</summary>
        ${process.env.PLAN}
        </details>

        *Pusher: @${{ github.actor }}, Action: \`${{ github.event_name }}\`*`;

        github.rest.issues.createComment ({
          issue_number: context.issue.number,
          owner: context.repo.owner,
          repo: context.repo.repo,
          body: output
        })
```

#### Troubleshooting comments

https://github.com/actions/github-script/issues/220#issuecomment-988937148
```yaml
      - name: Comment on PR
        uses: actions/github-script@v5
        if: failure()
        with:
          script: |
            console.log(JSON.stringify(context.issue))
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: "foo"
            })
```


## End
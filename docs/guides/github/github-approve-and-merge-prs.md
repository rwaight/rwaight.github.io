---
title: Approving and merging multiple pull requests using the gh cli
draft: false 
date:
  created: 2024-11-08
  updated: 2025-02-01
authors:
  - rwaight
categories:
  - GitHub
tags:
  - GitHub
  - GitHub/CLI
  - Automation
  - NeedToStandardizeTags
---

<!--- ## Approving and merging multiple PRs --->

You can use the **GitHub CLI** with **PowerShell** or **bash** to approve and merge multiple pull requests.  

### Merging multiple PRs with bash

The Bash example is:
```bash
# create the array
pr_array=(
"https://github.com/rwaight/actions/pull/36"
"https://github.com/rwaight/test-actions/pull/43"
"https://github.com/rwaight/rwaight.github.io/pull/20"
)

for pr in ${pr_array[@]}; do
  echo "Processing PR $pr ... "
  gh pr review --approve $pr
  echo "    PR approved ... "
  read -p "    Press enter to continue ... "
  gh pr merge -s -d $pr
  echo "    PR merged ... "
  read -p "    Press enter to continue ... "
done
```

### Merging multiple PRs with PowerShell

The PowerShell example is:
```powershell
# create the array
$pr_array = @(
"https://github.com/rwaight/actions/pull/36",
"https://github.com/rwaight/test-actions/pull/43",
"https://github.com/rwaight/rwaight.github.io/pull/20"
)

foreach ($pr in $pr_array) {
  Write-Host "Processing PR $pr ... "
  gh pr review --approve $pr
  Write-Host "    PR approved ... " -NoNewLine
  Pause
  gh pr merge -s -d $pr
  Write-Host "    PR merged ... " -NoNewLine
  Pause
}
```


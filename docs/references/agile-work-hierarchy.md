---
title: Agile Work Hierarchy Reference
description: >
  A working reference of how our team defines and uses tasks, stories, epics, and initiatives.
date:
  created: 2025-06-18
  updated: 2025-06-18
tags:
  - Agile
  - Kanban
  - Scrum
  - project-management
  - distributed-teams
  - team-practices
  - terminology
---

<!--- Do not use a H1 element when the title is set in the frontmatter --->
<!--- # Agile Work Hierarchy Reference --->


## Work Item Definitions

### 🧱 Task

- Smallest unit of execution.
- Represents **how** something gets done.
- Tied directly to one Story.
- Examples: Implement API endpoint, write unit tests, update stylesheets.

### 📗 Story

- Represents the **what** and **why**.
- Contains user requirements and acceptance criteria.
- May contain multiple Tasks.
- Follows user story format: *"As a [user], I want [goal], so that [reason]."*

### 📘 Epic

- A collection of related Stories.
- Often spans multiple sprints.
- Helps organize broader features or capabilities.

### 🗂 Initiative

- Strategic goal involving multiple Epics.
- Aligned with business objectives or large-scale project phases.

---

## Work Tracking Model

```text
Initiative → Epic → Story → Task
```

- **Initiatives** group Epics across teams.
- **Epics** organize related Stories.
- **Stories** define outcomes and value.
- **Tasks** show specific technical steps.


<!---  ### 🧩 Work Item Hierarchy Overview  --->

??? abstract "Work Item Hierarchy Overview"

    Here is the **Work Item Hierarchy Overview**:

    ```mermaid
    graph TD
        subgraph Initiative 1
            I1E1[Epic]
            I1E2[Epic]
            I1S1["Story: 'What?' & 'Why?'"]
            I1S2["Story: 'What?' & 'Why?'"]
            I1T1["Task: 'How?'"]
            I1T2["Task: 'How?'"]
            I1T3["Task: 'How?'"]
            I1T4["Task: 'How?'"]
            I1E1 --> I1S1
            I1E2 --> I1S2
            I1S1 --> I1T1
            I1S1 --> I1T2
            I1S2 --> I1T3
            I1S2 --> I1T4
        end

        Initiative1[Initiative 1] --> I1E1
        Initiative1 --> I1E2
    ```


---

## Key Differentiator

> **Stories = What & Why** (Requirements & Acceptance Criteria)\
> **Tasks = How** (Implementation to prove the requirements are met)

This reference may be updated as our workflow evolves.


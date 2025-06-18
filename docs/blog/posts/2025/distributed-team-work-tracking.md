---
title: Work tracking in a distributed team
draft: true
date:
  created: 2025-06-17
  updated: 2025-06-18
authors:
  - rwaight
categories:
  - Agile
#slug: work-tracking-in-a-distributed-team
tags:
  - Agile
  - Kanban
  - Scrum
---


???+ note

    While this document is ***not in draft mode*** it is definitely not complete...

<!--- ## Work Tracking --->

As mentioned in the [_Using Scrumban in a distributed team_](./distributed-team-using-scrumban.md) post, using Sprints to plan and define the work that will be completed can be extremely helpful in a distributed team. 
There _should be_ a formally established process to follow in order to help everyone understand expectations. 
In this scenario, we can find out how we can use [GitHub issues to plan and track work][01] which can be helpful given the [recent changes the GitHub team is making to issues and projects][02].

<!--- 
References for later:

- https://www.atlassian.com/agile/scrum/sprint-planning
- https://www.atlassian.com/software/jira/templates/sprint-backlog
- https://www.atlassian.com/agile/project-management/workflow
- https://www.atlassian.com/agile/project-management/epics-stories-themes
- https://medium.com/agile-adapt/how-to-plan-your-agile-projects-with-epics-and-milestones-d80287ca730e

--->

### Agile Project Management Terminology

<!--- from https://www.atlassian.com/agile/project-management/epics-stories-themes --->

What are stories, epics, and initiatives? (from [`atlassian.com`][11])

- [**Stories**][12], also called “user stories,” are short requirements or requests written from the perspective of an end user.
- [**Epics**][13] are large bodies of work that can be broken down into a number of smaller tasks (called stories).
- **Initiatives** are collections of epics that drive toward a common goal.


```mermaid
flowchart TD
    %% the preview is rendering the bottom
    %% subgraph first, so switching them here
    subgraph Initiative 2
        I2E1[Epic C]
        I2E2[Epic D]
        I2S1[Story C1]
        I2S2[Story D1]
        I2E1 --> I2S1
        I2E2 --> I2S2
    end

    subgraph Initiative 1
        I1E1[Epic A]
        I1E2[Epic B]
        I1S1[Story A1]
        I1S2[Story B1]
        I1E1 --> I1S1
        I1E2 --> I1S2
    end

    Initiative1[Initiative 1] --> I1E1
    Initiative1 --> I1E2
    Initiative2[Initiative 2] --> I2E1
    Initiative2 --> I2E2
```


<!--- ## End --->

[01]: https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/planning-and-tracking-work-for-your-team-or-project
[02]: https://github.blog/changelog/2025-04-09-evolving-github-issues-and-projects/
[11]: <https://www.atlassian.com/agile/project-management/epics-stories-themes> "Stories, epics, and initiatives"
[12]: https://www.atlassian.com/agile/project-management/user-stories
[13]: https://www.atlassian.com/agile/project-management/epics
[90]: https://www.atlassian.com/agile/project-management/workflow
[91]: https://www.atlassian.com/software/jira/templates/sprint-backlog
[92]: https://medium.com/agile-adapt/how-to-plan-your-agile-projects-with-epics-and-milestones-d80287ca730e


<!--- [999]: https://asana.com/resources/what-is-scrum --->

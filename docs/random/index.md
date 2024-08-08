---
title: Random pages index page
date:
  created: 2024-06-25
  updated: 2024-08-08
---

# Random pages index page

### Dark mode in chromium browsers

If you love dark mode for everything... you can enable **Auto Dark Mode for Web Contents**. In `chrome://flags/`, search for **Dark Mode**.

Referenced from [How do I set Google Calendar to Dark Mode?](https://support.google.com/calendar/thread/9762643?hl=en&msgid=37038653)
> turn on the flag **Force Dark Mode for Web Contents**
> you can do this by going to `chrome://flags/` and searching for it


### Random GitHub Notes

See the [random GitHub notes page](github/random-github-notes.md) for some random info.


### Running an Ubuntu container to test bash commands

If you want to use a specific version of Linux to run `bash`, you can create a container (for example, ubuntu) using:
```bash
docker run -dt --name ubuntu-temp ubuntu:22.04
```

Then you can access `bash` in the ubuntu container using:
```bash
docker exec -it ubuntu-temp /bin/bash
```

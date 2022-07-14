# Automation [![Python Version](https://img.shields.io/badge/python-3.6.1-brightgreen.svg?)](https://www.python.org/downloads/)

Collection of automated tasks.

> **Disclaimer**: Some of the scripts are small and may not be very useful such as [Open-essentials](https://github.com/endormi/automation/blob/master/open-essentials/essentials.py) and [Send-email](https://github.com/endormi/automation/blob/master/send-email/email.py), but are still pretty cool :).

> You might be wondering why I decided to keep [Expenses](https://github.com/endormi/automation/blob/master/expenses/expenses.py) and [Income](https://github.com/endormi/automation/blob/master/income/income.py) separate, it's just my personal preference.

> I created some of the scripts with the intention that they're a foundation for more complex automated scripts such as. expenses, income, selenium-testing and a few more. The files that are these types of scripts will have (X).

Clone repository:

```
git clone https://github.com/endormi/automation.git
```

Install requirements:

```sh
pip install -r requirements.txt
```

Now you can run every script.

- [DL-file](https://github.com/endormi/automation/blob/master/dl-file/dl.py) - X - File downloader.
- [Expenses](https://github.com/endormi/automation/blob/master/expenses/expenses.py) - X - Adds business and personal expenses to Excel (Currently has only one `.py` file, but I will be adding more later. Current code needs you to add the expenses manually, but will automatically add them to Excel. Not ideal I know, I'll be adding a better code when I have time). This is only a foundation for your excel files, which you can then update to your own liking.
- [Graph](https://github.com/endormi/automation/blob/master/graph/excel.py) - X - Excel graph.
- [Hue-light](https://github.com/endormi/automation/blob/master/hue-light/control.py) - X - Control hue lights.
- [Git-commands](https://github.com/endormi/automation/blob/master/git-commands/commands.py) - Automates the process of using commands such as clone, commit, branch, pull, merge, blame and stash.
- [Income](https://github.com/endormi/automation/blob/master/income/income.py) - X - Adds income to Excel (Currently has only one `.py` file, but I will be adding more later. Current code needs you to add the income manually, but will automatically add them to Excel. Not ideal I know, I'll be adding a better code when I have time). This is only a foundation for your excel files, which you can then update to your own liking.
- [Monitor-website](https://github.com/endormi/automation/blob/master/monitor-website/web.py) - If website isn't up-and-running, sends an email and plays a sound.
- [Move-cursor](https://github.com/endormi/automation/blob/master/move-cursor/cursor.py) - Move cursor every 10 seconds.
- [Open-essentials](https://github.com/endormi/automation/blob/master/open-essentials/essentials.py) - X - Open all of the essentials for development such as websites. tools and editor.
- [Organize-files](https://github.com/endormi/automation/blob/master/organize-files/organizer.py) - Organizes files (images, audio, texts, videos and compressed files) and moves them inside specified folders.
- [Repo](https://github.com/endormi/automation/tree/master/repo) - Creates a private or public GitHub repository.
- [Scheduler](https://github.com/endormi/automation/tree/master/scheduler/scheduler.py) - X - Scheduled jobs (open email, shutdown computer etc.).
- [Selenium-testing](https://github.com/endormi/automation/tree/master/selenium-testing) - X - Testing website functionality using websites such as GitHub and Stack Overflow. I am testing these specific websites, because the tests are easily modified to be used with personal and/or company websites.
- [Send-email](https://github.com/endormi/automation/blob/master/send-email/email.py) - Send emails (subject, content and image attachments).
- [Tweeter](https://github.com/endormi/automation/blob/master/tweeter/tweet.py) - Write and post tweets.
- [Whatsapp](https://github.com/endormi/automation/blob/master/whatsapp/msg.py) - Send Whatsapp message (I'm thinking of switching from Whatsapp, but thought this still should be added).
- [Youtube](https://github.com/endormi/automation/blob/master/youtube/dl.py) - Download an audio from YouTube.

## License

The source code is released under the [MIT License](https://github.com/endormi/automation/blob/master/LICENSE).

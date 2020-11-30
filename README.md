# mattermost-command-meet

![screenshot](https://github.com/nest-matt/mattermost-command-meet/blob/tec/screenshots/screenshot.png)

## Description

This API makes it possible to instantly create a room on **Google Meet** with the `/meet` command.

The command accepts a list of users to be marked as part of the meeting:

``
/meet @user1 @user2 @user3
``

The command returns the link to the room, as well as a message marking all invited users on the channel the posting user is in.

## Adding the command to Mattermost

- To add the command, follow the [custom slash command](https://docs.mattermost.com/developer/slash-commands.html#custom-slash-command) guide, making sure you use the following settings:
    - Title: Meet
    - Description: Generate a Google Meet link to start a meeting
    - Command Trigger Word: meet
    - Request URL: http://127.0.0.1:5001
- After creating the program, you will receive a `token`
- Create a `.env` file inside` src` with the `MATTERMOST_TOKEN = <token>` field
- Run `pip install pipenv` and then `pipenv install --system` 
- Start the application using the command `python3 wsgi.py &` from the `src/` directory
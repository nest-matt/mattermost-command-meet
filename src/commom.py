import time
from coolname import RandomGenerator


def get_meeting_response(user: str, user_mentions: list, room_name: str) -> str:
    generator = RandomGenerator({
        'all': {
            'type': 'cartesian',
            'lists': ['first_word', 'second_word']
        },
        'first_word': {
            'type': 'words',
            'words': ['crazy', 'shaking', 'global', 'different', 'incredible', 'embracing', 'creative', 'magic', 'innovative', 'brave', 'strong', 'insightful', 'curious', 'unstoppable', 'fearless', 'seeking', 'energetic', 'believing']
        },
        'second_word': {
            'type': 'words',
            'words': ['maverick', 'ant', 'heart', 'Energy Collective family member', 'personality']
        },
    })
    tec_random = ' '.join(generator.generate())
    return f"""
##### @{user} the *{tec_random}* has started a meeting
{", ".join(user_mentions)} join the meeting at [{room_name}]({room_name})
"""


def get_help_response() -> str:
    return f"""
Unknown option chosen. Here's help

Welcome to /meet. To create a new Google Meet meeting use the following slash command.
`/meet @user1 @user2 @user3`
For ex. `/meet @james-brown`

to get this message use:
`/meet help`

"""


def get_meeting_name() -> str:
    name = str(int(time.time()))
    name = name[3:]
    meetcode = name[0:4] + '-' + name[4:]
    return 'tec-' + meetcode


def mattermost_command_to_json(text: str) -> dict:
    splitted_text = text.split("&")
    fields = {
        "user_mentions": [],
        "user_mentions_ids": [],
        "channel_mentions": [],
        "channel_mentions_ids": [],
    }
    for field_name_and_field_value in splitted_text:
        field, value = field_name_and_field_value.split("=")
        if field in fields.keys():
            fields[field].append(value)
        else:
            fields[field] = value
    return fields

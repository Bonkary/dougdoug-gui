from platform_connection import Twitch


twitch = Twitch(channel_name="shroud")

twitch.connect()

messages = twitch.get_messages()
for message in messages:
    print(f"USER: {message['username']}")
    print(f"MESSAGE: {message['message']}")
    print("------------")
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.socket_mode.response import SocketModeResponse

# Your bot token goes here. You get this when you create a new app on Slack's API website.
BOT_TOKEN = "xoxb-4926330797984-6009354484372-CqKRezEXeK2tknBqaXx18fn2"
APP_TOKEN = "xapp-1-A060VSC8H3J-5992406833159-f86228cbae31724c24788e73e0d77c32a9d8eeca52ea174c0d90d26d361ed138"  # You get this under the "Basic Information" tab in your Slack App settings.

client = WebClient(token=BOT_TOKEN)

def handle_message(payload):
    event = payload['event']

    # Check if the bot was mentioned. '@igor_bot' is the bot's user ID.
    if 'bot_id' not in event and f'<@igor_bot>' in event['text']:
        channel_id = event['channel']
        thread_ts = event['ts']  # This ensures the reply goes into the thread.

        try:
            client.chat_postMessage(channel=channel_id, text="Yes, Master!", thread_ts=thread_ts)
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")

def main():
    socket_mode_client = SocketModeClient(app_token=APP_TOKEN, web_client=client)
    socket_mode_client.socket_mode_request_listeners.append(handle_message)
    socket_mode_client.start()

if __name__ == "__main__":
    main()

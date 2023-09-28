import os
import sys
import traceback

from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity, ActivityTypes, ChannelAccount
from botframework.connector import ConnectorClient
from botframework.connector.auth import MicrosoftAppCredentials
from config import DefaultConfig


CHANNEL_ID = "msteams"
CONVERSATION_ID = os.environ.get("CONVERSATION_ID", "")
SERVICE_URL = "https://smba.trafficmanager.net/emea/"
CONFIG = DefaultConfig()


async def on_bot_error(context: TurnContext, error: Exception) -> None:
    """Print and send out all exceptions from the bot."""

    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity("The bot encountered an error or bug.")
    await context.send_activity("To continue to run this bot, please fix the bot source code.")


def get_bot_adapter() -> BotFrameworkAdapter:
    """Create and return a bot adapter."""

    settings = BotFrameworkAdapterSettings(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
    adapter = BotFrameworkAdapter(settings)
    adapter.on_turn_error = on_bot_error
    return adapter


def get_teams_connector() -> ConnectorClient:
    """Create and return Teams connector."""

    credentials = MicrosoftAppCredentials(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
    return ConnectorClient(credentials=credentials, base_url=SERVICE_URL)


async def send_message(connector: ConnectorClient, conversation_id: str, message: str) -> None:
    """Send a message to specific conversation."""

    activity = Activity(
        type=ActivityTypes.message,
        channel_id=CHANNEL_ID,
        from_property=ChannelAccount(id=CONFIG.APP_ID),
        text=message,
    )
    connector.conversations.send_to_conversation(conversation_id, activity)

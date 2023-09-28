from botbuilder.core import ActivityHandler, TurnContext


class EchoBot(ActivityHandler):
    """Class to represent a Bot created using Microsoft Bot Framework."""

    async def on_message_activity(self, turn_context: TurnContext):
        """Send back a received message, imitating echoing."""

        return await turn_context.send_activity(turn_context.activity.text)

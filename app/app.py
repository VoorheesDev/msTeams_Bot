import os
from http import HTTPStatus

from aiohttp import web
from aiohttp.web import Request, Response
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity
from bots import EchoBot
from utils import get_bot_adapter, get_teams_connector, send_message


CONVERSATION_ID = os.environ.get("CONVERSATION_ID")
PORT = os.environ.get("PORT", 3978)

ADAPTER = get_bot_adapter()
BOT = EchoBot()
connector = get_teams_connector()


async def messages(req: Request) -> Response:
    """Listen to the incoming requests and handle messages to the bot."""

    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
    else:
        return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

    activity = Activity().deserialize(body)
    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return Response(body=response.body, status=response.status)
    return Response(status=HTTPStatus.ACCEPTED)


async def notify(req: Request) -> Response:
    """Listen to the incoming requests and send a notification to specific conversation."""

    message = "Hello there"
    await send_message(connector, CONVERSATION_ID, message)
    return Response(status=HTTPStatus.OK, text="Notification message have been sent")


APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/messages", messages)
APP.router.add_post("/api/notify", notify)


if __name__ == "__main__":
    web.run_app(APP, port=PORT)

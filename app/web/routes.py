from aiohttp.web import json_response as aiohttp_json_response
from aiohttp.web_app import Application
from aiohttp.web_urldispatcher import View


class HelloView(View):
    async def get(self):
        return aiohttp_json_response(
            data={
                "status": "ok",
                "data": "Welcome to binary-options-bot",
            }
        )


__all__ = ("setup_routes",)


def setup_routes(app: Application):
    app.router.add_view("/", HelloView)
    app.router.add_view("/hello", HelloView)

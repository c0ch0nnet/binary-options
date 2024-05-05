from aiohttp.web import json_response as aiohttp_json_response
from aiohttp.web_app import Application
from aiohttp.web_urldispatcher import View

__all__ = ("setup_routes",)


class HelloView(View):
    async def get(self):
        return aiohttp_json_response(
            data={
                "status": "ok",
                "data": "Welcome to binary-options-bot",
            }
        )


def setup_routes(application: Application):
    import app.users.routes

    app.users.routes.register_urls(application)

    application.router.add_view("/", HelloView)
    application.router.add_view("/hello", HelloView)

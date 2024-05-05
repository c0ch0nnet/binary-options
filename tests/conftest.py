import os
from asyncio import AbstractEventLoop

import pytest
from aiohttp.pytest_plugin import AiohttpClient
from aiohttp.test_utils import TestClient

from app.web.app import Application, setup_app


@pytest.fixture(scope="session")
def application() -> Application:
    app = setup_app(
        config_path=os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "config.yml"
        )
    )
    app.on_startup.clear()
    app.on_shutdown.clear()
    app.on_cleanup.clear()
    # app.on_startup.append(app.store.admins.connect)
    # app.on_shutdown.append(app.store.admins.disconnect)
    return app


@pytest.fixture(autouse=True)
def cli(
    aiohttp_client: AiohttpClient,
    event_loop: AbstractEventLoop,
    application: Application,
) -> TestClient:
    return event_loop.run_until_complete(aiohttp_client(application))

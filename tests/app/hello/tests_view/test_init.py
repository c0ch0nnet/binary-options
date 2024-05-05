from aiohttp.test_utils import TestClient



class TestHelloView:
    async def test_success(self, cli: TestClient) -> None:
        response = await cli.get("/hello")
        assert response.status == 200

        data = await response.json()
        assert data == {
            "status": "ok",
            "data": "Welcome to binary-options-bot",
        }

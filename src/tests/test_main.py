"""test for main function with pytest fixture"""


def test_ping(test_app):
    """test for function ping(basically health check)"""
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}

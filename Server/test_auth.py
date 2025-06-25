import requests

session = requests.Session()


def test_register():
    response = session.post(
        "http://localhost:5000/register",
        json={"email": "test@test.com", "password": "test"},
    )
    print(response.json())


def test_login():
    response = session.post(
        "http://localhost:5000/login",
        json={"email": "test@test.com", "password": "test"},
    )
    assert response.status_code == 200


def test_logout():
    response = session.post("http://localhost:5000/logout")
    assert response.status_code == 200


def test_get_user():
    response = session.get("http://localhost:5000/user")
    assert response.status_code == 200


if __name__ == "__main__":
    # if you havent created account yet
    test_register()
    test_login()
    test_get_user()
    test_logout()
    print("All tests passed")

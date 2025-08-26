from src.app.main import app
from fastapi.testclient import TestClient
from src.utils import get_age_from_dob
from freezegun import freeze_time
import mock
import datetime

# create test http client
client = TestClient(app)

# test get age from dob
@freeze_time("2025-08-25")
def test_get_age_from_dob():
    expected_age = 40
    actual_age = get_age_from_dob(datetime.date(1985, 6, 12))
    assert actual_age == expected_age

# test create user api
@mock.patch("src.utils.get_db_session")
def test_create_user(mock_db_session):
    request_data ={
        "first_name": "samir",
        "last_name": "malik",
        "dob": "1985-06-12",
    }
    response = client.post(
        "/users/create/",
        json=request_data,
    )
    assert response.status_code == 201
    assert mock_db_session.add.was_called()
    assert mock_db_session.commit.was_called()
    assert mock_db_session.refresh.was_called()
    actual_response = response.json()
    del actual_response["age"] # will test age in seperate test
    assert actual_response == request_data

# test get users api
@mock.patch("src.utils.get_db_session")
def test_get_users(mock_db_session):
    response = client.get("/users/")
    assert response.status_code == 200
    assert mock_db_session.query.was_called()

# test delete users api
@mock.patch("src.utils.get_db_session")
def test_delete_existing_user(mock_db_session):
    response = client.delete("/user/1/delete/")
    assert response.status_code == 204
    assert mock_db_session.query.was_called()
    assert mock_db_session.delete.was_called()
    assert mock_db_session.commit.was_called()


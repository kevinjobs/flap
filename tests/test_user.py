import json
import pytest
from sqlalchemy.exc import NoResultFound
from flask.testing import FlaskClient
from app.utils import now_timestamp
from app.exceptions import UserDoesntExistError


def test_register(client: FlaskClient):
    resp = client.post('/api/register', data={
        'name': 'kevinjobs{}'.format(now_timestamp()),
        'password': 'mytestpasswd',
        'email': 'kevinjobs{}@qq.com'.format(now_timestamp()),
    })
    assert resp.status_code == 200
    assert isinstance(resp.text, str)
    assert json.loads(resp.text)['code'] == 0


def test_get_users(client: FlaskClient):
    resp = client.get('/api/users')
    assert resp.status_code == 200
    assert isinstance(resp.text, str)
    assert json.loads(resp.text)['code'] == 0


def test_get_user_by_name(client: FlaskClient):
    with pytest.raises(UserDoesntExistError):
        resp = client.get('/api/user/kevinjobs')
        assert resp.status_code != 200


def test_delete_user_by_id(client: FlaskClient):
    with pytest.raises(NoResultFound):
        resp = client.delete('/api/user/3')
        assert resp.status_code != 200

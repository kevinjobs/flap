import json
import pytest
from flask.testing import FlaskClient


fields = ('name', 'password', 'email')
test_users = [
    ('kevinjobs', 'takemeaway', 'kevinjobs@qq.com'),
    ('kevinjobs1', 'takemeaway', 'kevinjobs1@qq.com'),
    ('kevinjobs2', 'takemeaway', 'kevinjobs2@qq.com'),
]


def _no_error_code(resp):
    return json.loads(resp.text)['code'] == 0 and resp.status_code == 200


@pytest.mark.parametrize(fields, test_users)
def test_add_new_user(client: FlaskClient, name, password, email):
    resp = client.post('/api/user', data={
        'name': name,
        'password': password,
        'email': email,
    })
    assert _no_error_code(resp)


@pytest.mark.parametrize(fields, test_users)
def test_get_user_by_name(client: FlaskClient, name, password, email):
    resp = client.get(f'/api/user/{name}')
    assert _no_error_code(resp)


def test_get_users(client: FlaskClient):
    resp = client.get('/api/users')
    assert _no_error_code(resp)
    assert len(json.loads(resp.text)['data']) == 3


@pytest.mark.parametrize(fields, test_users)
def test_delete_user_by_email(client: FlaskClient, name, password, email):
    resp = client.delete(f'/api/user/{email}')
    assert _no_error_code(resp)

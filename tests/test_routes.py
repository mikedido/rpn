import pytest
from fastapi.testclient import TestClient

from src.app import get_application
from src.routes import get_stack_service


@pytest.fixture
def client_app():
    app = get_application()
    return TestClient(app)


def test_get_operations(client_app):
    response = client_app.get('/rpn/op')

    assert response.json() == ['+', '-', '*', '/']
    assert response.status_code == 200 


def test_get_stacks(client_app):
    response = client_app.get('/rpn/stack')

    assert response.json() == {}
    assert response.status_code == 200 


def test_get_stack(client_app):
    response = client_app.get('/rpn/stack/1')

    assert response.json() == None
    assert response.status_code == 200 


def test_create_stack(client_app):
    response = client_app.post('/rpn/stack')

    assert response.status_code == 201 


def test_delete_stack(client_app):
    response = client_app.delete('/rpn/stack/0')

    assert response.status_code == 200


def test_push_value(client_app):
    stack = get_stack_service()
    stack.create_stack()

    response = client_app.post('/rpn/stack/0?value=2')

    assert response.status_code == 201


def apply_op_stack(client_app):
    stack = get_stack_service()
    stack.create_stack()
    stack.add_value_stack(0, 2)
    stack.add_value_stack(0, 3)

    response = client_app.post('/rpn/op/+/stack/0')

    assert response.status_code == 201

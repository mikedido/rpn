import pytest

from src.services import OperationService


@pytest.fixture
def operation_service():
    return OperationService()


def test_addition(operation_service):
    expected_list = ["+", "-", "*", "/"]
    assert operation_service.get_operations() == expected_list


def test_apply_operation_addition(operation_service):
    test_values = [6, 3]
    assert operation_service.apply_operation("+", test_values) == 9


def test_apply_operation_soustraction(operation_service):
    test_values = [6, 3]
    assert operation_service.apply_operation("-", test_values) == 3


def test_apply_operation_multiplcation(operation_service):
    test_values = [6, 3]
    assert operation_service.apply_operation("*", test_values) == 18

    
def test_apply_operation_division(operation_service):
    test_values = [6, 3]
    assert operation_service.apply_operation("/", test_values) == 2

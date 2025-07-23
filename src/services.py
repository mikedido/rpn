from src.utils import get_last_index


from math import prod
from functools import reduce
from collections.abc import Iterable


OPERATIONS = ["+", "-", "*", "/"]


class OperationService:

    def __init__(self):
        self.operations = OPERATIONS


    def get_operations(self):
        return self.operations
    

    def apply_operation(self, operation: str, values: Iterable):
        match operation:
            case "+":
                return sum(values)
            case "*":
                return prod(values)
            case "/":
                return reduce(lambda x, y: x / y if y != 0 else float('inf'), values)
            case "-":
                return reduce(lambda x, y: x - y, values)


class StackService:

    def __init__(self, operation_service: OperationService):
        self.stack = {}
        self.operation_service = operation_service


    def create_stack(self):
        stack_id = get_last_index(self.stack)
        self.stack[stack_id + 1] = []

    
    def get_stack(self, stack_id: int):
        return self.stack.get(stack_id)
    

    def get_stacks(self):
        return self.stack
    

    def add_value_stack(self, stack_id: int, value: int) -> None:
        stack = self.stack.get(stack_id)
        print(stack)
        if stack is not None:
            stack.append(value)
            self.stack[stack_id] = stack
    

    def apply_op(self, operation: str, stack_id: int) -> str:
        stack = self.get_stack(stack_id)
        
        if len(stack) >= 2:
            values = stack[-2:]
            calculation_value = self.operation_service.apply_operation(operation, values)
            del stack[-2:]
            stack.append(calculation_value)
            return f"Operation done on stack {stack_id}"
        
        return f"Stack {stack_id} must have 2 elements to make operation or stack {stack_id} not exist"


    def delete_stack(self, stack_id: int):
        return self.stack.pop(stack_id, None)
from fastapi import APIRouter, HTTPException, Depends, status

from src.services import StackService, OperationService

from functools import lru_cache

@lru_cache
def get_stack_service():
    return StackService(operation_service= OperationService()) 


@lru_cache
def get_operation_service():
    return OperationService()


rpn_router = APIRouter()


@rpn_router.get("/op", status_code=200)
def get_operande_list(operation_services = Depends(get_operation_service)):
    try:
        return operation_services.get_operations()
    except Exception as err:
        print(f"error occurs : {err}")
        raise HTTPException(status_code=404, detail="Op not found")


@rpn_router.get("/stack", status_code=200)
def get_stack_list(stack_service = Depends(get_stack_service)):
    try:
        return stack_service.get_stacks()
    except Exception:
        raise HTTPException(status_code=404, detail="stacks not found")


@rpn_router.get("/stack/{stack_id}", status_code=200)
def get_stack(stack_id: int, stack_service = Depends(get_stack_service)):
    try:
        return stack_service.get_stack(stack_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Stack not found")


@rpn_router.post("/stack", status_code=201)
def create_stack(stack_service = Depends(get_stack_service)):
    try:
        return stack_service.create_stack()
    except Exception:
        raise HTTPException(status_code=404, detail="Stack not created")


@rpn_router.post("/op/{op}/stack/{stack_id}", status_code=201)
def apply_operand_stack(op: str, stack_id: int, stack_service = Depends(get_stack_service)):
    try:
        return stack_service.apply_op(op, stack_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Appely operator error")


@rpn_router.post("/stack/{stack_id}", status_code=201)
def push_value_stack(value: int, stack_id: int, stack_service = Depends(get_stack_service)):
    try:
        return stack_service.add_value_stack(stack_id, value)
    except Exception:
        raise HTTPException(status_code=404, detail="Value append error")


@rpn_router.delete("/stack/{stack_id}", status_code=200)
def remove_stack(stack_id: int, stack_service = Depends(get_stack_service)):
    try:
        return stack_service.delete_stack(stack_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Stack delete error")

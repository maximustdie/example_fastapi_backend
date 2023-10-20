from fastapi import APIRouter

from abstractions.decorators.transactional import transactional

router = APIRouter(tags=["books"])


@router.get("/books")
def health():
    return {"book": "Ok!"}

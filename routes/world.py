from fastapi import APIRouter

router = APIRouter(prefix="/world")

# get world
@router.get("")
async def get_world():
    return {"message": "World"}

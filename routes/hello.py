from fastapi import APIRouter, Body
from logger import get_logger
logger = get_logger(__name__)
router = APIRouter(prefix="/hello")

# get world
@router.get("")
async def get_world():
    logger.info("get world")
    return {"message": "hello"}

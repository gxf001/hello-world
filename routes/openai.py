from fastapi import APIRouter
import openai
from openai import OpenAI
from config import Config

from logger import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/openai")

# get world
@router.get("")
async def get_openai():
    logger.info("openai begin")
    client = OpenAI(api_key=Config().openai_api_key)


    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "这幅图画的是什么"},
            {
              "type": "image_url",
              "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
              },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    logger.info(response.choices[0])
    
    return {"message": response.choices[0].message.content}

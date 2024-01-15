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
    # client = OpenAI(api_key=Config().openai_api_key, base_url="http://openai-proxy-openai-proxy-dejvykwdsv.us-west-1-vpc.fcapp.run")#"https://openai-proxy-openai-proxy-dejvykwdsv.us-west-1.fcapp.run")
    client = OpenAI(api_key=Config().openai_api_key, base_url="https://openai-proxy-openai-proxy-dejvykwdsv.us-west-1.fcapp.run")
# 
    try:
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
    except Exception as e:
      logger.error(f"request error: {e}")
      return {"message": f"error,{e}"}
      

    logger.info(response.choices[0])
    
    return {"message": response.choices[0].message.content}

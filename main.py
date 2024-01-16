import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from logger import get_logger
from routes.hello import router as hello
from routes.world import router as world
from routes.openai import router as openai

logger = get_logger(__name__)

app = FastAPI()

@app.get('/healthz')
def healthz():
    return JSONResponse(content={'healthy': 'true'}, status_code=status.HTTP_200_OK)

@app.get('/')
def index():
    return JSONResponse(content={'message': 'ok'}, status_code=status.HTTP_200_OK)

app.include_router(hello)
app.include_router(world)
app.include_router(openai)

def main():
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
    )

if __name__ == "__main__":
    main()
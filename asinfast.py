from fastapi import FastAPI
import httpx
import time

app = FastAPI()

async def fetch_data_async(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@app.get("/async")
async def get_async_data():
    start_time = time.time()  # Запоминаем время начала
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = await fetch_data_async(url)
    end_time = time.time()  # Запоминаем время окончания
    execution_time = end_time - start_time
    return {"data": data, "execution_time": execution_time}

#uvicorn FastApiProcessing.asinfast:app --reload --port 8000
#http://127.0.0.1:8000/async
from fastapi import FastAPI
import requests
import threading
import time

app = FastAPI()

def fetch_data_thread(url, result, index):
    response = requests.get(url)
    result[index] = response.json()

@app.get("/threading")
def get_threading_data():
    start_time = time.time()  # Запоминаем время начала
    url = "https://jsonplaceholder.typicode.com/posts/1"
    result = [None]
    thread = threading.Thread(target=fetch_data_thread, args=(url, result, 0))
    thread.start()
    thread.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return {"data": result[0], "execution_time": execution_time}

#uvicorn FastApiProcessing.treadfast:app --reload --port 8001
# http://127.0.0.1:8001/threading

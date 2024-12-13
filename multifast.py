from fastapi import FastAPI
import requests
from multiprocessing import Process, Manager
import time
app = FastAPI()

def fetch_data_process(url, return_dict):
    response = requests.get(url)
    return_dict["data"] = response.json()

@app.get("/multiprocessing")
def get_multiprocessing_data():
    start_time = time.time()
    url = "https://jsonplaceholder.typicode.com/posts/1"
    manager = Manager()
    return_dict = manager.dict()
    process = Process(target=fetch_data_process, args=(url, return_dict))
    process.start()
    process.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return {"data": return_dict["data"], "execution_time": execution_time}

#uvicorn FastApiProcessing.multifast:app --reload --port 8003
#http://127.0.0.1:8003/multiprocessing
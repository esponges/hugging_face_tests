from typing import Union
from gradio_client import Client, handle_file
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get('gradio/janhq/convert_and_display')
def get_hairstyle(q: Union[str, None] = ""):
    client = Client("jan-hq/Llama3.1-s-v0.2")
    result = client.predict(
        text=q,
        api_name="/convert_and_display"
    )

    return result

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import requests 
PRIVATE_KEY="361e3070-64c1-4149-ab5d-e6f7f2dbafb5"

app = FastAPI()

@app.post('/authenticate')
async def authenticate(user: User):
    response = requests.put('https://api.chatengine.io/users/',
        data={
            "username": user.username,
            "secret": user.username,
            "first_name": user.username,
        },
        headers={ "Project-ID": PRIVATE_KEY }
    )
    return response.json()
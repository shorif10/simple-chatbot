from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from message_handler import gemini_response
app = FastAPI()

class Message(BaseModel):
    message: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(message: Message):
    template = "Give a very concise response in html format of the below query.\n"
    msg = message.message.lower()
    msg = template + msg
    response = gemini_response(msg)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

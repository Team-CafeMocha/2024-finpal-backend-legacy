from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

async def call_openai_gpt(prompt: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"  # 예시 엔드포인트
    headers = {
        "Authorization": "Bearer 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",  # 실제 API 키로 대체
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            raise HTTPException(status_code=response.status_code, detail="OpenAI API failed to respond properly.")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    user_prompt = chat_request.prompt
    try:
        response_message = await call_openai_gpt(user_prompt)
        return {"response": response_message}
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

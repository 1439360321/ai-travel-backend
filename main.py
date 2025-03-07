
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI 旅行助手后端运行成功"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



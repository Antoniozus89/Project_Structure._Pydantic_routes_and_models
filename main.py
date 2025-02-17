from fastapi import FastAPI
from routers.task import router as task_router
from routers.user import router as user_router

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
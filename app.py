from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    secret = get_secret()
    return {"message": f"Hello world!"}
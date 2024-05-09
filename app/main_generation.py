from fastapi import FastAPI


app = FastAPI()


@app.get("/generate")
async def root():
    return {"message": "Hello, world"}

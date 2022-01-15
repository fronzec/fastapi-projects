from fastapi import FastAPI

app = FastAPI() # FastAPI instance


@app.get("/") # path operation decorator
async def root(): # path operation function
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

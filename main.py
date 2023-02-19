from fastapi import FastAPI

app = FastAPI() # What is going on here?

@app.get("/") # What is @ ?
def root():
    return {"Hello": "Will"}

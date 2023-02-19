from fastapi import FastAPI

# Q: What is going on here?
# A: We create instance of class FastAPI which is named app
app = FastAPI()

# Q: What is @ ?
# A: @ is decorator. Video which explains it https://youtu.be/r7Dtus7N4pI
@app.get("/")
def root():
    return {"Hello": "Will"}

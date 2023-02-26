from fastapi import FastAPI  # Here we import FastAPI class from \.venv\Lib\site-package\fastapi SOLVED

# SOLVED
# Q: What is going on here?
# A: We create instance of class FastAPI which is named app
app = FastAPI()

# SOLVED
# Q: What is @ ?
# A: @ is decorator. Video which explains it https://youtu.be/r7Dtus7N4pI
@app.get("/")
def root():
    return {"Hello": "Will"}

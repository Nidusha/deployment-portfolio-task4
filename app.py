from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Task 4.2: Python app running in Docker!"
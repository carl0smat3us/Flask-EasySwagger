from flask import Flask

from core import FlaskEasySwagger

app = Flask(__name__)
doc = FlaskEasySwagger(
    openapi="3.0.0",
    title="My Api Title",
    version="1.0",
    description="My Api Description",
    summary="My Api Summary",
)


@app.get("/")
def hello_world():
    return {"message": "Hello world!"}


doc.init_app(app)
if __name__ == "__main__":
    app.run(port=5000)

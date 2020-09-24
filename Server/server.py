from flask import Flask
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello_world():
    return "Hello World"


if __name__ == '__main__':
    logger.info("welcome to my flask server")
    app.run()
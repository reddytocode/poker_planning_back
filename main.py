from flask import Flask

app = Flask(__name__)


@app.route("/health")
def helth():
    return {"message": "Healthy"}


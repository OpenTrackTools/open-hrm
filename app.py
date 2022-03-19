from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


@app.route('/')
def root():
    return "<h1>My beautiful pyhrm application</h1>"


if __name__ == "__main__":
    app.run(debug=True)

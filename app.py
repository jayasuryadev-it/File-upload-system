import os

from flask import Flask
from flask_login import LoginManager

from config import Config
from models import db, User
from routes import main

app = Flask(__name__)

# Load all config first
app.config.from_object(Config)

# Upload folder (absolute path)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["ALLOWED_EXTENSIONS"] = {"pdf", "png", "jpg", "jpeg"}

# Create uploads folder if it doesn't exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "main.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(main)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
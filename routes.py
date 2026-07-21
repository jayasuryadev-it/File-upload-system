from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    current_app,
    send_from_directory
)
from flask_login import (
    login_user,
    login_required,
    current_user,
    logout_user
)
import os

from werkzeug.utils import secure_filename

from models import db, User, UploadedFile

main = Blueprint("main", __name__)

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in
        {"pdf", "png", "jpg", "jpeg"}
    )

@main.route("/")
def home():
    return render_template("home.html")


@main.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        address = request.form["address"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        password = request.form["password"]

        user = User(
            name=name,
            age=age,
            address=address,
            email=email,
            mobile=mobile
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("main.login"))

    return render_template("signup.html")


@main.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):

            login_user(user)

            return redirect(url_for("main.dashboard"))

        return "Invalid Email or Password"

    return render_template("login.html")

@main.route("/dashboard")
@login_required
def dashboard():

    uploaded_files = UploadedFile.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "dashboard.html",
        uploaded_files=uploaded_files
    )

@main.route("/upload", methods=["POST"])
@login_required
def upload():

    file1 = request.files.get("file1")
    file2 = request.files.get("file2")

    if not file1 or not file2:
        return "Please select both files."

    files = [file1, file2]

    os.makedirs(current_app.config["UPLOAD_FOLDER"], exist_ok=True)

    for file in files:

        if file.filename == "":
            return "Please select a file."

        if not allowed_file(file.filename):
            return "Only PDF, PNG, JPG and JPEG files are allowed."

        filename = secure_filename(file.filename)

        extension = filename.rsplit(".", 1)[1].lower()

        new_filename = f"{current_user.name}_{filename}"

        save_path = os.path.join(
            current_app.config["UPLOAD_FOLDER"],
            new_filename
        )

        file.save(save_path)

        uploaded_file = UploadedFile(
            filename=new_filename,
            filetype=extension,
            user_id=current_user.id
        )

        db.session.add(uploaded_file)

    db.session.commit()

    return "Files Uploaded Successfully"

@main.route("/download/<filename>")
@login_required
def download(filename):

    return send_from_directory(
        current_app.config["UPLOAD_FOLDER"],
        filename,
        as_attachment=True
    )

@main.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("main.login"))
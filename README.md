# 📁 File Upload Management System

A secure File Upload Management System built using **Flask** and **MySQL** with user authentication. Users can register, log in, upload files, view uploaded files, and download them securely.

## 🚀 Live Demo

🔗 https://file-upload-system-3.onrender.com

---

## 📌 Features

- User Registration
- Secure Login & Logout
- Password Hashing
- File Upload
- File Download
- User Dashboard
- MySQL Database Integration
- Responsive UI using Bootstrap
- Cloud Deployment using Render
- Cloud Database using Railway MySQL

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug Security

### Frontend
- HTML5
- CSS3
- Bootstrap 5

### Database
- MySQL (Railway)

### Deployment
- Render
- GitHub

---

## 📂 Project Structure

```
File-upload-system/
│
├── static/
│   ├── css/
│   └── uploads/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   └── dashboard.html
│
├── models.py
├── app.py
├── config.py
├── requirements.txt
├── Procfile
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/jayasuryadev-it/File-upload-system.git

cd File-upload-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DB_HOST=your_database_host
DB_PORT=your_database_port
DB_NAME=your_database_name
DB_USER=your_database_username
DB_PASSWORD=your_database_password
```

---

## ▶️ Run the Application

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000
```

---

## 📸 Application Workflow

1. User Registration
2. User Login
3. Dashboard Access
4. Upload File
5. View Uploaded Files
6. Download Files
7. Logout

---

## 🔒 Security Features

- Password hashing using Werkzeug
- User authentication with Flask-Login
- Protected dashboard routes
- Session management
- Secure file handling

---

## 📦 Deployment

- **Application:** Render
- **Database:** Railway MySQL
- **Version Control:** GitHub

---

## 👨‍💻 Author

**Jayasurya**

- GitHub: https://github.com/jayasuryadev-it

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

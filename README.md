# 🧠 AI Resume Parser with Firebase & Flask

This project is a **smart AI-powered resume parser** that extracts key information (Name, Email, Phone, Skills, Education, Experience, and Projects) from uploaded resumes (PDF format). Parsed data is stored securely in **Firebase Realtime Database** for future access and filtering.

---

## 🚀 Features

- Upload multiple resumes at once.
- Automatically extract and display key candidate information.
- Skill-matching against user-input skills.
- Store parsed results to **Firebase Realtime DB**.
- Built with Python, Flask, and basic HTML templates.

---

## 🛠️ Technologies Used

- **Backend:** Python 3, Flask
- **AI/NLP:** Custom Resume Parsing Logic
- **Database:** Firebase Realtime Database (free tier)
- **Frontend:** HTML + Jinja2 templates (index & result pages)

---

## 📁 Project Structure

```
Resume-Parser/
├── app/
│   └── run.py               # Core resume processing logic
├── web_app/
│   ├── main.py              # Flask app logic
│   ├── templates/
│   │   ├── index.html       # Upload page
│   │   └── result.html      # Parsed results page
│   └── uploads/             # Temporary resume storage
├── README.md
└── requirements.txt         # Python dependencies
```

---

## 🔧 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/resume-parser.git
cd resume-parser/web_app
```

2. **Create a virtual environment:**

```bash
python -m venv venv
venv\Scripts\activate    # Windows
```

3. **Install dependencies:**

```bash
pip install -r ../requirements.txt
```

4. **Run the Flask app:**

```bash
python main.py
```

The app will run on `http://127.0.0.1:5000/`.

---

## 🔐 Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com/).
2. Create a project.
3. Go to **Realtime Database** → Create database → Start in test mode.
4. Copy your database URL (ends with `.firebaseio.com` or `.asia-southeast1.firebasedatabase.app`).
5. Paste it in `main.py`:

```python
FIREBASE_DB_URL = "https://<your-project>.asia-southeast1.firebasedatabase.app/"
```

---

## 📥 Upload Format

Supported format: `.pdf`  
Make sure your resumes are cleanly structured for better parsing results.

---

## ✅ Example Output (Sample Fields Extracted)

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+91 9876543210",
  "skills": ["Python", "Flask", "SQL"],
  "education": ["B.Tech in Computer Science"],
  "experience": ["Software Engineer at XYZ Corp (2021-2023)"],
  "projects": ["AI Chatbot", "E-commerce Website"]
}
```

---

## 💡 Future Enhancements

- Add authentication to view stored resumes.
- Search/filter resumes based on skills or experience.
- Export parsed data to CSV/Excel.
- Frontend UI improvements.

---

## 🤝 Contributing

Feel free to fork and enhance this project. Pull requests are welcome!

---

## 📄 License

MIT License © 2025 [Joshua Yogendiran](https://github.com/Jidendiran-coder)

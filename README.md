# 💬 Full-Stack-ChatBot

A simple web-based chatbot built with **Python**, **Flask**, **HTML**, **CSS**, and **JavaScript**. The project provides a modern chat interface with user authentication, chat history management, dark/light themes, and a rule-based chatbot backend.

This project was developed to explore full-stack web development concepts, including frontend design, backend development, authentication, database management, and asynchronous communication using JavaScript.

---

## ✨ Features

* 🔐 User Registration & Login System
* 🔒 Secure password hashing using Flask-Bcrypt
* 👤 User authentication with Flask-Login
* 💬 Interactive chatbot interface
* ⚡ Real-time messaging using Fetch API
* ⌨️ Press **Enter** to send messages
* ⏳ Typing animation for bot responses
* 💡 Quick reply suggestions
* 🆕 Create new chat sessions
* 📂 Chat history stored in SQLite
* 👤 User profile page
* 🌙 Dark Mode & ☀️ Light Mode
* 💾 Theme preference saved in Local Storage
* 📜 Custom scrollbar and smooth animations
* 🎨 Modern glassmorphism-inspired UI
* 📱 Responsive layout

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-Bcrypt
* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript (ES6)

---

## 📂 Project Structure

ChatBot/
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── profile.html
│   └── base.html
│
├── app.py
├── requirements.txt
├── database.db
└── README.md


---

## 🚀 Installation

### 1. Clone the repository

git clone https://github.com/yourusername/chatbot.git


### 2. Move into the project directory

cd chatbot

### 3. Create a virtual environment

**Windows**

python -m venv venv
venv\Scripts\activate

**Linux / macOS**

python3 -m venv venv
source venv/bin/activate

### 4. Install dependencies

pip install -r requirements.txt

---

## ▶️ Running the Project

Start the Flask development server:

python app.py

Then open your browser and visit:

http://127.0.0.1:5000

---

## 💬 Chatbot Responses

The chatbot currently uses a simple keyword-based response system.

Example:

| User Input | Bot Response                     |
| ---------- | -------------------------------- |
| hello      | Hello! How can I help you today? |
| python     | Python is a powerful language.   |
| flask      | Flask is a Python web framework. |
| bye        | Goodbye!                         |

If no matching keyword is found, the chatbot replies:

I am still learning.

---

## 🗄️ Database

The project uses **SQLite** with the following models:

* User
* Chat
* Message

Messages and chat sessions are stored in the database for authenticated users.

---

## 🎨 User Interface

The application includes:

* Elegant dashboard
* Sidebar navigation
* Login & Registration pages
* Profile page
* Chat interface
* Quick reply buttons
* Typing animation
* Light/Dark mode
* Responsive design

---

## 📸 Screenshots

screenshots/
├── login.png =  <img width="1216" height="630" alt="login" src="https://github.com/user-attachments/assets/46116d21-5934-435b-845b-0a8c9d64fec3" />

├── register.png = <img width="1180" height="571" alt="register" src="https://github.com/user-attachments/assets/46cceaf1-e102-4cf3-82c4-1692e6fa7248" />

├── dashboard.png =<img width="1304" height="579" alt="dashboard1" src="https://github.com/user-attachments/assets/b8269ab6-c424-41b3-bc7a-cb0c2c8b9f7c" />

├── chat.png = <img width="1320" height="591" alt="dashboard2" src="https://github.com/user-attachments/assets/3cc8800a-2bc0-47fa-b5a5-174af72f99a6" />

└── profile.png

---

## 🔮 Future Improvements

Some planned enhancements include:

* 🤖 AI-powered responses using Gemini or OpenAI
* 💾 Persistent conversation history with better organization
* 🔍 Chat search
* 😊 Emoji support
* 📎 File upload support
* 🎤 Voice input
* 🌐 Multi-language support
* 📤 Export chat as PDF or TXT
* 📱 Improved mobile responsiveness
* 👥 User profile editing
* 🔔 Notifications

---

## 📦 Requirements

Example dependencies:

Flask
Flask-SQLAlchemy
Flask-Bcrypt
Flask-Login

Install them using:

pip install -r requirements.txt

---

## 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is intended for learning and educational purposes.

You may modify and extend it for your own projects.

---

## 👨‍💻 Author

Developed by **Dhanashri Phadtare**

If you found this project useful, consider giving it a ⭐ on GitHub.

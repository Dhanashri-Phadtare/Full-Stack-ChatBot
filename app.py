from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# DATABASE MODEL
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Chat(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )


class Message(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    text = db.Column(db.Text)

    sender = db.Column(db.String(20))

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    chat_id = db.Column(
        db.Integer,
        db.ForeignKey('chat.id')
    )

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# HOME
@app.route('/')
def home():
    return redirect(url_for('login'))


# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(username=username, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))

    return render_template('login.html')

#Profile
@app.route('/profile')
@login_required
def profile():

    return render_template(
        'profile.html'
    )

# DASHBOARD
@app.route('/dashboard')
@login_required
def dashboard():

    chats = Chat.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        'dashboard.html',
        chats=chats
    )

# CHATBOT API
  
@app.route('/chat', methods=['POST'])
@login_required
def chat():

    data = request.json

    user_message = data.get("message").lower()

    chat_id = data.get("chat_id")

    responses = {

        "hello":"Hello! How can I help you today?",

        "python":"Python is a powerful language.",

        "flask":"Flask is a Python web framework.",

        "bye":"Goodbye!"
    }

    bot_response = "I am still learning."

    for key in responses:

        if key in user_message:
            bot_response = responses[key]
            break

    # SAVE USER MESSAGE
    user_msg = Message(
        text=user_message,
        sender="user",
        chat_id=chat_id
    )

    db.session.add(user_msg)

    # SAVE BOT MESSAGE
    bot_msg = Message(
        text=bot_response,
        sender="bot",
        chat_id=chat_id
    )

    db.session.add(bot_msg)

    db.session.commit()

    return jsonify({
        "response":bot_response
    })

#new chat
@app.route('/new-chat')
@login_required
def new_chat():

    chat = Chat(
        title="New Chat",
        user_id=current_user.id
    )

    db.session.add(chat)
    db.session.commit()

    return redirect(
        url_for(
            'chat_page',
            chat_id=chat.id
        )
    )

# open chat
@app.route('/chat/<int:chat_id>')
@login_required
def chat_page(chat_id):

    chats = Chat.query.filter_by(
        user_id=current_user.id
    ).all()

    messages = Message.query.filter_by(
        chat_id=chat_id
    ).all()

    return render_template(
        'dashboard.html',
        chats=chats,
        messages=messages,
        active_chat=chat_id
    )

# LOGOUT
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

    
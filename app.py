from flask import Flask, render_template, redirect, url_for, flash, request
from extensions import db
from models import User
from forms import LoginForm, SignupForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'   # replace with a strong secret
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rewear.db'
db.init_app(app)

#@app.route('/')
#def home():
#    return render_template('landing.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # check if email already exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Please login.', 'danger')
            return redirect(url_for('login'))
        # create new user
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data   # ⚠️ In production, hash passwords!
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
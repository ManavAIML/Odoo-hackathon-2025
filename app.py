from flask import Flask, render_template, redirect, url_for, flash, request
from extensions import db
from models import User, Item
from forms import LoginForm, SignupForm, AddItemForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # replace with strong key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rewear.db'
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('home'))   # ✅ go to landing page first
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Please login.', 'danger')
            return redirect(url_for('login'))
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data  # ⚠️ hash in real app
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
    user = User.query.first()  # dummy user; replace later with logged-in user
    items = Item.query.filter_by(user_id=user.id).all() if user else []  # only this user's items
    return render_template('dashboard.html', user=user, items=items)

@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    form = AddItemForm()
    if form.validate_on_submit():
        new_item = Item(
            title=form.title.data,
            description=form.description.data,
            gender=form.gender.data,
            category=form.category.data,
            type=form.type.data,
            size=form.size.data,
            price=form.price.data,
            tags=form.tags.data,
            user_id=1  # replace later with logged-in user's ID
        )
        db.session.add(new_item)
        db.session.commit()
        flash('Item listed successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add_item.html', form=form)

@app.route('/item/<int:item_id>')
def item_detail(item_id):
    item = Item.query.get_or_404(item_id)
    return render_template('item.html', item=item)

@app.route('/browse-items')
def browse_items():
    items = Item.query.all()
    return render_template('browse_items.html', items=items)

@app.route('/women')
def women():
    return render_template('points_history.html')

@app.route('/men')
def men():
    return render_template('search_results.html')

# ✅ New routes for Women section image links
@app.route('/kurti')
def kurti_page():
    return render_template('kurti.html')

@app.route('/crop-top')
def crop_top_page():
    return render_template('crop_top.html')

@app.route('/dress')
def dress_page():
    return render_template('dress.html')

@app.route('/cardigans')
def cardigans_page():
    return render_template('cardigans.html')

@app.route('/cart')
def view_cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)

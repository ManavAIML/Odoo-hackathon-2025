# Style Shift 👗

A modern, user-friendly platform for fashion enthusiasts to *buy, sell, and swap* pre-loved clothing items.

---

## ✨ Key Features
- Smart swap system for trading clothes with other users
- Wishlist integration for easier swapping
- User profiles with style preferences
- Follow favorite sellers
- Outfit inspiration feed
- Add items to cart & manage them easily
- Dashboard to track your uploads and swap history
- Points or reward-based system for gamified swapping

---

## 🛠 Tech Stack
| Layer        | Technologies                                    |
| ------------ | ----------------------------------------------- |
| Frontend     | HTML5, CSS3, Jinja2 Templates                   |
| Backend      | Python, Flask                                    |
| Database     | SQLite (using SQLAlchemy ORM)                    |
| Authentication | Flask-Login, Flask-WTF                        |
| Deployment   | Render or Heroku (possible upgrade to PostgreSQL)|

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

---

### Installation & Setup

```bash

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
flask db init
flask db migrate
flask db upgrade

# Run the application
flask run

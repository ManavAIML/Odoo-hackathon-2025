# Odoo Hackathon
# 🛍 Style Shift — Modern Fashion Resale & Swap Store

<div align="center">
  <img src="https://i.imgur.com/JzQZQ9q.png" width="200" alt="Style Shift Logo">
  <p>A revolutionary platform for fashion enthusiasts to buy, sell, and swap pre-loved clothing items</p>
  
  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
  [![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)](https://flask.palletsprojects.com/)
  [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4%2B-green)](https://www.sqlalchemy.org/)
</div>

## ✨ Enhanced Features

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="background: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #6c5ce7;">
<h3>🔄 Smart Swap System</h3>
<ul>
<li>AI-powered matching algorithm for item swaps</li>
<li>Wishlist integration for automatic swap suggestions</li>
<li>Real-time swap request notifications</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #00b894;">
<h3>📱 Social Features</h3>
<ul>
<li>User profiles with style preferences</li>
<li>Follow favorite sellers</li>
<li>Outfit inspiration feed</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #fd79a8;">
<h3>🛒 Enhanced Shopping</h3>
<ul>
<li>Virtual try-on with AR integration</li>
<li>Size recommendation engine</li>
<li>Scheduled pickup/delivery options</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #fdcb6e;">
<h3>📊 Sustainability Dashboard</h3>
<ul>
<li>Track your environmental impact</li>
<li>Carbon footprint calculator</li>
<li>Eco-badges for sustainable sellers</li>
</ul>
</div>

</div>

## 🖥️ Screenshots

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">

<div>
<h4>🎯 Landing Page</h4>
<img src="https://i.imgur.com/JzQZQ9q.png" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
</div>

<div>
<h4>👗 Product View</h4>
<img src="https://i.imgur.com/JzQZQ9q.png" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
</div>

<div>
<h4>📱 Mobile Responsive</h4>
<img src="https://i.imgur.com/JzQZQ9q.png" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
</div>

</div>

## 🛠️ Tech Stack

<div style="background: #f5f6fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
<table>
<tr>
<td><strong>Frontend</strong></td>
<td>HTML5, CSS3, Jinja2 Templates</td>
</tr>
<tr>
<td><strong>Backend</strong></td>
<td>Python, Flask</td>
</tr>
<tr>
<td><strong>Database</strong></td>
<td>SQLite (SQLAlchemy ORM)</td>
</tr>
<tr>
<td><strong>Authentication</strong></td>
<td>Flask-Login, Bcrypt</td>
</tr>
<tr>
<td><strong>Deployment</strong></td>
<td>Render/Heroku (with PostgreSQL)</td>
</tr>
</table>
</div>

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/style-shift.git
cd style-shift

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Initialize database
flask db init
flask db migrate
flask db upgrade

# Run the application
flask run

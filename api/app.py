#!/usr/bin/env python3
"""
TechBlog - Simple Blog Platform
A basic blog and community platform
"""

from flask import Flask, request, render_template_string, redirect, url_for, session, make_response, send_file
import sqlite3
import os
import hashlib
import subprocess
import pickle
import base64
from werkzeug.utils import secure_filename
import xml.etree.ElementTree as ET
import tempfile

app = Flask(__name__)
app.secret_key = 'my_blog_secret_2023'

# Use temp directory for uploads in serverless environment
TEMP_DIR = tempfile.gettempdir()
UPLOAD_FOLDER = os.path.join(TEMP_DIR, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize database
def init_db():
    db_path = os.path.join(TEMP_DIR, 'techblog.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            email TEXT,
            role TEXT DEFAULT 'user'
        )
    ''')
    
    # Create posts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            author TEXT
        )
    ''')
    
    # Insert default users
    cursor.execute("SELECT * FROM users WHERE username='sarah_dev'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)",
                      ('sarah_dev', 'summer2023', 'sarah.johnson@gmail.com', 'admin'))
    
    cursor.execute("SELECT * FROM users WHERE username='mike_codes'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)",
                      ('mike_codes', 'password1', 'mike.rodriguez@outlook.com', 'user'))
    
    cursor.execute("SELECT * FROM users WHERE username='alex_js'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)",
                      ('alex_js', '123456', 'alex.chen@yahoo.com', 'user'))
    
    cursor.execute("SELECT * FROM users WHERE username='jenny_react'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)",
                      ('jenny_react', 'qwerty', 'jennifer.smith@hotmail.com', 'user'))
    
    # Insert sample posts
    cursor.execute("SELECT COUNT(*) FROM posts")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)",
                      ('Welcome to TechBlog', 'Hey everyone! Welcome to our new tech community platform. Share your thoughts and connect with fellow developers.', 'sarah_dev'))
        cursor.execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)",
                      ('Learning React Hooks', 'Just spent the weekend diving into React hooks. The useState and useEffect combo is game-changing!', 'jenny_react'))
        cursor.execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)",
                      ('Python vs JavaScript', 'Been coding in both lately. Python for data stuff, JS for web dev. Each has its place I guess.', 'mike_codes'))
        cursor.execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)",
                      ('Node.js Performance Tips', 'Some quick tips I learned about optimizing Node apps. Event loop is everything!', 'alex_js'))
    
    conn.commit()
    conn.close()

def get_db_connection():
    db_path = os.path.join(TEMP_DIR, 'techblog.db')
    return sqlite3.connect(db_path)

# Home page
@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>TechBlog - Share Your Tech Journey</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .container { max-width: 1000px; margin: 0 auto; background: white; min-height: 100vh; }
        .header { background: #2c3e50; color: white; padding: 30px 40px; text-align: center; }
        .header h1 { margin: 0; font-size: 2.5em; font-weight: 300; }
        .header p { margin: 10px 0 0 0; opacity: 0.9; }
        .nav { background: #34495e; padding: 0; }
        .nav a { display: inline-block; padding: 15px 25px; color: white; text-decoration: none; border-right: 1px solid #2c3e50; transition: all 0.3s; }
        .nav a:hover { background: #3498db; }
        .content { padding: 40px; }
        .welcome { background: #ecf0f1; padding: 30px; border-radius: 10px; margin: 30px 0; }
        .feature-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0; }
        .feature { background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #3498db; }
        .feature h3 { margin-top: 0; color: #2c3e50; }
        .cta { text-align: center; margin: 40px 0; }
        .btn { background: #3498db; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; display: inline-block; transition: all 0.3s; }
        .btn:hover { background: #2980b9; transform: translateY(-2px); }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>💻 TechBlog</h1>
            <p>Where developers share their journey</p>
        </div>
        
        <div class="nav">
            <a href="/login">Login</a>
            <a href="/search">Search Posts</a>
            <a href="/upload">Upload Files</a>
            <a href="/posts">All Posts</a>
            <a href="/contact">Contact Us</a>
            <a href="/ping">Network Tools</a>
        </div>
        
        <div class="content">
            <div class="welcome">
                <h2>Welcome to TechBlog! 🚀</h2>
                <p>Join our community of developers, designers, and tech enthusiasts. Share your projects, get help with coding problems, and connect with like-minded people.</p>
            </div>
            
            <div class="feature-grid">
                <div class="feature">
                    <h3>📝 Share Your Story</h3>
                    <p>Write about your coding journey, share tutorials, and help others learn from your experiences.</p>
                </div>
                <div class="feature">
                    <h3>🔍 Discover Content</h3>
                    <p>Find interesting posts, tutorials, and discussions from our growing community of developers.</p>
                </div>
                <div class="feature">
                    <h3>💬 Connect & Learn</h3>
                    <p>Get feedback on your projects, ask questions, and learn from experienced developers.</p>
                </div>
                <div class="feature">
                    <h3>⚡ Developer Tools</h3>
                    <p>Access useful tools and utilities to help with your development workflow.</p>
                </div>
            </div>
            
            <div class="cta">
                <h3>Ready to get started?</h3>
                <p>Join our community today and start sharing your tech journey!</p>
                <a href="/login" class="btn">Join TechBlog</a>
            </div>
        </div>
    </div>
</body>
</html>
    ''')

# Login page with SQL injection vulnerability
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Database query
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                session['role'] = user[4]
                return redirect(url_for('dashboard'))
            else:
                return render_template_string(login_template, error="Invalid username or password")
        except sqlite3.Error as e:
            return render_template_string(login_template, error="Database error occurred")
        finally:
            conn.close()
    
    return render_template_string(login_template)

login_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login - TechBlog</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        .container { max-width: 400px; margin: 0 auto; background: white; padding: 20px; border-radius: 5px; }
        .form-group { margin: 15px 0; }
        label { display: block; margin-bottom: 5px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 3px; }
        button { background: #1976d2; color: white; padding: 10px 20px; border: none; border-radius: 3px; cursor: pointer; }
        .error { color: red; margin: 10px 0; }
        .debug { background: #f0f0f0; padding: 10px; margin: 10px 0; font-family: monospace; }
        .nav { margin: 20px 0; }
        .nav a { color: #1976d2; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <div class="nav"><a href="/">← Back to Home</a></div>
        
        <form method="POST">
            <div class="form-group">
                <label>Username:</label>
                <input type="text" name="username" required>
            </div>
            <div class="form-group">
                <label>Password:</label>
                <input type="password" name="password" required>
            </div>
            <button type="submit">Login</button>
        </form>
        
        {% if error %}
            <div class="error">Error: {{ error }}</div>
        {% endif %}
        
        <p><small>Try: sarah_dev/summer2023, mike_codes/password1, alex_js/123456</small></p>
    </div>
</body>
</html>
'''

# Dashboard after login
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard - TechBlog</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 5px; }
        .nav { margin: 20px 0; }
        .nav a { margin-right: 15px; color: #1976d2; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Hey {{ session.username }}! 👋</h2>
        <p>Welcome to your dashboard</p>
        
        <div class="nav">
            <a href="/">Home</a>
            <a href="/search">Search</a>
            <a href="/upload">Upload</a>
            <a href="/posts">Posts</a>
            {% if session.role == 'admin' %}
                <a href="/admin">Admin</a>
            {% endif %}
            <a href="/logout">Logout</a>
        </div>
        
        <h3>Quick Actions</h3>
        <ul>
            <li><a href="/profile?id={{ session.user_id }}">View Profile</a></li>
            <li><a href="/posts/new">Write New Post</a></li>
            <li><a href="/download?file=readme.txt">Download Resources</a></li>
        </ul>
    </div>
</body>
</html>
    ''')

# Search with XSS vulnerability
@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = []
    
    if query:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Search query
        sql_query = f"SELECT * FROM posts WHERE title LIKE '%{query}%' OR content LIKE '%{query}%'"
        try:
            cursor.execute(sql_query)
            results = cursor.fetchall()
        except:
            pass
        conn.close()
    
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>Search - TechBlog</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 5px; }
        .nav { margin: 20px 0; }
        .nav a { color: #1976d2; text-decoration: none; }
        input[type="text"] { width: 60%; padding: 8px; border: 1px solid #ddd; border-radius: 3px; }
        button { background: #1976d2; color: white; padding: 8px 15px; border: none; border-radius: 3px; }
        .result { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 3px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Search Community Posts</h2>
        <div class="nav"><a href="/">← Back to Home</a></div>
        
        <form method="GET">
            <input type="text" name="q" value="{{ query }}" placeholder="Search posts...">
            <button type="submit">Search</button>
        </form>
        
        {% if query %}
            <h3>Search Results for: {{ query|safe }}</h3>
            {% for post in results %}
                <div class="result">
                    <h4>{{ post[1]|safe }}</h4>
                    <p>{{ post[2]|safe }}</p>
                    <small>by {{ post[3] }}</small>
                </div>
            {% endfor %}
        {% endif %}
        
        <p><small>Try searching for: javascript, python, react, tutorials</small></p>
    </div>
</body>
</html>
    ''', query=query, results=results)

# Simple API endpoints
@app.route('/api')
def api_info():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>API Documentation - TechBlog</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 5px; }
        .nav { margin: 20px 0; }
        .nav a { color: #1976d2; text-decoration: none; }
        .endpoint { background: #f0f0f0; padding: 10px; margin: 10px 0; border-left: 4px solid #2196f3; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Developer API</h2>
        <div class="nav"><a href="/">← Back to Home</a></div>
        
        <h3>Available Endpoints</h3>
        
        <div class="endpoint">
            <strong>GET /api/users</strong><br>
            Get all users (no authentication required)
        </div>
        
        <div class="endpoint">
            <strong>GET /api/users/{id}</strong><br>
            Get specific user by ID
        </div>
        
        <div class="endpoint">
            <strong>GET /api/posts</strong><br>
            Get all posts
        </div>
        
        <p><a href="/api/users">Try /api/users</a></p>
    </div>
</body>
</html>
    ''')

@app.route('/api/users')
def api_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, role FROM users")
    users = cursor.fetchall()
    conn.close()
    
    # API endpoint for users
    return {
        'users': [
            {'id': user[0], 'username': user[1], 'email': user[2], 'role': user[3]}
            for user in users
        ]
    }

@app.route('/api/users/<int:user_id>')
def api_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return {
            'id': user[0],
            'username': user[1], 
            'password': user[2],
            'email': user[3],
            'role': user[4]
        }
    return {'error': 'User not found'}, 404

# Posts endpoint
@app.route('/posts')
def view_posts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conn.close()
    
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>Posts - TechBlog</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 5px; }
        .nav { margin: 20px 0; }
        .nav a { color: #1976d2; text-decoration: none; margin-right: 15px; }
        .post { border: 1px solid #ddd; padding: 15px; margin: 15px 0; border-radius: 3px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Community Posts</h2>
        <div class="nav">
            <a href="/">← Home</a>
            <a href="/posts/new">Write Post</a>
        </div>
        
        {% for post in posts %}
            <div class="post">
                <h3>{{ post[1]|safe }}</h3>
                <p>{{ post[2]|safe }}</p>
                <small>by {{ post[3] }} | <a href="/posts/{{ post[0] }}">View</a></small>
            </div>
        {% endfor %}
    </div>
</body>
</html>
    ''', posts=posts)

# Placeholder routes for other functionality
@app.route('/upload')
def upload_placeholder():
    return "File upload functionality - under development"

@app.route('/contact')
def contact_placeholder():
    return "Contact form - under development"

@app.route('/ping')
def ping_placeholder():
    return "Network tools - under development"

@app.route('/admin')
def admin_placeholder():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return "Admin dashboard - under development"

@app.route('/profile')
def profile_placeholder():
    return "User profiles - under development"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Initialize database on startup
init_db()

# Vercel handler
def handler(request):
    return app(request.environ, lambda *args: None)

if __name__ == '__main__':
    app.run(debug=True)
from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/tools')
def tools():
    return render_template('tools.html')




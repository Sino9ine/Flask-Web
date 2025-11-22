# src/app.py
from flask import Flask, render_template

app = Flask(__name__)

# 1. Home Page: Route '/'
@app.route('/')
def home():
    return render_template(
        'index.html',
        github="https://github.com/Sino9ine/Flask-Web.git",
        docker="https://hub.docker.com/repository/docker/sino9inebtw/flask-web/general"
    )

# 2. Git Page: Route '/git'
@app.route('/git')
def git_summary():
    return render_template('git.html')

# 3. Docker Page: Route '/docker'
@app.route('/docker')
def docker_summary():
    return render_template('docker.html')

if __name__ == '__main__':
    # รันบน host 0.0.0.0 และ port 5000 ตามมาตรฐาน Docker/Flask
    app.run(host='0.0.0.0', port=5000)

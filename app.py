from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db_url = os.environ.get('DATABASE_URL')
if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

with app.app_context(): db.create_all()

@app.route('/')
def home():
    tasks = Task.query.all()
    done_count = Task.query.filter_by(done=True).count()
    return render_template('index.html', todos=tasks, done=done_count, total=len(tasks))

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task')
    if task_text:
        new_task = Task(task=task_text)
        db.session.add(new_task)
        db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')
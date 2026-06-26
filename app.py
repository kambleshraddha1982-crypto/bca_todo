from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_tasks():
    if os.path.exists(DATA_FILE):
        return json.load(open(DATA_FILE))
    return []

def save_tasks(tasks):
    json.dump(tasks, open(DATA_FILE, 'w'))

@app.route('/')
def home():
    tasks = load_tasks()
    done_count = sum(1 for t in tasks if t['done'])
    return render_template('index.html', tasks=tasks, done=done_count, total=len(tasks))

@app.route('/add', methods=['POST'])
def add():
    tasks = load_tasks()
    task = request.form.get('task')
    if task:
        tasks.append({'task': task, 'done': False})
        save_tasks(tasks)
    return redirect('/')

@app.route('/done/<int:id>')
def done(id):
    tasks = load_tasks()
    tasks[id]['done'] = not tasks[id]['done']
    save_tasks(tasks)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    tasks = load_tasks()
    tasks.pop(id)
    save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':

    from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_tasks():
    if os.path.exists(DATA_FILE):
        return json.load(open(DATA_FILE))
    return []

def save_tasks(tasks):
    json.dump(tasks, open(DATA_FILE, 'w'))

@app.route('/')
def home():
    tasks = load_tasks()
    done_count = sum(1 for t in tasks if t['done'])
    return render_template('index.html', tasks=tasks, done=done_count, total=len(tasks))

@app.route('/add', methods=['POST'])
def add():
    tasks = load_tasks()
    task = request.form.get('task')
    if task:
        tasks.append({'task': task, 'done': False})
        save_tasks(tasks)
    return redirect('/')

@app.route('/done/<int:id>')
def done(id):
    tasks = load_tasks()
    tasks[id]['done'] = not tasks[id]['done']
    save_tasks(tasks)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    tasks = load_tasks()
    tasks.pop(id)
    save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, redirect, render_template # type: ignore
import os

app = Flask(__name__)

TASKS_FILE = 'tasks.txt'


if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as file:
        pass

@app.route('/')
def index():
    with open(TASKS_FILE, 'r') as file:
        tasks = file.readlines()
    tasks = [task.strip() for task in tasks]  
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    time = request.form['time']
    date = request.form['date']
    with open(TASKS_FILE, 'a') as file:
        file.write(f"{task} - {time} - {date}\n")
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    with open(TASKS_FILE, 'r') as file:
        tasks = file.readlines()
    tasks.pop(task_id)  
    with open(TASKS_FILE, 'w') as file:
        file.writelines(tasks)
    return redirect('/')

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    new_task = request.form['task']
    new_time = request.form['time']
    new_date = request.form['date']
    with open(TASKS_FILE, 'r') as file:
        tasks = file.readlines()
    tasks[task_id] = f"{new_task} - {new_time} - {new_date}\n"
    with open(TASKS_FILE, 'w') as file:
        file.writelines(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
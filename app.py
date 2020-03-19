from flask import Flask, jsonify, abort


app = Flask(__name__)

tasks = [{
    'id': 1,
    'title': u'Buy groceries',
    'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
    'done': False
}, {
    'id': 2,
    'title': u'Learn Python',
    'description': u'Need to find a good python tutorail',
    'done': False
}]

@app.route('/')
def index():
    return 'Hello'


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id']== task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({'task':task})


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, abort, make_response, request

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
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(task)
    return jsonify({'tasks': task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = list(filter(lambda t: t['id']==task_id, tasks))
    if len(task)==0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' not in request.json and type(request.json['title'])!= unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    
    task[0]['title']=request.json.get('title', task[0]['title'])
    task[0]['description']=request.json.get('description', task[0]['description'])
    task[0]['done']=request.json.get('done', task[0]['done'])

    return jsonify({'task':task[0]})



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not Found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
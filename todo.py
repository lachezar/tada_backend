from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager, helpers
from models import some_lame_dependancy_here

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
Task = some_lame_dependancy_here(db)['Task'] # how to get rid of this :/
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Task, methods=['GET', 'POST', 'PUT'])

@app.route('/')
def index():
    tasks = Task.query.all()
    tasks_dict = map(helpers.to_dict, tasks)
    return render_template('index.html', tasks=tasks, tasks_dict=tasks_dict)

if __name__ == '__main__':
    debug = True
    
    db.create_all()
    app.run(debug=debug)



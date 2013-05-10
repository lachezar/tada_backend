# -*- coding: utf-8 -*-

import os

from operator import itemgetter
from itertools import ifilterfalse

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from flask.ext.gzip import Gzip

from models import some_lame_dependancy_here
from utils import sort_tasks


# bootstrap the app
run_config = dict(host='0.0.0.0')
heroku_db_url = os.environ.get('HEROKU_POSTGRESQL_AMBER_URL')
if heroku_db_url:
    # heroku
    run_config['debug'] = False
    run_config['port'] = os.environ['PORT']
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = heroku_db_url
else:
    # local
    run_config['debug'] = True
    app = Flask(__name__,
                static_folder='devstatic',
                template_folder='devtemplates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# gzip response and static files
gzip = Gzip(app)
db = SQLAlchemy(app)
Task = some_lame_dependancy_here(db)['Task']
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Task, methods=['GET', 'POST', 'PUT', 'DELETE'])


@app.route('/test')
def test():
    db.create_all()
    return 'hello world! -> ' + repr(Task.query.all())


@app.route('/', methods=['GET'])
def index():
    # the actual order of the task is done via "linked list"-like structure
    tasks = Task.query.all()
    sorted_tasks_dict = sort_tasks(tasks)
    remaining = len(list(ifilterfalse(itemgetter('done'), sorted_tasks_dict)))

    return render_template('index.html',
                           tasks=sorted_tasks_dict,
                           remaining=remaining)


@app.route('/api/task/complete-all', methods=['PATCH'])
def completeAll():
    Task.query.update({'done': True})
    db.session.commit()
    return ''


if __name__ == '__main__':
    db.create_all()
    app.run(**run_config)

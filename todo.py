from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from models import some_lame_dependancy_here

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
Task = some_lame_dependancy_here(db)['Task']
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Task) # how to get rid of this :/

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    
    db.create_all()
    app.run(debug=True)

    # serve static files from the root in debug mode
    if app.config['DEBUG']:
        from werkzeug import SharedDataMiddleware
        import os
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
          '/assets/scripts/': os.path.join(os.path.dirname(__file__), 'scripts'),
          '/assets/styles/': os.path.join(os.path.dirname(__file__), 'styles'),
        })

def some_lame_dependancy_here(db):

    # how to lose this db.Model dependecny??
    # i tried with from flask.ext.sqlalchemy import Model, but no luck
    class Task(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.Text)
        done = db.Column(db.Boolean)
        order = db.Column(db.Integer)

        def __init__(self, title=None):
            self.title = title
            self.done = False

        def __repr__(self):
            return '<Task %r>' % self.title

    return {'Task': Task}
        
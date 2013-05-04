def some_lame_dependancy_here(db):

    # how to lose this db.Model dependecny??
    # i tried with from flask.ext.sqlalchemy import Model, but no luck
    class Task(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.Text)
        done = db.Column(db.Boolean)
        next_id = db.Column(db.Integer)

        def __init__(self, title, done, next_id):
            self.title = title
            self.done = done
            self.next_id = next_id

        def __repr__(self):
            return '<Task %r>' % self.title

    return {'Task': Task}
        
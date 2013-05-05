Tada backend
============

This is the backend for the [Tada](https://github.com/lucho870601/tada) project - a simplistic todo app created mainly to let me explore some new javascript frameworks and libraries.

The framework of choice is Flask with SQLAlchemy and Flask-Restless to handle the REST layer.

Even though the frontend is using Backbone, the initial page request will prerender all elements as plain html, so that there wont be any more requests to populate tasks, no delay and flickering. 

One cool thing I wanted to achieve, but failed is to use the same templates for Backbone and the backend. In this case I picked Mustache for the frontend, but decided to stick to Jinja2 for the backend, so I could not reuse any template code between frontend and backend.

Deploy to Heroku
----------------

0. Probably you need to setup Heroku account and upload SSH public keys, etc.
1. Clone [Tada](https://github.com/lucho870601/tada) and [Tada Backend](https://github.com/lucho870601/tada_backend) so that their directories are in the same main directory.
2. Get in the Tada folder and run `grunt heroku` which will copy all assets and html from the frontend in the backend.
3. Get in the Tada Backend folder and commit the changes (newly arrived assets and html) and then push to heroku `git push heroku master`.
4. Go to [http://ta-da.herokuapp.com/test](http://ta-da.herokuapp.com/test) to setup the database.

    or

Just clone [Tada Backend](https://github.com/lucho870601/tada_backend) and push it to Heroku, since all assets and html files are already there.


Demo
----

Check it out: [http://ta-da.herokuapp.com/](http://ta-da.herokuapp.com/)
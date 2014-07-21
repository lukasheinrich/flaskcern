import flask
app = flask.Flask(__name__)

import datetime

@app.route('/')
def homepage():
    print 'routing homepage'
    return flask.render_template('index.html',year=datetime.datetime.now().year)

@app.route('/<name>')
def page(name):
    return flask.render_template('{}.html'.format(name),year=datetime.datetime.now().year)
        
if __name__ == "__main__":
    app.run()
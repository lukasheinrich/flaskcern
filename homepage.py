import flask
app = flask.Flask(__name__)

import datetime

@app.route('/')
def homepage():
    return flask.render_template('index.html',year=datetime.datetime.now().year)
        
if __name__ == "__main__":
    app.run()
import flask
app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.redirect(flask.url_for('flasktutorial'))
    
@app.route('/flask')
def flasktutorial():
    return flask.render_template('index.html')
        
if __name__ == "__main__":
    app.run()
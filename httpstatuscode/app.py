from flask import Flask, abort, render_template
from . import model

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to httpstatusco.de'

@app.route('/<int:statuscode>')
def statuscode(statuscode):
    if statuscode not in model.statuscodes:
        abort(404)
    status = model.statuscodes[statuscode]
    return render_template('statuscode.html', status=status)

@app.errorhandler(404)
def statuscode_not_found(error):
    return render_template('not_found.html'), 404

if __name__ == '__main__':
    app.debug = False
    app.run()

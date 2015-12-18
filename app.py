from flask import Flask, abort
import model

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to httpstatusco.de'

@app.route('/<int:statuscode>')
def statuscode(statuscode):
    if statuscode not in model.statuscodes:
        abort(404)
    code = model.statuscodes[statuscode]
    return 'Your statuscode is %s' % code

if __name__ == '__main__':
    app.debug = True
    app.run()

from flask import Flask, abort
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to httpstatusco.de'

@app.route('/<int:statuscode>')
def statuscode(statuscode):
    if statuscode > 599:
        abort(404)
    return 'Your statuscode is %d' % statuscode

if __name__ == '__main__':
    app.run()

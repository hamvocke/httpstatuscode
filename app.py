from flask import Flask, abort, render_template
import model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

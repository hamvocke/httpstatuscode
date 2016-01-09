from flask import Flask, abort, render_template, request, flash, redirect, url_for
import model

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:statuscode>')
def statuscode(statuscode):
    if statuscode not in model.statuscodes:
        abort(404)
    status = model.statuscodes[statuscode]
    return render_template('statuscode.html', status=status)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    if not query:
        flash('Please enter a search term')
        return redirect(url_for('index'))
    elif query not in model.statuscodes:
        flash("Sorry, I don't know the statuscode %s" % query)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('statuscode', statuscode=query))


@app.errorhandler(404)
def statuscode_not_found(error):
    return render_template('not_found.html'), 404

if __name__ == '__main__':
    app.run()

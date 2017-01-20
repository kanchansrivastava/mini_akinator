from flask import Flask, jsonify
from flask.ext.api import status


app = Flask(__name__)
guesses = ['Python', 'Java', 'C++']
questions = ['Is it compiled?', 'Does it run on a VM?', 'Does it enforce indentation?']


@app.route('/')
def index():
    return 'Welcome to Mini Akinator!!'


@app.route('/guess/<int:id>')
def guess(id):
    return ('<h1>Mini Akinator!!</h1>'
            '<p>My guess: <i>{0}</i></p>').format(guesses[id])


@app.route('/question/<int:id>')
def question(id):
    # return '{0} What is correct answer? [Yes/No]'.format(questions[id])

    return jsonify(msg='{0} What is correct answer? [Yes/No]'.format(
        questions[id]), responseCode=status.HTTP_200_OK), status.HTTP_200_OK


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)






q
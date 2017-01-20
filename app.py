from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)
guesses = ['Python', 'Java', 'C++']
questions = ['Is it compiled?', 'Does it run on a VM?', 'Does it enforce indentation?']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess=guesses[id])


@app.route('/question/<int:id>')
def question(id):
    if id >= len(questions):
        return redirect(url_for('index'))
    else:
        return render_template('question.html', question=questions[id], question_number=id)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)







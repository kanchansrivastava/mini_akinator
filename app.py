from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import Form
from wtforms.fields import RadioField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'shhhh!!!secret'
guesses = ['Python', 'Java', 'C++']
questions = ['Is it compiled?', 'Does it run on a VM?', 'Does it enforce indentation?']


class YesNoQuestionForm(Form):
    answer = RadioField('Your answer', choices=[('yes', 'Yes'), ('no', 'No')])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess=guesses[id])


@app.route('/question/<int:id>', methods=['GET', 'POST'])
def question(id):
    form = YesNoQuestionForm()
    if form.validate_on_submit():
        if form.answer.data == 'yes':
            return redirect(url_for('question', id=id+1))
        else:
            return redirect(url_for('question', id=id))
    return render_template('question.html', question=questions[id], question_number=id, form=form)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)







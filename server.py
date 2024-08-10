from flask import Flask ,request ,render_template , redirect, url_for

app = Flask(__name__, template_folder='template')


@app.route('/')
def input_number():
    if request.method == 'POST':
        score = request.form.get('score')
        return redirect(url_for('call_function', count=score))
    return render_template('input.html')


@app.route('/call_function', methods=['POST', 'GET'])
def call_function():
    count = request.form.get('input_number', type=int)
    return render_template('score.html', count=count)

@app.route('/call_average', methods=['POST'])
def call_average():
    names = request.form.getlist('name')
    scores = request.form.getlist('score')
    scores_float = list(map(float, scores))
    average_scores = sum(scores_float) / len(scores_float) if scores_float else 0
    return render_template('average.html', names=names, scores=scores, average=average_scores, zip=zip)

if __name__ == '__main__':
    app.run(debug=True)

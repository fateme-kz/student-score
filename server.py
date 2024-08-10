from flask import Flask ,request ,render_template
from controler import stu_num

app = Flask(__name__, template_folder='template')


@app.route('/')
def input_number():
    return render_template('input.html')


@app.route('/call_function', methods=['POST' ])
def call_function():
    number = request.form.get('input_number', type=int)
    result = stu_num(number)
    return render_template('score.html')


if __name__ == '__main__':
    app.run(debug=True)
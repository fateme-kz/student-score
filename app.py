from flask import Flask ,request ,render_template , redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')

#configure the SQLite database
#database file will be created in the project
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
#disable modification tracking for performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize the SQLAlchemy object
db = SQLAlchemy(app)

#define a model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f'Student {self.name}'

@app.route('/')
def input_number():
    return render_template('input.html')
    
    
@app.route('/call_function', methods=['POST', 'GET'])
def call_function():
    if request.method == 'POST':
        count = request.form.get('input_number', type=int)
        # class_name = request.form.get('class_name')

        return render_template('score.html', count=count)
    
    return render_template('score.html', count=0)

@app.route('/call_average', methods=['POST', 'GET'])
def call_average():
    if request.method == 'POST':

        names = request.form.getlist('name')
        scores = request.form.getlist('score')
        scores_float = [float(score) for score in scores]
        average_scores = sum(scores_float) / len(scores_float) if scores_float else 0
        class_name = request.form.get('class_name')

        if names and class_name:
            for name, score in zip(names,scores_float):
                student = Student(class_name=class_name, name=name, score=score)   
                db.session.add(student)
                db.session.commit()

        return render_template('average.html', names=names, scores=scores, average=average_scores, zip=zip)
    
    else:
        students = Student.query.all()
        database = [{   
            'id': Student.id,  
            'name': Student.name,  
            'score': Student.score,
            'class_name': Student.class_name
        }for Student in students]

        return jsonify(database)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  #ensure database tables are created
    app.run(debug=True)
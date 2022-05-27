from flask import Flask,request, abort, jsonify
from flask_migrate import Migrate
from sqlalchemy.exc import SQLAlchemyError
from model import Interest, db, migrate, config, Student

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config["SQLALCHEMY_DATABASE_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    app.config['SECRET_KEY'] = config['SECRET_KEY']
    db.init_app(app)
    migrate = Migrate(app, db)
    return app

app = create_app()

@app.route('/students', methods=['GET'])
def view_students(limit=5, offset=0):
    students = Student.query.order_by(
        Student.id.desc()).limit(limit).offset(offset).all()
    students_f = [student.format() for student in students]
    return jsonify(students_f)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
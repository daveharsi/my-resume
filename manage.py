from flask_script import Manager
from myresume import app, db, Professor, Course

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    prof1 = Professor(name='Bert Gibbons', department='CISC')
    prof2 = Professor(name='Ellen Monk', department='MISY')
    course1 = Course(course_no='CISC437', title="Database Systems", description="Learn DBMS", professor=prof1)
    course2 = Course(course_no='CISC181', title="Intro to CS II", description="Learn OOP in Java", professor=prof1)
    course3 = Course(course_no='MISY261', title="Business Information Systems", description="Learn Business IS", professor=prof2)
    course4 = Course(course_no='MISY380', title="Enterprise Resource Planning Systems", description="Learn SAP", professor=prof2)
    db.session.add(prof1)
    db.session.add(prof2)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()



if __name__ == "__main__":
    manager.run()

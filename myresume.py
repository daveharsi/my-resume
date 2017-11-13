from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/courses')
def show_courses():
    courses = [
        ['CISC108', 'Introduction to Computer Science I', 'You will learn Scheme Racket.'],
        ['CISC181', 'Introduction to Computer Science II', 'You will learn OOP in Java.'],
        ['CISC220', 'Data Structures', 'You will learn data structures in C++.']
    ]
    return render_template('courses.html', courses=courses)


if __name__ == '__main__':
        app.run()

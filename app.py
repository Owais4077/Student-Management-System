from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
conn = mysql.connector.connect(host='localhost', user='root', password='', database='StudentDB')
cursor = conn.cursor()

# Home route
@app.route('/')
def index():
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    return render_template('index.html', students=students)

# Add student
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']
    cursor.execute("INSERT INTO Students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
    conn.commit()
    return redirect('/')

# Delete student
@app.route('/delete/<int:id>')
def delete_student(id):
    cursor.execute("DELETE FROM Students WHERE id = %s", (id,))
    conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

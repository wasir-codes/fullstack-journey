-- Active: 1778098401115@@127.0.0.1@3306@student_db
CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    year_joined YEAR NOT NULL,
    sex VARCHAR(20) NOT NULL,
    class VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
)

CREATE TABLE subjects (
    subject_id INT NOT NULL AUTO_INCREMENT,
    subject_name VARCHAR(50) NOT NULL,
    teacher_name VARCHAR(50) NOT NULL,
    credit_hours INT NOT NULL,
    PRIMARY KEY (subject_id)
)

CREATE TABLE grades (
    id INT NOT NULL AUTO_INCREMENT,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    grade DECIMAL(5,2) NOT NULL,
    exam_date DATE,
    PRIMARY KEY (id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
)

INSERT INTO students (first_name, last_name, date_of_birth, year_joined, sex, class)
VALUES 
('Arafat', 'Hossain', '2004-03-12', 2020, 'Male', '10A'),

('Nusrat', 'Jahan', '2005-07-25', 2021, 'Female', '9B'),

('Tanvir', 'Ahmed', '2003-11-08', 2019, 'Male', '11C'),

('Mim', 'Akter', '2004-01-19', 2020, 'Female', '10B'),

('Sabbir', 'Rahman', '2005-09-30', 2021, 'Male', '9A');

INSERT INTO subjects (subject_name, teacher_name, credit_hours)
VALUES
('Math', 'Rahim Uddin', 3),

('Physics', 'Shahadat Hossain', 4),

('English', 'Farzana Akter', 2);

INSERT INTO grades (student_id, subject_id, grade, exam_date)
VALUES
(1, 1, 85.50, '2025-01-15'),
(1, 2, 78.00, '2025-01-15'),

(2, 1, 88.75, '2025-01-16'),
(2, 3, 92.25, '2025-01-16'),

(3, 2, 74.50, '2025-01-17'),
(3, 3, 95.00, '2025-01-17'),

(4, 1, 67.25, '2025-01-18'),
(4, 2, 81.50, '2025-01-18'),

(5, 3, 89.00, '2025-01-19'),
(5, 1, 72.75, '2025-01-19');

SELECT * FROM students;
SELECT * FROM subjects;
SELECT * FROM grades;

-- Query 1: Write a query that shows each student's full name alongside their grade and the subject name. You'll need a JOIN between all three tables.

SELECT students.first_name, students.last_name, subjects.subject_name, grades.grade
FROM grades
INNER JOIN students ON grades.student_id = students.id
INNER JOIN subjects ON grades.subject_id = subjects.subject_id

-- Query 2: Find the average grade for each subject. Use AVG() and GROUP BY. Output should show subject name and average grade.

SELECT subject_name, ROUND(AVG(grade), 2) AS average_grade
FROM grades
INNER JOIN subjects ON grades.subject_id = subjects.subject_id
GROUP BY subject_name

-- Query 3: Find the highest and lowest grade in the entire grades table. Use MAX() and MIN(). No JOIN needed, no GROUP BY needed. One line SELECT.

SELECT ROUND(MAX(grade), 2) AS highest_grade, ROUND(MIN(grade), 2) AS lowest_grade FROM grades

-- Query 4: Show all students who scored above 80, with their full name, subject name, and grade. You need a JOIN and a WHERE clause.

SELECT first_name, last_name, subject_name, grade
FROM grades
INNER JOIN students ON grades.student_id = students.id
INNER JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE grade > 80

-- Query 5: Show each student's full name and their total number of grades recorded. Use COUNT() and GROUP BY. Order the results from most grades to least using ORDER BY ... DESC.

SELECT first_name, last_name, COUNT(grade) AS total_grades
FROM grades
INNER JOIN students ON grades.student_id = students.id
GROUP BY first_name, last_name
ORDER BY COUNT(grade) DESC

-- Query 6: Show the student with the highest average grade across all subjects. Use AVG(), GROUP BY, and ORDER BY DESC with LIMIT 1.

SELECT first_name, last_name, ROUND(AVG(grade), 2) AS average_grade
FROM grades
INNER JOIN students ON grades.student_id = students.id
GROUP BY first_name, last_name
ORDER BY average_grade DESC
LIMIT 1

-- Query 7: Show all students and their grades, but this time only for the subject "Math". Filter by subject name using WHERE.

SELECT first_name, last_name, grade, subject_name
FROM grades
INNER JOIN students ON grades.student_id = students.id
INNER JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE subjects.subject_name = 'Math'

-- Query 8: Show the number of students per class. Just use the students table — no JOIN needed. Use COUNT() and GROUP BY class.

SELECT class, count(id) AS student_count
FROM students
GROUP BY class
ORDER BY class ASC

-- Query 9: Show only the subjects where the average grade is above 80. You need AVG(), GROUP BY, and HAVING.

SELECT subject_name, ROUND(AVG(grade), 2) AS average_grade
FROM grades
INNER JOIN subjects ON grades.subject_id = subjects.subject_id
GROUP BY subject_name
HAVING average_grade > 80
ORDER BY average_grade ASC

-- Query 10: Show all students who have NOT been assigned any grade yet. Use a LEFT JOIN between students and grades, and filter with WHERE grades.id IS NULL.

SELECT first_name, last_name
FROM students
LEFT JOIN grades ON students.id = grades.student_id
WHERE grades.id IS NULL

-- For Query 10 testing:
INSERT INTO students (first_name, last_name, date_of_birth, year_joined, sex, class)
VALUES ('Rahim', 'Uddin', '2004-06-15', 2021, 'Male', '9C');

DELETE FROM students WHERE first_name = 'Rahim';
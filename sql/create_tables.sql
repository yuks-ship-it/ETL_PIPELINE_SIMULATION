CREATE DATABASE IF NOT EXISTS student_etl;

USE student_etl;

CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade CHAR(1),
    email VARCHAR(150),
    department VARCHAR(50)
);

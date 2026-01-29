ETL Pipeline Simulation (Python & SQL)

Project Overview

This project is a simulation of an ETL (Extract, Transform, Load) pipeline built using Python, Pandas, and MySQL.
It demonstrates how raw student data is extracted from a database, transformed using Python, and loaded back into the database for further analysis.
The project is designed for learning and demonstration purposes, focusing on real-world data engineering concepts such as data cleaning, filtering, and database integration.

Objectives :-

Understand the ETL process step by step,
Extract student data from a MySQL database,
Transform data using Pandas,
Filter students based on grade conditions,
Load the transformed data back into the database,
Practice Python–SQL integration,
Learn basic Git & GitHub workflow,

Technologies Used:-

Python 
Pandas
MySQL
MySQL Workbench
Git & GitHub

 Project Structure:-
ETL-Pipeline-Simulation/
│
├── data/
│   └── students.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── database/
│   └── db_connection.py
│
├── requirements.txt
└── README.md

 ETL Workflow Explanation:-
 
1️⃣ Extract
Connects to the MySQL database
Reads data from the students table
Loads the data into a Pandas DataFrame

2️⃣ Transform

Handles missing values

Converts text to lowercase and strips whitespace

Filters students whose grade is greater than B

Cleans and prepares data for loading

3️⃣ Load

Inserts the transformed data back into MySQL

Updates or stores results in the existing table

🗄️ Database Schema (Example)
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(2),
    email VARCHAR(100),
    department VARCHAR(50)
);

🚀 How to Run the Project
Step 1: Clone the Repository
git clone https://github.com/your-username/ETL-Pipeline-Simulation.git
cd ETL-Pipeline-Simulation

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Configure Database

Update MySQL credentials in db_connection.py

Make sure MySQL server is running

Step 4: Run ETL Scripts
python extract.py
python transform.py
python load.py

📊 Sample Transformation Logic
df = df[df["grade"] < "B"]

📈 Learning Outcomes

Practical understanding of ETL pipelines

Hands-on experience with Pandas & MySQL

Data filtering and transformation skills

Basic GitHub project management

Foundation for advanced data engineering projects

📌 Future Enhancements

Add logging and error handling

Automate ETL using schedulers

Use large datasets

Add data validation checks

Deploy using Docker

👨‍💻 Author

Yukesh Dhakal
Student | Python & Data Engineering Learner

⭐ Acknowledgements

This project was created for educational purposes to understand ETL concepts and real-world data processing workflows.

import sqlite3 as sq

with sq.connect('deanary.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS faculties (
        id_faculty INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS departments (
        id_departments INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        id_faculty INTEGER NOT NULL,
        FOREIGN KEY (id_faculty) REFERENCES faculties (id_faculty)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS specialities (
        id_speciality INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        id_departments INTEGER NOT NULL,
        FOREIGN KEY (id_departments) REFERENCES departments (id_departments)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS subjects (
        id_subject INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL
    )""")
        
    cur.execute("""CREATE TABLE IF NOT EXISTS submission_form (
        id_submission_form INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL
    )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS syllabus(
        id_syllabus INTEGER PRIMARY KEY AUTOINCREMENT,
        id_speciality INTEGER,
        id_subject INTEGER NOT NULL,
        id_submission_form INTEGER NOT NULL,
        number_of_lecture_hours INTEGER,
        number_of_practical_hours INTEGER,
        number_of_laboratory_hours INTEGER,
        course_work BOOL NOT NULL,
        FOREIGN KEY (id_speciality) REFERENCES specialities (id_speciality),
        FOREIGN KEY (id_subject) REFERENCES subjects (id_subject),
        FOREIGN KEY (id_submission_form) REFERENCES submission_form (id_submission_form)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS applicants (
        id_applicant INTEGER PRIMARY KEY AUTOINCREMENT,
        surname TEXT NOT NULL,
        name TEXT NOT NULL,
        patronymic TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        birthday DATETIME,
        address TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        email TEXT NOT NULL,
        data_postupleniya DATETIME,
        speciality VARCHAR,
        FOREIGN KEY (speciality) REFERENCES specialities (name)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS study_card (
        id_study_card INTEGER PRIMARY KEY AUTOINCREMENT,
        FIO_student TEXT NOT NULL,
        groupp INTEGER NOT NULL,
        speciality TEXT NOT NULL,
        subjects TEXT NOT NULL,
        submission_form VARCHAR NOT NULL,
        grade INTEGER,
        FOREIGN KEY (subjects) REFERENCES subjects (name),
        FOREIGN KEY (submission_form) REFERENCES submission_form (name)
    )""")

    
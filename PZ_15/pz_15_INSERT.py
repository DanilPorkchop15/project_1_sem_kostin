import sqlite3 as sq
from data_pz_15 import *

with sq.connect('deanary.db') as con:
    cur = con.cursor()

    cur.executemany("INSERT INTO faculties VALUES (?, ?)", info_faculties)
    cur.executemany("INSERT INTO departments VALUES (?, ?, ?)", info_departments)
    cur.executemany("INSERT INTO specialities VALUES (?, ?, ?)", info_specialities)
    cur.executemany("INSERT INTO subjects VALUES (?, ?)", info_subjects)
    cur.executemany("INSERT INTO submission_form VALUES (?, ?)", info_submission_form)
    cur.executemany("INSERT INTO syllabus VALUES (?, ?, ?, ?, ?, ?, ?, ?)", info_syllabus)
    cur.executemany("INSERT INTO applicants VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", info_applicants)
    cur.executemany("INSERT INTO study_card VALUES (?, ?, ?, ?, ?, ?, ?)", info_study_card)
    


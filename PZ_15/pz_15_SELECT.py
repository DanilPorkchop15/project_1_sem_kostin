import sqlite3 as sq

with sq.connect('deanary.db') as con:
    cur = con.cursor()
    # Запросы на выборку данных

    # 1. Вывести список всех студентов, зачисленных на факультет, с указанием номера группы.
    cur.execute("SELECT * FROM study_card")
    all_students = cur.fetchall()
    print(all_students)
    # 2. Вывести список всех специальностей факультета и количество студентов, обучающихся по каждой из них.
    cur.execute("""SELECT id_speciality, name, 
    (SELECT COUNT(applicants.speciality) FROM applicants 
    WHERE applicants.speciality = specialities.name) 
    FROM specialities""")
    spec_students = cur.fetchall()
    print(spec_students)

    # 3. Вывести список всех кафедр факультета и количество студентов, обучающихся на каждой кафедре.
    cur.execute("""SELECT *, 
    (SELECT (SELECT COUNT(applicants.speciality) FROM applicants 
    WHERE applicants.speciality =specialities.name) FROM specialities
    WHERE specialities.id_departments = departments.id_departments)
    FROM departments
    """)
    deps_studs =  cur.fetchall()
    print(deps_studs)

    # 4. Вывести список всех предметов и количество часов, выделенных на каждый предмет в учебном плане каждой специальности.
    cur.execute("""SELECT *, 
    (SELECT (number_of_lecture_hours + number_of_practical_hours + number_of_laboratory_hours) 
    FROM syllabus WHERE syllabus.id_subject = subjects.id_subject) 
    FROM subjects
    """)
    print(cur.fetchall())

    # 5. Вывести список всех студентов, у которых есть неудовлетворительные оценки (меньше 4) по любому предмету.
    cur.execute("SELECT id_study_card, FIO_student, grade FROM study_card WHERE grade < 4")
    print(cur.fetchall()) 

    # 6. Вывести список всех предметов, которые изучают студенты первого курса.
    cur.execute("SELECT * FROM study_card WHERE groupp LIKE '1%'")
    print(cur.fetchall())

    # 7. Вывести список всех студентов, которые сдают курсовую работу в этом семестре.
    cur.execute("SELECT * FROM study_card WHERE submission_form = 'Курсовая работа'")
    print(cur.fetchall())

    # 8. Вывести список всех абитуриентов, зачисленных на специальность "Информатика и вычислительная техника".
    # вместо специальности "Информатика и вычислительная техника" - "ИС"
    cur.execute("SELECT * FROM applicants WHERE speciality = 'ИС'")
    print(cur.fetchall())

    # 9. Вывести список всех предметов, которые изучают студенты группы 101.
    # вместо группы 101 - группа 11
    cur.execute("SELECT subjects FROM study_card WHERE groupp = 11")
    print(cur.fetchall())
    
    # 10. Вывести список студенто и их оценки за все предметы на специальности "Программная инженерия"
    # вместо программная инженерия - ПЛА
    cur.execute("SELECT id_study_card, FIO_student, speciality, subjects, grade FROM study_card WHERE speciality = 'ПЛА'")
    print(cur.fetchall())

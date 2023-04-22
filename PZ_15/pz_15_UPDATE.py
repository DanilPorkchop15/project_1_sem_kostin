import sqlite3 as sq

with sq.connect('deanary.db') as con:
    cur = con.cursor()
        
       # Обновление названия факультета с id=1 на "Новый факультет"
    cur.execute("UPDATE faculties SET name = 'Новый факультет' WHERE id_faculty = 1") #1
    
    # Обновление названия кафедры с id=2 на "Новая кафедра"
    cur.execute("UPDATE departments SET name = 'Новая кафедра' WHERE id_departments = 2") #2
    
    # Обновление названия специальности с id=3 на "Новая специальность"
    cur.execute("UPDATE specialities SET name = 'Новая специальность' WHERE id_speciality = 3") #3
    
    # Обновление названия предмета с id=4 на "Новый предмет"
    cur.execute("UPDATE subjects SET name = 'Новый предмет' WHERE id_subject = 4") #4
    
    # Обновление названия формы сдачи предмета с id=5 на "Новая форма сдачи"
    cur.execute("UPDATE submission_form SET name = 'Новая форма сдачи' WHERE id_submission_form = 5") #5
    
    # Обновление количества лекционных часов на 30 для учебного плана с id=6
    cur.execute("UPDATE syllabus SET number_of_lecture_hours = number_of_lecture_hours + 30  WHERE id_syllabus = 6") #6
    
    # Обновление количества лекционных часов у предмета "математика" на учебном плане специальности "ИБТ"
    cur.execute("UPDATE syllabus SET number_of_lecture_hours = number_of_lecture_hours + 5 WHERE id_speciality = 2 AND id_subject = 3") #7
    
    # Обновление количества лабораторных часов и формы сдачи предмета у специальности "СА" для предмета "программирование"
    cur.execute("UPDATE syllabus SET number_of_laboratory_hours = number_of_laboratory_hours +10 WHERE id_speciality = 5 AND id_subject = 15") #8
    
    # Обновление количества лекционных и практических часов у предмета "информатика" на учебном плане кафедры "Информационный"
    cur.execute('''UPDATE syllabus 
    SET number_of_lecture_hours = number_of_lecture_hours + 5, 
    number_of_practical_hours = number_of_practical_hours + 5 
    WHERE id_subject = 20 AND id_speciality IN (SELECT id_departments FROM specialities WHERE id_departments = 9) ''') #9
    
    # Обновить кол-во лекционных часов для всех предметов, где количество лекционных часов больше 30
    cur.execute("UPDATE syllabus SET number_of_lecture_hours = number_of_lecture_hours + 10 WHERE number_of_lecture_hours > 30") #10
    
    # Обновить фамилию и имя абитуриента по его идентификатору
    cur.execute("UPDATE applicants SET name = 'Виктор',  surname = 'Баранов' WHERE id_applicant = 7") #11
    
    #  Обновить название кафедры для всех специальностей, где кафедра имеет id = 1
    cur.execute("UPDATE departments SET name = 'Кафедра' WHERE id_departments = 1") #12
    
    #Обновить оценку по определенному предмету и форме сдачи для конкретного студента
    cur.execute("UPDATE study_card SET grade = 5  WHERE submission_form = 'Взятка' AND FIO_student = 'Клименко Олег Юрьевич' ") #13
    
    # Обновить название специальности для всех студентов, где специальность имеет id = 2
    cur.execute("UPDATE study_card SET speciality = 'Специальность' WHERE speciality = (SELECT name FROM specialities WHERE id_speciality = 2)") #14
    
    # Обновить все оценки студента с именем "Иван" на предмете "Математика" на значение 5
    cur.execute("UPDATE study_card SET grade = 2  WHERE FIO_student LIKE 'Иван' AND subjects = 'математика' ") #15
    
    # Обновить название факультета на "Факультет информационных технологий" для всех кафедр, относящихся к этому факультету
    cur.execute("UPDATE faculties SET name = 'Факультет информационных технологий' WHERE id_faculty = 6") #16
    
    # . Обновить количество лабораторных часов на предмете "Информатика" для специальности "ВБ" на 30
    cur.execute("UPDATE syllabus SET number_of_laboratory_hours = 30 WHERE id_subject = 20 AND id_speciality = 11") #17
import sqlite3 as sq

with sq.connect('deanary.db') as con:
    cur = con.cursor()

import sqlite3 as sq

with sq.connect('deanary.db') as con:
    cur = con.cursor()

    # SQL-запросы на удаление данных из БД
    ## Удалить всех абитуриентов, у которых дата поступления ранее 2020 года.
    # cur.execute("DELETE FROM applicants WHERE data_postupleniya < '2021-01-01' ")
    ## Удалить все учебные планы, которые не связаны ни с одной специальностью.
    # cur.execute("DELETE FROM syllabus WHERE id_speciality IS NULL")
    ## Удалить все кафедры, которые не относятся ни к одному факультету.
    # cur.execute("DELETE FROM departments WHERE id_faculty IS NULL")
    ## Удалить все предметы, которые не входят ни в один учебный план.
    # cur.execute("DELETE FROM syllabus WHERE id_subject NOT IN (SELECT id_subject FROM syllabus)")
    ## Удалить всех студентов, не имеющих оценок.
    # cur.execute("DELETE FROM study_card WHERE grade IS NULL")
    ## Удалить все записи из таблицы "Учебная карточка" для предмета "Математика" с формой сдачи "Экзамен"
    # cur.execute("DELETE FROM study_card WHERE subjects = 'математика' AND submission_form = 'Экзамен'")
    ## Удалить все записи из таблицы "Учебная карточка" для студентов, обучающихся на факультете "Информационных технологий"
    # cur.execute("DELETE FROM study_card WHERE speciality IN (SELECT name FROM specialities WHERE id_departments =4)")
    ## Удалить все записи из таблицы "Учебная карточка" для студентов, не сдавших ни одного экзамена
    # cur.execute("DELETE FROM study_card WHERE grade = 2 OR grade IS NULL")
    ## Удалить всех абитуриентов, которые не поступили на заданную специальность
    # cur.execute("DELETE FROM applicants WHERE speciality IS NULL AND data_postupleniya IS NULL")
    ##Удалить все учебные карточки, связанные с предметом, который больше не входит в учебный план по заданной специальности
    ## 10 cur.execute("DELETE FROM study_card WHERE ") невозможен
    ## Удалить всех абитуриентов, не сдавших заданный предмет
    ## 11cur.execute("DELETE FROM applicants WHERE ") невозможен
    ## Удалить все учебные карточки, связанные с заданным преподавателем
    ## 12 cur.execute("DELETE FROM study_card WHERE ") невозможен
    ## Удалить все учебные карточки, связанные с заданной формой сдачи предмета
    # cur.execute("DELETE FROM study_card WHERE submission_form = 'Беседа'")
    ## Удалить всех абитуриентов, не зачисленных на заданную специальность
    # cur.execute("DELETE FROM applicants WHERE speciality IS NULL")
    ## Удалить всех абитуриентов, которые подавали заявку на специальность с названием "Информатика", вместе с их учебными карточками
    # cur.execute("DELETE FROM  study_card WHERE speciality = 'БУ' AND grade < 4 AND subjects = 'информатика'")
    ## Удалить всех студентов, которые учатся на специальности "Информационные технологии" и сдали экзамен по предмету "Алгоритмы и структуры данных" на
    ## более низкую оценку, вместе с их учебными карточками
    # cur.execute("DELETE FROM study_card WHERE subjects = 'физика' AND grade IS NULL")
    ## Удалить всех студентов, которые не сдали экзамен по предмету "Физика" в установленный срок, вместе с их учебными карточками
    ## 17 невозможен

    
import tkinter as tk
import sqlite3

BORDER_COLOR = 'gray'
DB_PATH = '/Users/zaur/Documents/GitHub/WebSchool/WebSchool/db.sqlite3'
selected_course = None

def select_courses():
    try:
        sqlite_connection = sqlite3.connect(DB_PATH)
        cursor = sqlite_connection.cursor()
        print("Соединение SQLite установлено")
        select_query = "SELECT * FROM school_course"
        cursor.execute(select_query)

        courses = cursor.fetchall()
        cursor.close()
        print("Курсы взяты")

        return courses
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        return None
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def select_students():
    try:
        sqlite_connection = sqlite3.connect(DB_PATH)
        cursor = sqlite_connection.cursor()
        print("Соединение SQLite установлено")
        select_query = "SELECT id, username, first_name, last_name FROM auth_user"
        cursor.execute(select_query)

        students = cursor.fetchall()
        cursor.close()

        print("Студенты взяты")
        return students
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        return None
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def select_students_from_course(id_course):
    try:
        sqlite_connection = sqlite3.connect(DB_PATH)
        cursor = sqlite_connection.cursor()

        select_query_for_students_id = f"SELECT id_student FROM school_groups WHERE id_course = {id_course}"
        cursor.execute(select_query_for_students_id)

        id_students = cursor.fetchall()
        if len(id_students) == 0:
            return None

        select_query_for_students = f"SELECT id, username, first_name, last_name FROM auth_user WHERE id = {id_students[0][0]}"
        for id in range(1, len(id_students)):
            select_query_for_students += f" OR id = {id_students[id][0]}"

        cursor.execute(select_query_for_students)
        students = cursor.fetchall()
        cursor.close()

        return students
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        return None
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def insert_to_groups(id_student, id_course):
    try:
        sqlite_connection = sqlite3.connect(DB_PATH)
        cursor = sqlite_connection.cursor()

        insert_query = f"INSERT INTO school_groups(id_student, id_course) VALUES " \
                       f"('{id_student}', '{id_course}')"
        cursor.execute(insert_query)

        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        return None
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def delete_group(id_student, id_course):
    try:
        sqlite_connection = sqlite3.connect(DB_PATH)
        cursor = sqlite_connection.cursor()

        delete_query = f"DELETE FROM school_groups WHERE id_student = {id_student} AND id_course = {id_course}"
        cursor.execute(delete_query)

        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        return None
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def load_courses():
    courses = select_courses()
    if courses is None:
        return
    lbox_courses.delete(0, tk.END)
    for i in courses:
        lbox_courses.insert(tk.END, f"{i[0]} {i[1]}")


def load_students():
    students = select_students()
    if students is None:
        return
    lbox_students.delete(0, tk.END)
    for i in students:
        lbox_students.insert(tk.END, f"{i[0]} {i[2]} {i[3]} {i[1]}")


def lbox_selected_course(event):
    if len(lbox_courses.curselection()) == 0:
        return
    else:
        selected_item = lbox_courses.get(lbox_courses.curselection()[0])
        id_course = int(selected_item.split()[0])
        students = select_students_from_course(id_course)

        global selected_course
        selected_course = id_course

        lbox_students_on_course.delete(0, tk.END)
        if students is not None:
            for i in students:
                lbox_students_on_course.insert(tk.END, f"{i[0]} {i[2]} {i[3]} {i[1]}")


def click_add_to_group():
    if selected_course is None or len(lbox_students.curselection()) == 0:
        return
    else:
        selected_item = lbox_students.get(lbox_students.curselection()[0])
        id_student = int(selected_item.split()[0])

        students_on_course = lbox_students_on_course.get(0, tk.END)
        for student in students_on_course:
            if int(student.split()[0]) == id_student:
                return

        insert_to_groups(id_student, selected_course)

        lbox_students_on_course.insert(tk.END, selected_item)


def click_delete_from_group():
    if selected_course is None or len(lbox_students_on_course.curselection()) == 0:
        return
    else:
        selected_item = lbox_students_on_course.get(lbox_students_on_course.curselection()[0])
        id_student = int(selected_item.split()[0])

        delete_group(id_student, selected_course)
        lbox_students_on_course.delete(lbox_students_on_course.curselection()[0])


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Группы")

    # ======Courses======

    frame_courses = tk.Frame(window, bg="green")
    frame_courses.place(x=0, y=0, width=240, height=450)

    lbl_courses = tk.Label(frame_courses, text="Курсы")
    lbl_courses.pack(side="top")

    lbox_courses = tk.Listbox(frame_courses)
    load_courses()
    lbox_courses.bind('<<ListboxSelect>>', lbox_selected_course)

    lbox_courses.pack(side="top")

    lbl_students_on_course = tk.Label(frame_courses, text="Ученики на курсе")
    lbl_students_on_course.pack(side="top")

    lbox_students_on_course = tk.Listbox(frame_courses)
    lbox_students_on_course.pack(side="top")

    # ======Students======

    frame_students = tk.Frame(window, bg="pink")
    frame_students.place(x=250, y=0, width=250, height=250)

    lbl_students = tk.Label(frame_students, text="Ученики")
    lbl_students.pack(side="top")

    lbox_students = tk.Listbox(frame_students)
    lbox_students.pack(side="top")
    load_students()

    # ======Panel======

    frame_panel = tk.Frame(window, bg="gray")
    frame_panel.place(x=250, y=260, width=250, height=190)

    btn_add_to_group = tk.Button(frame_panel, text='Добавить в группу', command=click_add_to_group)
    btn_add_to_group.pack(side='top', pady=30)

    btn_delete_from_group = tk.Button(frame_panel, text='Удалить из группы', command=click_delete_from_group)
    btn_delete_from_group.pack(side='top')

    window.mainloop()
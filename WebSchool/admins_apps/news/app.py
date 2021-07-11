import tkinter as tk
import sqlite3

BORDER_COLOR = 'gray'
DB_PATH = '/Users/zaur/Documents/GitHub/WebSchool/WebSchool/db.sqlite3'


def insert_course(title: str, content: str, author: str, img: str):
    try:
        sqlite_connection = sqlite3.connect(DB_PATH)
        cursor = sqlite_connection.cursor()
        print('Соединение с SQLite установлено.')
        insert_query = f"insert into school_news(title, content, author, img) " \
                       f"VALUES ('{title}', '{content}', '{author}', '{img}')"
        cursor.execute(insert_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def select_news():
    try:
        sqlite_connection = sqlite3.connect(DB_PATH)
        cursor = sqlite_connection.cursor()
        print('Соединение с SQLite установлено.')
        select_query = f"SELECT id, title FROM school_news"
        cursor.execute(select_query)
        data = cursor.fetchall()
        cursor.close()

        return data

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        return None
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def click_add():
    title = ent_title.get()
    content = str(txt_content.get('1.0', 'end')).strip('\n')
    author = ent_author.get()
    img = ent_img.get()

    insert_course(title, content, author, img)
    load_news()


def load_news():
    data = select_news()
    if data is None:
        return
    print(data)
    for i in data:
        lbox.insert(tk.END, str(i[0]) + " " + str(i[1]))


if __name__ == "__main__":
    window = tk.Tk()
    window.title('Новости')
    window.geometry('800x450')

    frame_add = tk.Frame(window)
    frame_add.place(x=0, y=0)

    lbl_add_main = tk.Label(frame_add, text='Добавить новость', font='Times 30')
    lbl_add_main.grid(row=0, column=0)

    lbl_title = tk.Label(frame_add, text='Заголовок')
    lbl_title.grid(row=1, column=0)

    ent_title = tk.Entry(frame_add, highlightbackground=BORDER_COLOR)
    ent_title.grid(row=2, column=0)

    lbl_content = tk.Label(frame_add, text='Описание')
    lbl_content.grid(row=3, column=0)

    txt_content = tk.Text(frame_add, width=50, height=10, highlightbackground=BORDER_COLOR)
    txt_content.grid(row=4, column=0)

    lbl_author = tk.Label(frame_add, text='Автор')
    lbl_author.grid(row=5, column=0)

    ent_author = tk.Entry(frame_add, highlightbackground=BORDER_COLOR)
    ent_author.grid(row=6, column=0)

    lbl_img = tk.Label(frame_add, text='Изображение')
    lbl_img.grid(row=7, column=0)

    ent_img = tk.Entry(frame_add, highlightbackground=BORDER_COLOR)
    ent_img.grid(row=8, column=0)

    btn_add = tk.Button(frame_add, text='Добавить', command=click_add)
    btn_add.grid(row=9, column=0)

    # -------------------------------------------
    frame_delete = tk.Frame(window)
    frame_delete.place(x=400, y=0, width=300)

    lbl_delete_main = tk.Label(frame_delete, text='Удалить новость', font='Times 30', highlightbackground=BORDER_COLOR)
    lbl_delete_main.pack(side='top')

    lbox = tk.Listbox(frame_delete)
    lbox.pack()

    load_news()

    window.mainloop()

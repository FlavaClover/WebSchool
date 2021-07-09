import tkinter as tk
import sqlite3

BORDER_COLOR = 'gray'
DB_PATH = '/Users/zaur/Documents/GitHub/WebSchool/WebSchool/db.sqlite3'


def insert_course(name: str, desc: str, price: int):
    try:
        sqlite_connection = sqlite3.connect(DB_PATH)
        cursor = sqlite_connection.cursor()
        print('Соединение с SQLite установлено.')
        insert_query = f"insert into school_course(name, description, price) VALUES ('{name}', '{desc}', '{price}')"
        cursor.execute(insert_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def click_add():
    name = ent_name.get()
    desc = str(txt_desc.get('1.0', 'end')).strip('\n')
    price = ent_price.get()

    

    insert_course(name, desc, price)


if __name__ == "__main__":
    window = tk.Tk()
    window.title('Курсы')
    window.geometry("500x350")

    lbl_main = tk.Label(window, text='Добавить курс', font='Times 30')
    lbl_main.pack(side='top')

    lbl_name = tk.Label(window, text='Название')
    lbl_name.pack()

    ent_name = tk.Entry(window, highlightbackground=BORDER_COLOR)
    ent_name.pack()

    lbl_desc = tk.Label(window, text='Название')
    lbl_desc.pack()

    txt_desc = tk.Text(window, width=50, height=10,  highlightbackground=BORDER_COLOR)
    txt_desc.pack()

    lbl_price = tk.Label(window, text='Цена')
    lbl_price.pack()

    ent_price = tk.Entry(window,  highlightbackground=BORDER_COLOR)
    ent_price.pack()

    btn_add = tk.Button(window, text='Добавить', command=click_add)
    btn_add.pack()

    window.mainloop()
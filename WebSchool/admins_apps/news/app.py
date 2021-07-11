import tkinter as tk
import sqlite3

BORDER_COLOR = 'gray'
DB_PATH = '/Users/zaur/Documents/GitHub/WebSchool/WebSchool/db.sqlite3'

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

    btn_add = tk.Button(frame_add, text='Добавить')
    btn_add.grid(row=7, column=0)

    # -------------------------------------------
    frame_delete = tk.Frame(window)
    frame_delete.place(x=400, y=0, width=300)

    lbl_delete_main = tk.Label(frame_delete, text='Удалить новость', font='Times 30', highlightbackground=BORDER_COLOR)
    lbl_delete_main.pack(side='top')

    lbox = tk.Listbox(frame_delete)
    lbox.pack()

    window.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from student import Student
from database.database import *


color = "#dde"

window = Tk()
window.title("Cadastro de Alunos")
window.geometry("524x490")
window.config(bg=color)
window.wm_maxsize(width=524, height=490)
window.wm_minsize(width=524, height=490)


#### -- SALVAR NO BANCO DE DADOS -- ####
def include():
    name = entry_name.get().upper()
    mat = entry_mat.get()
    note1 = entry_note1.get()
    note2 = entry_note2.get()
    note3 = entry_note3.get()
    note4 = entry_note4.get()
    if (
        name != ""
        and mat != ""
        and note1 != ""
        and note2 != ""
        and note3 != ""
        and note4 != ""
    ):
        if (
            (float(note1) <= 10)
            and (float(note2) <= 10)
            and (float(note3) <= 10)
            and (float(note4) <= 10)
        ):
            student = Student(mat, name, note1, note2, note3, note4)
            insert_students_database(student)
            update_treview()
            entry_name.delete(0, END)
            entry_mat.delete(0, END)
            entry_note1.delete(0, END)
            entry_note2.delete(0, END)
            entry_note3.delete(0, END)
            entry_note4.delete(0, END)
        else:
            messagebox.showinfo(
                title="Nota invalido",
                message="Favor informar uma nota valido de 0 a 10",
            )
    else:
        messagebox.showinfo(
            title="Campo vazio", message="Favor preencher todos os campos"
        )


#### -------- ATERAR VALOR -------- ####
def get_data_student():
    try:
        select_student = tv.selection()[0]
        value = tv.item(select_student, "values")
        return value
    except:
        messagebox.showinfo(
            title="Aluno não foi informado", message="Favor selecionar um aluno"
        )


def get_new_data():
    try:
        name = entry_name.get().upper()
        mat = entry_mat.get()
        note1 = entry_note1.get()
        note2 = entry_note2.get()
        note3 = entry_note3.get()
        note4 = entry_note4.get()
        entry_name.delete(0, END)
        entry_mat.delete(0, END)
        entry_note1.delete(0, END)
        entry_note2.delete(0, END)
        entry_note3.delete(0, END)
        entry_note4.delete(0, END)
        return [name, mat, note1, note2, note3, note4]
    except:
        messagebox.showinfo(
            title="Novo dado não foi informado", message="Favor informar o que deseja trocar do aluno selecionado aluno"
        )


def update_student():
    new_data = get_new_data()
    data_student = get_data_student()
    new_student = []
    for i in range(0, 6):
        if new_data[i] == "":
            i += 1
            new_student.append(data_student[i])
            i -= 1
        else:
            new_student.append(new_data[i])
    update_student_database(new_student, data_student[0])
    update_treview()


#### -------- DELETAR ALUNO ------- ####
def delete_student():
    try:
        selected_student = tv.selection()[0]
        value = tv.item(selected_student, "values")
        tv.delete(selected_student)
        delete_student_database(value[0])
    except:
        messagebox.showinfo(
            title="Aluno não foi informado", message="Favor selecionar um aluno"
        )


#### --- MOSTRAR CONTEUDO SALVO --- ####
def calculate_the_average(note1, note2, note3, note4):
    return (note1 + note2 + note3 + note4) / 4


def student_situation(average):
    if average >= 6:
        return "A"
    else:
        return "R"


def clear_treview():
    for i in tv.get_children():
        tv.delete(i)


def update_treview():
    clear_treview()
    arr_students = select_student_database()
    for i in arr_students:
        average = calculate_the_average(i[3], i[4], i[5], i[6])
        situation = student_situation(average)
        tv.insert(
            "",
            "end",
            values=(i[0], i[1], i[2], i[3], i[4],
                    i[5], i[6], average, situation),
        )


#### -------- TELA TEKINTER ------- ####
frame1 = Frame(window, borderwidth=1, relief="solid")
frame1.place(x=10, y=10, width=504, height=230)

Label(frame1, text="Cadastrar Alunos", height=2, font=("Arial 13 bold")).pack()

Label(frame1, text="Nome:", width=8, anchor=W).place(x=38, y=50)
entry_name = Entry(frame1, width=28)
entry_name.place(x=38, y=70)

Label(frame1, text="Matricula:", width=8, anchor=W).place(x=38, y=100)
entry_mat = Entry(frame1, width=28)
entry_mat.place(x=38, y=120)

Label(frame1, text="1ª Nota:", width=8, anchor=W).place(x=38, y=150)
entry_note1 = Entry(frame1, width=8)
entry_note1.place(x=38, y=170)

Label(frame1, text="2ª Nota:", width=8, anchor=W).place(x=158, y=150)
entry_note2 = Entry(frame1, width=8)
entry_note2.place(x=158, y=170)

Label(frame1, text="3ª Nota:", width=8, anchor=W).place(x=279, y=150)
entry_note3 = Entry(frame1, width=8)
entry_note3.place(x=279, y=170)

Label(frame1, text="4ª Nota:", width=8, anchor=W).place(x=400, y=150)
entry_note4 = Entry(frame1, width=8)
entry_note4.place(x=400, y=170)

Button(frame1, text="SALVAR", command=include).place(x=279, y=60)

Button(frame1, text="ATERAR", command=update_student).place(x=400, y=60)

Button(frame1, text="DELETAR", command=delete_student).place(x=395, y=110)

frame2 = Frame(window, borderwidth=1, relief="solid")
frame2.place(x=10, y=250, width=504, height=230)

tv = ttk.Treeview(
    frame2,
    columns=(
        "id",
        "nome",
        "matricula",
        "1ª nota",
        "2ª nota",
        "3ª nota",
        "4ª nota",
        "media",
        "aprov/reprov",
    ),
    show="headings",
)
tv.column("id", minwidth=0, width=20)
tv.column("nome", minwidth=0, width=70)
tv.column("matricula", minwidth=0, width=90)
tv.column("1ª nota", minwidth=0, width=60)
tv.column("2ª nota", minwidth=0, width=60)
tv.column("3ª nota", minwidth=0, width=60)
tv.column("4ª nota", minwidth=0, width=60)
tv.column("media", minwidth=0, width=50)
tv.column("aprov/reprov", minwidth=0, width=30)
tv.heading("id", text="ID")
tv.heading("nome", text="NOME")
tv.heading("matricula", text="MATRICULA")
tv.heading("1ª nota", text="1ª NOTA")
tv.heading("2ª nota", text="2ª NOTA")
tv.heading("3ª nota", text="3ª NOTA")
tv.heading("4ª nota", text="4ª NOTA")
tv.heading("media", text="MEDIA")
tv.heading("aprov/reprov", text="A/R")
tv.pack()


update_treview()

window.mainloop()

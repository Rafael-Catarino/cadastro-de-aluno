import sqlite3
from sqlite3 import Error
from Student import Student
import os


# - Conexão com o banco de dados - #
def database_connection():
    directory_path = os.path.dirname(__file__)
    database_path = directory_path + "/cadastro_aluno.db"
    connection = None
    try:
        connection = sqlite3.connect(database_path)
    except Error as erro:
        print(erro)
    return connection


# - Criação da tabela - #
def create_table_database():
    comand_sql = """CREATE TABLE IF NOT EXISTS student (
    s_nome_aluno      VARCHAR(50)    NOT NULL,
    i_matricula_aluno INTEGER UNIQUE NOT NULL PRIMARY KEY,
    f_nota1_aluno     NUMERIC NOT NULL,
    f_nota2_aluno     NUMERIC NOT NULL,
    f_nota3_aluno     NUMERIC NOT NULL,
    f_nota4_aluno     NUMERIC NOT NULL
);"""
    connection = database_connection()
    try:
        c = connection.cursor()
        c.execute(comand_sql)
    except Error as erro:
        print(erro)


create_table_database()


# - Inserindo na Tabela - #
def insert_students_database(student: Student):
    connection = database_connection()
    code_sql = "INSERT INTO student(s_nome_aluno, i_matricula_aluno, f_nota1_aluno, f_nota2_aluno, f_nota3_aluno," \
               " f_nota4_aluno)VALUES('" + student.name + "', '" + student.registration + "', '" + student.note1 + \
               "', '" + student.note2 + "', '" + student.note3 + "', '" + student.note4 + "');"
    try:
        c = connection.cursor()
        c.execute(code_sql)
        connection.commit()
    except Error as erro:
        print(erro)


# - DELETANDO ALUNO - #
def delete_student_database(average):
    connection = database_connection()
    sql_code = "DELETE FROM student WHERE i_matricula_aluno='" + average + "';"
    try:
        c = connection.cursor()
        c.execute(sql_code)
        connection.commit()
    except Error as erro:
        print(erro)


# - PEGANDO OS DADOS NO BANCO DE DADOS - #
def select_student_database():
    connection = database_connection()
    sql_code = "SELECT * FROM student"
    c = connection.cursor()
    c.execute(sql_code)
    result = c.fetchall()
    return result


# - ATUALIZAR OS DADOS NO BANCO - #
def update_student_database(student, average):
    connection = database_connection()
    sql_code = "UPDATE student SET s_nome_aluno='" + student[0] + "', i_matricula_aluno='" + student[
        1] + "', f_nota1_aluno='" + student[2] + "', f_nota2_aluno='" + student[3] + "', f_nota3_aluno='" + student[
        4] + "', f_nota4_aluno='" + student[5] + "' WHERE i_matricula_aluno='" + average + "'"
    try:
        c = connection.cursor()
        c.execute(sql_code)
        connection.commit()
    except Error as erro:
        print(erro)

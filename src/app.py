import sqlite3 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

def connect_db(db_file: str) -> sqlite3.Connection:
    try:
        return sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return None

# TO DO: find a way to refactor this whole function in order to make it work for the other plots
# Hint: get the attribute directly from cols 
# Hint: split the function into two: one for querying and another for plotting

def get_students_EIU() -> None:
    query = dat.execute('''
        SELECT Opcion.titulo AS Titulo
        FROM Encuesta
        INNER JOIN Respuesta
        ON Encuesta.num_encuesta = Respuesta.num_encuesta
        INNER JOIN Opcion
        ON Respuesta.num_pregunta = Opcion.num_pregunta
        AND Respuesta.num_opcion = Opcion.num_opcion
        AND Opcion.num_pregunta = 4
    ''')
    cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    # results.groupby(['Titulo']).size().plot(kind='pie', y='Titulo', autopct='%1.1f%%')
    # results.groupby(['Titulo']).size().plot(kind='pie', y='Titulo', autopct='%1.1f%%', figsize=(6, 6))
    results.groupby(['Titulo']).size().plot(kind='bar', y='Titulo', figsize=(6, 6))
    plt.title('¿Conocen los estudiantes el programa de "Estudiante Integral Ucabista"?')
    plt.show()




if __name__ == '__main__':
    dat = connect_db('datos.s3db')
    get_students_EIU()
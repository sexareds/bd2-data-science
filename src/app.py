import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


# TO DO: find a way to refactor this whole function in order to make it work for the other plots
# Hint: get the attribute directly from cols 
# Hint: split the function into two: one for querying and another for plotting

# def show_plot(query: str, cols: list, title: str, xlabel: str, ylabel: str) -> None:
#     results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
#     results.groupby(['Titulo']).size().plot(kind='pie', y='Titulo', autopct='%1.1f%%')
#     plt.show()

# def query_db(query: str) -> sqlite3.Cursor:
#     return dat.execute(query)

def get_students_EIU(dat) -> None:
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
    print(results)
    results.groupby(['Titulo']).size().plot(kind='pie', y='Titulo', autopct='%1.1f%%')
    plt.show()

def main() -> None:
    try:
        dat = sqlite3.connect('data/datos.s3db')
        get_students_EIU(dat)
    except sqlite3.Error as e:
        print(e)
    finally:
        dat.close()

if __name__ == '__main__':
    main()
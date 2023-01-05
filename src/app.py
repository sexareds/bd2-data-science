import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import sql_scripts

def get_sql(dat: sqlite3.Connection, sql_script: str) -> None:
    query = dat.execute(sql_script)
    cols = [column[0] for column in query.description]
    return query, cols

def show_plot(query: str, cols: list, title: str, xlabel: str, ylabel: str) -> None:
    results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    results.groupby(['Titulo']).size().plot(kind='pie', y='Titulo', autopct='%1.1f%%')
    plt.show()

def get_students_EIU(dat: sqlite3.Connection) -> None:
    query, cols = get_sql(dat, sql_scripts.sql_script_1)
    show_plot(query, cols, 'Estudiantes de la EIU', None, None)

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
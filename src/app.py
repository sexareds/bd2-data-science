import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import sql_scripts

def get_table(dat: sqlite3.Connection, sql_script: str) -> pd.DataFrame:
    query = dat.execute(sql_script)
    cols = [column[0] for column in query.description]
    df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    return df

def data_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
    df = df.dropna()
    for column in df.columns:
        df[column] = df[column].str.replace(r'\W', '', regex=True)
    for column in df.columns:
        df[column] = df[df[column].str.strip().astype(bool)] 
    return df

def q_1(dat: sqlite3.Connection) -> None:
    df = get_table(dat, sql_scripts.sql_script_1)
    print(df)

    for num_pregunta in df['num_pregunta'].unique():
        df.query('num_pregunta == {}'.format(num_pregunta)).groupby(['num_opcion']).size().plot(kind='bar', subplots=True)
        plt.title('Estudiantes que conocen el EIU')
        plt.show()

def q_2(dat: sqlite3.Connection) -> None:
    df = get_table(dat, sql_scripts.sql_script_2) 
    df = data_cleaning(df)
    print(df)
    df.groupby(['respuesta']).size().plot(kind='pie', subplots=True, autopct='%1.1f%%')
    plt.title('Cualidades que debe poseer un EIU')
    plt.show()

def q_3(dat: sqlite3.Connection) -> None:
    df = get_table(dat, sql_scripts.sql_script_3)
    df = data_cleaning(df)
    df = df.value_counts().reset_index(name='votos')
    df = df.set_index('respuesta').head(15)
    print(df)
    df['votos'].plot(kind='bar')
    plt.title('Top 15 estudiantes')
    plt.xlabel('Estudiantes')
    plt.ylabel('Votos')
    plt.show()

def main() -> None:
    try:
        dat = sqlite3.connect('data/data.s3db')
        q_1(dat)
        q_2(dat)
        q_3(dat)
    except sqlite3.Error as e:
        print(e)
    finally:
        dat.close()

if __name__ == '__main__':
    main()
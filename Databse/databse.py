import sqlite3
import pandas as pd

# Importing the dataset (Netflix)
df = pd.read_csv("C:/Users/Lenovo/OneDrive - St. Clair College/SEM_1/DAB 111 Pyhton Programming/netflix1.csv")
df.head(10)

# Creating a database
con = sqlite3.connect('Netflix.db')
cursor = con.cursor()

# Creating a table (movies)
create_table = """CREATE TABLE IF NOT EXISTS movies(
                        show_id VARCHAR(50) PRIMARY KEY,
                        type VARCHAR(20),
                        title VARCHAR(255),
                        director VARCHAR(255),
                        country VARCHAR(100),
                        date_added DATE,
                        release_year INT,
                        rating VARCHAR(10),
                        duration VARCHAR(20),
                        listed_in VARCHAR(255)
                        )"""
cursor.execute(create_table)
df.to_sql('movies', con, if_exists='replace', index=False)

con.commit()
con.close()

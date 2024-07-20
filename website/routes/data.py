import sqlite3
import pandas as pd
from flask import Blueprint, render_template

data_bp = Blueprint('data', __name__)

@data_bp.route('/data')
def data():
    # Connect to SQLite database and fetch data
    con = sqlite3.connect('Netflix.db')
    c = con.cursor()
    
    # Fetch the first 10 rows
    c.execute('SELECT * FROM movies LIMIT 10')
    data = c.fetchall()
    
    # Fetch the first 5 rows for the second table
    d = con.cursor()
    d.execute('SELECT * FROM movies LIMIT 5')
    data_movies = d.fetchall()
    
    # Convert the fetched data to a DataFrame for further operations
    df = pd.DataFrame(data, columns=['show_id', 'type', 'title', 'director', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in'])

    # Perform some basic operations
    movie_count = len(df)
    avg_release_year = df['release_year'].mean()
    rating_counts = df['rating'].value_counts().to_dict()
    
    # Generate HTML for the full data table
    data_html = df.to_html(classes='table table-striped', index=False)

    # Convert fetched data for the additional table
    df_movies = pd.DataFrame(data_movies, columns=['show_id', 'type', 'title', 'director', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in'])
    data_movies_html = df_movies.to_html(classes='table table-bordered', index=False)
    
    con.close()

    return render_template('data.html', data=data_html, data_movies=data_movies_html, movie_count=movie_count, avg_release_year=avg_release_year, rating_counts=rating_counts)


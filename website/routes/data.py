from flask import render_template_string
import sqlite3
import pandas as pd

@app.route('/data')
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

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data - DAB111 Project Group 1</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
            body {
                background-color: #f8f9fa;
            }
            header {
                background-color: #343a40;
                color: white;
                padding: 10px 0;
                text-align: center;
                margin-bottom: 20px;
            }
            nav a {
                color: white;
                margin: 0 10px;
                padding: 10px 20px;
                border-radius: 5px;
                background-color: #007bff;
                transition: background-color 0.3s, transform 0.3s;
            }
            nav a:hover {
                background-color: #0056b3;
                transform: scale(1.1);
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Data - DAB111 Project Group 1</h1>
            <nav class="nav justify-content-center">
                <a class="nav-link" href="/">Home</a>
                <a class="nav-link" href="/about">About</a>
                <a class="nav-link" href="/data">Data</a>
            </nav>
        </header>
        <div class="container">
            <h2>Full Data Sample</h2>
            {{ data|safe }}
            <h3>First 5 Records from the Database</h3>
            {{ data_movies|safe }}
            
            <h3>Operations Summary</h3>
            <p><strong>Total Movie Count:</strong> {{ movie_count }}</p>
            <p><strong>Average Release Year:</strong> {{ avg_release_year | round(0) }}</p>
            <p><strong>Rating Counts:</strong></p>
            <ul>
                {% for rating, count in rating_counts.items() %}
                <li>{{ rating }}: {{ count }}</li>
                {% endfor %}
            </ul>
        </div>
    </body>
    </html>
    ''', data=data_html, data_movies=data_movies_html, movie_count=movie_count, avg_release_year=avg_release_year, rating_counts=rating_counts)

from flask import render_template_string

@app.route('/home')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home - DAB111 Project Group 1</title>
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
            <h1>DAB111 Project Group 1</h1>
            <nav class="nav justify-content-center">
                <a class="nav-link" href="/">Home</a>
                <a class="nav-link" href="/about">About</a>
                <a class="nav-link" href="/data">Data</a>
            </nav>
        </header>
        <div class="container">
            <h2>Project Overview</h2>
            <p>Netflix is a popular streaming service that offers a vast catalog of movies, TV shows, and original contents. This dataset is a cleaned version of the original version which can be found here. The data consist of contents added to Netflix from 2008 to 2021. The oldest content is as old as 1925 and the newest as 2021.</p>
            <p>My name is Mr. Krunal and welcome to my page.</p>
        </div>
    </body>
    </html>
    ''')

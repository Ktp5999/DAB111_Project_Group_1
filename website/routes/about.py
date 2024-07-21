from flask import render_template_string
@app.route('/about')
def about():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Us - DAB111 Project Group 1</title>
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
            <h1>About Us - DAB111 Project Group 1</h1>
            <nav class="nav justify-content-center">
                <a class="nav-link" href="/">Home</a>
                <a class="nav-link" href="/about">About</a>
                <a class="nav-link" href="/data">Data</a>
            </nav>
        </header>
        <div class="container">
            <h2>About Us</h2>
            <p>We are Group 1 of the DAB111 project, focused on using data to solve real-world problems.</p>
        </div>
    </body>
    </html>
    ''')

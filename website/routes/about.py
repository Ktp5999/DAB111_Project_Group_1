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
            .container {
                margin-top: 20px;
            }
            .data-types-table {
                margin-top: 20px;
                border-collapse: collapse;
                width: 100%;
            }
            .data-types-table th, .data-types-table td {
                border: 1px solid #ddd;
                padding: 8px;
            }
            .data-types-table th {
                background-color: #343a40;
                color: white;
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

            <h3>SQL Data Types Used in the Project</h3>
            <p>Below is a summary of the SQL data types used for each column in our database:</p>
            <table class="data-types-table">
                <thead>
                    <tr>
                        <th>Column Name</th>
                        <th>Description</th>
                        <th>SQL Data Type</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>show_id</td>
                        <td>Unique identifier for each show</td>
                        <td>VARCHAR(50)</td>
                    </tr>
                    <tr>
                        <td>type</td>
                        <td>Type of content (e.g., Movie or TV Show)</td>
                        <td>VARCHAR(20)</td>
                    </tr>
                    <tr>
                        <td>title</td>
                        <td>Title of the show</td>
                        <td>VARCHAR(255)</td>
                    </tr>
                    <tr>
                        <td>director</td>
                        <td>Director of the show</td>
                        <td>VARCHAR(255)</td>
                    </tr>
                    <tr>
                        <td>country</td>
                        <td>Country where the show was produced</td>
                        <td>VARCHAR(100)</td>
                    </tr>
                    <tr>
                        <td>date_added</td>
                        <td>Date the show was added to Netflix</td>
                        <td>DATE</td>
                    </tr>
                    <tr>
                        <td>release_year</td>
                        <td>Year the show was released</td>
                        <td>INT</td>
                    </tr>
                    <tr>
                        <td>rating</td>
                        <td>Rating of the show (e.g., PG-13, TV-MA)</td>
                        <td>VARCHAR(10)</td>
                    </tr>
                    <tr>
                        <td>duration</td>
                        <td>Duration of the show (e.g., 90 min, 1 Season)</td>
                        <td>VARCHAR(20)</td>
                    </tr>
                    <tr>
                        <td>listed_in</td>
                        <td>Categories or genres the show belongs to</td>
                        <td>VARCHAR(255)</td>
                    </tr>
                </tbody>
            </table>

            <p><strong>Data Source:</strong> <a href="https://www.kaggle.com/datasets/shivamb/netflix-shows" target="_blank">Kaggle Netflix Dataset</a></p>
        </div>
    </body>
    </html>
    ''')

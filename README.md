
- `app.py`: The main Flask application file that initializes the app and registers the blueprints for different routes.
- `routes/`: Directory containing separate route files for each section.
  - `home.py`: Handles the Home page route.
  - `about.py`: Handles the About page route.
  - `data.py`: Handles the Data page route.
- `templates/`: Directory containing HTML templates for each section.
  - `base.html`: Base HTML structure that is extended by other templates.
  - `home.html`: HTML template for the Home page.
  - `about.html`: HTML template for the About page.
  - `data.html`: HTML template for the Data page.

## Dataset

The dataset used in this project is a cleaned version of the original Netflix dataset, which contains information about contents added to Netflix from 2008 to 2021.

## Setup

### Prerequisites

- Python 3.x
- Flask
- Pandas
- SQLite3

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd project

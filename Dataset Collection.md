# Data Collection

## Overview

This document outlines the data collection process for the DAB111 Project Group 1. The project utilizes a dataset from Kaggle containing information about Netflix movies and TV shows.

## Data Source

- **Source**: Kaggle
- **Dataset**: [Netflix Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
  - **Description**: This dataset includes various details about movies and TV shows available on Netflix, such as show ID, type, title, director, country, date added, release year, rating, duration, and listed-in categories.

## Dataset Details

The dataset contains the following columns:

1. **show_id** (VARCHAR(50)): Unique identifier for each show.
2. **type** (VARCHAR(20)): Type of content (e.g., Movie or TV Show).
3. **title** (VARCHAR(255)): Title of the show.
4. **director** (VARCHAR(255)): Director of the show.
5. **country** (VARCHAR(100)): Country where the show was produced.
6. **date_added** (DATE): Date the show was added to Netflix.
7. **release_year** (INT): Year the show was released.
8. **rating** (VARCHAR(10)): Rating of the show (e.g., PG-13, TV-MA).
9. **duration** (VARCHAR(20)): Duration of the show (e.g., 90 min, 1 Season).
10. **listed_in** (VARCHAR(255)): Categories or genres the show belongs to.

## Data Collection Process

1. **Downloading the Dataset**: 
   - The dataset was downloaded from Kaggle, which provides a wide range of datasets for various data science projects.

2. **Inspecting the Data**:
   - The dataset was inspected to ensure it contained the required variables and data types.

3. **Data Cleaning**:
   - Necessary data cleaning was performed, including handling missing values and correcting any inconsistencies.

4. **Loading into Database**:
   - The cleaned data was loaded into a SQLite database for further analysis and processing.

## Data Usage

- **Database**: The data is stored in a SQLite database for efficient querying and manipulation.
- **Python Libraries**: Pandas was used for data manipulation and SQLite3 for database interaction.

## Additional Information

- **Data Size**: The dataset includes multiple entries, with variables spanning text, numbers, and dates.

For more details or to access the dataset, visit the Kaggle dataset page: [Netflix Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

# SQLite Video Manager

A beginner-friendly Python project built while learning SQL and SQLite. This application demonstrates how to create a database, create tables, insert records, and retrieve data using SQL queries.

## Features

* Create SQLite database
* Create table automatically if it doesn't exist
* Add new video records
* View all saved videos
* Auto-increment video IDs
* Menu-free beginner implementation for understanding SQL basics

## Technologies Used

* Python 3
* SQLite3
* SQL

## SQL Concepts Covered

* CREATE TABLE
* INSERT INTO
* SELECT
* PRIMARY KEY
* AUTOINCREMENT

## Table Structure

| Column   | Type                              |
| -------- | --------------------------------- |
| ID       | INTEGER PRIMARY KEY AUTOINCREMENT |
| Title    | TEXT                              |
| Views    | INTEGER                           |
| Category | TEXT                              |

## Sample Output

```text
Enter Video title: Leather Armor Challenge
Enter the number of Views: 3200
Enter the Video category: Challenge

ID: 1
Title: Leather Armor Challenge
Views: 3200
Category: Challenge
-------------------
```

## Project Structure

```text
SQLite-Video-Manager/
│
├── main.py
├── videos.db
├── README.md
└── .gitignore
```

## Concepts Practiced

* Database Creation
* Table Creation
* SQL Queries
* User Input
* Data Storage
* Data Retrieval
* Python Functions
* SQLite Integration

## Future Improvements

* Search Videos
* Delete Videos
* Update Video Details
* Sort by Views
* Analytics Dashboard
* Tkinter GUI
* Flask Web Version

## Author

Jaspreet Singh

Learning Python and SQL through project-based development.

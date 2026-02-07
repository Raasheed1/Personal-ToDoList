# Python To-Do List Application

A command-line based To-Do List application written in Python.
It allows users to create, manage, and track tasks with categories, due dates, and completion status.
Tasks are stored persistently using a JSON file.

## Features

- A dd new tasks with description, category, and due date
- View all tasks with status details
- Automatically highlights priority tasks (due within 3 days)
- View pending tasks only
- Mark tasks as completed
- Edit existing tasks
- Delete tasks
- Persistent storage using tasks.json

## Technologies Used

- Python 3
- JSON for data storage
- datetime module for date handling

### Data Storage Format

Tasks are stored in 'tasks.json' using this structure:
'''
{
  "New_Task": "Task name",
  "Description": "Task description",
  "Category": "Work",
  "Due_Date": "YYYY-MM-DD",
  "Status": false
}
'''

## Error Handling

- Invalid date formats are rejected
- Invalid menu inputs are handled safely
- Corrupted JSON files reset gracefully

## Future Improvements

-Search and filter tasks
-Sorting by due date or category
-User authentication
-GUI or web-based interface

## Author

Developed as a learning project to practice:
Python fundamentals
File handling
CLI application design

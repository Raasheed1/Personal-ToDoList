Python To-Do List Application:

A command-line based To-Do List application written in Python.
It allows users to create, manage, and track tasks with categories, due dates, and completion status.
Tasks are stored persistently using a JSON file.

Features:

Add new tasks with description, category, and due date

View all tasks with status details

Automatically highlights priority tasks (due within 3 days)

View pending tasks only

Mark tasks as completed

Edit existing tasks

Delete tasks

Persistent storage using tasks.json

Technologies Used:

Python 3

JSON for data storage

datetime module for date handling

Project Structure
PerToDoList.py
tasks.json
README.md

PerToDoList.py – Main application file

tasks.json – Stores all tasks (created automatically)

How It Works:

When the program starts:

It loads existing tasks from tasks.json if available

Dates are converted back into Python date objects

If the file does not exist, a new task list is created

Tasks are saved automatically after every add, edit, delete, or status update.

How to Run

Make sure Python 3 is installed

Open a terminal in the project directory

Run the program:

python PerToDoList.py
Menu Options
1. Add new Task
2. View all Tasks
3. Mark the completed Task
4. Edit or Delete Task
5. Exit
Task Categories

Work

Personal

Urgent

Priority is automatically determined based on due date.

Data Storage Format

Tasks are stored in tasks.json using this structure:

{
  "New_Task": "Task name",
  "Description": "Task description",
  "Category": "Work",
  "Due_Date": "YYYY-MM-DD",
  "Status": false
}
Error Handling

Invalid date formats are rejected

Invalid menu inputs are handled safely

Corrupted JSON files reset gracefully

Future Improvements

Search and filter tasks

Sorting by due date or category

User authentication

GUI or web-based interface

Author

Developed as a learning project to practice:

Python fundamentals

File handling

Data structures

CLI application design  
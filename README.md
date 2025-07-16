# Project Management Tool

This repository contains a simple project management web application built with Flask. It provides basic functionality for managing tasks and work breakdown structure (WBS) items. The application stores its data in a SQLite database that can be placed on an on-premise server or any path you choose.

## Features

- Dashboard showing recent tasks and top-level WBS items
- Task list with form to add new tasks
- WBS page to create and list items
- Simple Bootstrap-based interface

## Requirements

- Python 3.8+
- Packages listed in `requirements.txt`

## Setup

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) Specify a custom database path by setting the `APP_DATABASE_PATH` environment variable. If omitted, `pm.db` will be created in the project directory.
3. Start the application:
   ```bash
   python run.py
   ```
4. Open `http://localhost:5000` in your browser.

The database file will be created automatically at the specified path. Team members can share the database on an on-premise server by pointing `APP_DATABASE_PATH` to the shared location.

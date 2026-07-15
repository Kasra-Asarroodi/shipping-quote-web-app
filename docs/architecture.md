# Project Architecture

## Overview

As this project grew, I realised that keeping every function inside a single `app.py` file was becoming difficult to manage. To make the code easier to understand and maintain, I separated the application into multiple modules, each with its own responsibility.

This modular approach makes future development much easier and reduces the chance of introducing bugs when adding new features.

---

## Overall Structure

The application is divided into the following components:

- **app.py**
  - Creates the Flask application.
  - Loads configuration values.
  - Starts the web server.

- **app_routes.py**
  - Contains all website routes.
  - Handles requests from customers and administrators.
  - Connects the user interface with the application logic.

- **calculation.py**
  - Performs all shipping price calculations.
  - Calculates insurance.
  - Calculates additional surcharges.
  - Applies promotional discounts.

- **database.py**
  - Creates and manages the SQLite database.
  - Saves enquiries.
  - Loads enquiries.
  - Updates enquiry status.
  - Deletes enquiries.

- **settings.py**
  - Stores and loads promotional settings.

- **templates/**
  - HTML pages used by Flask.

- **static/**
  - CSS styling.
  - JavaScript.
  - Images.

---

## Why I Chose This Design

Rather than placing everything into one large file, I wanted each file to have a single responsibility.

This makes the project easier to read, easier to debug, and much easier to expand in the future.

Although this project is relatively small, following this structure has helped me understand how larger Flask applications are organised.
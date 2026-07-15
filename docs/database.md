# Database Design

## Overview

This project uses SQLite to store customer enquiries.

I chose SQLite because it is lightweight, simple to use and requires no separate database server. Since this application is expected to receive a relatively small number of enquiries, SQLite provides a practical solution while allowing me to learn SQL database concepts.

---

## Database Table

The application stores all information inside a single table called:

- enquiries

Each enquiry stores:

- Sender details
- Receiver details
- Parcel information
- Shipping value
- Insurance cost
- Total quote price
- Promotional discount
- Current enquiry status

---

## Main Database Operations

The application performs five main database operations:

- Create the database table.
- Save new enquiries.
- Load enquiries.
- Update enquiry status.
- Delete enquiries.

Each operation has been separated into its own function to keep the code organised and reusable.

---

## Why SQLite?

For this project, SQLite offered several advantages:

- Easy to learn.
- No installation required.
- Perfect for small business applications.
- Easy deployment to Render.
- Good introduction to SQL before learning larger database systems such as PostgreSQL.

As this project grows in the future, migrating to PostgreSQL would be relatively straightforward because all database operations have already been separated into their own module.
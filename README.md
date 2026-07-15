
# Pack & Send Unley Shipping Quote Website

A Flask web application created for Pack & Send Unley.

The website allows customers to:

- calculate an estimated shipping price
- submit a shipping enquiry
- view their submitted enquiries using their email address
- view the current enquiry status

The administrator can:

- securely log in to an admin dashboard
- view all enquiries
- update enquiry statuses
- delete enquiries
- update the promotional discount rate

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Gunicorn
- Render

## Project Structure

- `app.py` — creates the Flask application
- `app_routes.py` — contains the website routes
- `calculation.py` — contains quote calculation functions
- `database.py` — contains SQLite database functions
- `settings.py` — contains promotional rate settings
- `templates/` — contains HTML pages
- `static/` — contains CSS, JavaScript and images


## Lessons Learned

This project helped me develop practical experience with:

- Flask web development
- SQLite databases
- User authentication
- Environment variables
- Git and GitHub
- Deploying applications with Render
- Debugging and modularising Python applications

## Screenshots

Home Page

Admin Dashboard

Customer Enquiry Page

## Environment Variables

The application requires:

- `SECRET_KEY`
- `ADMIN_PASSWORD`

These values are stored locally in a `.env` file and are not included in the GitHub repository.


## Future Improvements

Future versions of the application may include:

- Customer accounts
- Email notifications
- PDF quotations
- Shipment tracking
- Improved administrator analytics
- Automatic shipping rate updates


## Local Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py








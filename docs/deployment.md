# Deployment

## Overview

Once development was complete, I deployed the application using Render.

This allowed the project to become publicly accessible while giving me experience deploying a real Flask application to the cloud.

---

## Deployment Steps

The deployment process involved:

- Preparing the GitHub repository.
- Creating a requirements.txt file.
- Creating a Procfile.
- Moving sensitive information into environment variables such as the admin password, Secret key and the database.
- Configuring Render.
- Testing the deployed website.

---

## Environment Variables

Sensitive information is not stored inside the GitHub repository.

Instead, the following values are stored securely using environment variables:

- SECRET_KEY
- ADMIN_PASSWORD

This prevents confidential information from being exposed publicly.

---

## Lessons Learned

Deploying a project introduced several new concepts that I had not previously encountered, including:

- Production environments
- Environment variables
- GitHub repositories
- Deployment debugging
- Managing application configuration

Understanding these concepts has significantly improved my understanding of how web applications move from development into production.
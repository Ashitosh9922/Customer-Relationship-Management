
# Customer Relationship Management (CRM)

## Overview

The **Customer Management Platform (CMP)** is a web-based application built with Django, designed to simplify the process of managing customers, products, and orders. It offers businesses a streamlined solution to handle key operational tasks within a centralized and easy-to-use interface.

## Features

- **Dashboard**: Provides an intuitive overview of recent activities, including customer interactions and order updates.
- **Customer Management**: Easily manage customer information and track customer-related activities.
- **Product Management**: Maintain an inventory of products with detailed information like name, price, and category.
- **Order Management**: Efficiently track, update, and manage customer orders, including status changes and order histories.
- **Admin Interface**: Leverage Django’s built-in admin panel to manage all models (Customers, Products, Orders) with a simple, powerful UI.

## Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (No frameworks like Bootstrap used)
- **Database**: MySQL (Previously SQLite; can also be switched to PostgreSQL)
- **Version Control**: Git and GitHub for project management and version control

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/Customer-Management-Platform.git
   cd Customer-Management-Platform
   ```

2. **Install Dependencies:**

   Ensure you have `pip` installed, then install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup:**

   - **MySQL Configuration**: Make sure to update your `settings.py` file with your MySQL database credentials.
   - Run the migrations to set up the database:

     ```bash
     python manage.py migrate
     ```

4. **Run the Server:**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

5. **Access the Application:**

   Open your browser and navigate to:

   ```url
   http://127.0.0.1:8000/
   ```

## Contribution Guidelines

If you’d like to contribute to this project, feel free to submit a pull request or report any issues. All contributions are welcome!

---

This README now reflects your MySQL integration, with instructions on setup, database configuration, and improved clarity on features.




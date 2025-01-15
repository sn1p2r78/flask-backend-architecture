# Flask Backend Architecture

## Project Overview
This project provides a robust backend system built using Flask. It includes features such as user authentication, service management, and integration with Microsoft Graph API for managing Azure applications, users, and MFA management.

## Features
- **User Management** Secure user registration, login, and role-based access control.
- ***Admin Panel****: Manage users and services.- ***Service Usage and Statistics**** Track and retrieve service usage data.- **Microsoft Graph Integration***: 
 - Login to Azure accounts.
  - Create Azure applications.
  - Manage Azure users with MFA support.
  - Test MFA scenarios.
- ***Real-Time Communication*** SocketIO integration for live updates.

## Setup Instructions
### Preprequisites- Python 3.8 or higher
- SQLite (bundled with Python)- Microsoft Azure account for API integration-
## Installation1
  clone the repository::
   git clone https://github.com/sn1p2r78/flask-backend-architecture.git
cd flask-backend-architecture
## Start the server::
flask run


### API Documentation
- **User Registration*** POST /auth/register
- **Login*** POST /auth/login - Login with username and password
   - Responses the message with logging status.
- ***Real-Time Communication*** SocketIO integration for live updates.
# User Registration and Login System

This is a simple Python application that demonstrates user registration and login functionality with password encryption, hashing, and user data storage in an H5 file.

## Features

- User registration with the following details:
  - Username
  - Password (hashed for security)
  - Name
  - Status
  - Date of Birth

- Secure password storage:
  - Passwords are encrypted using Fernet symmetric encryption.
  - Hashed passwords are stored using bcrypt for added security.

- User login with password verification.

- Registration and login events are logged with timestamps.

## Prerequisites

- Python 3.x
- Required Python packages are listed in `requirements.txt`.
- use this command to download the requirement.
- ```bash
  pip freeze > requirement.txt

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/huho-0/register-login/
   cd register-login

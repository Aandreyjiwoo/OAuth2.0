# OAuth2.0
Securing APIs using OAuth 2.0 with GitHub and Auth0
System Integration and Architecture | Laboratory Activity
This repository contains the implementation of an intermediate-level laboratory activity focused on the OAuth 2.0 authorization framework. The project demonstrates how to integrate third-party authentication (GitHub and Auth0) into a Flask-based web application to secure API endpoints.

Objectives
Explain the core concepts of the OAuth 2.0 framework.

Implement a secure login flow using GitHub OAuth.

Secure API endpoints using session management.

Compare different identity providers (IDPs) like GitHub and Auth0.

Demonstrate the difference between authorized and unauthorized API access.

Technology Stack
Language: Python 3.x

Framework: Flask

Libraries: Authlib, Requests

Identity Providers: GitHub Developer Portal, Auth0

Tools: VS Code, Terminal

Getting Started
1. Prerequisites
Ensure you have Python installed, then install the necessary dependencies:

Bash
pip install flask authlib requests
2. GitHub OAuth Configuration
Navigate to GitHub Settings > Developer Settings > OAuth Apps.

Register a New OAuth App:

Homepage URL: http://localhost:5000

Authorization Callback URL: http://localhost:5000/callback

Generate a Client Secret and copy both the Client ID and Secret into the app.py file.

3. Running the Application
Clone this repository.

Navigate to the project folder.

Run the application:

Bash
python app.py
Access the login route at: http://localhost:5000/login

Implementation Details
OAuth Workflow
The application follows the Authorization Code Grant flow:

Login: User is redirected to GitHub/Auth0.

Authorize: User grants permission.

Callback: The provider sends a code back to our /callback route.

Token Exchange: The app exchanges the code for an Access Token.

Access: The app uses the token to fetch user profile data.

Protected Routes
The /profile endpoint is protected by a session check. If a user attempts to access it without a valid session['user'], the server returns a 401 Unauthorized status.

Project Structure
Plaintext
├── app.py              # Main Flask application logic
├── requirements.txt    # List of Python dependencies
├── screenshots/        # Evidence of successful implementation
└── README.md           # Documentation (this file)
Lab Results (Evidence)
The following scenarios were tested to verify the implementation:

Login Page: Initial entry point.

GitHub Authorization: The handshake between the app and GitHub.

Successful Login: Profile data retrieved and displayed via API.

Unauthorized Access: System correctly blocks access when no session exists.

Logout: Clearing session data and confirming re-secured endpoints.

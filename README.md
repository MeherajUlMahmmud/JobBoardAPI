# JobBoard REST API

[//]: # (A sample Django project that serves as a RESTful API backend.)
- [JobBoard](https://github.com/MeherajUlMahmmud/JobBoard)
- [GoCV](https://github.com/MeherajUlMahmmud/GoCV)

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Configuration](#configuration)
- [Usage](#usage)
- [Authentication and Permissions](#authentication-and-permissions)
- [Documentation](#documentation)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)
- [Contact Information](#contact-information)

## Installation

1. Make sure you have Python 3.x and pip installed.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Create and activate a virtual environment (optional, but recommended).
5. Install the project dependencies by running the following command:
    ```shell
    pip install -r requirements.txt
    ```

## Features
### Authentication
- [x] Register as an Applicant or an Organization.
- [x] Login as an Applicant or an Organization.
- [x] Reset password.
- [ ] Verify email.
- [x] Change password
- [ ] Change email.
- [ ] Update profile. (Applicant, Organization)

### Resume Builder
- [x] Create, update, and delete Resume.
- [x] Update Personal Information.
- [x] Update Contact Information.
- [x] Create, update and delete Work Experience.
- [x] Create, update and delete Education.
- [x] Create, update and delete Skills.
- [ ] Create, update and delete Projects.
- [x] Create, update and delete Certifications.
- [x] Create, update and delete Awards.
- [ ] Create, update and delete Publications.
- [x] Create, update and delete References.
- [x] Create, update and delete Languages.
- [x] Create, update and delete Interests.
- [ ] Preview Resume.
- [ ] Export Resume as PDF.

### Job 
- [ ] Create, update, and delete Job. (Organization)
- [ ] View Job details. (Applicant)
- [ ] View all Jobs. (Applicant)
- [ ] View all Jobs. (Organization)
- [ ] View all Jobs. (Public)
- [ ] Search Jobs by title, location, and company. (Public)
- [ ] Apply for a Job. (Applicant)
- [ ] View all Job applications. (Organization)
- [ ] View all Job applications. (Applicant)
- [ ] View all Job applications by Job. (Organization)
- [ ] View all Job applications by Job. (Applicant)
- [ ] View total Job applications by Job. (Public)

### Test
- [x] Create, update, and delete Test. (Organization)
- [x] View Test details. (Applicant)
- [x] View all Tests. (Organization)
- [x] Create, update, and delete Test questions. (Organization)
- [x] View all Test questions by Test. (Applicant)
- [x] View all Test questions by Test. (Organization)
- [x] View all Question Options by Test question. (Applicant)
- [x] View all Question Options by Test question. (Organization)
- [ ] Attempt Test. (Applicant)
- [ ] View all Test attempts. (Organization)
- [ ] View all Test attempts. (Applicant)
- [ ] View all Test attempts by Test. (Organization)
- [ ] View Test attempt by Test. (Applicant)

## Configuration
1. Set up your database connection in the settings.py file.
2. Run the following commands to perform database migrations:
    ```shell
    python manage.py makemigrations
    ```
    ```shell
    python manage.py migrate
    ```
3. (Optional) Configure environment variables for sensitive information.
4. (Optional) Customize the API settings in the settings.py file.

## Usage
1. Start the development server by running the following command:
    ```shell
    python manage.py runserver
    ```
2. Access the API at http://localhost:8000/.
3. Refer to the API documentation for available endpoints and usage examples.

## Authentication and Permissions
This API uses token-based authentication. To obtain a token:

1. Create a user account by registering at /api/auth/register/.
2. Obtain a token by authenticating at /api/auth/login/.

3. Include the obtained token in the request header as follows:
   ```makefile
   Authorization: Bearer <token>
   ```
To access restricted endpoints, make sure your token has the necessary permissions.

## Documentation
For detailed documentation and API reference, please visit the project wiki.

## Contribution Guidelines
Contributions, bug reports, and feature requests are welcome! Please follow the guidelines outlined in [Contributing](CONTRIBUTING.md).

Please note that this project follows a Code of Conduct. Make sure to review and adhere to it.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact Information
For any questions or feedback, please reach out to the project maintainer at `meherajmahmmd@gmail.com` or open an issue on GitHub.

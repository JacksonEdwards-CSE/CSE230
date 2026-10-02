# Discussion Board

A simple Django discussion board for creating and viewing community discussion topics. Users can submit a topic from the home page, receive validation feedback, and see saved topics displayed with the newest discussions first.

## Features

- Create a discussion topic from the home page.
- Validate that topics are between 3 and 80 characters.
- Store topics and creation times in a SQLite database.
- Display recent discussions in reverse chronological order.
- Provide success and error messages for submissions.
- Use responsive styling for desktop and mobile screens.

## Instructions for Build and Use

### Prerequisites

- Python 3.11 or a compatible Python 3 release
- `pip`

### Set up the project

From the repository root, open a terminal and run:

```text
cd discussion_board
python -m venv .venv
```

Activate the virtual environment:

Windows PowerShell:

```text
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```text
source .venv/bin/activate
```

Install the project dependencies and apply the database migrations:

```text
python -m pip install -r requirements.txt
python manage.py migrate
```

### Run the application

Start Django's development server:

```text
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a web browser.

### Use the application

1. Enter a discussion topic in the text field.
2. Click the Post Topic button
3. If the topic is valid, it is saved and appears under the Recent Discussions section.
4. If the topic is blank, shorter than 3 characters, or longer than 80 characters, correct the input using the displayed validation message.

## Development Environment

The application was developed with:

- Python 3.11
- Django 5.2.17
- SQLite (the default Django database for this project)
- HTML and Django templates
- CSS with responsive media queries

## Project Structure

```text
discussion_board/
├── manage.py                 # Django command-line utility
├── requirements.txt          # Python dependencies
├── db.sqlite3                # Local development database
├── config/                   # Project configuration and URL routing
└── main/                     # Discussion board application
    ├── models.py             # Post database model
    ├── views.py              # Topic submission and display logic
    ├── urls.py               # Application routes
    ├── templates/main/       # HTML templates
    └── static/main/          # CSS styles
```

## Useful Websites to Learn More

- [Django documentation](https://docs.djangoproject.com/en/5.2/)
- [Django tutorial: Writing your first Django app](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
- [Django models documentation](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [Django static files documentation](https://docs.djangoproject.com/en/5.2/howto/static-files/)

## Future Work

The following improvements could be added in future iterations:

- [ ] Add user accounts and authentication.
- [ ] Allow users to create replies to discussion topics.
- [ ] Add edit and delete controls for topics.
- [ ] Add automated model and view tests.
- [ ] Add pagination or search for larger discussion lists.
- [ ] Move sensitive settings, such as the secret key, into environment variables before production deployment.

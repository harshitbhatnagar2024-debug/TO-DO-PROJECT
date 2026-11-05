# To Do App

This is a small task list website built with Python and Django. You can add tasks, read the full list, edit a task, mark it as done, and delete it. The app saves tasks in a local SQLite database file named `db.sqlite3`.

## What you need

- Python 3.10 or newer
- A terminal or command prompt
- Internet access for the first install, so `pip` can download Django

## 1. Open the project folder

In your terminal, move into the folder that contains `manage.py`:

```bash
cd path/to/ezyZip
```

## 2. Create and activate a virtual environment

A virtual environment keeps this project's Python packages separate from other projects.

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

When it is active, your terminal usually shows `(.venv)` at the start of the prompt.

## 3. Install Django

```bash
python -m pip install -r requirements.txt
```

## 4. Prepare the database

Migrations are Django's instructions for creating and updating database tables. Run them before starting the site:

```bash
python manage.py migrate
```

The task app is registered in `todo_project/settings.py`. Its migration history is in `todo_app/migrations/`.

If you change a model in `todo_app/models.py`, create a new migration and apply it:

```bash
python manage.py makemigrations todo_app
python manage.py migrate
```

Do not edit a migration that has already been applied to a shared or important database. Make a new migration instead.

## 5. Start the website

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser. Stop the local server with `Ctrl+C` in the terminal.

## Using the app

1. Choose **Add Task** to open the task form.
2. Enter a title and description, then choose **Save**.
3. On the main page, use **Edit** to change a task.
4. Tick or untick the box to mark a task done or pending.
5. Choose **Delete** to remove a task. Deleting is permanent for that local database.

## Project map

- `manage.py` starts Django management commands.
- `todo_project/settings.py` contains project settings, including the installed apps and database configuration.
- `todo_project/urls.py` connects the site routes to the task app.
- `todo_app/models.py` describes how a task is stored.
- `todo_app/views.py` contains the code that responds to page requests.
- `todo_app/urls.py` lists the task page routes.
- `todo_app/migrations/` contains database update instructions.
- `template/` contains the HTML pages.
- `static/` contains the CSS styles.
- `db.sqlite3` is the local database created when migrations are applied.

## Optional: create an admin login

The Django admin page is available at <http://127.0.0.1:8000/admin/>. To create a login, run:

```bash
python manage.py createsuperuser
```

Follow the prompts, then sign in on the admin page. Tasks are not currently added to the admin site's list; the normal task pages are the way to manage them.

## Settings for deployment

The defaults are for local development. Before putting the site on the internet, set a private `DJANGO_SECRET_KEY`, set `DJANGO_DEBUG=False`, and set `DJANGO_ALLOWED_HOSTS` to the real host names. Do not publish a real secret key in source control.

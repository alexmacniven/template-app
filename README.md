# template-app
A dead simple Python app template.

This repo structure is suitable for a python app.
That is where you'd use `$ python -m app` to run.

## best development practice
Assume your app is based on *template-app*
 - Use *virtualenv* `python -m venv venv`
 - Install development requirements `pip install -r requirements-dev.txt`
   - Only use *requirements.txt* for production depencencies
 - Lint with *flake8* `flake8 app tests`
 - Format with *black* `black .`

## best production practice
Aim for simple usage
 - Use *virtualenv* `python -m venv venv`
 - Install requirements `pip install -r requirements.txt`
 - Run the main package `python -m app [args]`

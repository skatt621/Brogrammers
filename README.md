# Brogrammers
CpS 420-Software Development Team Project

This is where we begin our journey to a full application.

# Project Setup
These instructions are for a Windows 10 platform. While the process would be essentially the same, there will be differences for other platforms (i.e. instead of virtualenvwrapper-win other platforms use virtualenv)

1. Clone the project repo

    `$ cd \path\to\where\you\want\the\proj`

    `$ git clone https://github.com/skatt621/Brogrammers.git`

2. Make your own branch of the repo

    `git checkout -b [YourBranchName]`

    `git push origin [YourBranchName]`

3. Make sure you have Python3.6 & pip installed

4. Make sure you have `virtualenvwrapper-win` installed

    https://pypi.org/project/virtualenvwrapper-win/

5. Create the project virtual environment
    `$ cd Brogrammers`

    `$ mkvirtualenv -p path/to/Python34/python.exe brogrammers_env`

6. Start working in the environment

    - When you are working in the environment, you cwd path will have the format `(the_env_name) cwd $`. For example:

        `(brogrammers_env) C:\Users\Karyn\Documents\Fall2018\cps479\Brogrammers>`

    - to start working in the environment, use the command `$ workon brogrammers_env`

    - to stop working in the environment, use the `$ command deactivate`

7. Install requirements
    - make sure you are working in your environment
    - run the command `$ pip install -r check_hunters/requirements.txt`

8. To create a superuser to be able to edit accounts to test checkpoint locally, run

    `$ cd check_hunters`

    `$ python manage.py createsuperuser --username=YOUR_USERNAME --email=SOME_EMAIL@example.com`
    
    You will be prompted for a password twice. Once this is created, you will be able to log in to the admin page.

9. To run the project on your local machine, run 

    `$ python manage.py runserver`
	
    and go to localhost:8000 to check it out

# Management Commands

## Populating the database

- cd to the `check_hunters` folder
- run the command `python manage.py populate_db`

# Testing
## Run tests through link
- cd to the "Brogrammers" folder
- run 
	`$ python manage.py runserver`
- go to localhost:8000/utests to run unit tests and receive results

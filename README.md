School Management Dashboard
===========================

Installation
-------------

1. Git clone the repo `https://github.com/maheshgudi/school-management-dashboard.git` or via ssh through `git@github.com:maheshgudi/school-management-dashboard.git`
2. Change working directory to *schoolmanager*.
> Note - Please set-up and activate a **python3.6** or higher virtualenv and run `pip install -r requirements.txt`.
3. This also has a `db.sqlite3` which is preloaded with dummy data. 
> Note - Ideally avoid checking-in raw database files.
4. Run the server by running the command ```python manage.py runserver```.
5. Homepage can be found on the url `http://localhost:8000`
6. Admin password is `username-*admin*, password-*admin*`

Solution
--------

The following questions are answered in 

1. Tabular preview of the classroom, subjects being taught in those classrooms, teachers using the
same.
- This can be found in the `View Classroom` page.
2. Search option to show a list of students attending a teacher’s class (teacher can be searched by name)
- This can be found in the `search teacher` page.
3. No of students taught by teachers earning more than 1 Lac per month and the sum of their salaries.
- This can be found in the `Teachers With Salary More Than 1 LPA` page.
4. No of students, No of teachers, and total hours required for subjects that are taught by more than 1 teacher.
- This can be found in the `Search Subject` page

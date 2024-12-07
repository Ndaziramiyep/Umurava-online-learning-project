# django-courses (Learning Management System)

Introducing **Django Courses**: the all-in-one solution for educators who want to launch their Online Course Website quickly and effortlessly.

- **Effortlessly manage your courses and lectures:** Organize your content seamlessly, categorize Courses, and manage lessons.
- **Empower your students:** Provide a smooth learning experience with intuitive navigation, and secure user accounts.

## 👨🏻‍💻 Built With 
This Learning Management System project is built with 
1. **Front-End:** HTML, CSS, JavaScript and Bootstrap
2. **Back-End:** Django (Python)
3. **Database:** SQLite (_Any other database can be added_)

_**ADD a STAR ⭐️ to this project 👆 if you like "Django Courses" project.**_


# 🤩 Features of the Project 

## A. Admin Can
1. Create a Course and then add multiple lectures on a course
2. Manage Users (Students)
3. Manage Social App Login


## B. Users/Visitors Can
1. Secure Authentication (Sign up, Login, Reset, etc.)
2. Login with Google and Github
3. Enroll to the course
4. See Enrolled Course or Search for new Course
5. Update Profile
6. Change Password


# 🤝 Support This Project 
[Buy Me a Coffee ☕️](https://buymeacoffee.com/vijaythapa)


# ⚙️ How to Install and Run this Project? 

## Pre-Requisites:
1. Install Git Version Control [ https://git-scm.com/ ]
2. Install Python Latest Version [ https://www.python.org/downloads/ ]
3. Install Pip (Package Manager) [ https://pip.pypa.io/en/stable/installing/ ]

_Alternative to Pip is Homebrew_

## Installation
**1. Create a Folder Where you want to save this project.**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows

```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

**3. Clone This Project (Using SSH)**
```
$  git clone git@github.com:vijaythapa333/django-courses.git
```
Then Enter The Project

```
$  cd django-courses
```

**4. Install Requirements from "requirements.txt"**
```
$  pip install -r requirements.txt
```
**5. Add the Hosts**
- Go To Settings.py file
- Then, On allowed hosts, Add [‘*’].

```
ALLOWED_HOSTS = ['*']
```

_NO need to Change on Mac_
**6. Run Server**
For Windows
```
$ python manage.py runserver
```
For Mac
```
$ python3 manage.py runserver
```

**7. Login Credentials**
Create a Super User with following command
```
$  python manage.py createsuperuser
```
Then Add Email, Username and Password

**or Use Default Credentials**

Username: _admin_
Password: _admin_


## For Sponsor or Projects Enquiry
1. Email - hi@vijaythapa.com
2. LinkedIn - [vijaythapa](https://www.linkedin.com/in/vijaythapa "Vijay Thapa on LinkedIn")
3. Donate - [https://buymeacoffee.com/vijaythapa](https://buymeacoffee.com/vijaythapa)

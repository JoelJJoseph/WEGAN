# Wegan Backend Framework 

<p text-align="left">
    <a href="https://github.com/akhil-s-kumar/Wegan-Framework/issues" alt="Issues">
        <img src="https://img.shields.io/github/issues/akhil-s-kumar/Wegan-Framework" /></a>
    <a href="https://github.com/akhil-s-kumar/Wegan-Framework/pulls" alt="Pull Requests">
        <img src="https://img.shields.io/github/issues-pr/akhil-s-kumar/Wegan-Framework" /></a>
    <a href="https://github.com/akhil-s-kumar/Wegan-Framework/network/members" alt="Forks">
        <img src="https://img.shields.io/github/forks/akhil-s-kumar/Wegan-Framework" /></a>
    <a href="https://github.com/akhil-s-kumar/Wegan-Framework/stargazers" alt="Stars">
        <img src="https://img.shields.io/github/stars/akhil-s-kumar/Wegan-Framework" /></a>
</p>

Wegan is a django-based backend framework for Wegan WebApp and Wegan Mobile App. Wgan Identify plant diseases using Image Processing and Machine learning Algorihm, and give solutions.

## :minidisc: Installation Instructions

If you want to work with this project or create a version of it make sure to follow the steps below!

It is recommended to use virtual environment to avoid conflicts with other projects.

0. Make sure that you have `Python3`, `virtualenv`, and `pip` installed.

1. Create a Project directory

 ```bash
        $ mkdir Wegan
        $ cd Wegan
```

2. Create a python3 virtualenv, and activate the environment to install requirements.

```bash
    $ python3 -m venv env
    $ source env/bin/activate
``` 

3. Install the project dependencies from `requirements.txt`

```
    (env)$ pip install -r requirements.txt
```

4. Clone the repository
   
```bash
    (env)$ git clone https://github.com/akhil-s-kumar/Wegan-Framework.git
    (env)$ cd Wegan-Framework
```

You have now successfully set up the project on your environment.

## :rocket: How to run  the project?

Make sure you are in `env` and then do the following each at a time.

```bash
(env)$ python manage.py makemigrations
(env)$ python manage.py makemigrations Disease
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
```

## :wrench: Tech Stacks

* **Language:**  Python 3.7
* **Framework:** Django 3.2.4
* **API:** GraphQL (Graphene)

## :gem: Contributors

1. [Akhil S Kumar](https://github.com/akhil-s-kumar) - Backend, Frontend for WebApp and API
2. [Joel John Joseph](https://github.com/JoelJJoseph) - Image Processing and Machine Learning Model
3. [Dharanya Lavanya](https://github.com/dharanyav) - Disease solution dataset and weather integration
3. [Abhishek Choudhary](https://github.com/shreemaan-abhishek) - Mobile App developer

### How to Contribute?
1. Fork this repository to your GitHub account
2. Follow the above installation process.
3. Find an issue or feature, and work on it.
4. Push your contribution to your forked repo and make a pull request.

#### Note: Change the remote repository to your forked one before pushing.

### How to work on the Frontend

1. Make sure to install this backend framework before getting work into Frontend.
2. Follow the [installation procedure](https://github.com/akhil-s-kumar/Wegan-WebApp) in the README file, to work with Fronend for WebApp.

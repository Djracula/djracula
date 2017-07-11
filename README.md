# Djracula

### Dracula + Django

Because dark feels good.<br>
A refined and classy designed suit for your django admin that makes you feel happy about data :)

### Demo App

Steps to run demo app for development

```
# root directory is where djracula folder is present
cd demo
# first create virtual env
virtualenv --no-site-packages pyenv
source pyenv/bin/activate
pip install -r requirements.txt
cd ..
# install djracula in editable mode, so that changes can be seen
pip install -e .

# now after virtual env is setup, run migrate and createsuperuser
cd demo
python manage.py migrate
python manage.py createsuperuser

# run server
python manage.py runserver

```


# [Find_Dev](https://findev-me.herokuapp.com/)


# create virtual environment
```
python -m venv .venv
```
# Select interpreter 
#### ctrl + shift + P 

# IF any problem in env activation : 
#### in admin powershell paste the command. 
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

# install modules 
```
pip install -r requirements.txt
```
# To open the site

## run the server 
```
python manage.py runserver
```

## Go to : 
```
http://127.0.0.1:8000/
```
### https://findev-me.herokuapp.com/ ---> findev.me (future)


# if any changes in database model. than use .
``` 
python manage.py makemigration
python manage.py migrate
```
# Before Deployment run : 
```
python manage.py collectstatic
```
# Heroku commands
### debug throught heroku cli


```
heroku update
heroku logs --tail
heroku logs --source app --tail

```
```
heroku domains:add findev.me -a find-dev
```

# Hard Refresh 
ctrl + shift + R




# contributers:
 - Anu Kumar
 - Sinesh
 - Anand Shukla
 - Ajeet Yadav








# References 
### mail : https://github.com/AnubhavMadhav/SendBeautifulEmails-GeeksForGeeks , https://mailtrap.io/blog/django-send-email/ , 
### deployment : heroku docs
### ER Diagram : https://drawsql.app/find-dev/diagrams/find-dev# 

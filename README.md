# Find_Dev


# create virtual environment
```
python -m venv .venv
```
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


# if any changes in database model. than use .
``` 
python manage.py migrate
```

# Hard Refresh 
ctrl + shift + R




contributers:
    - Anu Kumar
    - Sinesh
    - Anand Shukla
    - Ajeet Yadav

python manage.py collectstatic
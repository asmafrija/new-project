# altimate-platform-service

1) Deploy to Heroku

a) Ask Raouf for Heroku account credentials
b) Clone altimate-platform-service application and postgress locally
c) Please Make sure that you test well you changes locally before pushing to git and Heroku
d) Install Heroku :
    Ubuntu 16+ : sudo snap install heroku --classic
    macOS: brew install heroku/brew/heroku
    Windows : https://devcenter.heroku.com/articles/getting-started-with-python#set-up

Once installed, you can use the heroku command from your command shell.

e) Login to heroku CLI with the account of step (a) using 
    heroku login

f) Make sure your github and heroku branches are synchronized
    Execute git remote -v
    You should see : 
        heroku  https://git.heroku.com/doghello.git (fetch)
        heroku  https://git.heroku.com/doghello.git (push)
        origin  https://github.com/RaoufGhrissi/doghello-fastapi.git (fetch)
        origin  https://github.com/RaoufGhrissi/doghello-fastapi.git (push)
    
g) Push changes to git
h) Push chnages to heroku using git push heroku main
Please if you add new packages, update requirements.txt using pip freeze > requirements.txt, it's mandatory to help heroku undestand versions

i) if you update the models, run the alembic upgrda command on heroku using
heroku run alembic upgrade head

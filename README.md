# Pollar-backend
This repository contains flask app for my project Pollar.
This repository contains Pollar package.The Pollar webapp is used for taking polls.Users can make their account and create polls.Users will get share link for created poll which user can share with his/her friends. people can answer poll by clicking on share link but for voating they will have to create account first.User can see list if created polls in Mypolls section and to see result  of poll they can click on the poll title.There is also Answerpoll section where user can anserwer 10 latest Public polls.There is deadline set for every poll after which other user won't be able to vote on that poll.

This project uses Flask as web development framework and postgresql as RDMS.
The database is named as My_project in config.py file and can be changed in config.py in DBNAME key's value.
To start localhost for flask type following commands.
1) export FLASK_APP=Pollar
2)flask initdb
3)flask run

This app is deployed at : https://pollar-poll.herokuapp.com/
 

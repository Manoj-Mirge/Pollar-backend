from flask import Flask,render_template



def create_app():
     
   app=Flask("Pollar")
   app.config.from_object("config.DevelopmentConfig")

   from Pollar.sql import db
   db.init_app(app)


   
   









   @app.route("/")
   def index():
     return render_template("index.html")
     
   return app  
  

from flask import Flask,render_template



def create_app():
   
   app=Flask("Pollar")
   app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
   app.config.from_object("config.DevelopmentConfig")

   from Pollar.sql import db
   db.init_app(app)

   from Pollar.auth.auth import bp_auth
   app.register_blueprint(bp_auth)
   


   
   









   @app.route("/")
   def index():
     return render_template("index.html")
     
   return app  
  

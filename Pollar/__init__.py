from flask import Flask,render_template



def create_app():
     
   app=Flask("Pollar")
   
   
   
   @app.route("/")
   def index():
     return render_template("index.html")
     
   return app  
  

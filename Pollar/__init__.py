from flask import Flask,render_template



def create_app():
   
   app=Flask("Pollar")
   app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
   app.config.from_object("config.DevelopmentConfig")

   from Pollar.db import db
   db.init_app(app)

   from Pollar.auth.auth import bp_auth
   app.register_blueprint(bp_auth)


   from Pollar.createpoll.createpoll import bp_createpoll
   app.register_blueprint(bp_createpoll)
   
   from Pollar.answerpoll.answerpoll import bp_answerpoll
   app.register_blueprint(bp_answerpoll)
   
   from Pollar.pollresult.pollresult import bp_pollresult
   app.register_blueprint(bp_pollresult)

   from Pollar.mypolls.mypolls import bp_mypolls
   app.register_blueprint(bp_mypolls)






   @app.route("/")
   def index():
     return render_template("index.html")
     
   return app  
  

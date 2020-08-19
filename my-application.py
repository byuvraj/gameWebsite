from  flask import Flask, render_template, request, url_for, redirect, session
#from flask_session import Session
#from sqlalchemy import create_engine
#from sqlalchemy.orm import scopperd_session, sessionmaker
#import os
app=Flask(__name__)

#engine = create_engine(os.getenv("DATABASE_URL"))
#db=scopperd_session(sessionmaker(bind=engine))
#app.config("SESSION_PERMANENT")=False
#app.config["SESSION_TYPE"]="filesystem"
#app.secret_key = "hello"
#Session(app)

@app.route("/")
def default_page():
    return render_template("default_page.html")

@app.route("/downloads",methods=["POST","GET"])
def downloads():
    return render_template("downloads.html")

if __name__ == '__main__':
    app.run(debug = True) 

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Pollar.auth.auth import login_required
from Pollar.db.db import get_db
import datetime

bp_answerpoll = Blueprint('answerpoll', __name__,url_prefix='/answerpoll')



@bp_answerpoll.route('/<link>', methods=('GET', 'POST'))
@login_required
def answerpoll(link):
    if request.method=='POST':
         conn=get_db()
         cursor=conn.cursor()
        
         selected_option_id=request.form['vote']
         cursor.execute(
            "SELECT poll_id FROM poll_options WHERE poll_options_id=%s",
         (selected_option_id,))
         poll_id=cursor.fetchone()[0]
         cursor.execute(
         "SELECT p.vote_id FROM poll_votes p,poll_options o WHERE (p.vote=o.poll_options_id AND o.poll_id=%s) AND voter_id=%s",
         (poll_id,g.user[0]))
         vote_id=cursor.fetchone()
         if vote_id:
              return render_template('answerpoll/answerpoll.html',already_voted=True)
         cursor.execute(
         "INSERT INTO poll_votes (vote,voter_id,voted_on) VALUES (%s,%s,%s)",
         (selected_option_id,g.user[0],datetime.datetime.now()))
         conn.commit()
         return render_template('answerpoll/answerpoll.html',answered=True)
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute(
        "SELECT s.poll_id,p.author_id,p.deadline FROM share_link s,polls p WHERE s.link=%s AND s.poll_id=p.poll_id",
        (link,))
    poll_id,author_id,deadline=cursor.fetchone()
    
    if author_id==g.user[0]:
        return "hii go to see your poll result"
    
    if deadline < datetime.datetime.now():
        return render_template('answerpoll/answerpoll.html',end_of_deadline=True)
    
    cursor.execute(
        "SELECT p.vote_id FROM poll_votes p,poll_options o WHERE (p.vote=o.poll_options_id AND o.poll_id=%s) AND voter_id=%s",
        (poll_id,g.user[0]))
    vote_id=cursor.fetchone()
    if vote_id:
        return render_template('answerpoll/answerpoll.html',already_voted=True)
    

    cursor.execute(
        "SELECT title,description,created_on FROM polls WHERE poll_id=%s",
        (poll_id,))
    title,description,created_on=cursor.fetchone()
    cursor.execute(
        "SELECT option_title,poll_options_id FROM poll_options WHERE poll_id=%s",
        (poll_id,))    
    options=cursor.fetchall()
    no_of_options=len(options)
    return render_template('answerpoll/answerpoll.html',title=title
                                                    ,description=description
                                                     ,created_on=created_on
                                                     ,deadline=deadline    
                                                    ,no_of_options=no_of_options
                                                    ,options=options
                                                    ,share_link=link)
                                                    





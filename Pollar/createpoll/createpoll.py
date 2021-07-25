from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Pollar.auth.auth import login_required
from Pollar.db.db import get_db
import datetime

bp_createpoll = Blueprint('createpoll', __name__,url_prefix='/poll')



@bp_createpoll.route('/options', methods=('GET', 'POST'))
def options ():
    if request.method == 'POST':
        no_of_options=request.form['no_of_options']
        return redirect(url_for('createpoll.create',no_of_options=no_of_options))
        

    return render_template('createpoll/options.html')            




@bp_createpoll.route('/create', methods=('GET', 'POST'))
def create ():
    
    if request.method == 'POST':
            title=request.form['title']
            descrition=request.form['description']
            options=request.form.getlist('option')
            poll_privacy=request.form['poll_privacy']
            last_date=request.form['date']
            last_time=request.form['time']
            last_datetime=f"{last_date}  {last_time}"
            deadline = datetime.datetime.strptime(last_datetime, '%Y-%m-%d %H:%M')
            created_on=datetime.datetime.now()
            conn=get_db()
            cursor=conn.cursor()
            
            cursor.execute(
                "INSERT INTO polls (author_id,title,description,created_on,deadline,privacy) VALUES (%s,%s,%s,%s,%s,%s)",
                (g.user[0],title,descrition,created_on,deadline,poll_privacy))
            
            cursor.execute(
                "SELECT poll_id FROM polls WHERE created_on=%s AND author_id=%s",
                (created_on,g.user[0]))
            poll_id=cursor.fetchone()[0]
            
            for option in options:
                cursor.execute(
                    "INSERT INTO poll_options (poll_id,option_title) VALUES (%s,%s)",
                    (poll_id,option))

            conn.commit()
            return redirect(url_for('index'))

    no_of_options=request.args.get('no_of_options',None)
    date_of_today=datetime.date.today()
    max_deadline=date_of_today+datetime.timedelta(days = 2)
    
           
    return render_template('createpoll/create.html',no_of_options=int(no_of_options),date_of_today=date_of_today,max_deadline=max_deadline)
           

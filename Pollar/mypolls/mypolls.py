from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Pollar.auth.auth import login_required
from Pollar.db.db import get_db
import datetime



bp_mypolls = Blueprint('mypolls', __name__,url_prefix='/mypolls')

@bp_mypolls.route('/<user>')
@login_required
def mypolls(user):
    
    if user != g.user[1]:
        abort(404)
  
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute(
        "SELECT p.title,p.description,s.link FROM polls p,share_link s WHERE s.poll_id=p.poll_id AND p.author_id=%s ORDER BY p.poll_id DESC",
        (g.user[0],))
    mypolls=cursor.fetchall()
    return render_template('mypolls/mypolls.html',mypolls=mypolls)


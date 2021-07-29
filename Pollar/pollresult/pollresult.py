from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Pollar.auth.auth import login_required
from Pollar.db.db import get_db
import datetime

bp_pollresult = Blueprint('pollresult', __name__,)


@bp_pollresult.route('/pollresult/<poll_id>', methods=('GET', 'POST'))
@login_required
def pollresult(poll_id):
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute(
        "SELECT author_id FROM polls WHERE Poll_id=%s",
        (poll_id,))
    valid_poll_id=cursor.fetchone()
    if valid_poll_id:
          author_id=valid_poll_id[0]

    else:
        abort(404)
    if g.user[0]==author_id:
        cursor.execute(
            "SELECT title,description,created_on,deadline,privacy FROM polls WHERE Poll_id=%s",
            (poll_id,))
        title,description,created_on,deadline,privacy=cursor.fetchone()
        cursor.execute(
            "SELECT poll_options_id,option_title FROM poll_options WHERE Poll_id=%s",
            (poll_id,))
        options=cursor.fetchall()
        votes={}
        for row in options:
            cursor.execute(
                "SELECT vote_id FROM poll_votes WHERE vote=%s",
                (row[0],))
            no_of_votes=cursor.rowcount
            votes[row[1]]=no_of_votes
        cursor.execute(
            "SELECT v.vote_id FROM poll_votes v, poll_options p WHERE v.vote=p.poll_options_id AND p.Poll_id=%s",
            (poll_id,))
        total_votes=cursor.rowcount    
        date_of_today=datetime.datetime.now()
        return render_template('pollresult/result.html',title=title,
                                                        description=description,
                                                        created_on=created_on,
                                                        deadline=deadline,
                                                        privacy=privacy,
                                                        options=options,
                                                        votes=votes,
                                                        date_of_today=date_of_today,
                                                        total_votes=total_votes)

    else:
        abort(404)
                                                                  
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from Pollar.db.db import get_db

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


@bp_auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        cursor=conn.cursor()
        error = None

       
        cursor.execute(
            'SELECT id FROM pollar_user WHERE username =%s', (username,)
        )
        already_reg_id=cursor.fetchone()


        if already_reg_id is not None:
            error = f"User {username} is already registered."

        if error is None:
            cursor.execute(
                'INSERT INTO pollar_user (username, password) VALUES (%s,%s);',
                (username, generate_password_hash(password))
            )
            conn.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')



@bp_auth.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        next_url=request.form.get('next')
        conn = get_db()
        cursor=conn.cursor()
        error = None
        cursor.execute(
            'SELECT * FROM pollar_user WHERE username = %s ;', (username,)
        )
        user=cursor.fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user[2], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user[0]
            if next_url != 'none':
                return redirect(next_url)
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')



@bp_auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        conn=get_db()
        cursor=conn.cursor()
        cursor.execute(
            'SELECT * FROM pollar_user WHERE id = %s ;', (user_id,)
        )
        g.user = cursor.fetchone() 





@bp_auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
    


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login',next=request.url))

        return view(**kwargs)

    return wrapped_view
from ExamForm import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
from ExamForm.models import Item, User, OrderItem
from ExamForm.forms import RegisterForm, LoginForm
from ExamForm import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/SignUp', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              Email=form.Email.data,
                              password=form.password1.data,
                              mobile=form.validate_mobile.data,
                              School=form.School.data
                              )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(
            f'Account Created Successfully! You are logged in as: {user_to_create.username}', category='success')

        return redirect(url_for('afterLogin'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(
                f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('SignUp.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(
            username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_passward=form.password.data
        ):
            login_user(attempted_user)
            flash(
                f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('afterLogin'))
        else:
            flash('Username and password are not match! Please try again',
                  category='danger')

    return render_template('login.html', form=form)
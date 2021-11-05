from phat import app,db
from flask import render_template,url_for,flash,redirect
from phat.forms import RegisterForm,LoginForm
from phat.model import User
from flask_login import  login_user , logout_user



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/register',methods=['POST','GET'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash (f'{err_msg}',category='danger')


    return render_template('register.html',form = form)

@app.route('/login',methods=['POST','GET'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash('Đăng Nhập Thành công',category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Đăng nhập không thành công ',category='danger')


    return render_template('login.html',form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("Bạn đã đăng xuất",category='info')
    return redirect(url_for('home_page'))
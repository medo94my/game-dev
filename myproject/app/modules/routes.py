from flask import render_template, flash, redirect, session, logging, request, url_for
import os
import dns
import bcrypt
from datetime import datetime
from app import app ,db
from app.modules.forms import LoginForm ,RegisterForm, GameForm
from app.modules.utils import is_logged_in
@app.route('/')
def home():
    return render_template('home.html')
# about page route
@app.route('/about')
def about():
    return render_template('about.html')

# user login route
@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # Get From Fields
        username = form.username.data
        password_candidate = form.password.data
        print(username,password_candidate)
        result = db.users
        login_user = result.find_one({'username': username})
        # ? checks if user exists
        if login_user:
            # get stored hash
            # compare the passwords
            if bcrypt.hashpw(password_candidate.encode('utf-8'), login_user['password']) == login_user['password']:
                # passed
                session['logged_in'] = True
                session['username'] = username
                flash('YOO ARE LOGGED IN', 'success')
                return redirect(url_for('home'))
            else:
                # if account password not correct redirect to login page with invalid login error
                error = 'invalid login'
                return render_template('login.html', error=error)

        else:
             # if account does not exists redirect to login page with invalid login error
            error = 'Username noy found'
            return render_template('login.html', error=error)

    return render_template('auth/login.html',form=form)
# Register page route
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        # age = request.form['age']
        # type_person = request.form['type']
        # edu_lvl = request.form['edu_lvl']
        # major = request.form['major']
        # job = request.form['job']
        password = bcrypt.hashpw(
            form.password.data.encode('utf-8'), bcrypt.gensalt())
        user_collection = db.users
        user_collection.insert_one({
                'name': name,
                'email': email,
                'username': username,
                'password': password,
            })
        #  check for empty field :age Occupation and education
        # if age == '' or type_person == "" or edu_lvl == '':
        #     flash('please complete your information ', 'danger')
        #     return render_template('register.html', form=form)
        # else:
        #     # check if username exists in the database duplication not allowed
        #     if user_collection.find({'username': username}).count() >= 1:
        #         # send back to register page with error message
        #         flash("username is taken", 'danger')
        #         return render_template('register.html', form=form)
        #     else:
        #         # check if user email has been registered previously
        #         if user_collection.find({'email': email}).count() >= 1:
        #             # send back to register page with error message
        #             flash('this email is duplicated before', 'danger')
        #             return render_template('register.html', form=form)
        #         else:
        #             # check for chosen occupation before store in database
        #             if type_person == 'Student':

        #                 user_collection.insert_one({'name': name,
        #                                             'email': email,
        #                                             'username': username,
        #                                             'password': password,
        #                                             'age': age,
        #                                             'profile': {
        #                                                 'occupation': type_person,
        #                                                 'education': edu_lvl,
        #                                                 'major': major,
        #                                             }

        #                                             })
        #                 # check for chosen occupation before store in database
        #             elif type_person == 'Non-Student':

        #                 user_collection.insert_one({'name': name,
        #                                             'email': email,
        #                                             'username': username,
        #                                             'password': password,
        #                                             'age': age,
        #                                             'profile': {
        #                                                 'occupation': type_person,
        #                                                 'job': job
        #                                             }
        #                                             })
        #             # if registration proccess completed at met all criteria user will be redircted to login screen
        flash('you are now registered and can login', 'success')
        return redirect(url_for('login'))
    # if somthing goes wrong user will be sent to register screen
    return render_template('auth/register.html', form=form)

# Games page route
@app.route('/games', methods=['GET','POST'])
@is_logged_in
def games():
    game = db.users
    games = game.find_one({'username': session['username']}, {
                      '_id': 0, 'game': 1})
    # checks if any game exists in user account
    form= GameForm(request.form)
    if request.method == 'POST' and form.validate():
        add_game(form,games)
        return redirect(url_for('games'))
    return render_template('game/games.html',
                            games=games,
                            form=form)
# add an Game route
def add_game(form,games):
    # Getting from request
    title = form.title.data
    x = db.users
    print(games)
    if games:
        for key in games['game']:
            if key['title'] != title:
                x.update_one({
                    'username': session['username']
                    },
                    {
                    '$push': {
                        'game': {
                            'title': title.strip(),
                            'Added_date': datetime.now().strftime("%d-%b-%y %H-%M-%p")
                            }
                    }})
                return flash('Game added', 'success')
        



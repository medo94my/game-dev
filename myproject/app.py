from flask import Flask, render_template, flash, redirect, session, logging, request, url_for
import os
import dns
from pymongo import MongoClient
import bcrypt
import datetime
from datetime import timedelta
from game_core import Student
from MM_A01_002 import Student2
from Dynamic import Dynamic
# game = Dynamic()
# Student1 = Student()
# Student2 = Student2()
# Student1.randomize()
# Student2.randomize()

app = Flask(__name__)
# connection to mongoDb atlas
# app.secret_key =\

print (app.secret_key)

client = MongoClient("mongodb+srv://ahmed:yt2kMlCzVVLT5A9d@flaskapp1-lohte.mongodb.net/test?retryWrites=true&w=majority")
mongo = client.test
# app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

# connection to mongo DB local
#app.config["MONGO_URI"] = "mongodb://localhost:27017/myapp"
# mongo = PyMongo(app)



# Check if user loggedin






# Register page route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        age = request.form['age']
        type_person = request.form['type']
        edu_lvl = request.form['edu_lvl']
        major = request.form['major']
        job = request.form['job']
        password = bcrypt.hashpw(
            form.password.data.encode('utf-8'), bcrypt.gensalt())
        user_collection = mongo.db.users
        #  check for empty field :age Occupation and education
        if age == '' or type_person == "" or edu_lvl == '':
            flash('please complete your information ', 'danger')
            return render_template('register.html', form=form)
        else:
            # check if username exists in the database duplication not allowed
            if user_collection.find({'username': username}).count() >= 1:
                # send back to register page with error message
                flash("username is taken", 'danger')
                return render_template('register.html', form=form)
            else:
                # check if user email has been registered previously
                if user_collection.find({'email': email}).count() >= 1:
                    # send back to register page with error message
                    flash('this email is duplicated before', 'danger')
                    return render_template('register.html', form=form)
                else:
                    # check for chosen occupation before store in database
                    if type_person == 'Student':

                        user_collection.insert_one({'name': name,
                                                    'email': email,
                                                    'username': username,
                                                    'password': password,
                                                    'age': age,
                                                    'profile': {
                                                        'occupation': type_person,
                                                        'education': edu_lvl,
                                                        'major': major,
                                                    }

                                                    })
                        # check for chosen occupation before store in database
                    elif type_person == 'Non-Student':

                        user_collection.insert_one({'name': name,
                                                    'email': email,
                                                    'username': username,
                                                    'password': password,
                                                    'age': age,
                                                    'profile': {
                                                        'occupation': type_person,
                                                        'job': job
                                                    }
                                                    })
                    # if registration proccess completed at met all criteria user will be redircted to login screen
                    flash('you are now registered and can login', 'success')
                    return redirect(url_for('login'))
    # if somthing goes wrong user will be sent to register screen
    return render_template('register.html', form=form)


# user login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get From Fields
        username = request.form['username']
        password_candidate = request.form['password']
        result = mongo.db.users
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
                return redirect(url_for('games'))
            else:
                # if account password not correct redirect to login page with invalid login error
                error = 'invalid login'
                return render_template('login.html', error=error)

        else:
             # if account does not exists redirect to login page with invalid login error
            error = 'Username noy found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# User logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('you are logged out', 'success')
    return redirect(url_for('login'))
# User Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    m = mongo.db.users
    games = m.find({'username': session['username']}, {'_id': 0, 'games': 1})
    if games:
        return render_template('dashboard.html', games=games)
    else:
        msg = 'No Game Found'
        return render_template('dashboard.html', msg=msg)
    # cur.close()

# Games page route
@app.route('/games')
@is_logged_in
def games():
    game = mongo.db.users
    games = game.find({'username': session['username']}, {
                      '_id': 0, 'game': 1})
    # checks if any game exists in user account
    if games:
        return render_template('games.html', games=games)
    else:
        msg = 'No Games Found'
        return render_template('games.html', msg=msg)
# # Single article route by passing article id
# @app.route('/article/<id>/')
# def article(id):
#     m = mongo.db.users.find_one()

#     return render_template('article.html', article=m)
# # Create a Class to initialize registration form
# # Class


class GameForm(Form):
    title = StringField('Title', [validators.length(min=1, max=200)])
    game_id = StringField('id', [validators.length(min=1, max=10)])
    # body = TextAreaField('Body', [validators.length(min=30)])
# add an Game route
@app.route('/add_game', methods=['GET', 'POST'])
@is_logged_in
def add_game():
    # Getting from request

    if request.method == 'POST':
        title = request.form['gamecode']
        x = mongo.db.users
        x.update({'username': session['username']}, {
            '$push': {
                'game': {'title': title,
                         'Added_date': datetime.datetime.now().strftime("%d-%b-%y %H-%M-%p")}
            }})
        flash('Game added', 'success')

        return redirect('games')
    return render_template('index.html')


# @app.route('/edit_game/<id>', methods=['GET', 'POST'])
# @is_logged_in
# def edit_game(id):

#     result = mongo.db.games
#     edit = result.find_one({})
#     # # Get form

#     form = GameForm(request.form)
#     # # populate article from fields
#     form.game_id.data = edit['_id']
#     form.title.data = edit['title']
#     # form.body.data = edit['body']

#     if request.method == 'POST' and form.validate():
#         game_id = request.form['game_id']
#         title = request.form['title']
#         # body = request.form['body']
#         updating = mongo.db.users
#         pprint.pprint(id)
#         updating.update_one({}, {
#             '$set': {"_id": game_id, "title": title}})
#         flash('Game updated', 'success')
#         return redirect(url_for('dashboard'))
#     return render_template(('edit_game.html'), form=form)

# # Delete Game route
# @app.route('/delete_game/<string:id>', methods=['POST'])
# @is_logged_in
# def delete_game(id):

#     delete = mongo.db.users
#     delete.delete_one({})
#     flash('Game Deleted', 'success')
#     return redirect(url_for('dashboard'))

# .................................................................
# game route
@app.route('/gameboard')
@is_logged_in
def gameboard():

    return render_template('gameboard.html')
# .................................................................
# game route
@app.route('/MM_A01_002')
@is_logged_in
def MM_A01_002():

    return render_template('MM_A01_002.html')
# ..............................................begin Game proscess..........................
# game route
@app.route('/MM_A02_002')
@is_logged_in
def MM_A02_002():

    return render_template('Dynamic.html')
# ..............................................begin Game proscess..........................
@app.route('/process', methods=['POST', 'GET'])
@is_logged_in
def process():
     # POST request
    if request.method == 'POST':
        if request.get_json() == 'counter':
            # Student1.check.res
            # Setting Score to 15
            Student1.Score = 15
            # Setting counter back to zero
            Student1.Counter = 0
            # run the analyzer fir the new game
            Student1.Value_Analyzer = []
            # crearte a new random list if game restart
            Student1.randomize()

            return 'yes'

        else:
            print('Incoming..')
            # recvieing json from java script and store it in variable and convert it from json to list
            Guessed = {"Guess": [int(request.get_json()['Guess'][i])
                                 for i in range(len(request.get_json()['Guess']))]}
            print({"Guess": [int(request.get_json()['Guess'][i])
                             for i in range(len(request.get_json()['Guess']))]})  # parse as JSON
            # make list as one line using join and map
            Guessed_oneline = ''.join(map(str, Guessed["Guess"]))
            # printing the recvied value through json
            print(Guessed)
            # printing variable Guessed in one line
            print(Guessed_oneline)
            # passing value to the game core
            Student1.check(Guessed_oneline)
            # Storing the result in dictionary
            result = {'right': Student1.cright,
                      'wrong': Student1.cwrong, 'correct': Student1.num_correct, "number": Guessed['Guess'], 'Counter': Student1.Counter}
            # result = Student1.Guesses_Dic
            # print result out to check for accuracy
            print(result)

            # print(Student1.Counter)
            #  checks if guessed numbers are correct store it in variable result
            if Student1.cright == 4:
                Student1.analyze()
                result = {'right': Student1.cright,
                          'wrong': Student1.cwrong,
                          'correct': Student1.num_correct,
                          "score": Student1.Score,
                          "number": Guessed['Guess'], 'Counter': Student1.Counter}
                # Sending the result to database
                mongo.db.users.update({'username':session['username']},{'$push':{"game.0.result":result}})
                print(result)
                Student1.Score = 15
                Student1.Counter = 0

            elif Student1.Counter == 10:
                mongo.db.users.update({'username':session['username']},{'$push':{"game.0.result":result}})
                Student1.Counter = 0
                print("You have exceeded the limit of 10 tries.")
            return result

    else:

        return render_template('gameboard.html')


# .........................................end......................
# ---------------------------------------MM_A01-002 play(begin)--------------
@app.route('/MM_A01_002_P', methods=['POST', 'GET'])
@is_logged_in
def MM_A01_002_P():
     # POST request
    if request.method == 'POST':
        if request.get_json() == 'counter':
            # Student1.check.res
            Student2.Score = 15
            Student2.Counter = 0
            Student2.Value_Analyzer = []
            Student2.randomize()

            return 'yes'

        else:
            print('Incoming..')
            Guessed = {"Guess": [int(request.get_json()['Guess'][i])
                                 for i in range(len(request.get_json()['Guess']))]}
            print({"Guess": [int(request.get_json()['Guess'][i])
                             for i in range(len(request.get_json()['Guess']))]})  # parse as JSON
            # print(request.get_json())
            Guessed_oneline = ''.join(map(str, Guessed["Guess"]))
            # Student1 = Student(Guessed_oneline)
            print(Guessed)
            print(Guessed_oneline)
            Student2.checked(Guessed_oneline)
            # result = {'values': Student1.Value_Analyzer,
            #           'score': Student1.Score}
            result = {'right': Student2.cright,
                      'wrong': Student2.cwrong, 'correct': Student2.num_correct, "number": Guessed['Guess'], 'Counter': Student2.Counter}
            # result = Student1.Guesses_Dic
            print(result)
            print(Student2.Counter)

            if Student2.cright == 6:
                Student2.analyze()
                result = {'right': Student2.cright,
                          'wrong': Student2.cwrong,
                          'correct': Student2.num_correct,
                          "score": Student2.Score,
                          "number": Guessed['Guess'], 'Counter': Student2.Counter}
                # result = Student1.Guesses_Dic
                print(result)
                Student2.Score = 15
                Student2.Counter = 0
                mongo.db.users.update({'username':session['username']},{'$push':{"game.1.result":result}})
            elif Student2.Counter == 10:
                Student2.Counter = 0
                print("You have exceeded the limit of 10 tries.")
            return result

    else:

        return render_template('gameboard.html')

# ---------------------------------------MM_A02-002 play(end)--------------

@app.route('/MM_A02_002_P', methods=['POST', 'GET'])
@is_logged_in
def MM_A02_002_P():
     # POST request
    
    if request.method == 'POST':
        # if request.get_json() == 'counter':
        #     # Student1.check.res
        #     Student2.Score = 15
        #     Student2.Counter = 0
        #     Student2.Value_Analyzer = []
        #     Student2.randomize()

            # return 'yes'

        # else:
        print(request.get_json())
        print(request.get_json()['number'])
        print(request.get_json()['color'])
        print(request.get_json()['letter'])
        number=int(request.get_json()['number'])
        color=int(request.get_json()['color'])
        letter=int(request.get_json()['letter'])
       
        game.randomize(number,color,letter)
        print(len(game.Answer))
        return str(len(game.Answer))

    else:

        return render_template('gameboard.html')

# ---------------------------------------MM_A02-002 play(end)--------------
@app.route('/MM_A02_002_Post', methods=['POST', 'GET'])
def Post():
    if request.method == 'POST':
        if request.get_json() == 'counter':
            # Student1.check.res
            game.Score = 15
            game.Counter = 0
            game.Value_Analyzer = []
            game.randomize(MM_A02_002_P.number,MM_A02_002_P.color,MM_A02_002_P.letter)

            return 'yes'
        else:
            if request.method=='POST':
                    print(request.get_json())
                    Guessed = request.get_json()['Guess']
                    print(Guessed) 
                    game.check(Guessed)
                    result = {'right': game.cright,
                        'wrong': game.cwrong, 'correct': game.num_correct, "number": Guessed, 'Counter': game.Counter,"score": 0}
                    length=len(game.Answer)
                    if game.cright == length:
                        game.analyze()
                        result = {'right': game.cright,
                                'wrong': game.cwrong,
                                'correct': game.num_correct,
                                "score": game.Score,
                                "number": Guessed, 'Counter': game.Counter}
                        # result = Student1.Guesses_Dic
                        print(result)
                        game.Score = 15
                        game.Counter = 0
                        mongo.db.users.update({'username':session['username']},{'$push':{"game.2.result":result}})
                    elif game.Counter == 10:
                            game.Counter = 0
                            print("You have exceeded the limit of 10 tries.")
                    return result

if __name__ == '__main__':
      # secret key for form to work
    app.run(debug=True,port=8000)

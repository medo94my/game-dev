# home page route
@app.route('/')
def index():
    return render_template('home.html')
# about page route
@app.route('/about')
def about():
    return render_template('about.html')
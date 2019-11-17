> # FUNMATHGAME Web Application

This a documentation of the steps of creating the back end of Fun Math Game web app
The backend is handled by using Flask framework

## The base for this application

Please refer to YouTube [Traversy media](https://www.youtube.com/watch?v=zRwy8gtgJ1A&list=PLillGF-RfqbbbPz6GSEM9hLQObuQjNoj_) channel for this flask tutorial

> ### Step 1: Tools and Technologies

1. Install python in your computer
2. Text Editor for writing code such as vscode (recommended), sublime text or notepad++

> ### Step 2: Setting up the environment

First, we need to download flask using.

```cmd
pip install flask
```

1. open a new file and name it app.py
2. To start your first flask follow below code:

```python
from flask import Flask

app = Flask ('__name)')

if __name__ =='__main__':
    app.run()
```

3. To run the application:

```cmd
python app.py
```

it will give a link like 128.0.0.1/5000 copy it and paste it in your browser then it will show not found because we did not create any route for main page.

4. now adding the route to flask :

```python
@app.route('/')
def index():
    return 'index'
```

if we run the application again it will show index like so :
![flask](img/flask/index.PNG)

5. to see the changes without restarting the server turn the debugging mode on

```python
if __name__ == '__main__':
    app.run(debug=True)
```

6.to add add a html page for the route need to import one more module

```python
from flask import Flask, render_template
```

this module will look for folder called templates to look for the file
so make a new folder and name it templates and make a new html file with name home.html
![new](img/flask/template.PNG)

and the code inside the app.py will look like this :

```python
from flask import Flask, render_template

app=Flask('__name__')

@app.route('/')
def index():
    return render_template('home.html')
if __name__ =='__main__':
    app.run(debug=True)
```

for home page we just write HOME to see if server will work correctly with the template.

```html
HOME
```

like so. Now server will go to home file and show it on the browser

Now create another html file and name it **layout.html** to hold our main html code so no need to repeat for each page created.

Now back to **home.html** and do the following :

```html
{% extends 'layout.html;' %} {% block body %} Home {% end block %}
```

as in previous example need to **extends the layout file** for server to know which file to call when want to call the code needed to be shown in the main layout.

#### Now to give the application more style and look more user friendly will use bootstrap cdn for CSS and JavaScript

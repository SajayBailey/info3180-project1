"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for
import time
from werkzeug.utils import secure_filename
from forms import LoginForm
from models import UserProfile
from flask_login import login_user, logout_user, current_user, login_required


def timeinfo():
    return time.strftime("%a, %d %b %Y")
    

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

    
@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="INFO3180 PROJECT 1")

## route for adding a profile
@app.route("/profile", methods=['POST', 'GET'])
def profile_form():
    
    prifile_pic_folder = 'app/static/pics'
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            age = request.form['age']
            sex = request.form['Sex']
            bio = request.form['bio']
            created_on = timeinfo()
            profile_pic = request.form['prfile_pic']
            
            
            # save pic to pics file
            filename = secure_filename(profile_pic.filename)
            profile_pic.save(os.path.join(prifile_pic_folder, filename))
            
            flash('Success!!!')
            return render_template('home.html')
    
    return render_template("profile_form.html")
    
   
   
## route for viewing a list of all user profiles
# @app.route("/profiles", method = ["GET"])
# def view_all_profiles():
#     return render_template("all_profiles.html")
    

## route for viewing an individual profile
# @app.route("/profile/<userid>", method = ["GET"])
# def search_profile():
#     return
    
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
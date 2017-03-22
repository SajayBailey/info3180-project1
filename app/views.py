"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from werkzeug.utils import secure_filename
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
# from forms import LoginForm
from app.models import UserProfile
import time
import os, random



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
    return render_template('about.html', name="Mary Jane")

@app.route('/secure-page/')
@login_required
def secure_page():
    """Render a secure page on our website that only logged in users can access."""
    return render_template('secure_page.html')
    
    
# function to calculate time profile was created
def timeinfo():
    return time.strftime("%a, %d %b %Y")
    
    
#route for adding a profile
@app.route("/profile", method = ['GET', 'POST'])
def add_profile():
    
    id_strt = random.randint(0,99999)
    prifile_pic_folder = 'app/static/pics'
    
    if request.method == 'POST':
        userid = id_strt
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        sex = request.form['sex']
        bio = request.form['bio']
        created_on = timeinfo()
        profile_pic = request.form['profile_pic']
        username = request.form['username']
        
        
        # save pic to pics file
        filename = secure_filename(profile_pic.filename)
        profile_pic.save(os.path.join(prifile_pic_folder, filename))
        
        user = UserProfile(userid, firstname,lastname,username, age, bio, created_on, profile_pic)
        db.session.add(user)
        db.session.commit()
        flash('Success!!!')
        
            
    return render_template('profile.html')





# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


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
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")

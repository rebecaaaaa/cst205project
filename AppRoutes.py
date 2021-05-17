##Title: CST205Project
##Abstract:
# ******
# Flask Application designed to create a social media platform for women
# where they can access careers, resources, and for employers to submit their
# job postings. Hopes to destroy the idea that women must destroy their feminity in order
# to be take seriously in the 'professional' world. Career women can be business - forward while also
# being feminine. One does not depend on the other. Careers do not destroy individuality.
# ******
##Class: CST205
##Prof: Avner Biblarz
##Authors: Alexia Leon Lopez, Rebeca Chavez, Stephanie Hernandez
##Date: Apr. 28th 2021
##Estimate: 20 Hours

from flask import Flask, render_template, flash, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from  flask_bootstrap import Bootstrap
from PIL import Image

# creating an instance of a Flask app
app = Flask(__name__)

# using bootstrap
bootstrap = Bootstrap(app)

# security feature wtf provides against forgery & scrapping/
# behind the scences of csrf.token in html
app.config['SECRET_KEY'] = 'csumb-proj'

# Connect Page Logic
class LinkedIn(FlaskForm):
    name = StringField(
        'Name: ',
        validators=[DataRequired()] # Won't submit unless something there (validator)
    )
    occupation = StringField(
        'Occupation: ',
        validators=[DataRequired()]
    )
    link = StringField(
        'Link: ',
        validators=[DataRequired()]
    )

class GitHub(FlaskForm):
    name = StringField(
        'Name: ',
        validators=[DataRequired()] # Won't submit unless aomething there (validator)
    )
    project = StringField(
        'Project Title: ',
        validators=[DataRequired()]
    )
    description = StringField(
        'Description: ',
        validators=[DataRequired()]
    )
    link = StringField(
        'Link: ',
        validators=[DataRequired()]
    )

people = []
repos = []

def store_ppl(my_name, my_occupation, my_link):
    people.append(dict(
        name = my_name,
        occupation = my_occupation,
        link = my_link

    ))

def store_repos(my_name, my_proj, my_descr, my_link):
    repos.append(dict(
        name = my_name,
        project = my_proj,
        description = my_descr,
        link = my_link

    ))

# creating route for main page, will display the images of authors + biography + links to other pages
@app.route('/', methods=('GET', 'POST')) ## all authors will collobarate on main page
def mp():
    form = LinkedIn()
    form2 = GitHub()

    if form.validate_on_submit():
        store_ppl(form.name.data, form.occupation.data, form.link.data)
        return redirect('/view_linkedIn')

    if form2.validate_on_submit():
        store_repos(form2.name.data, form2.project.data, form2.description.data, form2.link.data)
        return redirect('/view_gitHub')

    return render_template('main_page.html')

@app.route('/careerPage') ## career page = Rebeca
def cp():
    return render_template('career_page.html')

@app.route('/resourcePage',methods=('GET', 'POST')) ##resource page = Alexia L.
def rp():
    return render_template('resource_page.html')

@app.route('/connectPage', methods=('GET', 'POST')) ## connect page = Stephanie H.
def p4():
    form = LinkedIn()
    form2 = GitHub()

    return render_template('connect.html', form=form, form2=form2)

@app.route('/view_linkedIn')
def vppl():
    return render_template('vppl.html', people=people)

@app.route('/view_gitHub')
def vgh():
    return render_template('vgh.html', repos=repos)

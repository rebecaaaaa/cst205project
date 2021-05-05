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

from flask import Flask, render_template
from  flask_bootstrap import Bootstrap
from PIL import Image

# creating an instance of a Flask app 
app = Flask(__name__)

# using bootstrap 
bootstrap = Bootstrap(app)

# creating route for main page, will display the images of authors + biography + links to other pages
@app.route('/') ## all authors will collobarate on main page 
def mp(): 
    return render_template('main_page.html')

# @app.route('/careerPage/<linkClicked>') ## career page = Rebeca 
# def cp(): 
#     return render_template()

# @app.route('/resourcePage/<linkClicked>') ## resource page = 
# def cp(): 
#     return render_template()

# @app.route('/connectPage/<linkClicked>') ## connect page = 
# def cp(): 
#     return render_template()
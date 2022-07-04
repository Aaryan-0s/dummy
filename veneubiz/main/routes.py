import email
from turtle import title
from flask import  flash, redirect,render_template,url_for,request,abort,Blueprint,current_app
from venuebiz import bcrypt,db,mail
from venuebiz.main.forms import Contact
from venuebiz.models import Venue,venue_book
from flask_login import login_user,current_user,logout_user,login_required
from venuebiz.main.utils import send_contact







main=Blueprint('main',__name__)


@main.route("/",methods=['POST','GET'])
def home():
    if request.method=='POST':
        if request.form['search']=='search':
            if (Venue.query.filter_by(venue_name=request.form['srch-1']).first()):
                posts=Venue.query.filter_by(venue_name=request.form['srch-1']).first()
                return  render_template("search_venue.html",posts=posts)
            else:
                flash("venue doesnt exist")
    return render_template("home.html")






@main.route("/about")
def about():
    return render_template('about.html', title='aboutus')


@main.route("/contact",methods=['POST','GET'])
def contact():
    form=Contact()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        phone=form.phone.data
        query=form.query.data
        send_contact(email,name,phone,query)
        flash("Post has been created")
        return redirect(url_for("main.home"))
        
        
         
    return render_template('contact.html', title='contactus',form=form)






@main.route("/bookedview")
@login_required
def bookedview():
    return render_template('bookedview.html', title='bookedview')


@main.route("/wishlist")
@login_required
def wishlist():
    return render_template('wishlist.html', title='wishlist')

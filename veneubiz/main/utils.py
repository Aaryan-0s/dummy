import email
from email.mime import image
from turtle import title
from flask import  flash, redirect,render_template,url_for,request,abort,Blueprint,current_app
from venuebiz import bcrypt,db,mail
from flask_login import login_user,current_user,logout_user,login_required
from venuebiz.users.forms import UpdateAccountForm,RequestResetForm,ResetPasswordForm
import secrets
from PIL import Image
import os
from flask_mail import Message



# needs to be changed
def send_contact(email,name,phone,query):

    msg=Message('Password reset request ',sender='aaryanbasnet16@gmail.com',
                                        recipients=[email])
    msg.body=f'''
    name:{name}
    phone:{phone}
    query:{query}

'''
    mail.send(msg)
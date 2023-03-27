from flask import Blueprint, render_template as rt, request, flash, jsonify 
from flask_login import login_required,current_user
from .models import Profile
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        position = request.form.get('position')

        if len(fname) < 1:
            flash('Please enter a valid first name',category='Error')
        elif len(lname) < 1:
            flash('Please enter a valid last name',category='Error')
        elif len(position) < 1:
            flash('Please enter a valid position',category='Error')
        else:
            full_profile = Profile(fname=fname,lname=lname,position=position,user_id=current_user.id)
            db.session.add(full_profile)
            db.session.commit()

            flash('Information saved in database.',category='Success')

    return rt('home.html',user=current_user,name=request.form.get('fname'))

@views.route('/delete-field', methods=['POST'])
def delete_note():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Profile.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})





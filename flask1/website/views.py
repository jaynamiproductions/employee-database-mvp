from flask import Blueprint, render_template as rt, request, flash, jsonify, send_file
from flask_login import login_required,current_user
from .models import Profile, Cert
from . import db
import json
from io import BytesIO
import sqlite3


views = Blueprint('views', __name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    return rt('home.html',user=current_user)

@views.route('/demographics',methods=['GET','POST'])
@login_required
def demo():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        position = request.form.get('position')

        file = request.files['file']

        if len(fname) < 1:
            flash('Please enter a valid first name',category='Error')
        elif len(lname) < 1:
            flash('Please enter a valid last name',category='Error')
        elif len(position) < 1:
            flash('Please enter a valid position',category='Error')
        else:
            full_profile = Profile(fname=fname,lname=lname,position=position,filename=file.filename,filedata=file.read(),user_id=current_user.id)
            db.session.add(full_profile)
            db.session.commit()

            flash('Information saved in database.',category='Success')

    return rt('demo.html',user=current_user,name=request.form.get('fname'))


@views.route('/certificates',methods=['GET','POST'])
@login_required
def cert():
    if request.method == 'POST':
        acls = request.form.get('acls')
        trophon = request.form.get('trophon')
        full_cert = Cert(acls_cert=acls,annual_trophon=trophon,user_id=current_user.id)

        db.session.add(full_cert)
        db.session.commit()

    return rt('certs.html',user=current_user,name=request.form.get('fname'))

@views.route('/admin', methods=['GET','POST'])
@login_required
def admin(): # set admin users here
    if current_user.email == '':
        flash('Successfully accessed Admin page.',category='Success')
        connect = sqlite3.connect('instance/database.db')
        c = connect.cursor()
        sql1 = 'SELECT * FROM profile'
        c.execute(sql1)
        output = c.fetchall()
        return rt('admin2.html',user=current_user,data=output)
    else:
        flash('Admin page access denied.',category='Error')
        return rt('admin.html',user=current_user)

@views.route('/download/<upload_id>')
def download(upload_id):
    upload = Profile.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.filedata), download_name=upload.filename,as_attachment=True)

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

@views.route('/delete-field2', methods=['POST'])
def delete_note2():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Cert.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})







from flask import Blueprint, render_template, request, redirect, url_for

login_bp = Blueprint('login', __name__)

@login_bp.route('/')
def login():
    return render_template('login.html')
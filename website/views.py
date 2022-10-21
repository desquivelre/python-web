from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/index')
def index():
    return render_template("index.html")


@views.route('/view-table')
def view_table():
    return render_template("tables.html")

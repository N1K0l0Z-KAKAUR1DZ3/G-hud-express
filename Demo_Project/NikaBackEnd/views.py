from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def shop():
    return "<h1> Test </h1>"
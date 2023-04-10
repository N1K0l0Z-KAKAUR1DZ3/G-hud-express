from flask import Blueprint, render_template
from .models import User

front_man = Blueprint('front_man', __name__)

@front_man.route('/pending-accounts')
def pending_accounts():
    # Retrieve all users who have a status of "pending"
    users = User.query.filter_by(status='pending').all()
    return render_template('pending-accounts.html', users=users)


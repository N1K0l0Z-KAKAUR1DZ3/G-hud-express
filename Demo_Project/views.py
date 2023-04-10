from flask import Blueprint, render_template
from .models import User, db
from flask import redirect, flash, url_for


views = Blueprint('views', __name__)

@views.route('/')
def base():
    return render_template("base.html")

@views.route("/pending-approval")
def pending():
    return render_template("pending-approval.html")

@views.route("/shop")
def shop():
    return render_template("shop.html")

@views.route('/approve_user/<int:user_id>', methods=['POST'])
def approve_user(user_id):
    user = User.query.get_or_404(user_id)
    user.approved = True
    db.session.commit()
    flash('User approved successfully', 'success')
    return redirect(url_for('users.pending_approval'))

@views.route('/reject_user/<int:user_id>', methods=['POST'])
def reject_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User rejected successfully', 'success')
    return redirect(url_for('users.pending_approval'))


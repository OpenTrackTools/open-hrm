from flask import (
    Blueprint,
    request
)
from api.authentication.models import User


validation_bp = Blueprint(
    'validation',
    __name__,
    url_prefix='/validate'
)


@validation_bp.route("/check_email", methods=['POST'])
def check_email():
    email_to_check = request.form['email']
    user = User.query.filter_by(email=email_to_check).first()
    
    if user:
        return "<p>Email is already taken. Please try with a different name</p>", 422
    
    return "", 200


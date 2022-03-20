from flask import (
    render_template,
    Blueprint
)
from .forms import RegistrationForm


auth_bp = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/auth',
    url_prefix="/auth"
)


@auth_bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

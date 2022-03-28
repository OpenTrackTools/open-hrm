from flask import Blueprint, render_template

from pyhrm.auth.forms import RegistrationForm

auth = Blueprint(
    'auth',
    __name__,
    template_folder='templates',
    url_prefix='/auth'
)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        pass
    
    return render_template('registration.html', form=form, title='Registration Page')
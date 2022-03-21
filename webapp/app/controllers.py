from flask import Blueprint, render_template
from flask_login import login_required

app_bp = Blueprint(
    'app',
    __name__,
    url_prefix='/',
    template_folder='../templates/app'
)


@app_bp.route("/app")
@login_required
def dashboard():
    return render_template("dashboard.html", title="Dashboard-PyHRM")

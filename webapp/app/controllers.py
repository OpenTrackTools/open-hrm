from flask import Blueprint, render_template

app_bp = Blueprint(
    'app',
    __name__,
    url_prefix='/',
    template_folder='../templates/app'
)


@app_bp.route("/app")
def app():
    return render_template("dashboard.html", title="Dashboard-PyHRM")

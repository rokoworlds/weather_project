from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .weather import weather_request
from .models import User


views = Blueprint("views", __name__)


@views.route("/home/<id>")
@login_required
def get_user(id):
    user = User.query.filter_by(id=id).first()
    city_name = user.location
    result = weather_request(city_name)
    print(result)
    
    return render_template("home.html", user=current_user, result=result)


@views.route("/weather", methods=['GET', 'POST'])
@login_required
def weather():
    result = None
    if request.method == 'POST':
        city_name = request.form.get('city')
        result = weather_request(city_name)
        print(result)
        
        
    return render_template("search_weather.html", user=current_user, result=result)


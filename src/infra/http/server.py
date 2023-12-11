from flask import Flask, render_template, request

from src.application.usecase.titanic_mortality_predict import TitanicMortalityPredict
from src.domain.passenger import Passenger


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/api/predict", methods=["POST"])
    def predict():
        form_data = request.json
        passenger = Passenger(
            passenger_class=form_data["class"],
            age=form_data["age"],
            gender=form_data["gender"],
            number_of_siblings_or_spouses_aboard=form_data["adult_count"],
            number_of_parents_or_children_aboard=form_data["child_count"],
            fare=form_data["cabin"],
            port_of_embarkation=form_data["port"],
        )
        prediction = int(TitanicMortalityPredict().execute(passenger))
        print(prediction)
        return {"survived": prediction}

    return app

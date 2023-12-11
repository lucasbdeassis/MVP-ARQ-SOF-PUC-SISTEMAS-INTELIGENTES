from src.domain.passenger import Passenger


class TestPredictUseCase:
    def test_predict_survived(self):
        from src.application.usecase.titanic_mortality_predict import (
            TitanicMortalityPredict,
        )

        use_case = TitanicMortalityPredict()
        passenger = Passenger(
            passenger_class=1,
            age=38,
            gender=1,
            number_of_siblings_or_spouses_aboard=1,
            number_of_parents_or_children_aboard=0,
            fare=9,
            port_of_embarkation=1,
        )
        passenger_survived = use_case.execute(passenger)
        assert passenger_survived == 1

    def test_predict_not_survived(self):
        from src.application.usecase.titanic_mortality_predict import (
            TitanicMortalityPredict,
        )

        use_case = TitanicMortalityPredict()
        passenger = Passenger(
            passenger_class=3,
            age=38,
            gender=0,
            number_of_siblings_or_spouses_aboard=1,
            number_of_parents_or_children_aboard=0,
            fare=3,
            port_of_embarkation=0,
        )
        passenger_survived = use_case.execute(passenger)
        assert passenger_survived == 0

    def test_get_prediction_model(self):
        from src.application.usecase.titanic_mortality_predict import (
            TitanicMortalityPredict,
        )

        use_case = TitanicMortalityPredict()
        prediction_model = use_case._get_prediction_model()
        assert prediction_model is not None

    def test_get_scaler(self):
        from src.application.usecase.titanic_mortality_predict import (
            TitanicMortalityPredict,
        )

        use_case = TitanicMortalityPredict()
        scaler = use_case._get_scaler()
        assert scaler is not None

    def test_get_data(self):
        from src.application.usecase.titanic_mortality_predict import (
            TitanicMortalityPredict,
        )

        use_case = TitanicMortalityPredict()
        passenger = Passenger(
            passenger_class=1,
            age=38,
            gender=1,
            number_of_siblings_or_spouses_aboard=1,
            number_of_parents_or_children_aboard=0,
            fare=9,
            port_of_embarkation=1,
        )
        scaler = use_case._get_scaler()
        data = use_case._get_data(passenger, scaler)
        assert data is not None

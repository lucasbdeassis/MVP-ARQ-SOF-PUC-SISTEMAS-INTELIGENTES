class TestModelAccuracy:
    def test_model_accuracy(self):
        from src.application.usecase.titanic_mortality_predict import (
            TitanicMortalityPredict,
        )

        use_case = TitanicMortalityPredict()
        accuracy = use_case.get_model_accuracy()
        assert accuracy > 0.8

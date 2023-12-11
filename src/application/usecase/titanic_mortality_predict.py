import pickle

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

from src.domain.passenger import Passenger


class TitanicMortalityPredict:
    def execute(self, passenger: Passenger) -> bool:
        """Predicts if a passenger survived the Titanic disaster.

        Args:
            passenger (Passenger): Passenger to predict.

        Returns:
            bool: True if the passenger survived, False otherwise.
        """
        model = self._get_prediction_model()
        scaler = self._get_scaler()
        data = self._get_data(passenger, scaler)
        return model.predict(data)[0]

    def _get_prediction_model(self):
        """Loads the prediction model.

        Returns:
            PredictionModel: Prediction model.
        """
        with open("src/static/ml_model/titanic_prediction_model.pkl", "rb") as file:
            prediction_model = pickle.load(file)
        return prediction_model

    def _get_data(self, passenger: Passenger, scaler: StandardScaler) -> pd.DataFrame:
        """Gets the data to predict."""
        data = {
            "Pclass": [passenger.passenger_class],
            "Sex": [passenger.gender],
            "Age": [passenger.age],
            "SibSp": [passenger.number_of_siblings_or_spouses_aboard],
            "Parch": [passenger.number_of_parents_or_children_aboard],
            "Fare": [passenger.fare_group],
            "Embarked": [passenger.port_of_embarkation],
        }

        atributos = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
        entrada = pd.DataFrame(data, columns=atributos)

        array_entrada = entrada.values
        X_entrada = array_entrada[:].astype(float)
        X_entrada = pd.DataFrame(X_entrada, columns=atributos)

        # Padronização nos dados de entrada usando o scaler utilizado em X
        return scaler.transform(X_entrada)

    def _get_scaler(self):
        """Gets the scaler used to normalize the data."""
        with open(
            "src/static/scaler/titanic_prediction_model_scaler.pkl", "rb"
        ) as file:
            scaler = pickle.load(file)
        return scaler

    def _get_y_test(self) -> pd.DataFrame:
        with open("src/static/test_data/y_test.pkl", "rb") as file:
            return pickle.load(file)

    def _get_X_test(self) -> pd.DataFrame:
        with open("src/static/test_data/X_test.pkl", "rb") as file:
            return pickle.load(file)

    def get_model_accuracy(self) -> float:
        """Gets the model accuracy.

        Returns:
            float: Model accuracy.
        """
        model = self._get_prediction_model()
        scaler = self._get_scaler()
        y_test = self._get_y_test()
        X_test = self._get_X_test()
        rescaledTestX = scaler.transform(X_test)
        predictions = model.predict(rescaledTestX)
        return accuracy_score(y_test, predictions)

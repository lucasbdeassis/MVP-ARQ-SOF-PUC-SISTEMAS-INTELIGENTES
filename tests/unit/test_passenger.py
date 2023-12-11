class TestPassenger:
    def test_passenger_creation(self):
        from src.domain.passenger import Passenger

        passenger = Passenger(
            passenger_class=1,
            age=38,
            gender=1,
            number_of_siblings_or_spouses_aboard=1,
            number_of_parents_or_children_aboard=0,
            fare=9,
            port_of_embarkation=1,
        )

        assert passenger.passenger_class == 1
        assert passenger.age == 38
        assert passenger.gender == 1
        assert passenger.number_of_siblings_or_spouses_aboard == 1
        assert passenger.number_of_parents_or_children_aboard == 0
        assert passenger.fare == 9
        assert passenger.fare_group == 1
        assert passenger.port_of_embarkation == 1

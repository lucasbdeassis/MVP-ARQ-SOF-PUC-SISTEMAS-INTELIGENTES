from pydantic import BaseModel


class Passenger(BaseModel):
    passenger_class: int
    age: int
    gender: int
    number_of_siblings_or_spouses_aboard: int
    number_of_parents_or_children_aboard: int
    fare: float
    port_of_embarkation: int

    @property
    def fare_group(self):
        if self.fare <= 7.896:
            return 0
        if self.fare < 14.454:
            return 1
        if self.fare < 31:
            return 2
        return 3

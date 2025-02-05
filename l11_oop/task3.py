# Add required methods to the class Vehicle
class Vehicle:
    def __init__(self, name, is_truck=False):
        self.name = name
        self._is_truck = is_truck  

    def is_truck(self):
        return self._is_truck

if __name__ == "__main__":
    # Assign the needed value to the variable `c`
    # to make the script work without errors
    c = Vehicle("Mercedes", is_truck=True)

    assert isinstance(c, Vehicle)
    assert c.is_truck()

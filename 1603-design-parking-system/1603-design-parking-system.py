class ParkingSystem:
    # initialize the parking object
    def __init__(self, big: int, medium: int, small: int):
        self.lot = {}
        self.lot[1] = big
        self.lot[2] = medium
        self.lot[3] = small
        
    # if car can be parked then return True else False
    def addCar(self, carType: int) -> bool:
        if self.lot.get(carType) > 0:
            self.lot[carType] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
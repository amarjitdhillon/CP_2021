class ParkingSystem:
    # initialize the parking object
    def __init__(self, big: int, medium: int, small: int):
        # to hold various types of parking we are using a dict in constructor
        self.lot = {}  
        
        # add the parking counters in this lot dict
        self.lot[1] = big
        self.lot[2] = medium
        self.lot[3] = small
        
    # if car can be parked then return True else False
    def addCar(self, carType: int) -> bool:
        
        # if it has the space, then park the car and update the space
        if self.lot.get(carType) > 0: 
            self.lot[carType] -= 1
            return True
        else:
            # return False if car can not be parked
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
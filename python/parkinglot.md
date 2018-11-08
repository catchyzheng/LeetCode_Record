parking lot.

```python
VEHICLE_ID = {
    'MOTOCYCLE': 'MOTOCYCLE',
    'CAR': 'CAR',
    'BUS': 'BUS',
}

class vehicle:
    def __init__(self):
        self.TYPE = ''
        self.cost = 0
        self.at_level = None
        self.at_spots = None
    
    def unpark(self):
        if not self.at_level:
            return None
        
        for x,y in self.at_spots:
            self.at_level.spots[x,y] = None
        
        self.at_level = None
        self.at_spots = None

class Motorcycle(vehicle):
    def __init__(self):
        self.type = VEHICLE_ID['MOTOCYCLE']
        self.cost = 1
        
class Car(vehicle):
    def __init__(self):
        self.type = VEHICLE_ID['CAR']
        self.cost = 1
        
class Bus(vehicle):
    def __init__(self):
        self.type = VEHICLE_ID['BUS']
        self.cost = 5

class Level:
    def __init__(self, floor, num_rows, spots_per_row):
        self.floor = floor
        self.num_rows = num_rows
        self.spots_per_row = spots_per_row
        self.spots = {}
        
    def get_range(self, vehicle_type):
        if vehicle_type == VEHICLE_ID['CAR']:
            return range(self.spots_per_row//4, self.spots_per_row)

        if vehicle_type == VEHICLE_ID['BUS']:
            return range(self.spots_per_row//4*3, self.spots_per_row)
        
        return range(self.spots_per_row)
    
    def park_vehicle(self, vehicle):
        
        RANGE = self.get_range(vehicle.type)
        
        for x in range(self.num_rows):
            spots_found = 0
            avail_spots = []
            for y in RANGE:
                if self.spots.get((x,y)):
                    spots_found = 0
                    avail_spots = []
                    continue
                spots_found += 1
                avail_spots.append((x,y))
                
                if spots_found == vehicle.cost:
                    vehicle.at_level = self
                    vehicle.at_spots = avail_spots
                    for x,y in avail_spots:
                        self.spots[x,y] = vehicle
                    return True
        return False
    
class ParkingLot:
    
    def __init__(self, floors, num_rows, spots_per_row):
        self.levels = [Level(i, num_rows, spots_per_row) for i in range(floors)]
        
    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
#                vehicle.at_level = level
                return True
        return False
    
    def unpark_vehicle(self, vehicle):
        vehicle.unpark()
```


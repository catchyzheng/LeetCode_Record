[566. GFS客户端](<https://www.lintcode.com/problem/gfs-client/description>) medium

为GFS(Google文件系统)实现一个简单的客户端，提供一下功能：
1.`read(文件名)`，通过文件名从GFS中读取文件。
2.`write(文件名，内容)`，通过文件名和内容写入GFS中。
现在有两种已经在基础类中实现的方法：
1.`readChunk(文件名，块索引)`，从GFS中读取一个块。
2.`writeChunk(文件名，块索引，块数据)`，向GFS中写入一个块。
为了简化这个问题，我们可以假设块大小为 *chunkSize* 位的(在真实的文件系统中，是64M)，GFS客户端的任务是将一个文件分为若干块(如果需要的话)并且保存在远端的GFS服务器上，*chunkSize*会在构造函数中给出，你需要的是实现`read`和`write`这两个private方法。

### 样例

```shell
GFSClient(5)
read("a.txt")
>> null
write("a.txt", "World")
>> You don't need to return anything, but you need to call writeChunk("a.txt", 0, "World") to write a 5 bytes chunk to GFS.
read("a.txt")
>> "World"
write("b.txt", "111112222233")
>> You need to save "11111" at chink 0, "22222" at chunk 1, "33" at chunk 2.
write("b.txt", "aaaaabbbbb")
read("b.txt")
>> "aaaaabbbbb"
```

java

```java
/* Definition of BaseGFSClient
 * class BaseGFSClient {
 *     private Map<String, String> chunk_list;
 *     public BaseGFSClient() {}
 *     public String readChunk(String filename, int chunkIndex) {
 *         // Read a chunk from GFS
 *     }
 *     public void writeChunk(String filename, int chunkIndex,
 *                            String content) {
 *         // Write a chunk to GFS
 *     }
 * }
 */
public class GFSClient extends BaseGFSClient {

    public int chunkSize;
    public Map<String, Integer> chunkNum;

    public GFSClient(int chunkSize) {
        // initialize your data structure here
        this.chunkSize = chunkSize;
        this.chunkNum = new HashMap<String, Integer>();
    }
    
    // @param filename a file name
    // @return conetent of the file given from GFS
    public String read(String filename) {
        // Write your code here
        if (!chunkNum.containsKey(filename))
            return null;

        StringBuffer content = new StringBuffer();

        for (int i = 0; i < chunkNum.get(filename); ++i) {
            String sub_content = readChunk(filename, i);
            if (sub_content != null)
                content.append(sub_content);
        }
        return content.toString();
    }

    // @param filename a file name
    // @param content a string
    // @return void
    public void write(String filename, String content) {
        // Write your code here
        int length = content.length();

        int num = (length - 1) / chunkSize + 1;
        chunkNum.put(filename, num);

        for (int i = 0; i < num; ++i) {
            int start = i * chunkSize;
            int end = i == num -1 ? length : (i + 1) * chunkSize; 
            String sub_content = content.substring(start, end);
            writeChunk(filename, i, sub_content);
        }
    }
}
```

```python
'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''
class GFSClient(BaseGFSClient):

    # @param {int} chunkSize chunk size bytes
    def __init__(self, chunkSize):
        BaseGFSClient.__init__(self)
        # initialize your data structure here
        self.chunkSize = chunkSize
        self.chunkNum = dict()


    # @param {str} filename a file name
    # @return {str} conetent of the file given from GFS
    def read(self, filename):
        # Write your code here
        if filename not in self.chunkNum:
            return None
        content = ''
        for index in xrange(self.chunkNum.get(filename)):
            sub_content = BaseGFSClient.readChunk(self, filename, index)
            if sub_content:
                content += sub_content

        return content


    # @param {str} filename a file name
    # @param {str} content a string
    # @return nothing
    def write(self, filename, content):
        # Write your code here
        length = len(content)
        chunkNum = (length - 1) / self.chunkSize + 1
        self.chunkNum[filename] = chunkNum
        for index in xrange(chunkNum):
            sub_content = content[index * self.chunkSize :
                                  (index + 1) * self.chunkSize]
            BaseGFSClient.writeChunk(self, filename, index, sub_content)
     
```

c++

```c++
class GFSClient : public BaseGFSClient {
public:
    int chunkSize;
    map<string, int> chunkNum;

    GFSClient(int chunkSize) {
        // initialize your data structure here
        this->chunkSize = chunkSize;
    }

    // @param filename a file name
    // @return conetent of the file given from GFS
    string read(string& filename) {
        // Write your code here
        // return "" instead of NULL if file do not exist
        if (chunkNum.find(filename) == chunkNum.end()) {
            return "";
        }
        string content = "";
        int size = chunkNum[filename];
        for (int i = 0; i < size; ++i) {
            content += readChunk(filename, i);
        }

        return content;
    }

    // @param filename a file name
    // @param content a string
    // @return void
    void write(string& filename, string& content) {
        // Write your code here
        int length = content.size();
        int num = (length - 1) / chunkSize + 1;
        chunkNum[filename] = num;
        for (int i = 0; i < num; ++i) {
            string sub_content = content.substr(i * chunkSize, chunkSize);
            writeChunk(filename, i, sub_content);
        }
    }
};
```



[498. 停车场](<https://www.lintcode.com/problem/parking-lot/description>)

设计一个停车场

1. 一共有*n*层，每层*m*列，每列*k*个位置
   2.停车场可以停摩托车，公交车，汽车
   3.停车位分别有摩托车位，汽车位，大型停车位
   4.每一列，摩托车位编号范围为`[0,k/4)(注：包括0，不包括k/4)`,汽车停车位编号范围为`[k/4,k/4*3)`,大型停车位编号范围为`[k/4*3,k)`
   5.一辆摩托车可以停在任何停车位
   6.一辆汽车可以停在一个汽车位或者大型停车位
   7.一辆公交车可以停在一列里的连续5个大型停车位。

### 样例

level=1, num_rows=1, spots_per_row=11
parkVehicle("Motorcycle_1") // return true
parkVehicle("Car_1") // return true
parkVehicle("Car_2") // return true
parkVehicle("Car_3") // return true
parkVehicle("Car_4") // return true
parkVehicle("Car_5") // return true
parkVehicle("Bus_1") // return false
unParkVehicle("Car_5")
parkVehicle("Bus_1") // return true



```python
# python 2
# enum type for Vehicle
class VehicleSize:
    Motorcycle = 1
    Compact = 2
    Large = 3
    Other = 99

class Vehicle:
    # Write your code here
    def __init__(self):
        self.parking_spots = []
        self.spots_needed = 0
        self.size = None
        self.license_plate = None

    def get_spots_needed(self):
        return self.spots_needed

    def get_size(self):
        return self.size

    def park_in_spot(self, spot):
        self.parking_spots.append(spot)

    def clear_spots(self):
        for spot in self.parking_spots:
            spot.remove_vehicle()
        
        self.park_sports = []  

    def can_fit_in_spot(self, spot):
        raise NotImplementedError('This method should have implemented.')


class Motorcycle(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 1
        self.size = VehicleSize.Motorcycle

    def can_fit_in_spot(self, spot):
        return True


class Car(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 1
        self.size = VehicleSize.Compact

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Large or \
                spot.get_size() == VehicleSize.Compact


class Bus(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 5
        self.size = VehicleSize.Large

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Large


class ParkingSpot:
    # Write your code here
    def __init__(self, lvl, r, n, sz):
        self.level = lvl
        self.row = r
        self.spot_number = n
        self.spot_size = sz
        self.vehicle = None

    def is_available(self):
        return self.vehicle == None

    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.can_fit_in_spot(self)

    def park(self, v):
        if not self.can_fit_vehicle(v):
            return False

        self.vehicle = v
        self.vehicle.park_in_spot(self)
        return True

    def remove_vehicle(self):
        self.level.spot_freed()
        self.vehicle = None

    def get_row(self):
        return self.row
    
    def get_spot_number(self):
        return self.spot_number

    def get_size(self):
        return self.spot_size


class Level:
    # Write your code here
    def __init__(self, flr, num_rows, spots_per_row):
        self.floor = flr
        self.spots_per_row = spots_per_row
        self.number_spots = 0
        self.available_spots = 0;
        self.spots = []
        
        for row in xrange(num_rows):
            for spot in xrange(0, spots_per_row / 4):
                sz = VehicleSize.Motorcycle
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

            for spot in xrange(spots_per_row / 4, spots_per_row / 4 * 3):
                sz = VehicleSize.Compact
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

            for spot in xrange(spots_per_row / 4 * 3, spots_per_row):
                sz = VehicleSize.Large
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

        self.available_spots = self.number_spots
        
    def park_vehicle(self, vehicle):
        if self.get_available_spots() < vehicle.get_spots_needed():
            return False

        spot_num = self.find_available_spots(vehicle)

        if spot_num < 0:
            return False
        return self.park_starting_at_spot(spot_num, vehicle)

    def find_available_spots(self, vehicle):
        spots_needed = vehicle.get_spots_needed()
        last_row = -1
        spots_found = 0
        
        for i in xrange(len(self.spots)):
            spot = self.spots[i]
            if last_row != spot.get_row():
                spots_found = 0
                last_row = spot.get_row()
            if spot.can_fit_vehicle(vehicle):
                spots_found += 1
            else:
                spots_found = 0
            
            if spots_found == spots_needed:
                return i - (spots_needed - 1)

        return -1

    def park_starting_at_spot(self, spot_num, vehicle):
        vehicle.clear_spots()
        success = True

        for i in xrange(spot_num, spot_num + vehicle.get_spots_needed()):
            success = success and self.spots[i].park(vehicle)
        
        self.available_spots -= vehicle.get_spots_needed()
        return success

    def spot_freed(self):
        self.available_spots += 1

    def get_available_spots(self):
        return self.available_spots


class ParkingLot:
    # @param {int} n number of leves
    # @param {int} num_rows  each level has num_rows rows of spots
    # @param {int} spots_per_row each row has spots_per_row spots
    def __init__(self, n, num_rows, spots_per_row):
        # Write your code here
        self.levels = []
        for i in xrange(n):
            self.levels.append(Level(i, num_rows, spots_per_row))

	# Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle):
        # Write your code here
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        # Write your code here
        vehicle.clear_spots()
```



```java
/**
* This reference program is provided by @jiuzhang.com
* Copyright is reserved. Please indicate the source for forwarding
*/

// enum type for Vehicle
enum VehicleSize {
    Motorcycle,
	Compact,
	Large,
}

//abstract Vehicle class
abstract class Vehicle {
    // Write your code here
	protected int spotsNeeded;
	protected VehicleSize size;
	protected String licensePlate;  // id for a vehicle

	protected ArrayList<ParkingSpot> parkingSpots = new ArrayList<ParkingSpot>(); // id for parking where may occupy multi

	public int getSpotsNeeded() {
		return spotsNeeded;
	}
	
	public VehicleSize getSize() {
		return size;
	}

	/* Park vehicle in this spot (among others, potentially) */
	public void parkInSpot(ParkingSpot spot) {
		parkingSpots.add(spot);
	}
	
	/* Remove car from spot, and notify spot that it's gone */
	public void clearSpots() {
		for (int i = 0; i < parkingSpots.size(); i++) {
			parkingSpots.get(i).removeVehicle();
		}
		parkingSpots.clear();
	}
	//this need to be implement in subclass
	public abstract boolean canFitInSpot(ParkingSpot spot);
    public abstract void print(); 
}

class Motorcycle extends Vehicle {
    // Write your code here
	public Motorcycle() {
		spotsNeeded = 1;
		size = VehicleSize.Motorcycle;
	}
	
	public boolean canFitInSpot(ParkingSpot spot) {
		return true;
	}
    
    public void print() {  
        System.out.print("M");  
    }
}

class Car extends Vehicle {
    // Write your code here
	public Car() {
		spotsNeeded = 1;
		size = VehicleSize.Compact;
	}
	
	public boolean canFitInSpot(ParkingSpot spot) {
		return spot.getSize() == VehicleSize.Large || spot.getSize() == VehicleSize.Compact;
	}

    public void print() {  
        System.out.print("C");  
    } 
}

class Bus extends Vehicle {
    // Write your code here
	public Bus() {
		spotsNeeded = 5;
		size = VehicleSize.Large;
	}

	public boolean canFitInSpot(ParkingSpot spot) {
		return spot.getSize() == VehicleSize.Large;
	}

    public void print() {  
        System.out.print("B");  
    } 
}

class ParkingSpot {
    // Write your code here
	private Vehicle vehicle;
	private VehicleSize spotSize;
	private int row;
	private int spotNumber;
	private Level level;

	public ParkingSpot(Level lvl, int r, int n, VehicleSize sz) {
		level = lvl;
		row = r;
		spotNumber = n;
		spotSize = sz;
	}
	
	public boolean isAvailable() {
		return vehicle == null;
	}
	/* Checks if the spot is big enough for the vehicle (and is available). This compares
	 * the SIZE only. It does not check if it has enough spots. */
	public boolean canFitVehicle(Vehicle vehicle) {
		return isAvailable() && vehicle.canFitInSpot(this);
	}
	/* Park vehicle in this spot. */
	public boolean park(Vehicle v) {
		if (!canFitVehicle(v)) {
			return false;
		}
		vehicle = v;
		vehicle.parkInSpot(this);
		return true;
	}
	/* Remove vehicle from spot, and notify level that a new spot is available */
	public void removeVehicle() {
		level.spotFreed();
		vehicle = null;
	}
	
	public int getRow() {
		return row;
	}
	
	public int getSpotNumber() {
		return spotNumber;
	}
	
	public VehicleSize getSize() {
		return spotSize;
	}

    public void print() {  
        if (vehicle == null) {  
            if (spotSize == VehicleSize.Compact) {  
                System.out.print("c");  
            } else if (spotSize == VehicleSize.Large) {  
                System.out.print("l");  
            } else if (spotSize == VehicleSize.Motorcycle) {  
                System.out.print("m");  
            }  
        } else {  
            vehicle.print();  
        }  
    }
}

/* Represents a level in a parking garage */
class Level {
    // Write your code here
	private int floor;
	private ParkingSpot[] spots;
	private int availableSpots = 0; // number of free spots
	private int SPOTS_PER_ROW;


	public Level(int flr, int num_rows, int spots_per_row) {
		floor = flr;
        int SPOTS_PER_ROW = spots_per_row;
        int numberSpots  = 0;
		spots = new ParkingSpot[num_rows * spots_per_row];

		//init size for each spot in array spots
        for (int row = 0; row < num_rows; ++row) {
            for (int spot = 0; spot < spots_per_row / 4; ++spot) {
                VehicleSize sz = VehicleSize.Motorcycle;
                spots[numberSpots] = new ParkingSpot(this, row, numberSpots, sz);
                numberSpots ++;
            }
            for (int spot = spots_per_row / 4; spot < spots_per_row / 4 * 3; ++spot) {
                VehicleSize sz = VehicleSize.Compact;
                spots[numberSpots] = new ParkingSpot(this, row, numberSpots, sz);
                numberSpots ++;
            }
            for (int spot = spots_per_row / 4 * 3; spot < spots_per_row; ++spot) {
                VehicleSize sz = VehicleSize.Large;
                spots[numberSpots] = new ParkingSpot(this, row, numberSpots, sz);
                numberSpots ++;
            }
        }

        availableSpots = numberSpots;
	}

	/* Try to find a place to park this vehicle. Return false if failed. */
	public boolean parkVehicle(Vehicle vehicle) {
		if (availableSpots() < vehicle.getSpotsNeeded()) {
			return false; // no enough spots
		}
		int spotNumber = findAvailableSpots(vehicle);
		if(spotNumber < 0) {
			return false;
		}
		return parkStartingAtSpot(spotNumber, vehicle);
	}

	/* find a spot to park this vehicle. Return index of spot, or -1 on failure. */
	private int findAvailableSpots(Vehicle vehicle) {
		int spotsNeeded = vehicle.getSpotsNeeded();
		int lastRow = -1;
		int spotsFound = 0;

		for(int i = 0; i < spots.length; i++){
			ParkingSpot spot = spots[i];
			if(lastRow != spot.getRow()){
				spotsFound = 0;
				lastRow = spot.getRow();
			}
			if(spot.canFitVehicle(vehicle)){
				spotsFound++;
			}else{
				spotsFound = 0;
			}
			if(spotsFound == spotsNeeded){
				return i - (spotsNeeded - 1); // index of spot
			}
		}
		return -1;
	}

	/* Park a vehicle starting at the spot spotNumber, and continuing until vehicle.spotsNeeded. */
	private boolean parkStartingAtSpot(int spotNumber, Vehicle vehicle) {
		vehicle.clearSpots();

		boolean success = true;
		
		for (int i = spotNumber; i < spotNumber + vehicle.spotsNeeded; i++) {
			 success &= spots[i].park(vehicle);
		}
		
		availableSpots -= vehicle.spotsNeeded;
		return success;
	}

	/* When a car was removed from the spot, increment availableSpots */
	public void spotFreed() {
		availableSpots++;
	}

	public int availableSpots() {
		return availableSpots;
	}

    public void print() {  
        int lastRow = -1;  
        for (int i = 0; i < spots.length; i++) {  
            ParkingSpot spot = spots[i];  
            if (spot.getRow() != lastRow) {  
                System.out.print("  ");  
                lastRow = spot.getRow();  
            }  
            spot.print();  
        }  
    }
}

public class ParkingLot {
	private Level[] levels;
	private int NUM_LEVELS;
	
    // @param n number of leves
    // @param num_rows  each level has num_rows rows of spots
    // @param spots_per_row each row has spots_per_row spots
	public ParkingLot(int n, int num_rows, int spots_per_row) {
        // Write your code here
        NUM_LEVELS = n;
		levels = new Level[NUM_LEVELS];
		for (int i = 0; i < NUM_LEVELS; i++) {
			levels[i] = new Level(i, num_rows, spots_per_row);
		}
	}

	// Park the vehicle in a spot (or multiple spots)
    // Return false if failed
	public boolean parkVehicle(Vehicle vehicle) {
        // Write your code here
		for (int i = 0; i < levels.length; i++) {
			if (levels[i].parkVehicle(vehicle)) {
				return true;
			}
		}
		return false;
	}

    // unPark the vehicle
	public void unParkVehicle(Vehicle vehicle) {
        // Write your code here
		vehicle.clearSpots();
	}

    public void print() {  
        for (int i = 0; i < levels.length; i++) {  
            System.out.print("Level" + i + ": ");  
            levels[i].print();
            System.out.println("");  
        }  
        System.out.println("");  
    } 
}
```

c++

```c++
// enum type for Vehicle
enum class VehicleSize {
    Motorcycle,
    Compact,
    Large
};

class Vehicle {
public:
    virtual VehicleSize size() {}
    virtual int spot_num() {}
};

class Bus: public Vehicle {
public:
    VehicleSize size() {
        return VehicleSize::Large;
    }
    int spot_num() {
        return 5;
    }
};

class Car: public Vehicle {
public:
    VehicleSize size() {
        return VehicleSize::Compact;
    }
    int spot_num() {
        return 1;
    }
};

class Motorcycle: public Vehicle {
public:
    VehicleSize size() {
        return VehicleSize::Motorcycle;
    }
    int spot_num() {
        return 1;
    }
};

class Level {
public:
    Level(int num_rows, int spots_per_row) {
        for (int i = 0 ; i < num_rows; ++i) {
            spots.push_back(vector<Vehicle*>(spots_per_row, NULL));
        }
        this->num_rows = num_rows;
        this->spots_per_row = spots_per_row;
    }
    
    bool park_vehicle(Vehicle* vehicle) {
        for (int row = 0; row < num_rows; ++row) {
            int start = 0;
            if (vehicle->size() == VehicleSize::Compact) {
                start = spots_per_row / 4;
            } else if (vehicle->size() == VehicleSize::Large) {
                start = spots_per_row / 4 * 3;
            }
            for (int i = start; i < spots_per_row - vehicle->spot_num() + 1; ++i) {
                bool can_park = true;
                for (int j = i; j < i +  vehicle->spot_num(); ++j) {
                    if (spots[row][j] != NULL) {
                        can_park = false;
                        break;
                    }
                }
                if (can_park) {
                    for (int j = i; j < i + vehicle->spot_num(); ++j) {
                        spots[row][j] = vehicle;
                    } 
                    return true;
                }
            }
        }
        return false;
    }
    
    void unpark_vehicle(Vehicle *vehicle) {
        for (int row = 0; row < num_rows; ++row) {
            for (int i = 0; i < spots_per_row; ++i)
                if (spots[row][i] == vehicle) {
                    spots[row][i] = NULL;
                }
        }
    }
    
private:
    vector<vector<Vehicle*>> spots;
    int num_rows;
    int spots_per_row;
    
};

class ParkingLot {
public:
    // @param n number of leves
    // @param num_rows  each level has num_rows rows of spots
    // @param spots_per_row each row has spots_per_row spots
    ParkingLot(int n, int num_rows, int spots_per_row) {
        for (int i = 0; i < n; ++i) {
            Level *level = new Level(num_rows, spots_per_row);
            levels.push_back(level);
        }
    }

    // Park the vehicle in a spot (or multiple spots)
    // Return false if failed
    bool parkVehicle(Vehicle* vehicle) {
        for (int i = 0; i < levels.size(); ++i) {
            if (levels[i]->park_vehicle(vehicle)) {
                vehicle_to_level[vehicle] = levels[i];
                return true;
            }
        }
        return false;
    }

    // unPark the vehicle
    void unParkVehicle(Vehicle* vehicle) {
        Level *level = vehicle_to_level[vehicle];
        if (level) {
            level->unpark_vehicle(vehicle);
        }
    }
    
private:
    vector<Level*> levels;
    map<Vehicle*, Level*> vehicle_to_level;
};
```



[712. 自动售货机 OO Design](<https://www.lintcode.com/problem/vending-machine-oo-design/description>)

解答不能通过

### 描述

- Vending Machine一共有三种状态：`NoSelection`, `HasSelection`, `InsertedMoney`
- Vending Machine一共卖三种饮料：`Coke`, `Sprite`和`MountainDew`
- 要求Vending Machine在正确的状态要有正确的输出

### 样例

输入：

```
select("Coke")
select("Sprite")
insert(500)
execTrans()
```

输出:

```
Current selection is: Coke, current inserted money: 0, current state is : HasSelection
Current selection is: Sprite, current inserted money: 0, current state is : HasSelection
Current selection is: Sprite, current inserted money: 500, current state is : InsertedMoney
Current selection is: null, current inserted money: 0, current state is : NoSelection
```



下面的java解答貌似通不过。。奇怪

```java
public class VendingMachine {
    private String currentSelectedItem;
	private int currentInsertedMoney;
	private AbstractState state;
	private NoSelectionState noSelectionState;
	private HasSelectionState hasSelectionState;
	private InsertedMoneyState insertedMoneyState;
	private Map<String, Integer> itemPrice;

	public VendingMachine() {
		currentInsertedMoney = 0;
		currentSelectedItem = null;
		noSelectionState = new NoSelectionState(this);
		hasSelectionState = new HasSelectionState(this);
		insertedMoneyState = new InsertedMoneyState(this);
		state = noSelectionState;

		itemPrice = new HashMap<>();
		itemPrice.put("Coke", 199);
		itemPrice.put("Sprite", 299);
		itemPrice.put("MountainDew", 399);
	}

	public void setSelectedItem(String item) {
		this.currentSelectedItem = item;
	}

	public String getSelectedItem() {
		return currentSelectedItem;
	}

	public void insertMoney(int amount) {
		this.currentInsertedMoney += amount;
	}

	public void emptyInsertedMoney() {
		this.currentInsertedMoney = 0;
	}

	public int getInsertedMoney() {
		return currentInsertedMoney;
	}

	public int getSalePrice() {
		if (currentSelectedItem == null) {
			System.out.println("Please make a selection before asking price");
			return 0;
		} else {
			return itemPrice.get(currentSelectedItem);
		}
	}

	public void changeToNoSelectionState() {
		state = noSelectionState;
	}

	public void changeToHasSelectionState() {
		state = hasSelectionState;
	}

	public void changeToInsertedMoneyState() {
		state = insertedMoneyState;
	}

	public void selectItem(String selection) {
		state.selectItem(selection);
	}

	public void addMoney(int value) {
		state.insertMoney(value);
	}

	public void executeTransaction() {
		state.executeTransaction();
	}

	public int cancelTransaction() {
		return state.cancelTransaction();
	}

	public String printState() {
		String res = "";

		res = "Current selection is: " + currentSelectedItem + ", current inserted money: " + currentInsertedMoney
				+ ", current state is : " + state;

		return res;
	}
}

interface State {
	public void selectItem(String selection);
	public void insertMoney(int value);
	public void executeTransaction();
	public int cancelTransaction();
	public String toString();
}

abstract class AbstractState implements State {
	protected VendingMachine vendingMachine;

	public AbstractState(VendingMachine vendingMachine) {
		this.vendingMachine = vendingMachine;
	}
}

class NoSelectionState extends AbstractState{

	public NoSelectionState(VendingMachine vendingMachine) {
		super(vendingMachine);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void selectItem(String selection) {
		// TODO Auto-generated method stub
		vendingMachine.setSelectedItem(selection);
		vendingMachine.changeToHasSelectionState();
	}

	@Override
	public void insertMoney(int value) {
		// TODO Auto-generated method stub
		System.out.println("Please make a selection first");
	}

	@Override
	public void executeTransaction() {
		// TODO Auto-generated method stub
		System.out.println("Please make a selection first");
	}

	@Override
	public int cancelTransaction() {
		// TODO Auto-generated method stub
		System.out.println("Please make a selection first");
		return 0;
	}

	@Override
	public String toString(){
		return "NoSelection";
	}
}

class HasSelectionState extends AbstractState{

	public HasSelectionState(VendingMachine vendingMachine) {
		super(vendingMachine);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void selectItem(String selection) {
		// TODO Auto-generated method stub
		vendingMachine.setSelectedItem(selection);
	}

	@Override
	public void insertMoney(int value) {
		// TODO Auto-generated method stub
		vendingMachine.insertMoney(value);
		vendingMachine.changeToInsertedMoneyState();
	}

	@Override
	public void executeTransaction() {
		// TODO Auto-generated method stub
		System.out.println("You need to insert money first");
	}

	@Override
	public int cancelTransaction() {
		// TODO Auto-generated method stub
		System.out.println("Transaction canceled");
		vendingMachine.setSelectedItem(null);
		vendingMachine.changeToNoSelectionState();
		return 0;
	}
	@Override
	public String toString(){
		return "HasSelection";
	}
}

class InsertedMoneyState extends AbstractState{

	public InsertedMoneyState(VendingMachine vendingMachine) {
		super(vendingMachine);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void selectItem(String selection) {
		// TODO Auto-generated method stub
		System.out.println("Already has a selection, please cancel transaction to make a new selection");
	}

	@Override
	public void insertMoney(int value) {
		// TODO Auto-generated method stub
		vendingMachine.insertMoney(value);
	}

	@Override
	public void executeTransaction() {
		// TODO Auto-generated method stub
		int diff = vendingMachine.getInsertedMoney() - vendingMachine.getSalePrice();
		if(diff >= 0){
			System.out.println("Executing transaction, will return you : " + diff + " money and item: " + vendingMachine.getSelectedItem());
			vendingMachine.setSelectedItem(null);
			vendingMachine.emptyInsertedMoney();
			vendingMachine.changeToNoSelectionState();
		}
		else{
			System.out.println("Not enough money, please insert " + (-diff) + " more.");
		}
	}

	@Override
	public int cancelTransaction() {
		// TODO Auto-generated method stub
		int insertedMoney = vendingMachine.getInsertedMoney();
		vendingMachine.setSelectedItem(null);
		vendingMachine.emptyInsertedMoney();
		vendingMachine.changeToNoSelectionState();
		return insertedMoney;
	}

	@Override
	public String toString(){
		return "InsertedMoney";
	}
}
```

c++

```c++
class VendingMachine;

class State{
public:

    virtual void selectItem(string selection) = 0;
	virtual void insertMoney(int value) = 0;
	virtual void executeTransaction() = 0;
	virtual int cancelTransaction()=0;
	virtual string toString() = 0;
};

class AbstractState :public State{
protected:
	VendingMachine *vendingMachine;

public:

	AbstractState(VendingMachine *vendingMachine){
		this->vendingMachine = vendingMachine;
	}

};

class NoSelectionState :public AbstractState{
public:

	NoSelectionState(VendingMachine *vendingMachine) :AbstractState(vendingMachine) {}

	void selectItem(string selection);

	void insertMoney(int value)
	{
		//cout << "Please make a selection first" << endl;
	}

	void executeTransaction()
	{
	//	cout << "Please make a selection first" << endl;
	}

	int cancelTransaction()
	{
		//cout << "Please make a selection first" << endl;
		return 0;
	}

	string toString()
	{
		return "NoSelection";
	}
};

class HasSelectionState :public AbstractState
{
public:

	HasSelectionState(VendingMachine *vendingMachine) :AbstractState(vendingMachine) {}

	void selectItem(string selection);

	void insertMoney(int value);

	void executeTransaction()
	{
		//cout << "You need to insert money first" << endl;
	}

	int cancelTransaction();

	string toString()
	{
		return "HasSelection";
	}

};

class InsertedMoneyState :public AbstractState
{
public:

	InsertedMoneyState(VendingMachine *vendingMachine) :AbstractState(vendingMachine) {}

	void selectItem(string selection)
	{
		//cout << "Already has a selection, please cancel transaction to make a new selection" << endl;
	}

	void insertMoney(int value);

	void executeTransaction();

	int cancelTransaction();

	string toString()
	{
		return "InsertedMoney";
	}
};

class VendingMachine
{
private:

	string currentSelectedItem;
	int currentInsertedMoney;
	AbstractState *state;
	NoSelectionState *noSelectionState;
	HasSelectionState *hasSelectionState;
	InsertedMoneyState *insertedMoneyState;
	map<string, int> *itemPrice;

public:

	VendingMachine()
	{
		currentInsertedMoney = 0;
		currentSelectedItem = "null";
		noSelectionState = new NoSelectionState(this);
		hasSelectionState = new HasSelectionState(this);
		insertedMoneyState = new InsertedMoneyState(this);
		state = noSelectionState;

		itemPrice = new map<string, int>;
		(*itemPrice)["Coke"] = 199;
		(*itemPrice)["Sprite"] = 299;
		(*itemPrice)["MountainDew"] = 399;
	}

	void setSelectedItem(string item)
	{
		this->currentSelectedItem = item;
	}

	string getSelectedItem()
	{
		return currentSelectedItem;
	}

	void insertMoney(int amount)
	{
		this->currentInsertedMoney += amount;
	}

	void emptyInsertedMoney()
	{
		this->currentInsertedMoney = 0;
	}

	int getInsertedMoney()
	{
		return currentInsertedMoney;
	}

	int getSalePrice()
	{
		if (currentSelectedItem == "null")
		{
			//cout << "Please make a selection before asking price" << endl;
			return 0;
		}
		else
		{
			return (*itemPrice)[currentSelectedItem];
		}
	}

	void changeToNoSelectionState()
	{
		state = noSelectionState;
	}

	void changeToHasSelectionState()
	{
		state = hasSelectionState;
	}

	void changeToInsertedMoneyState()
	{
		state = insertedMoneyState;
	}

	void selectItem(string selection)
	{
		state->selectItem(selection);
	}

	void addMoney(int value)
	{
		state->insertMoney(value);
	}

	void executeTransaction()
	{
		state->executeTransaction();
	}

	int cancelTransaction()
	{
		return state->cancelTransaction();
	}

	string printState()
	{
		string res = "";
		res = "Current selection is: " + currentSelectedItem + ", current inserted money: " + to_string(currentInsertedMoney)
			+ ", current state is : " + state->toString();
		return res;
	}
};

void NoSelectionState::selectItem(string selection)
{
	vendingMachine->setSelectedItem(selection);
	vendingMachine->changeToHasSelectionState();
}

void HasSelectionState::selectItem(string selection)
{
	vendingMachine->setSelectedItem(selection);
}

void HasSelectionState::insertMoney(int value)
{
	vendingMachine->insertMoney(value);
	vendingMachine->changeToInsertedMoneyState();
}

int HasSelectionState::cancelTransaction()
{
	//cout << "Transaction canceled" << endl;
	vendingMachine->setSelectedItem(NULL);
	vendingMachine->changeToNoSelectionState();
	return 0;
}

void InsertedMoneyState::insertMoney(int value)
{
	vendingMachine->insertMoney(value);
}

void InsertedMoneyState::executeTransaction()
{
	int diff = vendingMachine->getInsertedMoney() - vendingMachine->getSalePrice();

	if (diff >= 0)
	{
		//cout << "Executing transaction, will return you : " + to_string(diff) +
		//	" money and item: " + vendingMachine->getSelectedItem() << endl;
		vendingMachine->setSelectedItem("null");
		vendingMachine->emptyInsertedMoney();
		vendingMachine->changeToNoSelectionState();
	}
	else
	{
		//cout << "Not enough money, please insert " + to_string(-diff) + " more." << endl;
	}
}

int InsertedMoneyState::cancelTransaction()
{
	int insertedMoney = vendingMachine->getInsertedMoney();
	vendingMachine->setSelectedItem(NULL);
	vendingMachine->emptyInsertedMoney();
	vendingMachine->changeToNoSelectionState();
	return insertedMoney;
}
```




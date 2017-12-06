class Wheel:
    def __init__(self, model, weight, cost, type = ""):
        self.__model = model
        self.__weight = weight
        self.__cost = cost
        self.__type = type

    @property
    def weight(self):
        return self.__weight

    @property
    def cost(self):
        return self.__cost

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def toStr(self):
        return ("model: " + self.__model + ", weigth: " + self.__weight + ", cost: " + self.__cost + ", type: " + self.__type)

class Frame:
    def __init__(self, material, weight, cost):
        self.__material = material
        self.__weight = weight
        self.__cost = cost

    @property
    def weight(self):
        return self.__weight

    @property
    def cost(self):
        return self.__cost

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, value):
        self.__material = value

    def toStr(self):
        return ("material: " + self.__material + ", weigth: " + self.__weight + ", cost: " + self.__cost)

class Bicycle(object):
    def __init__(self, model, wheels = None, frame = None):
        self.__model = model
        self.__wheels = wheels
        self.__frame = frame
        self.__weight = float(self.__wheels.weight) * 2 + float(self.__frame.weight)
        self.__cost = float(self.__wheels.cost) * 2 + float(self.__frame.cost)

    @property
    def model(self):
        return self.__model

    @property
    def weight(self):
        return self.__weight

    @property
    def cost(self):
        return self.__cost

    def toStr(self):
        return ("model: " + str(self.__model) + ", weigth: " + str(self.__weight) + ", cost: " + str(self.__cost))

class Item:
    def __init__(self, bicycle, quantity = 0, percentOverCost = 20):
        self.__bicycle = bicycle
        self.__pricePerUnit = bicycle.cost + bicycle.cost * percentOverCost / 100
        self.__quantity = quantity
        self.__percentOverCost = percentOverCost

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def bicycle(self):
        return self.__bicycle

    @property
    def pricePerUnit(self):
        return self.__pricePerUnit

    def toStr(self):
        return ("bicycle: " + self.__bicycle.toStr() + ", quantity: " + str(self.__quantity) + ", price: " + str(self.__pricePerUnit))

class Shop:
    def __init__(self, name, inventory = None, percentOverCost = 20):
        self.__name = name
        self.__inventory = inventory
        self.__selledBikes = []
        self.__percentOverCost = percentOverCost

    def sellABike(self, bike):
        self.__selledBikes.append(bike)

    def toStr(self):
        return ("name: " + self.__name + ", number of bike in inventory: " + self.__inventory.length + ", number of selled bike: " + self.__selledBikes.length)

    @property
    def inventory(self):
        return self.__inventory

    @inventory.setter
    def inventory(self, value):
        self.__inventory = value

    @property
    def selledBikes(self):
        return self.__selledBikes

    @selledBikes.setter
    def selledBikes(self, value):
        self.__selledBikes = value

    def printInventory(self):
        for item in self.__inventory:
            print(item.toStr())

    def getProfit(self):
        totalCost = 0
        for bike in self.selledBikes:
            totalCost += bike.cost + bike.cost * self.__percentOverCost / 100;
        return totalCost

class Customer:
    def __init__(self, name, money = 0, bicycle = None, bicyclePrice = 0):
        self.__name = name
        self.__money = money
        self.__bicycle = bicycle
        self.__bicyclePrice = bicyclePrice

    @property
    def bicyclePrice(self):
        return self.__bicyclePrice

    @property
    def money(self):
        return self.__money

    @property
    def bicycle(self):
        return self.__bicycle

    @bicycle.setter
    def bicycle(self, value):
        self.__bicycle = value

    def buyABicycle(self, bicycle, bicyclePrice):
        self.__bicycle = bicycle
        self.__bicyclePrice = bicyclePrice
        self.__money = self.__money - bicyclePrice

    def toStr(self):
        return ("name: " + self.__name + ", money: " + str(self.__money))

def createWheels():
    print("------------Create Wheel(three different wheel types)--------------")
    wheels = []
    while True:
        print("Create Wheel: ")
        wheelModel = input(">Enter wheelModel:")
        wheelWeight = input(">Enter wheelWeight:")
        wheelCost = input(">Enter wheelCost:")
        wheelType = input(">Enter wheelType:")
        wheel = Wheel(wheelModel, wheelWeight, wheelCost, wheelType)
        wheels.append(wheel)
        check = input(">Do you want continue Yes(Y)/ No(N): ")
        if(check.upper() == "YES" or check.upper() == "Y"):
            continue
        else:
            break
    return wheels

def createFrames():
    frames = []
    while True:
        print("\nCreate Frame: ")
        frameMaterial = input(">Enter frameMaterial (aluminum, carbon, or steel):")
        if(frameMaterial.lower() != "aluminum" and frameMaterial.lower() != "carbon" and frameMaterial.lower() != "steel"):
            continue
        frameWeight = input(">Enter frameWeight:")
        frameCost = input(">Enter frameCost:")
        frame = Wheel(frameMaterial, frameWeight, frameCost)
        frames.append(frame)
        check = input(">Do you want continue Yes(Y)/ No(N): ")
        if(check.upper() == "YES" or check.upper() == "Y"):
            continue
        else:
            break
    return frames

def printWheels(wheels):
    for i in range(len(wheels)):
        print(str(i + 1) + ". " + wheels[i].toStr())

def printFrames(frames):
    for i in range(len(frames)):
        print(str(i + 1) + ". " + frames[i].toStr())

def createOneBicycle(wheels, frames):
    print("\nCreate new bicycle")
    bicycleModel = input(">Enter bicycle model:")
    printWheels(wheels)
    wheelNum = input(">Choose wheel of bicycle (1 -> " + str(len(wheels)) + ") :")
    printFrames(frames)
    frameNum = input(">Choose frame of bicycle (1 -> " + str(len(frames)) + ") :")
    bicycle = Bicycle(bicycleModel, wheels[int(wheelNum) - 1], frames[int(frameNum) - 1])
    return bicycle

def createInventory(wheels, frames):
    print("\n Create a inventory")
    inventory = []
    for i in range(6):
        bicycle = createOneBicycle(wheels, frames)
        quantity = input(">Enter bicycle quantity:")
        item = Item(bicycle, int(quantity))
        inventory.append(item)
    return inventory

def createShop(wheels, frames):
    name = input(">Enter shop name:")
    inventory = createInventory(wheels, frames)
    shop = Shop(name, inventory)
    return shop

def createCustomer(money):
    name = input(">Enter customer name:")
    customer = Customer(name, money)
    return customer

def printCustomerAndOfferBike(customerList, inventory):
    for customer in customerList:
        print("\n")
        print("Customer:" + customer.toStr())
        print("Bikes offered by the bike shop")
        for item in inventory:
            if item.pricePerUnit <= customer.money:
                print(item.bicycle.toStr() + ", price: " + str(item.pricePerUnit))

def customerBuyABicycle(customer, shop):
    print("\n")
    print("Customer:" + customer.toStr())
    print("Bikes offered by the bike shop")
    for i in range(len(shop.inventory)):
        item = shop.inventory[i]
        if item.pricePerUnit <= customer.money:
            print(str(i + 1) + ". " + item.bicycle.toStr() + ", price: " + str(item.pricePerUnit))
    num = input(">Choose bicycle to buy:")
    customer.buyABicycle(shop.inventory[int(num) - 1].bicycle, shop.inventory[int(num) - 1].pricePerUnit)
    shop.inventory[int(num) - 1].quantity = shop.inventory[int(num) - 1].quantity - 1
    shop.sellABike(shop.inventory[int(num) - 1].bicycle)

def mainProgram():
    wheels = createWheels()
    frames = createFrames()
    print("\n-------------")
    shop = createShop(wheels, frames)

    print("\n-------------")
    customerA = createCustomer(200)
    customerB = createCustomer(500)
    customerC = createCustomer(1000)

    customerList = []
    customerList.append(customerA)
    customerList.append(customerB)
    customerList.append(customerC)

    printCustomerAndOfferBike(customerList, shop.inventory)

    print("\n-------------")
    shop.printInventory();

    print("\n-------------")
    customerBuyABicycle(customerA, shop)
    customerBuyABicycle(customerB, shop)
    customerBuyABicycle(customerC, shop)

    print("\n-------------")
    print("Customer:" + customerA.toStr() + ", bicycle: " + customerA.bicycle.model + ", price bicycle: " + str(customerA.bicyclePrice))
    print("Customer:" + customerB.toStr() + ", bicycle: " + customerB.bicycle.model + ", price bicycle: " + str(customerB.bicyclePrice))
    print("Customer:" + customerC.toStr() + ", bicycle: " + customerC.bicycle.model + ", price bicycle: " + str(customerC.bicyclePrice))

    print("\n-------------")
    shop.printInventory();
    print("Profit of shop: " + str(shop.getProfit()))

mainProgram()
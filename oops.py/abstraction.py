# 11. Using abc module: 
# • Create an abstract class Shape with area(), perimeter() 
# • Implement Circle, Rectangle, Triangle Demonstrate:
# • why base class should NOT contain calculation logic 
# • what happens if a subclass fails to implement one of the methods 

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class circle(Shape):
#     def area(self):
#         print("circle area")
#     def perimeter(self):
#         print("circle perimeter")
# class Rectangle(Shape):
#     def area(self):
#         print("Rectangle area")
#     def perimeter(self):
#         print("Rectangle perimeter")
# class  Triangle(Shape):
#     def area(self):
#         print("traingle area") 
#     def perimeter(self):
#         print("Traingel perimeter")
# print(Shape.__abstractmethods__)  
# print(circle.__abstractmethods__)       
# K=Triangle()
# K.area()                             

# 12. Design an abstract class PaymentGateway with:
#  • authenticate() • pay(amount) • refund(amount) Implement subclasses:
#  • UPIPayment • CardPayment • 
#  NetBankingPayment Show how abstraction helps your main program call payment methods without caring about the payment type.
 
# from abc import ABC,abstractmethod
# class PayemntGateway(ABC):
#     @abstractmethod
#     def authenticate(self):
#         pass
#     @abstractmethod
#     def Pay(self):
#         pass
#     @abstractmethod
#     def refund(self):
#         pass
# class UPIpayment(PayemntGateway):
#     def authenticate(self):
#         print("authentication succesfull")
#     def Pay(self,amount): 
#         print(amount,"paid")
#     def refund(self,amount):
#         print(amount,"refunded")
# class cardpayment(PayemntGateway):
#       def authenticate(self):
#             print("authentication succesfull")
#       def Pay(self,amount): 
#            print(amount,"paid")
#       def refund(self,amount):
#           print(amount,"refunded")
# print(PayemntGateway.__abstractmethods__)
# print(UPIpayment.__abstractmethods__)
# A=cardpayment()
# A.authenticate()
# A.Pay(500)
# A.refund(200)

# 13. Create: • Abstract class VehicleControl with methods accelerate(), brake(), steer()
# • Implement CarControl, BikeControl, TruckControl Demonstrate calling each through a single interface. 

# from abc import ABC, abstractmethod
# class VehicleControl(ABC):
#     @abstractmethod
#     def accelerate(self):
#         pass
#     @abstractmethod
#     def brake(self):
#         pass
#     @abstractmethod
#     def steer(self):
#         pass
# class CarControl(VehicleControl):
#     def accelerate(self):
#         print("Car is accelerating")
#     def brake(self):
#         print("Car is braking")
#     def steer(self):
#         print("Car is steering")
# class BikeControl(VehicleControl):
#     def accelerate(self):
#         print("Bike is accelerating")
#     def brake(self):
#         print("Bike is braking")
#     def steer(self):
#         print("Bike is steering")
# class TruckControl(VehicleControl):
#     def accelerate(self):
#         print("Truck is accelerating")
#     def brake(self):
#         print("Truck is braking")
#     def steer(self):
#         print("Truck is steering")
# def control_vehicle(vehicle):
#     vehicle.accelerate()
#     vehicle.brake()
#     vehicle.steer()
# car = CarControl()
# bike = BikeControl()
# truck = TruckControl()
# control_vehicle(car)
# print()
# control_vehicle(bike)
# print()
# control_vehicle(truck)

# 14. Create an abstract class DatabaseDriver with:
#  • connect() • execute(query) • close() Implement concrete drivers:
#  • MySQLDriver • PostgresDriver • SQLiteDriver Show how abstraction helps switch databases without rewriting main code. 

# from abc import ABC,abstractmethod
# class Databasedriver(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#     @abstractmethod
#     def execute(self,query):
#         pass
#     @abstractmethod
#     def close(self):
#         pass
# class Mysqldriver(Databasedriver):
#     def connect(self):
#         print("mysqldriver connected")
#     def execute(self, query):
#         print(query)
#     def close(self):
#         print("mysqldriver")
# class postgresDriver(Databasedriver):
#     def connect(self):
#         print("mysqldriver connected")
#     def execute(self, query):
#         print(query)
#     def close(self):
#         print("mysqldriver")     
# class SQLliteDriver(Databasedriver):
#     def connect(self):
#         print("mysqldriver connected")
#     def execute(self, query):
#         print(query)
#     def close(self):
#         print("mysqldriver")

# print(Databasedriver.__abstractmethods__) 
# print(SQLliteDriver.__abstractmethods__)
# print(postgresDriver.__abstractmethods__)
# # M=Mysqldriver()
# # M.connect()
# # M.execute("SELECT *FROM students ORDER BY marks DESC;")         

# from abc import ABC,abstractmethod
# class Main(ABC):
#     @abstractmethod
#     def on(self):
#         pass
#     @abstractmethod
#     def off(self):
#         pass
#     def pause(self):
#         pass
# # i=Main()
# # i.on()    
# class Fan(Main):
#     def on(self):
#         print("fan on")
#     def off(self):
#         print("Fan off")
# i=Fan()
# i.on()           
# print(Main.__abstractmethods__)
# print(Fan.__abstractmethods__)
# print(Fan.mro())       


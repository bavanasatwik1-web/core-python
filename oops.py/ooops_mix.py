# 9. Classes: • LightDevice • SecurityDevice • SmartCamera(LightDevice, SecurityDevice) Requirements:
# • Resolve method conflicts using MRO • Encapsulate internal camera logs
# • SmartCamera overrides both parents’ behaviors • Use super() responsibly in multiple inheritance


# 5. Classes: • User • Instructor(User) • Student(User) • TeachingAssistant(Student, Instructor) Requirements: 
# • Track course assignments privately • Ensure TAs override submit_work() and grade_work() 
# • Print MRO and explain how Python resolves conflicts

# 7. Design: • Abstract class MediaFile with play(), stop() • Subclasses: MP3File, MP4File, WAVFile
# • Private file path validation done internally • A function start_player(media) that works with ANY object that has play() (duck typing)
# Demonstrate mixing true polymorphism + duck typing. 
# from abc import ABC,abstractmethod
# class MediaFile(ABC):
#     @abstractmethod
#     def play(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class MP3file(MediaFile):
#     def play(self):
#         print("mp3 started playing") 
#     def stop(self):
#         print("Mp3 stopped playing")       
# class MP4File(MediaFile):
#     def play(self):
#         print("MP4 started playing")
#     def stop(self):
#         print("MP4 stopped playing")
# class WAVFILE(MediaFile):
#     def play(self):
#             print("Wavfile started playing")
#     def stop(self):
#             print("Wavfile stopped playing")
# A1=MP3file()
# A2=MP4File()
# A3=WAVFILE()
# A=[A1,A2,A3]        
# def start_player(media):
#      media.play()
# for i in A:
#      start_player(i)   
     
# 13. Build: • Transport abstract class • Subclasses: Taxi, Bus, Train • Each implements: 
# o calculate_fare() differently • Use static method to validate distance • Encapsulate fare state
# • Add class method to update government tax slab

# from abc import ABC,abstractmethod
# class Transport(ABC):
#     @abstractmethod
#     def ticket_price(self);
#         pass
#     @abstractmethod
#     def book(self);
#         pass
# class Taxi(Transport):
#     def ticket_price(self):
#         print("ticket price=100")
#     def book(self):
#         print("Ticket booked for taxi")        
# class Bus(Transport):
#     def ticket_price(self):
#         print("ticket price=10")
#     def book(self):
#         print("Ticket booked for Bus")        
# class Train(Transport):
#     def ticket_price(self):
#         print("ticket price=150")
#     def book(self):
#         print("Ticket booked for Train")

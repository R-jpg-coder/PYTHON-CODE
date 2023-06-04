class Vechile:
    def __init__(self,name,speed,miliege):
        self.name=name
        self.speed=speed
        self.miliege=miliege
    def display_info(self):
        print(f"Vechile name:{self.name}")
        print(f"Vechile speed:{self.speed}")
        print(f"Vechile miliege:{self.miliege}")
class Bus(Vechile):
    pass
my_bus=Bus("School",180,12)
my_bus.display_info()

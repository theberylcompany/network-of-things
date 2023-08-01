import time


class Thermostat:
    current_temp = 0;
    pref_temp = None
    humidity = 0;
    scale = None


    def set_temp(self):
        time.sleep(1)
        setter = input('What would you like the temperature to be? ')
        self.current_temp = int(setter)
        
    
    def set_scale(self):
        # This will be linked to a button on the device that a user can choose between F or C
        switcher_scale = True
        while(switcher_scale == True):
            setter = input('Please select your scale. Fahrenheit or Celsius? (F or C):')
            if(setter.lower() == 'f'):
                self.scale = 'fahrenheit'
                switcher_scale = False
            elif(setter.lower() == 'c'):
                self.scale = 'celsius'
                switcher_scale = False
            else:
                print('Wrong input. Please select F or C.')
            
        
    def get_temp(self):
        # This will also read sensor data in Fahrenheit from the device
        if(self.scale == 'fahrenheit'):
            return f"{self.current_temp}F"
        elif(self.scale == 'celsius'):
            convert = (self.current_temp - 32) * (5/9)
            return f"{str(convert)} C"
        else:
            return 'You have not set your degree scale. Please do so.'
        
    def set_humidity(self):
        # This will get sensor data at some point
        humid_setter = True
        while(humid_setter == True):
            setter = input("What is the current humidity level? (please enter a number between 0-100): ")
            if(int(setter) < 0 and  int(setter) > 100):
                return "Please enter a number from 0 to 100"
            else:
                self.humidity = int(setter)
                humid_setter = False

    def get_humidity(self):
        return f"{self.humidity}%"



def main():
    
    thermostat = Thermostat()

    
    thermostat.set_scale()        
    thermostat.set_humidity()
    thermostat.set_temp()
    print(thermostat.get_temp())
    print(thermostat.get_humidity())

main()
## Smart Thermostat

We are going to start writing our Thermostat App with Python. Here's is the initial code I started with in order to begin fleshing out the logic side of things.

```python
import time


class Thermostat:
    current_temp = 0;
    pref_temp = None
    humidity = 0;
    scale = None

```

This code imports the *time* library. This helps with setting timers. Then, we set some base attributes for the <span style="color: orange; font-weight:bold;">Thermostat</span> class.

## Methods

We do not want to update our variables directly. So, we have to develop some methods that update the properties of our Thermostat class. 

### Set Desired Temperature

```python

    def set_temp(self):
        time.sleep(1)
        setter = input('What would you like the temperature to be? ')
        self.current_temp = int(setter)

```

### Set Degree Scale
Another method we have developed is a way to change from Fahrenheit to Celsius. 

```python
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

```

### Returning The Temperature

```python
  def get_temp(self):
        # This will also read sensor data in Fahrenheit from the device
        if(self.scale == 'fahrenheit'):
            return f"{self.current_temp}F"
        elif(self.scale == 'celsius'):
            convert = (self.current_temp - 32) * (5/9)
            return f"{str(convert)} C"
        else:
            return 'You have not set your degree scale. Please do so.'
```


### Setting and Getting Humidity

This will be designed for returning and parsing sensor data to return the correct humidity percentage.

```python

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
 
```
```python
    # A Simple Return
   def get_humidity(self):
        return f"{self.humidity}%"

```

## Wrapping Up

This is the base code for the Smart Thermostat app. As we progress with our research, we will update the codebase. We are also working on the
research and development of a prototype device.
#Question1
class calculator:
    def __init__(self ,input1 ,input2):
        self.input1=input1
        self.input2=input2
    
    def adder(self):
        """Create a addition function"""
        result = self.input1 + self.input2
        return result

    def subtractor(self):
        """Create a subtraction function"""
        result = self.input1 - self.input2
        return result
    
    def multiplier(self):
        """Create a multiplication function"""
        result = self.input1 * self.input2
        return result
    
    def divider(self):
        """Create a division function"""
        result = self.input1 / self.input2
        return result
    
    def clear(self):
        """Create a clear function"""
        return 0
    
#Enter 2 number and storing it as int in variable input1 and input2
input1 = int(input("Enter the first number : "))
input2 = int(input("Enter the second number : "))

#Printing out input1,input2 and with the different functions
cal = calculator(input1, input2)
print("The addition of {} and {} is {}" .format(input1 ,input2, cal.adder()))
print("The subtraction of {} and {} is {}" .format(input1 ,input2, cal.subtractor()))
print("The multiplication of {} and {} is {}" .format(input1 ,input2, cal.multiplier()))
print("The division of {} and {} is {}" .format(input1 ,input2, cal.divider()))
print("The result after clear is", cal.clear())

#Question2
class clockTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def setHours(self):
        """Set hours function"""
        return self.hours
    
    def setMinutes(self):
        """Set minutes function"""
        return self.minutes
        
    def setSeconds(self):
        """Set seconds function"""
        return self.seconds
        
    def setTime(self, hours, minutes, seconds):
        """Set time function"""
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds 
        
    def showTime(self):
        """Show time function"""
        print("%d:%02d:%02d" %(self.hours, self.minutes, self.seconds))

#Get hours, minutes and seconds from user. Storing it in getHours, getMinutes and getSeconds accordingly.
getHours = int(input("Enter the number of hours: "))
getMinutes = int(input("Enter the number of minutes: "))
getSeconds = int(input("Enter the number of seconds: "))
time = clockTime(getHours, getMinutes, getSeconds)
#Print out the time set by user.
time.showTime()

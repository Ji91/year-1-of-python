###################### 1 ##########
# using simple mathematical calculations
# Python Program to Convert seconds 
# into hours, minutes and seconds 
  
def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 
      
# Driver program 
n = int(input("Enter seconds: "))
print(convert(n))


########## 2 ##########
# By using the divmod() function, which does only a
# single division to produce both the quotient and the remainder,
# you can have the result very quickly with only
# two mathematical operations.

# Python Program to Convert seconds 
# into hours, minutes and seconds 
  
def convert(seconds): 
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    return "%d:%02d:%02d" % (hour, min, sec) 
      
# Driver program 
n = int(input("Enter seconds: "))
print(convert(n))


#### 3 ######

#Using timedelta (Object of datetime module)

# Datetime module provides timedelta object which represents a duration,
# the difference between two dates or times. datetime.timedelta
# can be used to represent seconds into hours, minutes and seconds format.


# Python Program to Convert seconds 
# into hours, minutes and seconds 
import datetime 
  
def convert(n): 
    return str(datetime.timedelta(seconds = n)) 
      
# Driver program 
n = int(input("Enter seconds: "))
print(convert(n)) 



######## 4 ###########

#  Using time.strftime()

# time.strftime() gives more control over formatting. The format
# and time.gmtime() is passed as argument. gmtime is
# used to convert seconds to special tuple format that strftime() requires.


# Python Program to Convert seconds 
# into hours, minutes and seconds 
  
import time 
  
def convert(seconds): 
    return time.strftime("%H:%M:%S", time.gmtime(n)) 
      
# Driver program 
n = int(input("Enter seconds: "))
print(convert(n))


###### 5 ########

# convert hours, mins, and seconds to seconds


# days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = hours + minutes + seconds

print("The  amounts of seconds", time)

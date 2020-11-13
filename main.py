# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pywhatkit as kit

#kit.add_driver_path('chromedriver.exe')
x = 19
#kit.load_QRcode()
while x <= 30:
    kit.sendwhatmsg('+237698806036', 'je teste quelque chose', 12, x)
    x = x+1

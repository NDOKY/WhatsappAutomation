# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import strftime

import pywhatkit as kit
import datetime
from pyxlsb import convert_date

tempsMinute = datetime.datetime.now().minute +1
tempsHeures = datetime.datetime.now().hour

print(tempsMinute)

heureEnvoi = 4
minuteEnvoi = 4

#while tempsMinute <= minuteEnvoi and tempsHeures <= heureEnvoi:
while tempsMinute != 60:
    kit.sendwhatmsg('+237699130619', 'hahahahahahahahaha', heureEnvoi, tempsMinute)
    tempsMinute = tempsMinute + 1


#incrementer les secondes
# if tempsMinute == 60:
#        tempsHeures = tempsHeures + 1
#    tempsMinute = tempsMinute + 1

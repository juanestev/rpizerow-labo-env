from gpiozero import RGBLED
from time import sleep 

#declaro los pines 
ledquique = RGBLED(13,19,26)

#declaro al bucle 
while True:
   ledquique.color = (1,1,1)
   sleep(0.25)
   ledquique.color = (0,1,1)
   sleep(0.25)
   ledquique.color = (1,0,1)
   sleep(0.25)
   ledquique.color = (0,0,1)
   sleep(0.25)
   ledquique.color = (1,1,0)
   sleep(0.25)
   ledquique.color = (0,1,0)
   sleep(0.25)
   ledquique.color = (1,0,0)
   sleep(0.25)
   ledquique.color = (0,0,0)
   sleep(0.25)

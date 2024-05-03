#importo librerias
from gpiozero import LED, Button
#declaro los pines
led = LED(26)
button = Button(18)

while True:
	#pregunto si esta presionado
	if button.is_pressed:
		#prendo el LED
		led.on()
	else:
		led.off()
	

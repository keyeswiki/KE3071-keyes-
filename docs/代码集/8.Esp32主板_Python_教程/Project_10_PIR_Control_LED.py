# 导入 Pin and time 库.
from machine import Pin
import time

# 定义人体红外传感器和led的引脚. 
sensor_pir = Pin(15, Pin.IN)
led = Pin(2, Pin.OUT)

while True: 
      if sensor_pir.value():
          led.value(1)
          time.sleep(0.5)
          led.value(0)
          time.sleep(0.5)         
      else:
          led.value(0)
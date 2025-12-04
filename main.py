from machine import Pin
from time import sleep

lampubiru = Pin(2, Pin.OUT)
lampukuning = Pin(1, Pin.OUT)
lampuhijau = Pin(0, Pin.OUT)

lampuputih = Pin(26, Pin.OUT)
lampumerah = Pin(27, Pin.OUT)
lampuungu = Pin(28, Pin.OUT)

tombol = Pin(15, Pin.IN, Pin.PULL_DOWN)

group = 1
step = 0
last_state = 0

def matikan_semua():
    lampubiru.off()
    lampukuning.off()
    lampuhijau.off()
    lampuputih.off()
    lampumerah.off()
    lampuungu.off()

while True:
    matikan_semua()

    if group == 1:
        if step == 0:
            lampubiru.on()
            print("Grup 1 - Lampu Biru ON")
        elif step == 1:
            lampukuning.on()
            print("Grup 1 - Lampu Kuning ON")
        elif step == 2:
            lampuhijau.on()
            print("Grup 1 - Lampu Hijau ON")
    else:
        if step == 0:
            lampuputih.on()
            print("Grup 2 - Lampu Putih ON")
        elif step == 1:
            lampumerah.on()
            print("Grup 2 - Lampu Merah ON")
        elif step == 2:
            lampuungu.on()
            print("Grup 2 - Lampu Ungu ON")

    current_state = tombol.value()
    if current_state == 1 and last_state == 0:
        group = 2 if group == 1 else 1
        print("Tombol ditekan! Ganti ke Grup", group)
        step = 0 
    last_state = current_state

    sleep(0.2) #Ganti perpindahan antar lampu
    step = (step + 1) % 3

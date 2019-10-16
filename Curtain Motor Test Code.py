temperature = int(input("Temperature: "))
light = int(input("Light Level: "))

if temperature > 33 or light > 15000:
    print("close")
elif temperature < 30 and light < 7000:
    print("open")

#Conversione temperature Celsius, Fahrenheit, Kelvin

#Dati iniziali
celsius = float(input("Inserisci i gradi celsius:"))

#Elaborazione
fah = celsius * 1.8 +32
kel = celsius +273.15

#Output
print("Temperatura in Celsius:", celsius)
print("Temperatura in Fahrenheit:", round(fah, 2))
print("Temperatura in Kelvin:", round(kel, 2))

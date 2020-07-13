#Calcolo della velocità in Km/h e m/s

#Dati iniziali
minuti= 21
secondi = 34
km = 4.1

#Elaborazione
secondi_totali = minuti * 60 + secondi

#Velocità in m/s
metri = km * 1000
m_s = metri / secondi_totali

#velocità in km/h
km_h = m_s * 3.6

#velocità in mph
mph = km_h / 1.609344

#Output
print("Velocità", round(m_s, 2), "m/s")
print("Velocità", round(km_h, 2), "Km/h")
print("Velocità", round(mph, 2), "mph")
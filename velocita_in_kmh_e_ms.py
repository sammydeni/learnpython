#Calcolo della velocità in Km/h e m/s v1

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

#Output
print("Velocità in millisecondi", round(m_s, 2), "m/s")
print("Velocità in chilometri", round(km_h, 2), "Km/h")

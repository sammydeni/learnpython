#Calcolo dell'interesse composto
capitale_iniziale=100
tasso= 0.03
n_anni=10

capitale_finale= capitale_iniziale * (1+ tasso) ** n_anni
print("Dopo", n_anni, "anni il capitale è:",round(capitale_finale,2))
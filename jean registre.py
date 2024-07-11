from tkinter import *
from math import *
# Constantes pour le calcul de la trajectoire
GRAVITE = 9.81  # Accélération due à la gravité (m/s^2)
MASSE_BALLE = 0.045  # Masse d'une balle de golf (kg)
COEFFICIENT_TRAINEE = 0.24  # Coefficient de traînée d'une balle de golf
DENSITE_AIR = 1.225  # Densité de l'air (kg/m^3)
SURFACE_BALLE = 0.0014  # Surface en coupe d'une balle de golf (m^2)

# Fonction pour calculer la portée de la balle de golf
def calculer_portee(vitesse, angle):
    # Convertir l'angle en radians
    angle_rad = radians(angle)
    print(angle_rad)
    # Calculer les composantes de la vitesse initiale
    vitesse_x = vitesse * cos(angle_rad)
    vitesse_y = vitesse * sin(angle_rad)
    # Calculer le temps de vol
    temps_vol = (2 * vitesse_y) / GRAVITE
    # Calculer la portée de la balle de golf
    portee = vitesse_x * temps_vol
    return portee
#rungekuta4
# Fonction pour mettre à jour la trajectoire sur le canevas
def maj_trajectoire():
    # Obtenir la vitesse et l'angle des entrées utilisateur
    vitesse = float(entree_vitesse.get())
    angle = float(entree_angle.get())
    # Calculer la portée de la balle de golf
    portee = calculer_portee(vitesse, angle)
    # Effacer le canevas
    canevas.delete("all")
    # Dessiner la trajectoire
    points = []  # Liste pour stocker les coordonnées des ovales
    for d in range(int(portee)):
        x = 50 + vitesse * cos(radians(angle)) * d
        y = 250 - (vitesse * d * sin(radians(angle)) - 0.5 * GRAVITE * d**2)
        points.append((x, y))  # Ajouter les coordonnées à la liste
        canevas.create_oval(x-3, y-3, x+3, y+3, fill="red")
    canevas.create_line(points, fill="blue")  # Dessiner une ligne entre les ovales
    # Mettre à jour l'étiquette de portée
    etiquette_portee.config(text=f"Portée: {portee:.2f} mètres")



# Créer la fenêtre principale
fenetre = Tk()
fenetre.title("Trajectoire de la Balle de Golf")

# Créer un canevas pour dessiner la trajectoire
canevas = Canvas(fenetre, width=600, height=300, bg="white")
canevas.pack()

# Créer des étiquettes et des entrées pour la vitesse et l'angle
etiquette_vitesse = Label(fenetre, text="Vitesse (m/s):")
etiquette_vitesse.pack()
entree_vitesse = Entry(fenetre)
entree_vitesse.pack()

etiquette_angle = Label(fenetre, text="Angle (degrés):")
etiquette_angle.pack()
entree_angle = Entry(fenetre)
entree_angle.pack()

# Créer un bouton pour mettre à jour la trajectoire
bouton_maj = Button(fenetre, text="Mettre à Jour la Trajectoire", command=maj_trajectoire)
bouton_maj.pack()

# Créer une étiquette pour afficher la portée
etiquette_portee = Label(fenetre, text="Portée: 0 mètres")
etiquette_portee.pack()


fenetre.mainloop()

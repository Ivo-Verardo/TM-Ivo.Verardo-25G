from tkinter import *
from math import *
# Constantes pour le calcul de la trajectoire
g = 9.81  # Accélération due à la gravité (m/s^2)
m = 0.042  # Masse d'une balle de golf (kg)
C_d = 0.24  # Coefficient de traînée d'une balle de golf
C_l = 0.11 # Coefficient de portance d'une balle de golf
ρ = 1.225  # Densité de l'air (kg/m^3)
A = 0.0014  # Surface en coupe d'une balle de golf (m^2)
e = 0.83 # Coefficient de restitution

def choc(v_c, m_c) :
    vitesse = ((2*m_c*v_c)/(m_c+m))*e
    return vitesse

def calculer_portee(v_b, a):
    # Convertir l'angle en radians
    α = radians(a)
    l = (2*m)/(ρ*A*C_d)
    portee = 0.5*l*cos(α)*log(1+4*(v_b**2/(g*l))*sin(α))
    return portee
    
def maj_trajectoire():
    # Obtenir la vitesse et l'angle des entrées utilisateur
    vitesse = choc(float(entree_v_c.get()),float(entree_m_c.get()))
    angle = float(entree_angle.get())
    
    # Calculer la portée de la balle de golf
    portee = calculer_portee(vitesse, angle)
    # Effacer le canevas
    canevas.delete("all")
    # Dessiner la trajectoire
    points = [(50, 250)]  # Liste pour stocker les coordonnées des ovales
    y = 250
    t = 0
    l = (2*m)/(ρ*A*C_d)
    h = l*tan(radians(angle))
    L = 50+l
    H = 250 - h
    points.append((L, H))
    vit_2 = vitesse*2.71828**(-(sqrt(l**2+h**2)/vitesse)/l)
    while y <= 250:
        
        x = L + vit_2 * cos(radians(angle)) * t
        y = H - vit_2 * sin(radians(angle)) * t + 0.5 * g * t**2
        
        points.append((x, y))  
        canevas.create_oval(x, y, x, y, fill="white")
        canevas.create_line(50, 250, 50+portee, 250)
        t +=0.1
    canevas.create_line(points, fill="blue")  # Dessiner une ligne entre les ovales
    # Mettre à jour l'étiquette de portée
    etiquette_portee.config(text=f"Portée: {portee:.2f} mètres")
        


# Créer la fenêtre principale
fenetre = Tk()
fenetre.title("Trajectoire de la Balle de Golf")

# Créer un canevas pour dessiner la trajectoire
canevas = Canvas(fenetre, width=600, height=300, bg="white")
canevas.pack()

# Créer des étiquettes et des entrées pour la vitesse, la masse et l'angle du club
etiquette_v_c = Label(fenetre, text="vitesse du club (m/s):")
etiquette_v_c.pack()
entree_v_c = Entry(fenetre)
entree_v_c.pack()

etiquette_m_c = Label(fenetre, text="masse du club (kg):")
etiquette_m_c.pack()
entree_m_c = Entry(fenetre)
entree_m_c.pack()

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

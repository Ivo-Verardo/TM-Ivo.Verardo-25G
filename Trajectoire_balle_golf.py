from tkinter import *
from math import *
# Constantes pour le calcul de la trajectoire
g = 9.81  # Accélération due à la gravité (m/s^2)
m = 0.042  # Masse d'une balle de golf (kg)
ρ = 1.095  # Densité de l'air (kg/m^3)
A = 0.0014  # Surface en coupe d'une balle de golf (m^2)

def choc(v_c, m_c) :
  
    vitesse = ((2*m_c*v_c)/(m_c+m))
    return vitesse
    
def maj_trajectoire():
    # Obtenir la vitesse, la masse et l'angle des entrées utilisateur
    vit_club = float(entree_v_c.get())
    mas_club = float(entree_m_c.get())
    angle = float(entree_angle.get())
    #
    vitesse = choc(vit_club, mas_club)
    α = radians(angle)
    # Effacer le canevas
    canevas.delete("all")
    # Dessiner la trajectoire
    points = [(50, 250)]  # Liste pour stocker les coordonnées des ovales
    x = 50
    y = 250
    dt = 0.01
    Vx = vitesse*cos(α)
    Vy = vitesse*sin(α)
    #calcul des coefficients
    C_l = 2*angle/(30*mas_club*vit_club)
    C_d = 2*C_l-0.03
    #calcul de la trajectoire
    while y <= 250 :
        #Calcul de la force de traînée
        Fdx = -C_d*0.5*ρ*A*Vx**2
        Fdy = -C_d*0.5*ρ*A*Vy**2
        #Calcul de la force de portance
        Flx = -C_l*0.5*ρ*A*Vx**2
        Fly = C_l*0.5*ρ*A*Vy**2
        #Calcul de la force de pesanteur
        Fp = m*-g
        #Calcul de la somme des forces
        SFx = Fdx + Flx
        SFy = Fdy + Fly + Fp
        #Calcul de l'acceleration
        ax = SFx/m
        ay = SFy/m
        #Calcul du nouveau point
        x += Vx*dt
        y -= Vy*dt
        #Calcul de la nouvelle vitesse
        Vx += ax*dt
        Vy += ay*dt
        #dessin du point
        points.append((x, y))
        canevas.create_oval(x, y, x, y, fill="blue")
        
        portee = x-50
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

from tkinter import *
from math import *
from random import *
# Constantes pour le calcul de la trajectoire
g = 9.81  # Accélération due à la gravité (m/s^2)
m = 0.042  # Masse de la balle de golf (kg)
ρ = 1.124  # Densité de l'air à 1000m d'altitude [wind-data.ch] (kg/m^3) 
A = 0.0014  # Surface en coupe d'une balle de golf (de 4.2cm de diamètre) (m^2)


'''
La fonction "choc" calcule et renvoie la vitesse initiale de la balle après l'impact en utilisant comme valeur la vitesse de club et la masse du club grâce à la formule v_2'=(2m_1 v_1)/(m_1+m_2).
'''
def choc(v_c, m_c) :

    vitesse = ((2*m_c*v_c)/(m_c+m))
    return vitesse

'''
La fonction "dessin_trajectoire" calcule point après point la position de la balle lors de son "carry" et dessine et relie ces points sur le canvas à leurs coordonées respectives.
Cette fonction note aussi la distance que la balle a parcourue en vol.
'''
def dessin_trajectoire(v_b, m_c, v_c, angle) :
    points = [(50, 250)]  # Liste pour stocker les coordonnées des ovales
    x = 50
    y = 250
    dt = 0.001
    α = radians(angle)
    Vx = v_b*cos(α)
    Vy = v_b*sin(α)
    #Calcul des coefficients
    C_l = angle/(15*m_c*v_c)
    C_d = 2*C_l-0.03
    #Calcul de la trajectoire
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
        #Dessin du point
        points.append((x, y))
        canevas.create_oval(x, y, x, y, fill="black", tags="courbe",)
    portee = x-50
    canevas.create_line(points, fill="gray", tags="courbe",)  # Dessiner une ligne entre les points
    # Mettre à jour l'étiquette de portée
    etiquette_portee.config(text=f"Portée: {portee:.2f} mètres")
    return

'''
La fonction "dessin_trajectoire" ajoute une "image" de fond au canevas.
'''
def fond():
    for i in range(5) :
        x = randint(0, 550)
        y = randint(20, 100)
        dx = randint(50, 100)
        dy = randint(10, 25)
        canevas.create_oval(x, y, x+dx, y-dy, outline="white", fill="white")
    canevas.create_rectangle(0, 300, 600, 250, outline="green", fill="green")
    canevas.create_rectangle(535, 251, 565, 250, outline="light green", fill="light green")
    canevas.create_line(550, 250, 550, 240, fill="dark red")
    canevas.create_rectangle(550, 243, 554, 240, outline="red", fill="red")
    
'''
La fonction "sys_axe" dessine sur le canevas un système d'axe qui a comme unité 1m = une unité.
'''
def sys_axe():
    canevas.create_line(50, 250, 50, 50)
    canevas.create_line(50, 250, 550, 250)
    y=250
    while y >= 50 :
        canevas.create_line(48, y, 50, y)
        y -= 10
    y=250
    while y >= 50 :
        canevas.create_line(45, y, 50, y)
        canevas.create_text((35, y),text=250-y)
        y -= 50
    x=50
    while x <= 550 :
        canevas.create_line(x, 252, x, 250)
        x += 10
    x=50
    while x <= 550 :
        canevas.create_line(x, 255, x, 250)
        canevas.create_text((x, 265),text=x-50)
        x += 50
    
    
'''
La fonction "maj_trajectoire" est la fonction qui va récupérer les données entrés par l'utilisateur et qui va "gérer" les autres fonctions dans le bon ordre.
'''
def maj_trajectoire():
    # Obtenir la vitesse, la masse et l'angle des entrées utilisateur
    vit_club = float(entree_v_c.get())
    mas_club = float(entree_m_c.get())/1000
    angle = float(entree_angle.get())
    # Faire appelle à la fonction choc()
    vitesse = choc(vit_club, mas_club)
    # Effacer la courbe du canevas
    canevas.delete("courbe")
    # Dessiner la trajectoire
    dessin_trajectoire(vitesse, mas_club, vit_club, angle)
    return

# Créer la fenêtre principale
fenetre = Tk()
fenetre.title("Trajectoire de la Balle de Golf")

# Créer un canevas pour dessiner la trajectoire
canevas = Canvas(fenetre, width=600, height=300, bg="light blue")
canevas.grid(row=0, column=0, columnspan=3)
fond()
sys_axe()

# Créer des étiquettes et des entrées pour la vitesse, la masse et l'angle du club
etiquette_v_c = Label(fenetre, text="vitesse du club (m/s):")
etiquette_v_c.grid(row=1, column=0)
entree_v_c = Entry(fenetre)
entree_v_c.grid(row=2, column=0)

etiquette_m_c = Label(fenetre, text="masse du club (g):")
etiquette_m_c.grid(row=1, column=1)
entree_m_c = Entry(fenetre)
entree_m_c.grid(row=2, column=1)

etiquette_angle = Label(fenetre, text="Angle (degrés):")
etiquette_angle.grid(row=1, column=2)
entree_angle = Entry(fenetre)
entree_angle.grid(row=2, column=2)

# Créer une étiquette pour afficher la portée
etiquette_portee = Label(fenetre, text="Portée: 0 mètres")
etiquette_portee.grid(row=3, column=1)

# Créer un bouton pour mettre à jour la trajectoire
bouton_maj = Button(fenetre, text="Mettre à Jour la Trajectoire", command=maj_trajectoire)
bouton_maj.grid(row=4, column=1)

fenetre.mainloop() 

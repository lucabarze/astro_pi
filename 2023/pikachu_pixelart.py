# Importa le librerie
from sense_hat import SenseHat
from time import sleep

# Imposta il Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Imposta il sensore di colore
sense.color.gain = 60 # Imposta la sensibilità del sensore
sense.color.integration_cycles = 64 # L'intervallo con cui verrà eseguita la lettura

# Aggiungi variabili per il colore e immagine
# Tavolozza dei colori
a = (255, 255, 255) # Bianco
b = (105, 105, 105) # Grigio scuro
c = (0, 0, 0) # Nero
d = (100, 149, 237) # Blu Fiordaliso
e = (0, 0, 205) # Blu Medio
f = (25, 25, 112) # Blu Notte
g = (0, 191, 255) # Blu Cielo Profondo
h = (0, 255, 255) # Ciano
j = (143, 188, 143) # Mare Verde Scuro
k = (46, 139, 87) # Mare Verde
l = (0, 255, 127) # Verde Primavera
m = (34, 139, 34) # Foresta Verde
n = (154, 205, 50) # Giallo Verde
o = (128, 128, 0) # Oliva
p = (240, 230, 140) # Cachi
q = (255, 255, 0) # Giallo
r = ( 184, 134, 11) # Verga Oro Scuro
s = (139, 69, 19) # Sella Marrone
t = (255, 140, 0) # Arancio Scuro
u = (178, 34, 34) # Mattone
v = (255, 0, 0) # Rosso
w = (255, 192, 203) # Rosa
y = (255, 20, 147) # Rosa Scuro
z = (153, 50, 204) # Orchidea Scura

time = 0

while time < 25:
    
    # ottenere il colore dal sensore
    colore = sense.color 
    a = (colore.red, colore.green, colore.blue) # usa il colore percepito.red, rgb.green, rgb.blue) # usa il colore percepito

    # Crea l'immagine
    immagine = [
      a, c, c, a, a, a, a, c,
      a, a, q, t, a, a, a, t,
      a, a, a, q, q, q, q, t,
      t, t, a, q, c, q, q, c,
      t, t, a, v, q, q, q, t,
      a, v, a, q, t, t, t, a,
      a, v, q, t, q, t, q, a,
      a, a, q, t, v, v, t, a]
    
    # Mostra l'immagine
    sense.set_pixels(immagine)

    time = time + 1
    sleep(1)

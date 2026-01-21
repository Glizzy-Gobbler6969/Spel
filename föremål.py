from spelaren import *
from ryggsäck import *
from slowtypeshii import *

import random as r

def föremål_kista():
    kistföremål = ["Styrkebryggd","Livselixir","Ruttet kött","Gammal sko","Mattebok","Deoderant","Bok","Guldäpple","Silverring","Bronsmynt"]
    
    ditt_föremål = r.choice(kistföremål)
    return ditt_föremål
from spelaren import *
from ryggsäck import *
from föremål import *
from slowtypeshii import *
from rensa import *

import random as randit
def kistrum():
    slowprint("""
Du tar dig in i nästa rum och hittar en kista mitt på golvet.
När du närmar dig kistan inser du att den är hårig.
Det är en äcklig syn, men det kan ju trots allt finnas något värdefullt i kistan.
                        
                        Vill du öppna kistan?
                        
                        1. Ja       2. Nej
""")
    öppna_kista = input("""
Ditt val -->""")
    rensa()
    if öppna_kista == "2":
        slowprint("""
Du kollar äcklat på den håriga kistan medan du ger dig iväg.
""")
    elif öppna_kista == "1":
        kista = randit.randint(1,3)
        if kista == 1:
            slowprint("""
Du öppnar kistan och känner det sträva håret mot dina händer.
Till din besvikelse är kistan tom.
""")
        elif kista == 2 or 3:
            ditt_föremål = föremål_kista()
            slowprint(f"""
Du öppnar kistan och stoppar ner handen.
Du plockar upp föremålet i förvånan och du utrbrister:
"{ditt_föremål}!?!?"
""")
            ryggsäck.append(ditt_föremål)
            slowprint(f"""
Du stoppar ner {ditt_föremål} i din ryggsäck.
""")
            
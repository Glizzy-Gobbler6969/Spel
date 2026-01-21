from spelaren import *
from ryggsäck import *
from slowtypeshii import *
from rensa import *




def lång_korridoren():
    while True:
        slowprint("""
                
                                    Vad vill du göra?
                        
            1. Gå till trappuppgången.     2. Gå till kiosken.     3. Prata med en elev.
""")
        korridor_väg = input("""
Ditt val -->""")
        rensa()

        if korridor_väg == "1":
            slowprint("""
Du går fram till trappuppgången och ser en skallig man vars otäcka leende tvingar dig till att prata med honom.
""")
            if klassval == "1":
                slowprint("""
Han kollar på dig med en skeptisk men förstående blick när han inser att du går bygg
"Jaha. Du är korkad du alltså. Men det är den starkaste klassen så det får väl gå an.
Det skulle ej förvåna mig om du inte begriper vad jag säger just nu.
Du borde vandra nedåt." säger den skalliga mannen med en nedlåtande ton.
                
Du gör som han säger och börjar vandra nedåt till våning två.
""")
            
                from Våning_2 import troll_våning_2
                klass.levande = troll_våning_2()
                return klass.levande

            elif klassval == "2":
                slowprint("""
Den skalliga mannen blir genast glad när han inser att du går teknik.
"Åh, vad kul! Du går teknik jag kan känna det på lukten.
Eftersom du är så smart och duktig så borde du vandra nedåt." säger den skalliga mannen glatt
                
Du gör som han säger och börjar vandra nedåt till våning två.
""")
                from Våning_2 import troll_våning_2
                klass.levande = troll_våning_2()
                return klass.levande
            
            elif klassval == "3":
                slowprint("""
Han kollar på dig med en skum blick när han inser att du går samhäll
"Ah, du är en sån där alltså. En samelev som tror du är huvudpersonen.
Gå ner för trappan du." säger den skalliga mannen obrytt.
                               
""")
                from Våning_2 import troll_våning_2
                klass.levande = troll_våning_2()
                return klass.levande

        elif korridor_väg == "2":
            slowprint("""
Du går fram till kiosken där den vanliga mattanten sitter och läser en tidning.
Du går fram och kikar på priserna, men får snabbt PTSD från alla tidigare köp.
Du väljer därför att inte köpa något.
""")
        elif korridor_väg == "3":
            if klassval == "1":
                slowprint("""
Du bestämmer dig för att försökra prata med en elev i korridoren,
men när du öppnar din mun inser du att du har glömt hur man pratar.
Du går därifrån skamset.
""")
            elif klassval == "2":
                slowprint("""
Du närmar dig en elev som ser ut att vara trevlig,
men så fort han känner stanken av dig springer han iväg skrikandes.
""")
            elif klassval == "3":
                slowprint("""
Du närmar dig en elevn, men vänder snabbt om igen 
då du inser att ingen vill ha med dig att göra eftersom du går sam.
""")
        else:
            slowprint("Välj ett av alternativen!")


def lång_korridoren_återvänd():
    slowprint("""
Du har tagit dig upp till våning tre igen där du nu är säker från fiender.
""")
    while klass.levande == True:
        slowprint("""     
                                    Vad vill du göra?
                        
            1. Gå till trappuppgången.     2. Gå till kiosken.     3. Prata med en elev.
                """)
        korridor_väg = input("""
Ditt val -->""")
        rensa()

        if korridor_väg == "1":
            slowprint("""
Du återvänder till trappuppgången och ser den skalliga mannen stirra på dig.
Han följer dig med blicken medan du fortsätter ner i trappan till våning två.
""")
            from Våning_2 import troll_våning_2
            klass.levande = troll_våning_2()
            if klass.levande == False:
                return klass.levande
    
        elif korridor_väg == "2":
            slowprint("""
Du går fram till kiosken där den vanliga mattanten sitter och läser en tidning.
Du går fram och kikar på priserna, men får snabbt PTSD från alla tidigare köp.
Du väljer därför att inte köpa något.
""")
        elif korridor_väg == "3":
            if klassval == "1":
                slowprint("""
Du bestämmer dig för att försökra prata med en elev i korridoren,
men när du öppnar din mun inser du att du har glömt hur man pratar.
Du går därifrån skamset.
""")
            elif klassval == "2":
                slowprint("""
Du närmar dig en elev som ser ut att vara trevlig,
men så fort han känner stanken av dig springer han iväg skrikandes.
""")
            elif klassval == "3":
                slowprint("""
Du närmar dig en elevn, men vänder snabbt om igen 
då du inser att ingen vill ha med dig att göra eftersom du går sam.
""")
        else:
            slowprint("Välj ett av alternativen!")
    return klass.levande
from Lång_korridor import *
from spelaren import *
from ryggsäck import *
from Bibliotek import *
from slowtypeshii import slowprint
from rensa import *
from levelup import *

def main():
    klass.exp += 10000
    kant = 100 * (1.1**klass.lvl)
    while kant <= klass.exp:
        klass.exp -= kant
        levelup()
        kant = 100 * (1.1**klass.lvl)
    while klass.levande == True:
        slowprint("""
                                Vill du gå in i entrén?
                                
                                1. Ja           2. Nej
""")
        välkommen = input("""
Ditt val -->""")
        rensa()

        if välkommen == "1":
            slowprint("""
Du hör en röst med dansk brytning från receptionen.
"Hej lilla vännen, vad går du för program?"
                      
Du ignorerar rösten och går vidare in i skolan

"Hallå!! Svara mig!!"
                      
Du svarar inte
""")
        else:
            slowprint("""
Du tvekar vid entrén, men till slut puttar en okänd kraft dig framåt genom dörren.
""")

        slowprint("""
Framför dig finns det två vägar att välja mellan. 
Du kan gå rakt fram för att gå in i Biblioteket eller till vänster där du inte vet vad som väntar.
""")

        slowprint("""
                            Vilken väg väljer du?
                                
                        1. Vänster       2. Rakt fram
""")
        första_väg = input("""
Ditt val -->""")
        rensa()

        if första_väg == "2":
            slowprint("""
Du inser att biblioteket är under renovering och går ledsamt ut ur entrén igen.
""")
        elif första_väg == "1":
            slowprint("""
Du ser en lång korridor framför dig. 
Till vänster finner du en trappuppgång och till höger finner du en kiosk.
Det finns elever runt om i hela korridoren.
""")
            klass.levande = lång_korridoren()
            if klass.levande == False:
                return klass.levande
        else:
            slowprint("""
Välj ett av alternativen annars fungerar inte spelet.😡😡😡
""")


main()
slowprint("""
Du dog och nu är spelet slut""")
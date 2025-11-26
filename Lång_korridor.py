from spelaren import *


korridor_väg = (input(
"""Du ser en lång korridor framför dig. 
Till vänster finner du en trappuppgång och till höger finner du en kiosk.
Det finns elever runt om i hela korridoren.
                
                                    Vad vill du göra?
                        
            1. Gå till trappuppgången.     2. Gå till kiosken.     3. Prata med en elev.
                """))

if korridor_väg == "1":
    print("""
Du går fram till trappuppgången och ser en skallig man vars otäcka leende tvingar dig till att prata med honom.
""")
    if klassval == "1":
        print("""
"Jaha. Du är korkad du alltså.
Det skulle ej förvåna mig om du inte begriper vad jag säger just nu.
Du borde vandra nedåt." säger den skalliga mannen med en nedlåtande ton.
              
Du gör som han säger och börjar vandra nedåt till våning två.
""")
    elif klassval == "2":
        print("""
Den skalliga mannen blir genast glad när han inser att du går teknik.
"Åh, vad kul! Du går teknik jag kan känna det på lukten.
Eftersom du är så smart och duktig så borde du vandra uppåt." säger den skalliga mannen glatt
              
Du gör som han säger och börjar vandra uppåt till våning fyra.
""")
    elif klassval == "3":
        sam_trappa = input("""
"Ah, du är en sån där alltså. En samelev som tror du är huvudpersonen.
Gör vad du vill jag kunde inte bry mig mindre." säger den skalliga mannen obrytt
                           
                           Vill du gå upp eller ner?
                           
                           1. Upp        2. Ner
                    """)
        if sam_trappa == "1":
            print("det kommer coolare saker här senare")
        elif sam_trappa == "2":
            print("det kommer coolare saker här senare")
        else:
            print("det kommer coolare saker här senare")
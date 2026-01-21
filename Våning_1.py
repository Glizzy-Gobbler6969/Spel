from ryggsäck import *
from spelaren import *
from troll import *
from Lång_korridor import lång_korridoren_återvänd
from fälla import *
from kistrum import *
from slowtypeshii import *
from rensa import *
from Våning_0 import *

import random as randit

antal_rum_våning1 = 0

def våning_1():
    global antal_rum_våning1
    slowprint("""
Du tar dig ner till våning ett.
Det är mörkt, kallt och fuktigt, och du ser knappt någonting.
Du inser snabbt att du måste fortsätta framåt för att komma vidare.
                        
                            Vad vill du göra?
                            
            1. Återväd till våning tre      2. Fortsätt framåt
""")
    entre_v1 = input("""
Ditt val -->""")
    rensa()
    if entre_v1 == "1":
        lång_korridoren_återvänd()
    elif entre_v1 == "2":
        while antal_rum_våning1 < 10:
            slump_rum = randit.randint(1,5)
            if slump_rum == 1:
                slowprint("""
Du rör dig framåt på våning ett och stöter plötsligt på ett troll!

                    Väljer du att fly eller slåss?
                    
            1. Fly till våning tre      2. Slåss mot trollet
""")
                troll_v1 = input("""
Ditt val -->""")
                rensa()
                if troll_v1 == "1":
                    lång_korridoren_återvänd()
                elif troll_v1 == "2":
                    klass.levande = singelstrid(None)
                    if klass.levande == False:
                        return klass.levande
                    antal_rum_våning1 += 1
                    slowprint(f"""
Du har klarat {antal_rum_våning1}/10 rum.
""")
                    slowprint("""
Vill du fortsätta framåt eller återvända till våning tre?
                                        
            1. Återvänd till våning tre      2. Fortsätt framåt
""")
                    efter_troll = input("""
Ditt val -->""")
                    rensa()
                    if efter_troll == "1":
                        lång_korridoren_återvänd()
                    elif efter_troll == "2":
                        print("""
Du väljer att fortsätta framåt efter att ha besegrat trollet.
""")                                        
            elif slump_rum == 2:
                fälla()

                antal_rum_våning1 += 1
                print(f"""
Du har klarat {antal_rum_våning1}/10 rum.""")
                
                slowprint("""
Vill du fortsätta framåt eller återvända till våning tre?

            1. Återvänd till våning tre      2. Fortsätt framåt
""")
                efter_fälla = input("""
Ditt val -->""")
                rensa()
                if efter_fälla == "1":
                    lång_korridoren_återvänd()
                elif efter_fälla == "2":
                    slowprint("""
Du väljer att fortsätta framåt även om du blev förnedrad av fällan.
""")
            elif slump_rum == 3:
                slowprint("""
Du traskar vidare genom våning ett beredd på att möta det värsta.
Till din förvånan var det inget som väntade på dig i detta rum.
""")
                antal_rum_våning1 += 1
                slowprint(f"""
Du har klarat {antal_rum_våning1}/10 rum.
""")                                 
                slowprint("""
                                Vad vill du göra?
                                    
            1. Återvänd till våning tre      2. Fortsätt framåt
""")
                ofarligt_rum = input("""
Ditt val -->""")
                rensa()

                if ofarligt_rum == "1":
                    lång_korridoren_återvänd()
                elif ofarligt_rum == "2":
                    slowprint("""
Du trallar glatt vidare genom våning ett.
""")
            elif slump_rum == 4:
                kistrum()
                antal_rum_våning1 += 1
                slowprint(f"""
Du har klarat {antal_rum_våning1}/10 rum.
""")
                slowprint("""
                        Vad vill du göra?
                                    
            1. Återvänd till våning tre      2. Fortsätt framåt
""")
                efter_kistrum = input("""
Ditt val -->""")
                rensa()

                if efter_kistrum == "1":
                    lång_korridoren_återvänd()
                elif efter_kistrum == "2":
                    slowprint("""
Du fortsätter vidare genom våning ett efter att ha öppnat den lebbiga kistan.
""")
        våning_0()
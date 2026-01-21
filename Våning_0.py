from kistrum import *
from ryggsäck import *
from spelaren import *
from troll import *
from slowtypeshii import *
from rensa import *
import random as randit
from trollhättan import *
from fälla import *
rätt_dörr_w = False
rätt_dörr_v = 1
rätt_dörr_r = randit.randint(1,5)




def våning_0():
    slowprint("""
Efter 10 svåra rum på våning ett har du äntligen nått bottenvåningen.
När du ser dig omkring ser du fem dörrar framför dig.
""")
    
    slowprint("""
            Vill du fortsätta på våning noll eller återvända?
                            
        1. Fortsätt framåt på våning noll      2. Återvänd till våning tre
""")
    botten_våning = input("""
Ditt val -->""")
    rensa()
    if botten_våning == "2":
            from Lång_korridor import lång_korridoren_återvänd
            lång_korridoren_återvänd()
    elif botten_våning == "1":
        while rätt_dörr_w == False:
            välj_dörr = input("""
Välj en dörr att öppna (1-5)
Ditt val -->""")
            rensa()
            
            öppnade_dörrar = [""]
            öppnade_dörrar.append(välj_dörr)
            slowprint(f"""
Öppnade dörrar: {öppnade_dörrar}
""")
            
            if välj_dörr == str(rätt_dörr_r):
                slowprint(f"""
Du öppnar dörren till Trollhättan aka HELVETET!!!
""")
                klass.levande = trollhättan()
                if klass.levande == False:
                    return klass.levande
            else:
                fel_dörr = randit.randint(1,4)

                if fel_dörr == 1:
                    slowprint("""
Du valde fel dörr och stöter på ett troll!
""")
                    klass.levande = singelstrid(None)
                    if klass.levande == False:
                        return klass.levande

                elif fel_dörr == 2:
                    slowprint("""
Du öppnar fel dörr...
""")
                    fälla()
                         
                elif fel_dörr == 3:
                    slowprint("""
Du öppnar fel dörr...
""")
                    kistrum()

                elif fel_dörr == 4:
                    slowprint("""
Du öppnar fel dörr, men innuti rummet är det tomt.
""")
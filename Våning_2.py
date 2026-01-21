from spelaren import *
from ryggsäck import *
from troll import *
from Våning_1 import *
from slowtypeshii import *
from rensa import *

antal_dödade_fiender_bygg = 0
våning2_inte_klarad = True
korV2_val = 0
def troll_våning_2():
    global antal_dödade_fiender_bygg, våning2_inte_klarad, korV2_val
    from Lång_korridor import lång_korridoren_återvänd
    if antal_dödade_fiender_bygg != 5:
        while våning2_inte_klarad == True:
            if antal_dödade_fiender_bygg == 0:
                slowprint("""
Du ser dig omkring på våning två där du en gång i tiden haft alla dina lektioner,
men nu mer är allt dystert och du känner knappt igen vart du är.
Plötsligt ser du ett troll dyka upp framför dig.
                                    
                                        Vad vill du göra?
                            
                        1. Fly upp till våning tre   2. Slåss mot trollet
""")
                första_troll = input("""
Ditt val -->""")
                rensa()
                if första_troll == "1":
                    return lång_korridoren_återvänd()
                elif första_troll == "2":
                    slowprint("""
Du väljer att gå fram till trollet och är redo för att slåss.
Trollet får till slut syn på dig och höjer sin klubba för att gå till attack.""")
                    klass.levande = singelstrid("Monkel Tronkel Jr")
                    if klass.levande == False:
                        return klass.levande
                    antal_dödade_fiender_bygg += 1
                    slowprint("""
Du har dödat 1/5 troll
""")
            elif antal_dödade_fiender_bygg == 1:
                slowprint("""
Du stannar och ser dig omkring i korridoren, men det är för mycket dimma för att se någonting.

                                    Vad väljer du?
                                    
                    1. Fly till våning tre      2. Fortsätt framåt
                          """)
                andra_troll = input("""
Ditt val -->""")
                rensa()
                if andra_troll == "1":
                    from Lång_korridor import lång_korridoren_återvänd
                    return lång_korridoren_återvänd()
                elif andra_troll == "2":
                    slowprint("""
Ur dimman kommer det plötsligt ett troll!
Nu finns det ingen återvändo.""")
                    klass.levande = singelstrid("Blorg den korte")
                    if klass.levande == False:
                        return klass.levande
                    antal_dödade_fiender_bygg +=1
                    slowprint("""
Du har dödat 2/5 troll.""")
            elif antal_dödade_fiender_bygg == 2:
                slowprint("""
Du fortsätter fram i korridoren en bit till.
Det känns som att korridoren är oändlig, 
men till slut får du syn på ytterligare ett troll
                    
                                Vad väljer du?
                                    
                    1. Fly till våning tre      2. Slåss mot trollet
""")
                tredje_troll = input("""
Ditt val -->""")
                rensa()
                if tredje_troll == "1":
                    from Lång_korridor import lång_korridoren_återvänd
                    return lång_korridoren_återvänd()
                elif tredje_troll == "2":
                    slowprint("""
Du närmar dig trollet, som du strax ser är skadat.
Även om du saknar en normalstor hjärna, så känner du någon form av sympati.
                        
                            Vad väljer du?
                        
                1. Döda trollet   2. Hjälpa trollet
""")
                    hjälpa_troll = input("""
Ditt val -->""")
                    rensa()
                    
                    if hjälpa_troll == "1":
                        slowprint("""
Du håller dig till dina hjärndöda aktiviteter och därmed dödar trollet.
Du har dödat 3/5 troll""")
                        antal_dödade_fiender_bygg += 1
                    elif hjälpa_troll == "2":
                        slowprint("""
Du väljer att försöka hjälpa trollet,
men med din inkompetens råkar du istället ha ihjäl det stackars trollet.
Du har dödat 3/5 troll.""")
                        antal_dödade_fiender_bygg +=1
            elif antal_dödade_fiender_bygg == 3:
                slowprint("""
Du fortsätter fram i korridoren och är nästan säker på vad som kommer ske härnäst.
Mycket riktigt var dina misstankar rätt. Ett troll dycket plötsligt upp.
                                    
                            Vad väljer du?
                                    
            1. Fly upp till våning tre.    2. slåss mot trollet.
""")
                fjärde_troll = input("""
Ditt val -->""")
                rensa()
                if fjärde_troll == "1":
                    from Lång_korridor import lång_korridoren_återvänd
                    return lång_korridoren_återvänd()
                elif fjärde_troll == "2":
                    slowprint("""
Du väljer att gå fram till trollet och startar en strid.
""")
                    klass.levande = singelstrid("Gorg den fete")
                    if klass.levande == False:
                        return klass.levande
                    antal_dödade_fiender_bygg += 1
                    slowprint("""
Du har dödat 4/5 troll.""")
            elif antal_dödade_fiender_bygg == 4:
                slowprint("""
Efter fyra hela strider mot troll känner du dig trött,
men du väljer att fortsätta fram i korridoren i alla fall.
Till slut får du syn på det sista trollet i den långa korridoren.
                                    
                        Vad väljer du?
                                    
            1. Fly upp till våning tre  2. Slåss mot trollet
""")
                sista_troll = input("""
Ditt val -->""")
                rensa()
                if sista_troll == "1":
                    return lång_korridoren_återvänd()
                elif sista_troll == "2":
                    slowprint("""
Helt slut i armarna fortsätter du framåt till trollet som är gigantiskt.
Han får syn på dig och går till attack.
""")
                    klass.levande = singelstrid("Throg den smarte")
                    if klass.levande == False:
                        return klass.levande
                    
                    antal_dödade_fiender_bygg += 1
                    slowprint("""
Du har nu dödat 5/5 troll och har utrotat allt ont på våning två.
Du återvänder upp till våning tre igen,
men nu kan du även ta dig till våning ett.
""")
                    våning2_inte_klarad = False
                    return lång_korridoren_återvänd()
    else:
        return våning_1()
korridor_väg = int(input(
"""Du ser en lång korridor framför dig. 
Till vänster finner du en trappuppgång och till höger finner du en kiosk.
Det finns elever runt om i hela korridoren.
                
                                    Vad vill du göra?
                        
                1. Gå till vänster.     2. Gå till kiosken.     3. Prata med en elev.
                """))

if korridor_väg == 1:
    print("""
Du går fram till trappuppgången och ser en skallig man vars otäcka leende tvingar dig till att prata med honom.
""")
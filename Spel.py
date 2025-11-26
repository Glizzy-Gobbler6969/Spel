välkommen = (input("""
                            Hej, och välkommen till Åva!
                            Vill du gå in i entrén?
                      
                            1. Ja           2. Nej
                """))

if välkommen == "1":
    print("""
                            Du hör en röst med dansk brytning från receptionen.
                            "Hej lilla vännen, vad går du för program?"
          """)
else:
    print("Jahopp")

from spelaren import *

print("""
Framför dig finns det två vägar att välja mellan. 
Du kan gå rakt fram för att gå in i Biblioteket eller till vänster där du inte vet vad som väntar.""")

första_väg = (input("""
                            Vilken väg väljer du?
                       
                       1. Vänster       2. Rakt fram
                       """))

if första_väg == "2":
    from Bibliotek import *
else:
    print("babbaa")
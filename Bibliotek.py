from spelaren import *

if klassval == 1:
    klass.hp -= 5
    print(f"""
          Du har aldrig varit i ett bibliotek förut och vet därför inte hur man ska bete sig.
          Du känner rädsla på grund av denna främmande miljö och därför skriker efter hjälp.
          Det slutar med att biliotekarien smäller till dig i huvudet. -5HP
                
          Resterande HP {klass.hp}/{klass.maxhp}""")
elif klassval == 2:
    klass.int += 5
    print(f"""Du som teknikare känner dig hemma i denna miljö och din stank tvingar iväg alla andra från bilioteket.
          Du väljer att börja läsa diverse böcker och därmed känner din hjärna pulsera. +5int
                
          Din nya int är {klass.int}""")
elif klassval == 3:
    print("""Du känner dig smart som för första gången klivit in i ett biliotek, även om du hatar att läsa.
          Alla ger dig konstiga blickar och du känner dig utstirrad och därför återvänder ut.""")
else:
    print("bbabbababa")
class spelaren():
    def __init__(self,atk,hp,int,maxhp):
        self.atk = atk
        self.hp = hp
        self.int = int
        self.maxhp = maxhp

klas = False

while not klas:
    klassval = int(input("""
                        1. Bygg  

                        2. Teknik

                        3. Samhäll
    Ditt val---> """))

    if klassval == 1:
        klass = spelaren(21,21,0,21)
        print(f"Random Dansk: Du går bygg och har därmed statsen: {klass.atk} atk, {klass.hp} hp och {klass.int} int")
        klas = True
        print("""
Du ser dig omkring, men du är lite för korkad för att lista ut vart du bör ta vägen.""")

    elif klassval == 2:
        klass = spelaren(5,12,21,12)
        print(f"Random Dansk: Det var alltså du som lukta, du har statsen: {klass.atk} atk, {klass.hp} hp och {klass.int} int")
        klas = True
        print("""
Du känner hur stanken av dig själv sticker i näsan, men detta kanske kan vara ett bra vapen mot monster.""")
    elif klassval == 3:
        klass = spelaren(14,14,14,14)
        print(f"Random Dansk: Du går nu sam med statsen: {klass.atk} atk, {klass.hp} hp och {klass.int} int")
        klas = True
        print("""
Här står du vid receptionen och tror att du är den smartaste i denna skola, men detta kunde inte vara längre ifrån sanningen.""")
    else:
        print("System: Välj ett av alternativen tack :)")






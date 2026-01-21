from spelaren import *
from slowtypeshii import *
import random as randit

def fälla():
    slump_fälla = randit.randint(1,3)
    if slump_fälla == 1:
        slowprint("""
Du kliver in i nästa rum, men blir mött av en stank.
Du märker nu att denna stank kommer från en farlig gasfälla!
""")
        klass.hp -= 5
        slowprint(f"""
Du förlorar 5 hp av den stinkande fällan och nu har du {klass.hp}/{klass.mhp} hp kvar.
""")
    elif slump_fälla == 2:
        slowprint("""
Du tar dig in i nästa rum och känner hur golvet under dig börjar skaka.
Innan du hinner reagera faller du ner i en grop som blivit skapad i golvet!
Till slut tar du dig upp ur gropen, men du är skadad.
""")
        klass.hp -= 15
        slowprint(f"""
Du förlorar 5hp och nu har du bara {klass.hp}/{klass.mhp} kvar
""")
    elif slump_fälla == 3:
        slowprint("""
Du fortsätter genom nästa rum, men snabbt inser du att rummet är täckt med trollslem.
Du inser att det inte finns någon återvändo, så du traskar igenom slemmet.
När du kommer ut ur rummet är du täckt i slem och du är svagare än innan.
""")
        klass.base_atk -= 5
        slowprint(f"""
Din styrka gick från {klass.base_atk+5} till {klass.base_atk}
""")
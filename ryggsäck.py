ryggsäck=[]
from slowtypeshii import *

def öppna_säckfan():
    if len(ryggsäck)>0:
        for item in ryggsäck:
            slowprint(item)
    else:
        slowprint("Det är tomt här...")

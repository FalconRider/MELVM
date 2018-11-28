# My Ethereum Like Virtual Machine
# MELVM   Paul J. Gitschner 2018    100 Transaction Module
#       ver 20181108001
# ---------------------------------------------------------
#GOALS
# make up 10 or 100 transactions
# Make a pickle file with the info



import pickle
import hashlib
import random

ta = ["a"]
ta[0] =9999

#-------------------------------------------------------------------

def header():
    print(" ********************************************************")
    print(" *******   Welcome to MELVM VM     **********************")
    print(" ************************************* 100 transactions *")
    print()

print()
print()
#-------------------------------------------hash sha256

def hashSha256(thekey):
    global thesignature
    thesignature = hashlib.sha256(thekey.encode("utf8")).hexdigest()
    

#----------------------------Main-------LOOP----------------

header()

for i in range(1, 100):
    
    theAdd  = "MVM5b65712d56"
    theSig  = "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce"
    theAmt  = random.randint(200, 10000)
    theRec  = random.randint(1000000000, 2000000000)
    
    theFix  = "MVM"
    theRec = theFix + str(theRec) 
    
    print()
    itn = str(i) +"MTN" + str(i)
    
    print ("transaction      ",itn)
    
    print("  FROM  ", theAdd)
    print("  hidden  ", theSig)
    print("  TO    ", theRec)
    print("  valid account name length is 13, this is   ",len(theRec))
    print ("  AMOUNT", theAmt)
    #print()
    print()
    #hold  = input('Hit Enter')
    ta.append(itn)
    ta.append(theAdd)
    ta.append(theSig)
    ta.append(theRec)
    ta.append(theAmt)

hold  = input('Hit Enter')

print ('Creating a pickle file copy as mvmtafile')

print(ta)
print ()
hold  = input('Hit Enter')
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx pickle array
f = open('mvmtafile', 'wb')
pickle.dump(ta,f)
f.close()


print()
header()
hold = input("Hit Return to  end: ")
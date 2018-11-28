# My Ethereum Like Virtual Machine
# MELVM   Paul J. Gitschner 2018    Signature Comtrol Module
#       ver 20181106002
# ---------------------------------------------------------

# Input address and signature
# reecalc and compare
# print both
# pass or fail

import pickle
import hashlib

#-------------------------------------------------------------------

def header():
    print(" ********************************************************")
    print(" *******   Welcome to MELVM VM     **********************")
    print(" ********************************************************")
    print()

#-------------------------------------------hash sha256

def hashSha256(thekey):
    global thesignature
    thesignature = hashlib.sha256(thekey.encode("utf8")).hexdigest()
    

#----------------------------Main-------LOOP----------------
header()
#thekey  = input('Enter keyword or string for Account Generation: ')
theAdd  = input('Enter Address including Prefix: ')
theSig  = input('Enter Signature')

print(theAdd)
print(theSig)
theCut=(theAdd[3:13])
print (theCut)
hashSha256(theSig)
print (thesignature)
#cut this to 10 digits
theTen = (thesignature[0:10])
print (theTen)

hold  = input('Hit Enter')
if theTen == theCut:
    print("pass")
else: 
    print("fail")
    
hold  = input('Hit Enter')  
    
    
    
    
#*****************************************************
hashSha256(thekey)

recover = thekey
thekey = thesignature

print ()
thefinalsig = thesignature
hashSha256(thekey)
#----------------------------------- slice digits
thecutkey = thesignature
ccc = thecutkey 
jjj = (ccc[0:10])

# ---------------------------------- add prefix 
cccx = ("MVM"+ jjj)

#-------------------------------------pickle
Wallet321 = ["a", "b",]
Wallet321[0] = cccx
Wallet321[1] = thekey

print ('Creating a pickle file copy as Wallet321.pickle')
print()
print("  -----  address             ---        signature ---- ")
print(Wallet321)
print ()

f = open('Wallet321.pickle', 'wb')
pickle.dump(Wallet321,f)
f.close()

print()
print("Your Recovery Keyword or string -not in the file-  is   ", recover )
print ('                Remember your keywords')

print(" *******Write it down somewhere ********************")
print()
print()
header()
hold = input("Hit Return to  end: ")
# My Ethereum Like Virtual Machine
# MELVM   Paul J. Gitschner 2018    Wallet and Signature Module
#       ver 20181106001
# ---------------------------------------------------------
# Generates FORMATED Address and sha256 based Signature based on single Keyword
# Makes picklefile of only Address and Sig for cutnpaste ease 
# Addresses have MVM prefix plus 10 hex digits
# Note on pickle file entries take off trailng q's



import pickle
import hashlib

#-------------------------------------------------------------------

def header():
    print(" ********************************************************")
    print(" *******   MELVM Wallet Generator  **********************")
    print(" ********************************************************")
    print()

#-------------------------------------------hash sha256

def hashSha256(thekey):
    global thesignature
    thesignature = hashlib.sha256(thekey.encode("utf8")).hexdigest()
    

#----------------------------Main-------LOOP----------------
header()
thekey  = input('Enter keyword or string for Account Generation: ')

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
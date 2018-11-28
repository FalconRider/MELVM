# My Ethereum Like Virtual Machine
# MELVM   Paul J. Gitschner 2018    100 Transaction READER  Module
#       ver 20181110001
# ---------------------------------------------------------
#GOALS
# make up 10 or 100 transactions
# Make a pickle file with the info
#-------------next
#read above file parse


import pickle
import hashlib
import random

ta = ["a"]
ta[0] =9999

#-------------------------------------------------------------------

def header():
    print(" ********************************************************")
    print(" *******   Welcome to MELVM VM     **********************")
    print(" *******************100 transactions reader *")
    print()

print()
print()
#-------------------------------------------hash sha256

def hashSha256(thekey):
    global thesignature
    #thesignature = 'hashlib.sha256(thekey.encode("utf8")).hexdigest()
    

#----------------------------Main-------LOOP----------------
header
f = open('mvmtafile', 'rb')
tarray = pickle.load(f) 
f.close()
header()
#----------------this print whole state file
tarray
#hold  = input('Hit  Enter')

#-----------------------------------------------------------------
#print (tarray)

(sstart) = input('Hit what tx number Enter')


# range controls needed

sstart = int(sstart) 
# need modulus    sst
sstart = (sstart * 5)+ 1

#---------------------------------
print("Transaction No    ",tarray[sstart])
print("From Address      ",tarray[sstart+1])
print("Signature   ",tarray[sstart+2])
print("To Address        ",tarray[sstart+3])
print("Tranaction VALUE  ",tarray[sstart+4])
hold  = input('Hit  Enter')


print()
header()
hold = input("Hit Return to  end: ")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compare JISCMAIL list to collaboration list
===========================================

  Assumes python path includes 01-Code.

"""

import os
import pandas as pnds

import Member as Mmbr

##! Start:
print(" ========  compareJISCMAIL2CollaborationLst start  ========")


##! --------  Read membership list and mailing list
Block = 1
print()
print(" ----> Block:", Block, " initialise.")

LhARAPATH = os.getenv('LhARAPATH')
fileDIR  = os.path.join(LhARAPATH, '11-CollaborationList')
print("     ----> Directory to get files from:", fileDIR)

try:
    filepath     = os.path.join(LhARAPATH, '99-Scratch')
except:
    print("     ----> Failed to create path to scratch directory!", \
          "  Execution terminated.")
    raise Exception

##! Load:
print("========  Load files  ========")
fileLIST = sorted(os.listdir(fileDIR))
nMembers = 0
for file in fileLIST:
    if file.find('.csv') <= 0:
        pass
    else:
        filePATH = os.path.join(fileDIR, file)
        newMembers = Mmbr.Member.parseMemberDatabase(filePATH)
        nMembers  += newMembers
        
print("     ----> OK!", nMembers, " members read.")

filename  = os.path.join(LhARAPATH, \
                         '12-CCAP-LhARA-JISCMAIL/new-JISCMAIL-lst.csv')
JISCMlLst = pnds.read_csv(filename)
print("     ----> OK!", JISCMlLst.shape[0], " email addresses found.")
print(" <---- Initialisation done.")

##! --------  Clean and sort members
Block += 1
print()
print(" ----> Block:", Block, " sort members by name.")
nClnd  = Mmbr.Member.cleanMemberDatabase()
print("     ----> Cleaned", nClnd, "members.")
Result = Mmbr.Member.sortAlphabeticalByName()
print("     ---->", Result)
print(" <--- Cleaning and sorting done.")

##! Members not in email list
Block += 1
print()
JISCMlLst["email"] = JISCMlLst["email"].apply(str.lower)
print(" ----> Block:", Block, \
      " search for members whose emails are not in list.")
iCnt = 0
for iMmbr in Mmbr.Member.getAlphaMemberSort():
    if iMmbr.getemail().lower() in JISCMlLst.values:
        pass
    else:
        print("     ----> Member", \
              iMmbr.getSurname(), ", ", iMmbr.getInitials(), \
              " email:", iMmbr.getemail(), \
              " not in JISCMail list.")
        iCnt += 1
if iCnt == 0:
    print("     ----> All emails in JISCMAIL list correspond to members")
        
print(" <---- List of emails not in membership list, done.")

##! Emails not in list of members
Block += 1
print()
iCnt = 0
print(" ----> Block:", Block, " people in email list who are not members")
for iRow in JISCMlLst.itertuples(index = True):
    JISCemail = getattr(iRow, "email").lower()
    foundMEMBER = False
    for iMmbr in Mmbr.Member.getAlphaMemberSort():
        Mmbremail = iMmbr.getemail().lower()
        if JISCemail == Mmbremail:
            foundMEMBER = True
    
    if not foundMEMBER:
        print("     ----> JISCMAIL entry", JISCemail, \
              " not a member of LhARA.")
        iCnt += 1
if iCnt == 0:
    print("     ----> All members are in JISCMAIL list")

print(" <--- List of members not in JISCMaill list, done.")

##! Complete:
print()
print("========  Member: tests complete  ========")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Get list of IB members and pair them to Institute list
======================================================

  Assumes python path includes 01-Code.

"""

import os
import pandas as pnds

import Member    as Mmbr
import Institute as Instt

##! Start:
print(" ========  Institute Board checks  ========")


##! Read membership list and mailing list
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

##! Clean and sort members
Block += 1
print()
print(" ----> Block:", Block, " sort members by name.")
nClnd  = Mmbr.Member.cleanMemberDatabase()
print("     ----> Cleaned", nClnd, "members.")
Result = Mmbr.Member.sortAlphabeticalByName()
print("     ---->", Result)
print(" <--- Cleaning and sorting done.")

##! Emails not in membership list
Block += 1
print()
print(" ----> Block:", Block, " print members attending IB.")
IBmmbr = []
for iMmbr in Mmbr.Member.getAlphaMemberSort():
    if iMmbr.getInstBrd():
        print("        ---->", \
              iMmbr.getSurname(), ", ", iMmbr.getInitials(), \
              " organisation:", iMmbr.getOrganisation().getName())
        IBmmbr.append(iMmbr)
print(" <--- IB attendees list done.")

##! Members not in email list
Block += 1
print()
print(" ----> Block:", Block, " IB members by institute.")
Result = Instt.Institute.sortAlphabeticalByName()
for iInst in Instt.Institute.getAlphaInstituteSort():
    iCnt = 0
    print("     ----> Institute:", iInst.getName())
    for iMmbr in IBmmbr:
        if iMmbr.getOrganisation().getName() == iInst.getName():
            print("         ----> iMmbr:", \
                   iMmbr.getSurname(), iMmbr.getInitials())
            iCnt += 1
    if iCnt == 0:
        print("         ----> No institute board representative!")
print(" <--- IB members by institute done.")


##! Complete:
print()
print("========  Member: tests complete  ========")

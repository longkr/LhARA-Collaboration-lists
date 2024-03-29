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
filename  = os.path.join(LhARAPATH, \
                         '11-CollaborationList/new-spread.csv')
print("     ----> Member database file name:", filename)
nMbrs = Mmbr.Member.parseMemberDatabase(filename)
print("     ----> OK!", nMbrs, " members read.")
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
    print("     ----> Institute:", iInst.getName())
    for iMmbr in IBmmbr:
        if iMmbr.getOrganisation().getName() == iInst.getName():
            print("         ----> iMmbr:", \
                   iMmbr.getSurname(), iMmbr.getInitials())
print(" <--- IB members by institute done.")


##! Complete:
print()
print("========  Member: tests complete  ========")

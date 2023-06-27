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
print(" ----> Block:", Block, " search for emails not in membership list.")
for iMmbr in Mmbr.Member.getAlphaMemberSort():
    JISCMlLst["email"] = JISCMlLst["email"].apply(str.lower)
    if iMmbr.getemail().lower() in JISCMlLst.values:
        pass
    else:
        print("        ----> Member", \
              iMmbr.getSurname(), ", ", iMmbr.getInitials(),\
              " not in JISCMail list.")
print(" <--- List of emails not in membership list, done.")

##! Members not in email list
Block += 1
print()
print(" ----> Block:", Block, " search for members not in email list.")
for iRow in JISCMlLst.itertuples(index = True):
    JISCemail = getattr(iRow, "email")
    Mmbremail = getattr(Mmbr.Member.getAlphaMemberSort(), "_email", \
                        JISCemail)
    if JISCemail != Mmbremail:
        print("        ----> JISCMAIL entry", getattr(iRow, "email"), \
              " not a member of LhARA.")
print(" <--- List of members not in JISCMaill list, done.")


##! Complete:
print()
print("========  Member: tests complete  ========")

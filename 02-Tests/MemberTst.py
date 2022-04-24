#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for "Member" class
=====================================

  Assumes python path includes 01-Code.

  Script starts by testing built in methods.

"""

import os

import Member as Mmbr

##! Start:
print("========  Member: tests start  ========")


##! Check built-in methods:
MemberTest = 1
print()
print("MemberTest:", MemberTest, " check built-in methods.")

#.. __init__
print("    __init__:")
try:
    Inst = Mmbr.Member(1)
except:
    print('      ----> Correctly trapped bad argument at __init__.')
Inst = Mmbr.Member( \
                    "Prof", "John", "Smith", "J.A.", \
                    "J.A.Smith@gmail.com", \
                    "John A. Smith", \
                    "Funny Farm", \
                    "DOE", \
                    "666", \
                    True)
print('      ----> instance Inst created.')
print("    <---- __init__ done.")
#.. __repr__
print("    __repr__:")
print("      ---->", repr(Inst))
print("    <---- __repr__ done.")
#.. __str__
print("    __str__:")
print(Inst)
print("    <---- __str__ done.")


##! Check parsing and file handling methods:
MemberTest += 1
print()
print("MemberTest:", MemberTest, " check read of member list.")

LhARAPATH = os.getenv('LhARAPATH')
filename  = os.path.join(LhARAPATH, \
                         '11-CollaborationList/new-spread.csv')
print("     ----> Member database file name:", filename)
print("     ----> parseMemberDatabase load test")
try:
    Tst = Mmbr.Member.parseMemberDatabase()
except:
    print("        ----> Correctly trapped no filename.")
try:
    Tst = Mmbr.Member.parseMemberDatabase("Dummy")
except:
    print("        ----> Correctly trapped file does not exist.")
Tst = Mmbr.Member.parseMemberDatabase(filename)
print("        ----> OK!", Tst, " new members cretaed.")
print("    <---- Load test done")

##! Test sorting methods
MemberTest += 1
print()
print("MemberTest:", MemberTest, " check sorting methods.")

nClnd  = Mmbr.Member.cleanMemberDatabase()
print("     ----> Cleaned", nClnd, "members.")
Result = Mmbr.Member.sortAlphabeticalByName()
print("     ---->", Result)
Result = Mmbr.Member.sortAlphabeticalByName()
print("     ---->", Result)

##! Complete:
print()
print("========  Member: tests complete  ========")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for "List" class
===============================

  Assumes python path includes LhARA code.

  Script tests the methods written to create lists from the LhARA costing
  data structure.

"""

import os

import List as Lst
import Member as Mmbr


##! Start:
print("========  Initialisation complete  ========")

##! Start:
print(" ")
print("========  List: tests start  ========")

##! Check built-in methods:
ListTest = 1
print()
print("ListTest:", ListTest, " check built in base-class methods.")
#.. __init__
print("    List.__init__:")
try:
    Lst1 = Lst.List()
except:
    print('      ----> Successfully trapped no input exception`.')
try:
    Lst1 = Lst.List("OnlyOneArgument")
except:
    print('      ----> Successfully trapped "only one argument exception".')
LhARAPATH = os.getenv('LhARAPATH')
try:
    Lst1 = Lst.List("Test list", "BadPath", "TestList.csv")
except:
    print('      ----> Successfully trapped "bad path exception".')
NoWritePath = os.path.join(LhARAPATH, '98-NoWriteAccess')
try:    
    Lst1 = Lst.List("Test list", NoWritePath, "TestList.csv")
except:
    print('      ----> Successfully trapped "no write access exception".')
try:    
    Lst1 = Lst.List("Test list", LhARAPATH, "TestList.csv")
except:
    print('      ----> Failed to create List instance.')
    raise Exception
print('      ----> instance Lst1 created.')
print("    <---- __init__ done.")
#.. __repr__
print("    __repr__:")
print("      ---->", repr(Lst1))
print("    <---- __repr__ done.")
#.. __str__
print("    __str__:")
print(str(Lst1))
print("    <---- __str__ done.")

##! Check lists:

#.. Author list:
ListTest = 2
print()
filename  = os.path.join(LhARAPATH, \
                         '11-CollaborationList/new-spread.csv')
print("     ----> Member database file name:", filename)
MemberList = Mmbr.Member.parseMemberDatabase(filename)
print("ListTest:", ListTest, \
      " check alphabetic author list derived class methods.")
LhARAPATH = os.getenv('LhARAPATH')
try:
    filepath  = os.path.join(LhARAPATH, '99-Scratch')
    AlphaAuthLst = Lst.AlphaAuth(filepath, "01-AuthorList.tex")
except:
    print("     ----> Failed to create alphabetic author list list instance!",
          "  Execution terminated.")
    raise Exception
print("    ----> Alphabetic author list instance created.")
#.. __repr__
print("    __repr__:")
print("      ---->", repr(AlphaAuthLst))
print("    <---- __repr__ done.")
#.. __str__
print("    __str__:")
print(str(AlphaAuthLst))
print("    <---- __str__ done.")
#.. write list:
AlphaAuthLst.writeList()
print("    <---- List written.")

#.. Institute list:
ListTest += 1
print()
print("ListTest:", ListTest, \
      " check alphabetic institute list derived class methods.")
try:
    filepath  = os.path.join(LhARAPATH, '99-Scratch')
    AlphaInstLst = Lst.AlphaInst(filepath, "01-InstituteList.tex")
except:
    print(\
       "     ----> Failed to create alphabetic institute list list instance!",
       "  Execution terminated.")
    raise Exception
print("    ----> Alphabetic institute list instance created.")
#.. __repr__
print("    __repr__:")
print("      ---->", repr(AlphaInstLst))
print("    <---- __repr__ done.")
#.. __str__
print("    __str__:")
print(str(AlphaInstLst))
print("    <---- __str__ done.")
#.. write list:
AlphaInstLst.writeList()
print("    <---- List written.")


##! Complete:
print()
print("========  List: tests complete  ========")




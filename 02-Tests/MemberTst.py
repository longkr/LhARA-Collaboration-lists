#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for "Member" class
=====================================

  Assumes python path includes 01-Code.

  Script starts by testing built in methods.

"""

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

##! Complete:
print()
print("========  Member: tests complete  ========")

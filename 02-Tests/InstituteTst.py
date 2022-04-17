#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for "Institute" class
=====================================

  Assumes python path includes 01-Code.

  Script starts by testing built in methods.

"""

import Institute as Inst

##! Start:
print("========  Institute: tests start  ========")


##! Check built-in methods:
InstituteTest = 1
print()
print("InstituteTest:", InstituteTest, " check built-in methods.")
#.. __init__
print("    __init__:")
try:
    InstInst = Inst.Institute(1)
except:
    print('      ----> Correctly trapped bad argument at __init__.')
InstInst = Inst.Institute("Imperial College London",              \
                          "Exhibition Road, London, SW7 2AZ, UK", \
                          True)
print('      ----> instance InstInst created.')
print("    <---- __init__ done.")
#.. __repr__
print("    __repr__:")
print("      ---->", repr(InstInst))
print("    <---- __repr__ done.")
#.. __str__
print("    __str__:")
print(InstInst)
print("    <---- __str__ done.")

##! Complete:
print()
print("========  Institute: tests complete  ========")

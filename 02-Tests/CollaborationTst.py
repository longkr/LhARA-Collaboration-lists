#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for "Collaboration" class
=====================================

  Assumes python path includes 01-Code.

  Script starts by testing built in methods.

"""

import Collaboration as Cllbrtn

##! Start:
print("========  Collaboration: tests start  ========")


##! Check built-in methods:
CollaborationTest = 1
print()
print("CollaborationTest:", CollaborationTest, " check built-in methods.")
#.. __init__
print("    __init__:")
try:
    CllbrtnInst = Cllbrtn.Collaboration(1)
except:
    print('      ----> Correctly trapped bad argument at __init__.')
CllbrtnInst = Cllbrtn.Collaboration("LhARA", \
                                "Laser-hybrid Accelerator for Radiobiological Applications",   \
                                "Not yet implemented", \
                                "https://ccap.hep.ph.ic.ac.uk/trac/wiki/Research/DesignStudy", \
                                True)
print('      ----> instance CllbrtnInst created.')
print("    <---- __init__ done.")
#.. __repr__
print("    __repr__:")
print("      ---->", repr(CllbrtnInst))
print("    <---- __repr__ done.")
#.. __str__
print("    __str__:")
print(CllbrtnInst)
print("    <---- __str__ done.")

##! Complete:
print()
print("========  Collaboration: tests complete  ========")

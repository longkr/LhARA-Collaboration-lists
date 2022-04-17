#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for "Template" class
============================

  Assumes python path includes 01-Code.

  Script starts by testing built in methods.

"""

import Template as Tmplt

##! Start:
print("========  Template: tests start  ========")


##! Check built-in methods:
TemplateTest = 1
print()
print("TemplateTest:", TemplateTest, " check built-in methods.")
#.. __init__
print("    __init__:")
try:
    TmpltInst = Tmplt.XXXXXX(1)
except:
    print('      ----> Correctly trapped bad argument at __init__.')
TmpltInst = Tmplt.XXXXXX(True)
print('      ----> instance TmpltInst created.')
print("    <---- __init__ done.")
#.. __repr__
print("    __repr__:")
print("      ---->", repr(TmpltInst))
print("    <---- __repr__ done.")
#.. __str__
print("    __str__:")
print(TmpltInst)
print("    <---- __str__ done.")

##! Complete:
print()
print("========  Template: tests complete  ========")

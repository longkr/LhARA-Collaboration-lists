#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build collaboation lists:
=========================

  Assumes python path includes LhARA code.

"""

import os

import List      as Lst
import Institute as inst
import Member    as Mmbr


##! Start:
print("========  Initialise  ========")

LhARAPATH = os.getenv('LhARAPATH')
fileDIR  = os.path.join(LhARAPATH, '11-CollaborationList')
print("     ----> Directory to get files from:", fileDIR)

try:
    filepath     = os.path.join(LhARAPATH, '99-Scratch')
except:
    print("     ----> Failed to create alphabetic author list list instance!",
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

##! Make lists:
print("========  Make lists  ========")

AlphaAuthLst = Lst.AlphaAuth(filepath, "01-AuthorList.tex")
AlphaAuthLst.writeList()

AlphaInstLst = Lst.AlphaInst(filepath, "01-InstituteList.tex")
AlphaInstLst.writeList()

AuthByInst = Lst.AlphaInstAuth(filepath, "01-AuthorsByInstitute.tex")
AuthByInst.writeList()

##! Complete:
print("========  Complete  ========")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class List:
===========

  Collection of derived classes to generate lists.

  Class attributes:
  -----------------
  __Debug    : Boolean: set for debug print out
  __Instances: List of instances of list class


  Instance attributes:
  --------------------
    _Name      : (str) name of report
    _ListPath: Path to directory into which report file will be written
    _FileName  : List filename
    _Header    : List of header fields; initialised to [].  
                 Filled in derived classes.
    _Lines     : Lines of report; initialised to [].
                 Filled in derived classes.

    
  Methods:
  --------
  Built-in methods __new__, __repr__ and __str__.
      __init__: Creates instance and prints some parameters if __Debug is 
                True.
      __repr__: One liner with call.
      __str__ : Dump of constants.


  Processing methods:
      XXXXXX:  Creates ....


  I/o methods:
      XXXXXX: Creates ....


  Exceptions:
        NoListNameProvided: List instance call with invalid name

        NoOutputPathProvided: Path to directory for report is not provided

          NoFilenameProvided: No file name provided for report

           OutputPathInvalid: Path to directory for report invalid

   NoWriteAccessToOutputPath: Can not write into report directory



Created on Sun 17Apr22. Version history:
----------------------------------------
 1.0: 17Apr22: First implementation


@author: kennethlong
"""

import os
from datetime import date

import Member as Mmbr

"""
         -------->  Base "List" class  <--------
"""
class List:
    __Debug   = False
    __Instances = []

    
#--------  "Built-in methods":
    def __init__(self, _Name=None, _ListPath=None, _FileName=None):

        self._Name       = _Name
        self._ListPath   = _ListPath
        self._FileName   = _FileName
        self._Header     = []
        self._Lines      = []

        if _Name == None:
            raise NoListNameProvided( \
                  'No report name provided; execution termimated.')
        
        if _ListPath == None:
            raise NoOutputPathProvided( \
                  'No output path provided; execution termimated.')
        
        if _FileName   == None:
            raise NoFilenameProvided( \
                  'No CSV filename provided; execution termimated.')

        if not os.path.isdir(_ListPath):
            raise OutputPathInvalid('Output path:', _ListPath, ' invalid')

        if not os.access(_ListPath, os.W_OK):
            raise NoWriteAccessToOutputPath( \
                     'No write access to output path:', _ListPath)
            
        List.__Instances.append(self)

    def __repr__(self):
        return "List(ListName, PathToDirectory, ListFile)"

    def __str__(self):
        print(" List: Name: ", self._Name)
        if self.__Debug:
            print("     Output directory path: ", self._ListPath)
        else:
            dirname,  basename   = os.path.split(self._ListPath)
            print("     Output directory path: ", basename)
        print("     List file name: ", self._FileName)
        for i in range(len(self._Header)):
            print("     ---->", self._Header[i])
        for i in range(len(self._Lines)):
            print("     ---->", self._Lines[i])
        return "     <---- List __str__ done."


#--------  Processing methods

    
#--------  List:
        
    
#--------  I/o methods
    def writeList(self):
        ListFile = self._ListPath + "/" + self._FileName
        
        f = open(ListFile, "w")
        for Line in self._Header:
            f.write(Line + "\n")
        for Line in self._Lines:
            f.write(Line + "\n")
        f.close()


"""
Class AlphaAuth: -------->  "Alphabetic author list"; derived class  <--------
================

  

"""
class AlphaAuth(List):
    __Debug   = True

    def __init__(self, _ListPath, _FileName):

        """
           --------> Get started:
        """
        
        List.__init__(self, "Alphabetic authorlist", _ListPath, _FileName)

        self.getHeader()
        self.getAuthors()
        self.getInstitutes()

        
#--------  List elements:
    def getHeader(self):
        self._Header.append("\\vspace{0.75cm}")
        self._Header.append("\\begin{center}")
        self._Header.append( \
       "  {\\bf \\color{BlueViolet} The LhARA collaboration} \\\\")
        self._Header.append("  \\vspace{0.25cm}")
        self._Header.append( \
       "  {\\bf \\color{RedViolet} The author list is being compiled.} \\\\")
        self._Header.append( \
       "  {\\bf \\color{DarkGreen} Lead:} D. Kordopati \\\\")
        self._Header.append("  \\vspace{0.25cm}")

    def getAuthors(self):
        nAuth = 0
        if Mmbr.Member._AlphaMmbrSort == None:
            nClnd  = Mmbr.Member.cleanMemberDatabase()
            Result = Mmbr.Member.sortAlphabeticalByName()
            if AlphaAuth.__Debug:
                print(" AlphaAuth(List).getAuthors: Cleaned", nClnd, \
                      "members.")
                print(" AlphaAuth(List).getAuthors:", Result)
        nInst = 0
        gInst = []
        for iMmbr in Mmbr.Member._AlphaMmbrSort:
            nAuth += 1
            Author =  iMmbr.getInitials() + "~" + iMmbr.getSurname()
            
            Org = iMmbr._Organisation
            if not Org._Name in gInst:
                gInst.append(Org._Name)
            nInst = gInst.index(Org._Name) + 1

            if iMmbr._Affiliation != None:
                Affil = iMmbr._Affiliation
                if not Affil._Name in gInst:
                    gInst.append(Affil._Name)
                nAffil = gInst.index(Affil._Name) + 1
                Line = "  " + Author + "$^{" + \
                    str(nInst) + "," + str(nAffil) + \
                    "}$"
            else:
                Line = "  " + Author + "$^{" + str(nInst) + "}$"
            
            if nAuth < len(Mmbr.Member._Instances):
                Line += ","
                
            self._Lines.append(Line)
            
        Line = "\\end{center}"
        self._Lines.append(Line)

    def getInstitutes(self):
        Line = "\\vspace{2.5cm}"
        self._Lines.append(Line)
        Line = "\\noindent\\textit{\\footnotesize"
        self._Lines.append(Line)
        Line = "  \\begin{tabbing}"
        self._Lines.append(Line)
        Line = "    \\hspace*{0.45cm}\\= \\hspace{17.5cm} \\kill"
        self._Lines.append(Line)
        nInst = 0
        gInst = []
        for iMmbr in Mmbr.Member._AlphaMmbrSort:
            Org = iMmbr._Organisation
            if not Org in gInst:
                gInst.append(Org)
                nInst += 1
                Line = "     $^{" + str(nInst) + "}$ \\> " + \
                    Org.getAddress() + "\\\\"
                self._Lines.append(Line)
            if iMmbr._Affiliation != None:
                Affil = iMmbr._Affiliation
                if not Affil._Name in gInst:
                    gInst.append(Affil._Name)
                    nInst += 1
                    Line = "     $^{" + str(nInst) + "}$ \\> " + \
                        Affil.getAddress() + "\\\\"
                    self._Lines.append(Line)
        Line = "    ~   \\> \\\\"
        self._Lines.append(Line)
        Line = "  \\end{tabbing}"
        self._Lines.append(Line)
        Line = "}"
        self._Lines.append(Line)

            
    
#--------  List:
        

                

#--------  Exceptions:
class NoListNameProvided:
    pass

class NoOutputPathProvided:
    pass

class NoFilenameProvided:
    pass

class OutputPathInvalid:
    pass

class NoWriteAccessToOutputPath:
    pass

class WorkPackageInstanceInvalid:
    pass

class ProjectInstanceInvalid:
    pass

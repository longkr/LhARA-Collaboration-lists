#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class Institute:
====================

  Description


  Class attributes:
  -----------------
  __xxxx: Description
      

  Instance attributes:
  --------------------
   _Debug: Debug flag
    

  Methods:
  --------
  Built-in methods __new__, __repr__ and __str__.
      __new__ : Creates instance
      __repr__: One liner with call.
      __str__ : Dump of constants


  Get/set methods:   <-------- believed to be "self documenting"!
     getXyyy

  Print methods:
     print: Prints ....



  
Created on xxx DdMmmYy;hh:mm: Version history:
----------------------------------------------
 1.0: DdMmmYy: First implementation

@author: kennethlong
"""

#.. import 

class Institute:
    __Debug    = False
    _Instances = []

#--------  "Built-in methods":
    def __init__(self, __Name=None, __Address=None, __Debug=False):

        self._Debug = False
        if not isinstance(__Debug, bool):
            raise BadArgumentList
        if __Debug:
            self._Debug = True

        if __Name == None or not isinstance(__Name, str):
            raise BadArgumentList
        if __Address == None or not isinstance(__Address, str):
            raise BadArgumentList
        
        self._Name    = __Name
        self._Address = __Address
        
        if self.__Debug:
            print(" Institute.__init__: called")

        Institute._Instances.append(self)

    def __repr__(self):
        return " Institute(Name, Address, Debug)"

    def __str__(self):
        print(" Institute parameters:")
        print("     Name   :", self._Name)
        print("     Address:", self._Address)
        print("     Debug  :", self._Debug)
              
        return "     <---- __str__ done."


#--------  "Get methods" only
    def getAddress(self):
        return self._Address

    def getName(self):
        return self._Name

    @classmethod
    def getInstituteId(cls, InstCode):
        Id  = -1
        Cnt = -1
        for iInst in cls._Instances:
            Cnt += 1
            if iInst._Name == InstCode:
                Id = Cnt
                break
        return Id
        
    @classmethod
    def getInstituteInst(cls, InstId):
        return cls._Instances[InstId]
    
#--------  "Set methods" only
        
    
#--------  Print methods:
    def print(self):
        print(" Institute print:")
        return "     <---- Done."

    
#--------  Exceptions:
class BadArgumentList(Exception):
    """Bad argument list"""
    pass

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class Collaboration:
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

class Collaboration:
    __Debug    = False

#--------  "Built-in methods":
    def __init__(self, __ShortName=None, __LongName=None, __WWW=None, __Wiki=None, __Debug=False):

        self._Debug = False
        if not isinstance(__Debug, bool):
            raise BadArgumentList
        if __Debug:
            self._Debug = True

        if __ShortName == None or not isinstance(__ShortName, str):
            raise BadArgumentList
        if __LongName == None or not isinstance(__LongName, str):
            raise BadArgumentList
        if __WWW == None or not isinstance(__WWW, str):
            raise BadArgumentList
        if __Wiki == None or not isinstance(__Wiki, str):
            raise BadArgumentList
        
        self._ShortName = __ShortName
        self._LongName  = __LongName
        self._WWW       = __WWW
        self._Wiki      = __Wiki
        
        if self.__Debug:
            print(" Collaboration.__init__: called")

    def __repr__(self):
        return " Collaboration(ShortName, LongName, WWW, Wiki, Debug)"

    def __str__(self):
        print(" Collaboration parameters:")
        print("     Short name:", self._ShortName)
        print("     Long name :", self._LongName)
        print("     WWW       :", self._WWW)
        print("     Wiki      :", self._Wiki)
        print("     Debug     :", self._Debug)
              
        return "     <---- __str__ done."


#--------  "Get methods" only
        
    
#--------  "Set methods" only
        
    
#--------  Print methods:
    def print(self):
        print(" Collaboration print:")
        return "     <---- Done."

    
#--------  Exceptions:
class BadArgumentList(Exception):
    """Bad argument list"""
    pass

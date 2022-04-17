#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class XXXXXXX:
==============

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

class XXXXXX:
    __Debug    = False

#--------  "Built-in methods":
    def __init__(self, __Debug=False):

        self._Debug = False
        if not isinstance(__Debug, bool):
            raise BadArgumentList
        if __Debug:
            self._Debug = True
            
        if self.__Debug:
            print(" XXXXXX.__init__: called")

    def __repr__(self):
        return " XXXXXX()"

    def __str__(self):
        print(" XXXXXX parameters:")
        print("     _Debug:", self._Debug)
              
        return "     <---- __str__ done."


#--------  "Get methods" only
        
    
#--------  "Set methods" only
        
    
#--------  Print methods:
    def print(self):
        print(" XXXXXX print:")
        return "     <---- Done."

    
#--------  Exceptions:
class BadArgumentList(Exception):
    """Bad argument list"""
    pass

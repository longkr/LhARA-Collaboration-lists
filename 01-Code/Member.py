#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class Member:
=============

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

class Member:
    __Debug    = False

#--------  "Built-in methods":
    def __init__(self, \
                 __Title, __Name=None, __Surname=None, __Initials=None, \
                 __email=None, \
                 __PubName=None, \
                 __Organisation=None, \
                 __Affiliations=None, \
                 __ORCID=None, \
                 __Debug=False):

        self._Debug = False
        if not isinstance(__Debug, bool):
            raise BadArgumentList
        if __Debug:
            self._Debug = True

        """
        if __Name == None or not isinstance(__Name, str):
            raise BadArgumentList
        if __Address == None or not isinstance(__Address, str):
            raise BadArgumentList
        """
        
        self._Title        = __Title
        self._Name         = __Name
        self._Surname      = __Surname
        self._Initials     = __Initials
        self._email        = __email
        self._PubName      = __PubName 
        self._Organisation = __Organisation
        self._Affiliations = __Affiliations
        self._ORCID        = __ORCID

        if self.__Debug:
            print(" Member.__init__: called")

    def __repr__(self):
        return " Member(Title, Name, Surname, email, PubName, Organisation, Affiliations)"

    def __str__(self):
        print(" Member parameters:")
        print("            Title:", self._Title)
        print("             Name:", self._Name)
        print("          Surname:", self._Surname)
        print("         Initials:", self._Initials)
        print("            email:", self._email)
        print("          PubName:", self._PubName)
        print("     Organisation:", self._Organisation)
        print("     Affiliations:", self._Affiliations)
        print("            ORCID:", self._ORCID)
              
        return "     <---- __str__ done."


#--------  "Get methods" only
        
    
#--------  "Set methods" only
        
    
#--------  Print methods:
    def print(self):
        print(" Member print:")
        return "     <---- Done."

    
#--------  Exceptions:
class BadArgumentList(Exception):
    """Bad argument list"""
    pass

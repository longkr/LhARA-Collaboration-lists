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
   __Debug: Debug flag
   __Instances: List of instances
   __AlphaMmbrSort
    

  Methods:
  --------
  Built-in methods __new__, __repr__ and __str__.
      __new__ : Creates instance
      __repr__: One liner with call.
      __str__ : Dump of constants


  I/o and data-constructor methods:
      parseStaffDatabase: Read staff database CSV file and create Staff
                          instances.
                     Input: Path to CSV file containing staff database.
                    Return: Number of staff instances
                     [Class method]

        getStaffDatabase: Uses pandas to create pandas dataframe from
                          CSV file.  Called from parseStaffDatabase.
                     Input: Path to CSV file containing staff database.
                    Return: Pandas dataframe instance containing staff 
                            data base
                     [Class method]

   createPandasDataframe: Creates pandas data frame from instances of
                          Staff.
                      Return: Pandas dataframe instance
                     [Class method]

               createCSV: Creates CSV file from pandas dataframe.
                       Inputs: Pandas dataframe instance
                               Path to output file


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

import os
import math
from operator import attrgetter
import pandas as pnds

import Institute as Inst

class Member:
    _Debug         = False
    _Instances     = []
    _AlphaMmbrSort = None

#--------  "Built-in methods":
    def __init__(self, \
                 __Title, __Name=None, __Surname=None, __Initials=None, \
                 __email=None, \
                 __PubName=None, \
                 __Organisation=None, \
                 __Affiliation=None, \
                 __ORCID=None, \
                 __InstBrd=None, \
                 __Debug=False):

        self._Debug = False
        if not isinstance(__Debug, bool):
            raise BadArgumentList
        if __Debug:
            self._Debug = True
            print(" Member.__init__: debug set")

        """
        if __Name == None or not isinstance(__Name, str):
            raise BadArgumentList
        if __Address == None or not isinstance(__Address, str):
            raise BadArgumentList
        """
        
        self._Title            = __Title
        self._Name             = __Name
        self._Surname          = __Surname
        self._Initials         = __Initials
        self._email            = __email
        self._PubName          = __PubName 
        self._Organisation     = __Organisation
        self._Affiliation      = __Affiliation
        self._ORCID            = __ORCID
        self._InstBrd         = __InstBrd

        Member._Instances.append(self)

    def __repr__(self):
        return " Member(Title, Name, Surname, Initials, email, PubName, "  \
            "Organisation, Affiliation, Debug)"

    def __str__(self):
        print(" Member parameters:")
        print("               Title:", self._Title)
        print("                Name:", self._Name)
        print("             Surname:", self._Surname)
        print("            Initials:", self._Initials)
        print("               email:", self._email)
        print("             PubName:", self._PubName)
        print("        Organisation:", self._Organisation)
        print("         Affiliation:", self._Affiliation)
        print("               ORCID:", self._ORCID)
        print("     Institute Board:", self._InstBrd)
              
        return "     <---- __str__ done."


#--------  I/o and data-constructor methods:
    @classmethod
    def parseMemberDatabase(cls, filename=None):
        if cls._Debug:
            print(" Member.parseMemberDatabase: start!")
            
        if filename == None:
            raise NoMemberDataBaseFile(" Member.parseMemberDatabase: \
                         no file name given, execution terminated.")
        elif not os.path.isfile(filename):
            raise MemberDataBaseFileDNE(" Member.parseMemberDatabase: \
                   staff database file ", filename, \
                   " does not exist, execution terminated.")

        _MmbrDtbsParams = cls.getMemberDatabase(filename)
        if cls._Debug:
            xDummy = cls.printMemberDatabase(_MmbrDtbsParams)

        iRow = _MmbrDtbsParams.index
        for i in iRow:
            AffilCode = []
            AffilAddr = []
            Title     = _MmbrDtbsParams.iat[i,0]
            Name      = _MmbrDtbsParams.iat[i,1]
            Surname   = _MmbrDtbsParams.iat[i,2]
            Initials  = _MmbrDtbsParams.iat[i,3]
            Email     = _MmbrDtbsParams.iat[i,4]
            PubName   = _MmbrDtbsParams.iat[i,5]
            Org       = _MmbrDtbsParams.iat[i,6]
            Address   = _MmbrDtbsParams.iat[i,7]
            nAffil    = 0
            if not math.isnan(_MmbrDtbsParams.iat[i,8]):
                nAffil    = int(_MmbrDtbsParams.iat[i,8])
            for iAff in range(nAffil):
                AffilCode.append(str(_MmbrDtbsParams.iat[i,9+2*iAff]))
                AffilAddr.append(str(_MmbrDtbsParams.iat[i,10+2*iAff]))
             
            OrcId     = _MmbrDtbsParams.iat[i,13]
            InstBrd   = False
            if str(_MmbrDtbsParams.iat[i,14]).lower() == "ib":
                InstBrd = True

            if cls._Debug:
                print("     ----> Title              :", Title)
                print("     ----> Name               :", Name)
                print("     ----> Surname            :", Surname)
                print("     ----> Initials           :", Initials)
                print("     ----> Email              :", Email)
                print("     ----> PubName            :", PubName)
                print("     ----> Org                :", Org)
                print("     ----> Address            :", Address)
                print("     ----> n affiliations     :", nAffil)
                print("     ----> Affiliation code   :", AffilCode)
                print("     ----> Affiliation address:", AffilAddr)
                print("     ----> OrcId              :", OrcId)
                print("     ----> Institute Board    :", InstBrd)

            #.. Find, or set, Org instance:
            OrgInst = None
            for iInst in Inst.Institute._Instances:
                if iInst._Name == Org:
                    OrgInst = iInst
            if OrgInst == None:
                OrgInst = Inst.Institute(Org, Address, True)
                if Member._Debug:
                    print("     ----> Created: \n", OrgInst)
            else:
                if Member._Debug:
                    print("     ----> Using: \n", OrgInst)

            #.. Iff affilations, fill:
            AffilInst = []
            if int(nAffil) > 0 and len(AffilCode) > 0:
                for iAff in range(len(AffilCode)):
                    if Member._Debug:
                        print( \
                          "        ----> Additional affiliation identified:",\
                               AffilCode[iAff])
                    InstId = iInst.getInstituteId(AffilCode[iAff])
                    if InstId == -1:
                        AffilInst.append(Inst.Institute(AffilCode[iAff], \
                                                        AffilAddr[iAff], \
                                                        Member._Debug)\
                                         )
                        if Member._Debug:
                            print("         ----> Created:")
                    else:
                        AffilInst.append(iInst.getInstituteInst(InstId))
                        if Member._Debug:
                            print("         ----> Using:")
                    if Member._Debug:
                        print(AffilInst[iAff])

            MmbrDummy = Member( \
                                Title, Name, Surname, Initials, \
                                Email, \
                                PubName, \
                                OrgInst, \
                                AffilInst, \
                                OrcId, \
                                InstBrd, \
                                False
                               )
        return len(cls._Instances)

    @classmethod
    def getMemberDatabase(cls, _filename):
        MmbrDBParams = pnds.read_csv(_filename)
        return MmbrDBParams

    @classmethod
    def createPandasDataframe(cls):
        MemberData = []
        MemberData.append(cls.getHeader())
        for inst in Member.instances:
            MemberData.append(inst.getData())
        MemberDataframe = pnds.DataFrame(MemberData)
        if cls._Debug:
            print(" Staff; createPandasDataframe: \n", MemberDataframe)
        return MemberDataframe

    @classmethod
    def createCSV(cls, _MmbrDataFrame, _filename):
        _MmbrDataFrame.to_csv(_filename)


#--------  "Get methods" only
    def getSurname(self):
        return self._Surname
    
    def getInitials(self):
        return self._Initials

    def getemail(self):
        return self._email

    def getOrganisation(self):
        return self._Organisation
    
    def getInstBrd(self):
        return self._InstBrd

    @classmethod
    def getAlphaMemberSort(cls):
        return cls._AlphaMmbrSort
    

#--------  "Set methods" only
        
    
#--------  Print methods:
    @classmethod
    def printMemberDatabase(cls, _MmbrDtbsParams):
        print(_MmbrDtbsParams)

    def print(self):
        print(" Member print:")
        return "     <---- Done."

        
#--------  Member sort methods:
    @classmethod
    def sortAlphabeticalByName(cls):

        OutStr = "Member.sortAlphabeticalByName: failed."
        if cls._AlphaMmbrSort == None:
            if cls._Debug:
                print(" Member.sortAlphabeticalByName: Start.")
                for Inst in cls._Instances:
                    print(" Surname:", Inst._Surname, " Initials:", \
                          Inst._Initials)
        
            cls._AlphaMmbrSort = \
                sorted(cls._Instances, key=attrgetter('_Surname', \
                                                      '_Initials'))

            if cls._Debug:
                print("     ----> Sorted list:")
                for Inst in cls._AlphaMmbrSort:
                    print(" Surname:", Inst._Surname, " Initials:", \
                          Inst._Initials)
                    
            OutStr = "Member.sortAlphabeticalByName: "\
                "sorted alphabetically by name."
            
        else:
            OutStr = "Member.sortAlphabeticalByName: already sorted."
        
        return OutStr


#--------  Processing methods
    @classmethod
    def cleanMemberDatabase(cls):
        Deletions =[]
        for iMmbr in cls._Instances:
            if not isinstance(iMmbr._Surname, str):
                Deletions.append(iMmbr)
            if not isinstance(iMmbr._Initials, str):
                Deletions.append(iMmbr)
        
        if cls._Debug:
            for i in range(len(Deletions)):
                print(" Member; cleanMemberDatabase: instances marked for ", \
                      "deletion: ", Deletions[i]._Surname)

        OldInstances = cls._Instances
        cls._Instances = []
        for iMmbr in OldInstances:
            try:
                i = Deletions.index(iMmbr)
                del iMmbr
            except ValueError:
                cls._Instances.append(iMmbr)

        return len(Deletions)


#--------  Exceptions:
class BadArgumentList(Exception):
    """Bad argument list"""
    pass

class MemberDataBaseFileDNE(Exception):
    pass

########################################################################################################################
# ABlood pressure Early Warning And Detection Root file
########################################################################################################################
# Authors
#   Richard Johnston 
#   Jyothi Cameron
#
# Created Date
#   2022-11-06
#
# Description
#   Calculate blood pressure information
#
########################################################################################################################
# BEGIN WORKING DOCUMENT
########################################################################################################################

# import custom module from BPEWAD_Modules Package
import BPEWAD_Modules.bp_math as bpm

# define the class
class Root():
    # define the scope of the project
    def __init__(self):
        super(Root, self).__init__()
        # call the app
        self.app()
    
    def app(self):
        # since the calculations and printing is handled by the 
        # "bp_math" module in the "BPEWAD_MOdules" package, this will do nothing. 
        # the calculations are completed simply by importing the module. 
        # for reference, this is bad practice so it should be changed.
        pass

def main():
    # call Root(), which wiill call app()
    Root()


if __name__ == "__main__":
    # call main(), which will call Root(), which wiill call app(). This technique
    # is called a "main guard" and defines the "entry point" into the program.
    # allows you to both run code in the module directly and also use classes from other modules
    main()
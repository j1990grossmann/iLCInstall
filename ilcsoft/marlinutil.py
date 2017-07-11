##################################################
#
# MarlinUtil module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import MarlinPKG

class MarlinUtil(MarlinPKG):
    """ Responsible for the MarlinUtil installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "MarlinUtil", userInput )

        self.hasCMakeFindSupport = True

        # required modules
        self.reqmodules = [ "Marlin", "GSL", "CLHEP", "GEAR", "LCIO" , "CED" , "ROOT" ]

        # cvs root
        self.download.root = "marlinreco"
        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'iLCSoft'
        self.download.gitrepo = 'MarlinUtil'

    def postCheckDeps(self):
        MarlinPKG.postCheckDeps(self)
        self.envpath["LD_LIBRARY_PATH"].append( self.installPath+'/lib' )

##################################################
#
# MarlinTrk module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class MarlinTrk(BaseILC):
    """ Responsible for the MarlinTrk software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "MarlinTrk", "MarlinTrk")

        self.reqfiles = [ ["lib/libMarlinTrk.so","lib/libMarlinTrk.a","lib/libMarlinTrk.dylib"] ]

        self.reqmodules = [ "LCIO", "GEAR", "Marlin", "KalTest", "KalDet", "ROOT" ]

        # svn root
        self.download.root = "marlinreco"

    def compile(self):
        """ compile MarlinTrk """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

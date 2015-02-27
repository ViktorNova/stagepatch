#!/usr/bin/env python2
# filename: nsm-git-ui

import os
from PyQt4 import QtCore,QtGui
import sys
import subprocess
import stagepatch_ui
import argparse

# -----------------------------------------------------------------------

class hwl(QtGui.QDialog,stagepatch_ui.Ui_Stagepatch):
        # Parse the arguments sent by the main process 
        # so that we know what we're working with
        parser = argparse.ArgumentParser()
        parser.add_argument("saveFile") # First argument (AJ-Snapshot saveFile)
        parser.add_argument("pid")      # Second argument  (AJ-Snapshot PID)
        args = parser.parse_args()

        # Convert the parsed arguments into variables
        saveFile = args.saveFile
        pid = int(args.pid)       
        # Print the stuff
        
        print "Patchbay save file is %s" % saveFile
        print "aj-snapshot pid is " 
        print pid
        """
        hwl is inherited from both QtGui.QDialog and hw.Ui_Dialog
        """
        def __init__(self,parent=None):
            """
                Initialization of the class. Call the __init__ for the super classes
            """
            super(hwl,self).__init__(parent)
            self.setupUi(self)
            self.connectActions()
        def main(self):
            self.show()
        def connectActions(self):
            # Call a different function for each button that 
            # gets clicked
            self.overwritePatchbay.clicked.connect(self.overwrite)        
            
        def overwrite(self): # Save Patchbay
            #self.lblShow.setText('This is a test')
            print "Overwritepatchbay is clicked"
            print "Saving current MIDI and JACK connections over existing patchbay"
            subprocess.call(["aj-snapshot", "-f", self.saveFile],
                             stdout=subprocess.PIPE,
                             preexec_fn=os.setsid)
            # Replace this with a proper python sendsignal thing                
            subprocess.call(["kill", "-HUP", self.pid],
                             stdout=subprocess.PIPE,
                             preexec_fn=os.setsid)            
            
        
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    hwl1 = hwl()
    hwl1.main()
    sys.exit(app.exec_())

# -----------------------------------------------------------------------


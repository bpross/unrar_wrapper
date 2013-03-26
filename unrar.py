"""
This is a wrapper around unrar
The unrar license does not allow the creation of a library
so here we are...
"""

import os
import sys
import subprocess

class unrar:

    def __init__ (self, archive = None):
        """
        This initializes the rar file
        @param file: rar file to operate on
        """
        if file:
            self.archive = archive
        else:
            sys.exit("Specify an archive")

    def list(self):
        """
        This prints the listing of the rar file
        """

    def list_bare(self):
        """
        This prints out the bare listing of the rar file
        Pretty much only the file name
        """
        cmd = "unrar lb " + str(self.archive)
        args = [cmd]
        proc = subprocess.Popen(args,shell=True, stdout=subprocess.PIPE)
        if proc:
            print "Success!"
            for line in proc.stdout:
                print("stdout: " + line.rstrip())
        else:
            print "ERROR!"

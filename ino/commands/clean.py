# -*- coding: utf-8; -*-

import os.path
import shutil

from ino.commands.base import Command
from ino.exc import Abort


class Clean(Command):
    """
    Remove all intermediate compilation files and directories completely.

    In fact `.build' directory is simply removed.
    """

    name = 'clean'
    help_line = "Remove intermediate compilation files completely"
    error= 0

    def run(self, args):
        if os.path.isdir(self.e.output_dir):
            shutil.rmtree(self.e.output_dir,onerror=self.onerror)
        if self.error > 0: 
          raise Abort('Can\'t remove the build directory - ' + self.e.output_dir) 

    def onerror(self, func, path, excinfo):
      self.error += 1


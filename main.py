# coding=utf-8
#
#  main.py
#  PythonAsYouType
#
#  Created by Anders Hovmoller on 5/19/09.
#  Copyright Anders Hovmöller 2009. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import PythonAsYouTypeAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()

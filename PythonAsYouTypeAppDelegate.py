# coding=utf-8
#
#  PythonAsYouTypeAppDelegate.py
#  PythonAsYouType
#
#  Created by Anders Hovmoller on 5/19/09.
#  Copyright Anders Hovmöller 2009. All rights reserved.
#

from Foundation import *
from AppKit import *
from objc import *
import re
import sys
import ConsoleDelegate

def run_expression(expression):
    return eval(compile(expression, '<string>', 'exec'))

class PythonAsYouTypeAppDelegate(NSObject):
    window = IBOutlet()
    path = IBOutlet()
    setup_input = IBOutlet()
    experimental_input = IBOutlet()
    setup_output = IBOutlet()
    experimental_output = IBOutlet()
    error_output = IBOutlet()
    
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(self, self.textDidChange_, NSControlTextDidChangeNotification, self.experimental_input)
        #self.textDidChange_(None)

    @IBAction
    def executeSetup_(self, sender):
        if self.path.stringValue() not in sys.path:
            sys.path.append(self.path.stringValue())
        run_expression(self.setup_input.textStorage().string())
        output = ''.join(sys.stdout.buffer)
        self.setup_output.setStringValue_(output)
        sys.stdout.buffer = []
            
    @IBAction
    def textDidChange_(self, notification):
        try:
            run_expression(self.experimental_input.textStorage().string())
            output = ''.join(sys.stdout.buffer)
            self.error_output.setStringValue_('')
            self.experimental_output.setStringValue_(output)
        except Exception,e:
            self.error_output.setStringValue_('error: %s' % e)
        sys.stdout.buffer = []
    

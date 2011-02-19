# coding=utf-8
#
#  Console.py
#  Superfluidity
#
#  Created by Anders Hovmoller on 2009-05-03.
#  Copyright (c) 2009 Satans Killingar. All rights reserved.
#

from objc import YES, NO, IBAction, IBOutlet
from Foundation import *
from AppKit import *
import traceback

console = None
      
class ConsoleDelegate(NSObject):
    input = IBOutlet()
    buffer = IBOutlet()
    window = IBOutlet()
    
    def awakeFromNib(self):
        global console
        console = self
        
    def ask_console_for_string(self):
        self.update_display()
        self.window.orderFront_(self)
        NSApplication.sharedApplication().runModalForWindow_(self.window)
        return self.input.stringValue()

    def update_display(self):
        self.buffer.setStringValue_(''.join(sys.stdout.buffer))
        self.buffer.scrollPoint_(NSPoint(0, 100))

    @IBAction
    def input_(self, sender):
        NSApplication.sharedApplication().abortModal()
        self.window.resignKeyWindow()
        self.window.orderOut_(None)

# override stdio for our GUI
class StdIn:
    def readline(self):
        return console.ask_console_for_string()
        
class StdOut:
    def __init__(self, old):
        self.buffer = []
        self.old = old
        
    def write(self, data):
        self.buffer.append(data)
        if len(self.buffer) > 5000:
            del(self.buffer[0])
        self.old.write(data)
        
import sys
#sys.stdin = StdIn()
sys.stdout = StdOut(sys.stdout)
# -*- coding: utf8 -*-
# -----------------------------------------------------------------------------
# Author : yongchan jeon (Kris) poucotm@gmail.com
# File   : testing.py
# Create : 2017-08-31 22:09:10
# Editor : sublime text3, tab size (4)
# -----------------------------------------------------------------------------

print ('load testing')

import sublime, sublime_plugin
import sys, imp
import traceback

##  sub-modules  ______________________________________________

try:
    print ('try testing')
    # reload
    mods = ['testing.core.persist', 'testing.core.engine']
    for mod in list(sys.modules):
        if any(mod == m for m in mods):
            imp.reload(sys.modules[mod])
    # import
    from .core import persist
    from .core import engine
    import_ok = True
except Exception:
    traceback.print_exc()
    import_ok = False

# package control
try:
    from package_control import events
    package_control_installed = True
except Exception:
    package_control_installed = False

##  plugin_loaded  ____________________________________________

def plugin_loaded():

    # import
    if not import_ok:
        sublime.status_message("* TEST : Error")
        return

    if package_control_installed and (events.install('testing') or events.post_upgrade('testing')):
        print ('install/upgrade')
    else:
        print ('else install/upgrade')
    print ('plugin_loaded')


##  plugin_unloaded  __________________________________________

def plugin_unloaded():

    # engine stop
    if package_control_installed:
        if events.remove('testing') or events.pre_upgrade('testing'):
            print ('else remove/pre_upgrade')
    print ('plugin_unloaded')

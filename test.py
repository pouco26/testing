import sublime
import sublime_plugin


# package control
try:
    from package_control import events
    package_control_installed = True
except Exception:
    package_control_installed = False


def plugin_loaded():
    if package_control_installed:
        if events.install('testing'):
            print ('install testing')
        elif events.post_upgrade('testing'):
            print ('post_upgrade testing')
    print ('plugin_loaded')


def plugin_unloaded():
    if package_control_installed:
        if events.remove('testing'):
            print ('remove testing')
        elif events.pre_upgrade('testing'):
            print ('pre_upgrade testing')
    print ('plugin_unloaded')

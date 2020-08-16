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

    get_log_extension()
    lhs = get_prefs()
    lhs.clear_on_change('testing-prefs')
    lhs.add_on_change('testing-prefs', get_log_extension)



def plugin_unloaded():
    if package_control_installed:
        if events.remove('testing'):
            print ('remove testing')
        elif events.pre_upgrade('testing'):
            print ('pre_upgrade testing')
    print ('plugin_unloaded')


def get_prefs():
    return sublime.load_settings('testing.sublime-settings')

def get_log_extension():
    global EXT_ALL
    global EXT_DIC
    global OUT_DIC
    EXT_ALL = []
    EXT_DIC = {}
    OUT_DIC = {}
    lol = get_prefs().get('log_list')
    lgl = list(lol.keys())
    for ltype in lgl:
        extl = lol.get(ltype).get('extension')
        for ext in extl:
            EXT_ALL.append(ext)
            EXT_DIC[ext] = ltype
        outl = lol.get(ltype).get('output.panel')
        for out in outl:
            OUT_DIC[out] = ltype
    return

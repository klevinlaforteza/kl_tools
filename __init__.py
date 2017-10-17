import maya.cmds as mc

import utils
reload(utils)


class KLToolsWindow(object):

    klToolsWindow = "klToolsWindow"

    def show(self):

        if mc.window(self.klToolsWindow, query=True, exists=True):
            mc.deleteUI(self.klToolsWindow)

        self.buildUI()
        mc.showWindow(self.klToolsWindow)

    def buildUI(self):
        ui = "kl_tools/ui/kl_toolsUI.ui"
        self.klToolsWindow = mc.loadUI(uiFile=(mc.internalVar(userScriptDir=True) + ui))

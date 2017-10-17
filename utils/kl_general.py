import maya.cmds as mc


def maya_window(win):

    """
    -----------------------------------------------------------------------------------------------------
    This function loads and shows up the specified maya window
    :param win:
    :return:
    -----------------------------------------------------------------------------------------------------
    """

    exec ("mc.%s()" % win)


def list_selection():

    """
    -----------------------------------------------------------------------------------------------------
    This function creates a list from the selected objects
    :return:
    -----------------------------------------------------------------------------------------------------
    """

    # Create a list from selected objects and get their long names
    selection = mc.ls(selection=True, long=True)

    return selection

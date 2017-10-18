import maya.cmds as mc


def joint_display():

    """
    -----------------------------------------------------------------------------------------------------
    This function sets the joint display size
    :return:
    -----------------------------------------------------------------------------------------------------
    """

    # Query UI information and assign them to variables
    joint_size = mc.intSlider("jointSize_sld", query=True, value=True) / 10.00

    # Set the joint display size
    mc.jointDisplayScale(joint_size)


def joint_display_reset():

    """
    -----------------------------------------------------------------------------------------------------
    This function resets the joint display size to default setting
    :return:
    -----------------------------------------------------------------------------------------------------
    """

    mc.intSlider("jointSize_sld", edit=True, value=10)
    mc.jointDisplayScale(1)
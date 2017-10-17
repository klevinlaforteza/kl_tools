import maya.cmds as mc

import kl_general


def color_override(index):

    """
    -----------------------------------------------------------------------------------------------------
    This function changes the override color of the shape nodes of selected objects
    :param index: A value between 0-31 to determine the color
    :return:
    -----------------------------------------------------------------------------------------------------
    """

    # Query selection
    selection = kl_general.list_selection()

    for object in selection:
        # Create a list of shapes of each object
        shapes = mc.listRelatives(object, shapes=True)

        # Enable and change the override color for each shape
        for shape in shapes:
            mc.setAttr("%s.overrideEnabled" % shape, True)
            mc.setAttr("%s.overrideColor" % shape, index)


def text_curve():
    """
    -----------------------------------------------------------------------------------------------------
    This function creates a set of curves of a text on a single transform node
    :return:
    -----------------------------------------------------------------------------------------------------
    """

    # Query the input text and assign it to a variable
    text = mc.textField("textCurve_text", query=True, text=True)

    if text:
        if text.startswith(" "):
            mc.warning("Please make sure text doesn't start with a space.")

        else:
            # Create text curves and rename it to remove "Shape" from its name
            crv = mc.textCurves(text=text, constructionHistory=False, name="%s_text_crv" % text)[0]
            crv = mc.rename(crv, crv.split("Shape")[0])

            # List all the children of the created text curve
            children = mc.listRelatives(crv, allDescendents=True, type="transform")

            # List the children that has shape nodes
            curves = [child for child in children if mc.listRelatives(child, shapes=True)]

            # Parent the curves to crv transform node
            for curve in curves:
                mc.parent(curve, crv)
                mc.makeIdentity(curve, apply=True, translate=True)

            # Add the shape nodes to transform node and hide them in the outliner
            curves.append(crv)
            mc.select(curves)
            shape_add()
            shape_show()
            mc.delete(mc.listRelatives(crv, allDescendents=True, type="transform"))

            # Center the pivot of the transform node and snap it back in the origin
            mc.xform(crv, centerPivots=True)
            pivot = mc.xform(crv, query=True, rotatePivot=True)
            mc.move(-pivot[0], -pivot[1], -pivot[2], crv)
            mc.makeIdentity(crv, apply=True, translate=True)

    else:
        mc.warning("Please input text.")


def control_curve():
    pass


def shape_show(show=False):
    """
    -----------------------------------------------------------------------------------------------------
    This function shows or hides the shape nodes from the channel box
    :param show: Determines whether to show or hide the shape nodes
    :return:
    -----------------------------------------------------------------------------------------------------
    """

    # Query the selection
    selection = kl_general.list_selection()

    # Check if there are any selection
    if selection:
        for object in selection:
            # Create a list of shapes for each object
            shapes = mc.listRelatives(object, shapes=True)

            # Check if object has shape nodes
            if shapes:
                # Show or hide each shape node for each object
                for shape in shapes:
                    mc.setAttr("%s.isHistoricallyInteresting" % shape, show)

        # Return to original selection
        mc.select(selection)


def shape_add():
    """
    -----------------------------------------------------------------------------------------------------
    This function adds the shape nodes of selection to last selected object
    :return:
    -----------------------------------------------------------------------------------------------------
    """

    # Query selection
    selection = kl_general.list_selection()

    # Define the parent object and remove it from the list
    parent = selection[-1]
    selection.remove(parent)

    for object in selection:
        # Create a list of shapes for each object
        shapes = mc.listRelatives(object, shapes=True, path=True)

        # Check if object has shape nodes
        if shapes:
            # Add each shape node of the object to the parent object and delete the object afterwards
            for shape in shapes:
                mc.parent(shape, parent, add=True, shape=True)
            mc.delete(object)

    # Select parent object and rename its shape node accordingly
    mc.select(parent)
    shape_rename()


def shape_rename():
    """
    -----------------------------------------------------------------------------------------------------
    This function renames the shape nodes according to the name of the tranform nodes
    :return:
    -----------------------------------------------------------------------------------------------------
    """

    # Query selection
    selection = kl_general.list_selection()

    # Check if there are any selection
    if selection:
        for object in selection:
            # Define the short name of each object
            short_name = object.split("|")[-1]

            # Create a list of shape nodes of each object
            shapes = mc.listRelatives(object, shapes=True, path=True)

            # Check if object has shape nodes
            if shapes:
                # Reverse the list and count the shape nodes of each object
                shapes.reverse()
                i = len(shapes)

                # Rename each shape node accordingly
                for shape in shapes:
                    mc.rename(shape, "%sShape%s" % (short_name, i))
                    i -= 1

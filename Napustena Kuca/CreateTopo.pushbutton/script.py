# script.py

from pyrevit import revit, DB, forms
import os
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from System.Collections.Generic import List

# Function to import OBJ file and create a topography surface
def import_obj_as_topography(doc, obj_file_path, scale=2.325):
    if not os.path.exists(obj_file_path):
        raise Exception("OBJ file not found at: " + obj_file_path)

    points = []
    with open(obj_file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):
                # parts = line.split()
                if len(parts) >= 4:
                    x = float(parts[1])
                    y = float(parts[2])
                    z = float(parts[3])
                    # Adjust axes to match Revit coordinate system
                    point = XYZ(x * scale, -z * scale, y * scale)
                    points.append(point)

    if len(points) == 0:
        raise Exception("No points were found in the OBJ file.")

    point_list = List[XYZ](points)
    topo_surface = TopographySurface.Create(doc, point_list)
    return topo_surface

# Prompt user to select OBJ file
obj_file_path = forms.pick_file(file_ext='obj', title='Select OBJ File for Topography')

# Prompt user for scale factor
if obj_file_path:
    scale_input = forms.ask_for_string(
        default='2.325',
        prompt='Enter scale factor for OBJ coordinates:',
        title='Scale Factor Input'
    )

    try:
        scale = float(scale_input)
    except:
        forms.alert("Invalid scale value. Must be a number.", title="Input Error")
        scale = None

    if scale:
        doc = revit.doc
        t = Transaction(doc, "Create Topography from OBJ")
        t.Start()
        try:
            topo = import_obj_as_topography(doc, obj_file_path, scale)
            t.Commit()
            forms.alert("Topography created successfully!", title="Success")
        except Exception as e:
            t.RollBack()
            forms.alert("Error: " + str(e), title="Failed")

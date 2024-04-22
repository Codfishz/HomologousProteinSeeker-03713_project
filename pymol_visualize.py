import pymol
from pymol import cmd

def visualize_structure(pdb_filename):
    """
    This function initializes PyMOL, loads a PDB file, sets up a basic visualization, and saves the image.
    """
    pymol.finish_launching()

    # Load the PDB file
    cmd.load(pdb_filename)

    # Basic visualization settings
    cmd.hide('everything')
    cmd.show('cartoon')
    cmd.color('blue', 'all')

    # Zoom to the molecule
    cmd.zoom()

    # Add some more visualization details, such as a molecular surface
    cmd.show('surface', 'all')
    cmd.set('transparency', 0.5)

    # Save the image to the current directory
    cmd.png('visualized_structure.png')

if __name__ == "__main__":
    # The path to the PDB file
    pdb_file_path = 'sample.pdb'
    visualize_structure(pdb_file_path)

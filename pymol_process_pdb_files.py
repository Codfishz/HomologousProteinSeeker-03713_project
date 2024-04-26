#This script should be put in the directory with all input pdb files.
#This script will output the image for all pdb files and the rmsd scores between each pair of pdb files.
#Make sure pymol is available in the environment
import os
import pymol
from pymol import cmd, stored

def visualize_and_calculate_rmsd(directory):
    # Initialize PyMOL
    pymol.finish_launching(['pymol', '-c'])

    # Find all PDB files in the directory
    pdb_files = [f for f in os.listdir(directory) if f.endswith('.pdb')]
    pdb_paths = [os.path.join(directory, f) for f in pdb_files]

    # Load each PDB file into PyMOL
    objects = []
    for pdb in pdb_paths:
        object_name = os.path.splitext(os.path.basename(pdb))[0]
        cmd.load(pdb, object_name)
        objects.append(object_name)

    ## Generate images for all molecules
    cmd.png("all_molecules.png")


    # Calculate RMSD between each pair of PDB files
    rmsd_results = []
    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            rmsd = cmd.align(objects[i], objects[j])[0]
            rmsd_results.append(f"RMSD between {objects[i]} and {objects[j]}: {rmsd:.2f}")
            print(rmsd_results[-1])

    # Write RMSD results to a file
    with open("rmsd_scores.txt", "w") as file:
        for result in rmsd_results:
            file.write(result + "\n")

if __name__ == "__main__":
    visualize_and_calculate_rmsd('.')  # Current directory

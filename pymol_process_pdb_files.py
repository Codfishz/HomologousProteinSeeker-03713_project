#This script takes two input args, the first is the input directory path, the second is the output directory path
#This script will output the image for all pdb files and the rmsd scores between each pair of pdb files.
#Make sure pymol is available in the environment
import os
import argparse
import pymol
from pymol import cmd, stored

def visualize_and_calculate_rmsd(input_directory, output_directory):
    # Initialize PyMOL in non-GUI mode
    pymol.finish_launching(['pymol', '-c'])

    # Find all PDB files in the input directory
    pdb_files = [f for f in os.listdir(input_directory) if f.endswith('.pdb')]
    pdb_paths = [os.path.join(input_directory, f) for f in pdb_files]

    # Load each PDB file into PyMOL
    objects = []
    for pdb in pdb_paths:
        object_name = os.path.splitext(os.path.basename(pdb))[0]
        cmd.load(pdb, object_name)
        objects.append(object_name)

    # Generate an image for all molecules and save it to the output directory
    cmd.png(os.path.join(output_directory, "all_molecules.png"))

    # Calculate RMSD between each pair of PDB files
    rmsd_results = []
    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            rmsd = cmd.align(objects[i], objects[j])[0]
            rmsd_results.append(f"RMSD between {objects[i]} and {objects[j]}: {rmsd:.2f}")
            print(rmsd_results[-1])

    # Write RMSD results to a file in the output directory
    with open(os.path.join(output_directory, "rmsd_scores.txt"), "w") as file:
        for result in rmsd_results:
            file.write(result + "\n")

def main():
    parser = argparse.ArgumentParser(description='Process PDB files in a specified directory and output to a specified directory.')
    parser.add_argument('input_directory', type=str, help='Directory containing PDB files.')
    parser.add_argument('output_directory', type=str, help='Directory to save output files.')
    args = parser.parse_args()

    visualize_and_calculate_rmsd(args.input_directory, args.output_directory)

if __name__ == "__main__":
    main()

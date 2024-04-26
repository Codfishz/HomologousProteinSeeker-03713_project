import os
import argparse
import pymol
from pymol import cmd, stored

def visualize_and_calculate_rmsd(input_directory, output_directory):
    # Initialize PyMOL in non-GUI mode
    pymol.finish_launching(['pymol', '-c'])

    # Traverse subdirectories to find PDB files
    objects = []
    for subdir, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.pdb'):
                pdb_path = os.path.join(subdir, file)
                subdirectory_name = os.path.basename(subdir)
                cmd.load(pdb_path, subdirectory_name)
                objects.append(subdirectory_name)
                
    for molecule in objects:
        # Generate individual image for each molecule
        cmd.disable("all")
        cmd.enable(molecule)
        cmd.png(os.path.join(output_directory, f"{molecule}.png"))

    # Generate a collective image for all molecules
    cmd.enable("all")
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
    parser = argparse.ArgumentParser(description='Process PDB files from subdirectories of a specified directory and output to a specified directory.')
    parser.add_argument('input_directory', type=str, help='Directory containing subdirectories with PDB files.')
    parser.add_argument('output_directory', type=str, help='Directory to save output files.')
    args = parser.parse_args()

    visualize_and_calculate_rmsd(args.input_directory, args.output_directory)

if __name__ == "__main__":
    main()

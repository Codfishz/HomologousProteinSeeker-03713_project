echo "Read input file (.pdb)"
read input
echo "Read database folder"
read database
echo "Read output folder"
read output

foldseek easy-search $input  $database/afdb $output/test_afdb_aln tmp --format-output query,target,alntmscore,u,t,prob
foldseek easy-search $input  $database/afsp $output/test_afsp_aln tmp --format-output query,target,alntmscore,u,t,prob

(cat $output/test_afsp_aln | cut -d $'\t' -f 2,3; cat $output/test_afdb_aln | cut -d $'\t' -f 2,3) > $output/combined_results.txt
output="./"
extracted_IDs=$(sort -k1,1 -k2,2nr "${output}combined_results.txt" | uniq | sort -k2,2nr | head -n 10 | sed -n 's/AF-\([A-Z0-9]*\)-.*/\1/p')
for ID in $extracted_IDs; do
    #echo $ID
    wget -qO- "https://www.uniprot.org/uniprot/${ID}.txt" | grep "GO;" > $output/${ID}_annotation.txt
done
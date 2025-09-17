This python script is used to combine all the gene trees in PhyloNet format in 
Tree gt0=(...)
Tree gt1=(...)
Tree gt2=(...)
....
After creating the file in the name 'infer_Network_MPL.nexus', you have to manually add the head "#NEXUS" and tail "BEGIN PHYLONET;

InferNetwork_MPL (all) 3 -x 20 -pl 20;

END;" to complete the input.

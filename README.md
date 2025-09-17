Please put all of the gene trees and this script in the same dir. 
Usage: python combine_trees_in_nexus.py.

This python script is used to combine all the gene trees in PhyloNet format in 
Tree gt0=(...)
Tree gt1=(...)
Tree gt2=(...)
....
After generating the file in the name 'infer_Network_MPL.nexus', you have to manually add the head "#NEXUS" and tail "BEGIN PHYLONET;

InferNetwork_MPL (all) 3 -x 20 -pl 20;

END;" to complete the input.

import Bio as Bio
from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import matplotlib
import matplotlib.pyplot as plt

with open("sequence.aln","r") as aln:
	alignment = AlignIO.read(aln,"clustal")
print(type(alignment))

calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)
print(distance_matrix)

constructor = DistanceTreeConstructor(calculator)
tree = constructor.build_tree(alignment)
print(tree)

Phylo.draw_ascii(tree)
Phylo.draw(tree)
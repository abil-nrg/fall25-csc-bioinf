try:
    __codon__
    from biocodon.Bio import motifs
except NameError:
    from Bio import motifs
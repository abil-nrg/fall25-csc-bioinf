from dbg import DBG
from utils import read_data
import sys

sys.setrecursionlimit(1000000000)

if __name__ == "__main__":
    argv = sys.argv
    fdir = './' + argv[1]
    short1, short2, long1 = read_data(fdir)

    k = 25
    dbg = DBG(k=k, data_list=[short1, short2, long1])
    fpath = fdir + 'contig.fasta'
    with open(fpath, 'w') as f:
        for i in range(20):
            c = dbg.get_longest_contig()
            if c is None:
                break
            print(i, len(c))
            f.write(f'>contig_{i}\n')
            f.write(c + '\n')

#!/usr/bin/env python3
import subprocess
import time
import os
from pathlib import Path

FDIR = "week1/data/"
DATASETS = ["data1", "data2", "data3", "data4"]   # list dataset directories here
SCRIPT_PY = "week1/code/main.py"
SCRIPT_CO = "week1/code/main_codon.py"
PYTHON = "python3"
CODON = ["codon", "run", "-release"]

def compute_n50(fasta_file: Path) -> int:
    lengths = []
    with open(fasta_file) as f:
        for line in f:
            if line.startswith(">"):
                continue
            lengths.append(len(line.strip()))
    lengths.sort(reverse=True)
    total = sum(lengths)
    half = total / 2
    csum = 0
    for L in lengths:
        csum += L
        if csum >= half:
            return L
    return 0

def run_cmd(cmd, cwd="."):
    start = time.time()
    subprocess.run(cmd, cwd=cwd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end = time.time()
    return end - start

def fmt_runtime(seconds: float) -> str:
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"

def main():
    print("Dataset\tLanguage\tRuntime\tN50")
    print("-------------------------------------------------------------------------------------------------------")

    for dataset_fname in DATASETS:
        dataset = FDIR + dataset_fname
        outdir = Path(dataset) / "output"
        outdir.mkdir(parents=True, exist_ok=True)

        # Python run
        py_out = outdir / "contigs_py.fasta"
        t = run_cmd([PYTHON, SCRIPT_PY, f"{dataset}/"])
        os.rename(Path(dataset) / "contig.fasta", py_out)
        n50 = compute_n50(py_out)
        print(f"{dataset_fname}\tpython\t\t{fmt_runtime(t)}\t{n50}")

        # Codon run
        codon_out = outdir / "contigs_codon.fasta"
        t = run_cmd(CODON + [SCRIPT_CO, f"{dataset}/"])
        os.rename(Path(dataset) / "contig.fasta", codon_out)
        n50 = compute_n50(codon_out)
        print(f"{dataset_fname}\tcodon\t\t{fmt_runtime(t)}\t{n50}")

if __name__ == "__main__":
    main()

# BIOINFORMATICS Fall 2025 
## Week 1 Delivarable Report
This is the report for the week 1 delivarable which includes all steps and gotchas  

# Repo Set Up  
- Created a repo on my github with a project structure  

- week1/  
    - code/  
        - evaluate.py  
        - main.py  
        - main_codon.py    
        - dbg.py  
        - utils.py    
        - test.py  
    - data/  
        - data1/    
        - data2/  
        - data3/  
        - data4/  
    - evaluate.sh  
    - ai.md  
    - ai.html  
    - report.md    

- Added a Github Actions CI  

# Python Setup & Runs  
- Ran the program on all four data files

# Codon Conversion  
- Had to figure out what exact format codon wanted
- Strongly typed most variables, replaces the empty children from being None to -1, to avoiud the Optional[int] and turn it into int  
- After noticing that codon was running out of memory I tried to rewrite the algorithm iteratievly, but that was too time consuming. I then realized I could just 
> ulimit -s unlimited 
- after reading piazza more carefully 
- It was definetly dificult as there are no blog posts (e.g. stack overflow) talking about specific issues with codon. The documentation left a lot to be desired (maybe a getting started page which tells the user exactly how one would convert python to codon)  
- Benchmarked the codon and python as well  

(quant) abil@abils-machine:~/Documents/univers/bio/week1$ ./evaluate.sh 
+ ulimit -s unlimited
+ python3 evaluate.py
Dataset	Language	Runtime	N50
-------------------------------------------------------------------------------------------------------
data1	python		00:36	9990
data1	codon		00:17	9990
data2	python		01:17	9992
data2	codon		00:37	9992
data3	python		01:27	9824
data3	codon		00:32	9824
data4	python		08:28	159255
data4	codon		05:08	159255

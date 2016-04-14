import preprocess.py
import graph_normalize.py

def read_all_files(path):
    for (dirpath, dirnames, filenames) in walk(path):
        for directory in dirnames:
            read_all_files(join(dirpath,directory))
        for file in filenames:
            if file.endswith(".txt") and file!='README.txt':
                f.append(join(dirpath,file))
        break
    
f = []
read_all_files("data")
for each in f:
    #CALL PREPROCESS FUNCTION HERE
    #CREATE GRAPH OBJECT AND CALCULATE HITS SCORE HERE
    #graph=Graph()
    #graph.set_structure([["d1","d2"],["d1","d3"],["d2","d1"],["d2","d3"],["d3","d2"],["d3","d4"],["d4","d2"]])
    #graph.calculate_scores()
    #graph.HITS()
    #graph.sort_nodes()

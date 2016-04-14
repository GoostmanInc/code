

class Node:
    def __init__(self,name):
        self.name=name
        self.auth_score=0
        self.hub_score=1
        self.HITS_score=0
        
class Graph:
    def __init__(self):
        self.structure={}
        self.threshold=0
        self.window=2
        self.nodeList=[]
    def find(self,name):
        #print("NAME:",name)
        nodeList=self.nodeList
        for node in nodeList:
            #print(node.name)
            if name==node.name:
                #print("FOUND")
                return node
        return "null"
    def set_threshold(self,thresh):
        self.threshold=thresh
    def set_window(self,win):
        self.window=win
    def set_structure(self,wordlist):
        structure=self.structure
        window=self.window
        nodeList=self.nodeList
        for sentence in wordlist:
            for index in range(len(sentence)):
                curr_word=sentence[index]
                next_words=sentence[index+1:index+window]
                if curr_word not in structure:
                    node=Node(curr_word)
                    nodeList.append(node)
                    structure[curr_word]={}
                    for word in next_words:
                        structure[curr_word][word]=1
                else:
                    for word in next_words:
                        if word not in structure[curr_word]:
                            structure[curr_word][word]=1
        print(structure)
    def calculate_scores(self):
        min_delta=0
        max_iterations=100
        structure=self.structure
        nodeList=self.nodeList
        while max_iterations>0:
            max_iterations-=1
            print("AUTH: ")          
            prev_auth=[]
            for each in nodeList:
                prev_auth.append(each.auth_score)
            for out_keys in structure:
                #print("outkeys",out_keys)
                for in_keys in structure[out_keys]:
                    #print(in_keys)
                    curr_node=self.find(in_keys)
                    #print(type(curr_node))
                    curr_node.auth_score+=self.find(out_keys).hub_score
                    #print("CURRENT: ",curr_node.name,curr_node.auth_score)
            flag=0
            total=0
            for index in range(len(nodeList)):
                nodeList[index].auth_score-=prev_auth[index]
                total+=nodeList[index].auth_score
            for each in nodeList:
                each.auth_score/=total
            print("HUB: ")
            prev_hub=[]
            for each in nodeList:
                prev_hub.append(each.hub_score)
            for out_keys in structure:
                for in_keys in structure[out_keys]:
                    curr_node=self.find(out_keys)
                    curr_node.hub_score+=self.find(in_keys).auth_score
                    #print("CURRENT: ",curr_node.name,curr_node.hub_score)
            flag=0
            total=0
            for index in range(len(nodeList)):
                nodeList[index].hub_score-=prev_hub[index]
                total+=nodeList[index].hub_score
            for each in nodeList:
                each.auth_score/=total
            delta=0
            for index in range(len(nodeList)):
                delta+=abs(prev_hub[index] - nodeList[index].hub_score)
            print("Delta:",delta)
            if delta==min_delta:
                for each in nodeList:
                    print(each.name," ",each.auth_score," ",each.hub_score)
                return
            #raw_input()
            
    def HITS(self):
        nodeList=self.nodeList
        for each in nodeList:
            each.HITS_score=(each.hub_score+each.auth_score)/2
        print("HITS")
        for each in nodeList:
                print(each.name," ",each.HITS_score)
    def sort_nodes(self):
        nodeList=self.nodeList
        nodeList.sort(key=lambda x: x.HITS_score, reverse=True)
        for each in nodeList:
                print(each.name," ",each.HITS_score)

#TESTING...
graph=Graph()
graph.set_structure([["d1","d2"],["d1","d3"],["d2","d1"],["d2","d3"],["d3","d2"],["d3","d4"],["d4","d2"]])
graph.calculate_scores()
graph.HITS()
graph.sort_nodes()

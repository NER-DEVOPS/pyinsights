import json
import pprint

import math
import re

names = []
with open("names.txt") as n:
    for l in n:
        n2 = l.split(" ")[0]
        names.append(n2)

def entropy(string):
    "Calculates the Shannon entropy of a string"
    
    # get probability of chars in string
    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]
    
    # calculate the entropy
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])
    
    return entropy
                                                
fields = {
    #'awsRegion': 99000,
    #     'count(*)': 99000,
          
    #     'eventSource': 98987,
    #     'eventName': 98987,
          
         'resources.0.ARN': 91999,
         'resources.1.ARN': 84033,
    #     'userIdentity.arn': 32328,
    #     'errorCode': 2491
}


splitter = re.compile(r"[:/\._-]+")

import collections
with open("total.json") as fi :
    d = json.load(fi)

    overview = collections.Counter()
    named = collections.Counter()
    values = {}
    
            
    for x in d:
        for k in x:

            isnamed = False

            pattern = []
            
            if k in fields :
                #overview[k] = overview[k] +1
                v = x[k]
                v2 = v
                
                for p in re.split(splitter, v):
                    overview[p] = overview[p] +1
                    if p in names:
                        isnamed = True
                        #pattern.append(p)

                    else:
                        #pattern.append(".")
                        v2 = v2.replace(p,"." * len(p))
                        
            if isnamed:
                named[v2] = named[v2]+ 1
                        
                #values[k][v] = values[k][v] + 1
            
    #pprint.pprint(overview)
    #pprint.pprint(values)
    
    for x,y in named.most_common(20000):
        print(x,y,entropy(x))

import json
import pprint

import math

with open("names.txt") as n:
    for l in n:
        n2 = l.split(" ")[0]
        print(n2)

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

import re
splitter = re.compile(r"[:/\._-]+")

import collections
with open("total.json") as fi :
    d = json.load(fi)

    overview = collections.Counter()
    values = {}
    #values2 = {}
    
    #for k in fields:
    #    values[k] = collections.Counter()
        
            
    for x in d:
        for k in x:
            if k in fields :
                #overview[k] = overview[k] +1

                v = x[k]
                
                for p in re.split(splitter, v):

                    overview[p] = overview[p] +1
                #values[k][v] = values[k][v] + 1
            
    #pprint.pprint(overview)
    #pprint.pprint(values)
    
    for x,y in overview.most_common(20000):
        if re.match(r"^[a-zA-Z]+$",x):
            print(x,y,entropy(x))

import json
import pprint

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

import collections
with open("total.json") as fi :
    d = json.load(fi)

    overview = collections.Counter()
    values = {}
    
    for k in fields:
        values[k] = collections.Counter()
        
            
    for x in d:
        for k in x:
            if k in fields :
                overview[k] = overview[k] +1
                v = x[k]
                values[k][v] = values[k][v] + 1
            
    pprint.pprint(overview)
    pprint.pprint(values)

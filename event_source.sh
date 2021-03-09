jq '.[]|.eventSource' all_*.json | sort | uniq -c | sort -n > eventsources
jq '.[]|keys' all_*.json | sort | uniq -c > fields.txt
jq '.[]|.["userIdentity.arn"]' all_*.json | sort | uniq -c | sort -n > users.txt
jq '.[]|.eventSource +"|"+.eventName' all_*.json | sort | uniq -c | sort -n  > event_names.txt
jq '.[]|.errorCode' all_*.json | sort | uniq -c | sort -n > errorCode

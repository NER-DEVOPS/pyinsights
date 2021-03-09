grep -h -v '\\[0m' *.json | jq '.[]|.["userIdentity.arn"]' | sort | uniq -c | sort -n  > users2.txt 

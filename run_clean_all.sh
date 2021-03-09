grep -h -v '\\[0m' *.json *.yml | jq . > total.txt

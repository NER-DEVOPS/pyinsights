jq '.[]|select(.errorCode=="AccessDenied")' all_*.json

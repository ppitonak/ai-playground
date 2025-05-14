DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
source $DIR/.env

curl -X POST \
    "$MODELS_CORP_API_URL/v1/completions" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $MODELS_CORP_API_KEY" \
    -d '{
    "model": "'$MODELS_CORP_MODEL'",
    "prompt": "Poprad is a",
    "max_tokens": 15,
    "temperature": 0
}'

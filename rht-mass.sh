source .env

echo -e "=== Deepseek R1 14B ===\n"
curl -X POST \
    "$DEEPSEEK_API_URL/v1/completions" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
    -d '{
    "model": "'$DEEPSEEK_MODEL'",
    "prompt": "Poprad is a",
    "max_tokens": 15,
    "temperature": 0
}'

echo -e "\n=== Granite 8B ===\n"
curl -X POST \
    "$GRANITE_API_URL/v1/completions" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GRANITE_API_KEY" \
    -d '{
    "model": "'$GRANITE_MODEL'",
    "prompt": "Poprad is a",
    "max_tokens": 15,
    "temperature": 0
}'
$apiKey = "<API_KEY>"
# Define the OpenAI API endpoint
$endpoint = "https://api.openai.com/v1/chat/completions"

# Define the request payload
$jsonPayload = @{
    model = "gpt-3.5-turbo-0125"
    messages = @(@{role="user"; content="Say this is a test!"})
    temperature = 0.7
} | ConvertTo-Json
$jsonPayload

# Print the response
$response
try {
    $response = Invoke-RestMethod -Uri $endpoint -Method Post -Headers @{ "Authorization" = "Bearer $apiKey"; "Content-Type" = "application/json" } -Body $jsonPayload
    $response
} catch {
    Write-Host "Error: $($_.Exception.Message)"
}

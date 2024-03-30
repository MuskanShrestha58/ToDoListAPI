import requests
import json

response = requests.get(
    'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# Print the HTTP response status code
print(response)
# Print the JSON response data (useful for debugging)
print(response.json())

# Iterate over each question item in the response
for data in response.json()['items']:
    # Check if the question has no answers
    if data['answer_count'] == 0:
        # Print the title of the unanswered question
        print(data['title'])
        # Print the link to the unanswered question
        print(data['link'])
    else:
        # If the question has answers, indicate it was skipped
        print('skipped')
    # Print a blank line for better readability between questions
    print()

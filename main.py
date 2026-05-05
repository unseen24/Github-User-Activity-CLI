import argparse
import requests

github_api_url = "https://api.github.com/"
def get_user_activity(username):
    user_event_url = f"{github_api_url}users/{username}/events"
    response = requests.get(user_event_url)

    if response.status_code == 200:
        user_data = response.json()
        print('Data retrieved successfully!')
        return user_data
        
    else:
        print('Failed to retrieve data. Status code:', response.status_code)

def main():
    parser = argparse.ArgumentParser(description='Github User Activity')

    parser.add_argument('-username', type=str, required=True, help='Github username')

    args = parser.parse_args()

    if args.username != None:
        username = args.username
        user_data = get_user_activity(username)


#iterate user_data(list) values
    for event in user_data:
        #get specific value (type) and check if its a CreateEvent
        if event['type'] == 'CreateEvent':
            print(f'{username} Created a branch at {event["repo"]["name"]}')

        elif event['type'] == 'PushEvent':
            print(f'{username} Pushed {event["commits"].length} to {event["payload"]["ref"].removeprefix("refs/heads/")} at {event["repo"]["name"].split("/")[1]}')
if __name__ == "__main__":
    main()
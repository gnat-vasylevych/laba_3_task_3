import requests


def get_data(access_token: str, name: str):
    """
    Requests information about name with API access_token
    """
    base_url = "https://api.twitter.com/"

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
        }

    search_params = {
        'screen_name': name,
        'count': 20
    }

    search_url = '{}1.1/friends/list.json'.format(base_url)
    response = requests.get(search_url, headers=search_headers, params=search_params)
    return response.json()


def extract_info(data: dict):
    """
    Extract location and screen_name of users
    """
    check = []
    friends = []
    for elem in data['users']:
        if elem['location'] != '' and elem['location'] not in check:
            check.append(elem['location'])
            location = elem['location']
            screen_name = elem['screen_name']
            friends.append((location, screen_name))
    return friends

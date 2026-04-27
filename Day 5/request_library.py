import requests

def get_github_user(username):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()

        print("Username:", data["login"])
        print("Name:", data["name"])
        print("Public Repos:", data["public_repos"])
        print("Followers:", data["followers"])
        print("Following:", data["following"])
    else:
        print("User not found!")


# Call function
get_github_user("abdulrehman538")
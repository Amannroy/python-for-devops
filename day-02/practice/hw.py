import requests
import json

#API_KEY = "dabb41bdfbeb488eaa812971ce14a172"

api_url = 'https://api.github.com/users/octocat'

# 3 Step-> Fetch Data, Print Data, Save Data

# Function to fetch data
def fetch_github_user():
    response = requests.get(api_url)

    # Convert response to JSON
    data = response.json()
    
    # Extracting meaningful information
    user_data = {
        "username": data.get("login"),
        "name": data.get("name"),
        "public_repositories": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "profile_url": data.get("html_url"),
    }

    return user_data

# Function to save data into JSON file
def save_to_json(data):
    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)


# Main function (program starts here)
def main():
    # Fetch data from Github API
    user_data = fetch_github_user()

    #Print data on terminal
    print("Processed Github User Data:")
    print(user_data)

    # Save data into JSON file
    save_to_json(user_data)

    print("\nData saved successfuly to output.js")


# Run main function
if __name__ == "__main__":
    main()


import requests


def get_user(user_id):

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response = requests.get(url)

    return response


def test_get_user(user_id):

    response = get_user(user_id)

    data = response.json()

    print(f"\nTesting User {user_id}")

    if response.status_code == 200:
        print("✅ Status code test: PASS")
    else:
        print("❌ Status code test: FAIL")

    if "username" in data:
        print("✅ Username test: PASS")
    else:
        print("❌ Username test: FAIL")

    if "id" in data:
        if data["id"] == user_id:
            print("✅ User ID test: PASS")
        else:
            print("❌ User ID test: FAIL")
    else:
        print("❌ User does not exist")


for user_id in [1, 2, 3, 999]:
    test_get_user(user_id)
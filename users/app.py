import json

"""Simple lambda function to create and fetch users from mock db"""


def get_users(event, context):
    """Fetch all users"""
    return {
        "statusCode": 200,
        "body": json.dumps({"Name": "Methuselah", "Age": 190}),
        "Content-Type": "application/json",
    }


def create_user(event, context):
    """Test POST request by creating a user"""
    user_object = event.get("body")
    user = user_object
    user_name = json.loads(user).get("Name")
    return {"statusCode": 201, "body": f"User {user_name} created successfully"}

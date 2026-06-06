import json


def get_users(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"Name": "Methuselah", "Age": 190}),
        "Content-Type": "application/json",
    }


def create_user(event, context):
    user_object = event.get("body")
    user = user_object
    user_name = json.loads(user).get('Name')
    return {"statusCode": 201, "body": f"User {user_name} created successfully"}

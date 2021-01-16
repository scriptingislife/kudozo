import json
import logging
import os
import time
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')

def main(event, context):
    data = json.loads(event['body'])
    if 'value' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create feedback item.")

    timestamp = str(time.time())
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'createdAt': timestamp,
        'value': data["value"]
    }

    table.put_item(Item=item)

    body = {
        "message": "Thank you for your feedback!",
        "item": item,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
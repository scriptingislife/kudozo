import os
import json
import boto3

def get_table_items(dynamodb, TableName):
    paginator = dynamodb.get_paginator("scan")
    for page in paginator.paginate(TableName=TableName):
        yield from page["Items"]

def main(event, context):
    dynamodb = boto3.client('dynamodb')
    table = os.environ['DYNAMODB_TABLE']
    items = get_table_items(dynamodb, table)
    paths = {}
    for item in get_table_items(dynamodb, TableName=table):
        value = int(item["value"]["N"])
        if value == 0:
            feedback = "Not Helpful"
        elif value == 1:
            feedback = "Helpful"
        else:
            feedback = "wat"

        path = item["path"]["S"]
        if path not in paths:
            paths[path] = {}
        if feedback not in paths[path]:
            paths[path][feedback] = 1
        else:
            paths[path][feedback] = paths[path][feedback] + 1
        


    response = {
        "statusCode": 200,
        "body": json.dumps(paths)
    }

    return response

if __name__ == "__main__":
    main(None, None)
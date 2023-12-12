import os
import json
import datetime
from urllib.parse import unquote


def main(event, context):
    referer = event["headers"].get("Referer", "")
    origin = event["queryStringParameters"]["url"]

    #print(referer)
    print(origin)
    
    origin = unquote(origin)
    print(origin)

    with open("html/button.html", "r") as html:
        body = html.read()

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
            "Access-Control-Allow-Origin": "*"
        },
        "body": body % (os.environ.get("FEEDBACK_URL"), origin)
    }

    return response
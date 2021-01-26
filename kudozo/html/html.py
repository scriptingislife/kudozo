import os
import json
import datetime


def main(event, context):
    with open("html/button.html", "r") as html:
        body = html.read()

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
            "Access-Control-Allow-Origin": "*"
        },
        "body": body%os.environ.get("FEEDBACK_URL")
    }

    return response
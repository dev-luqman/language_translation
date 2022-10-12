import json
import boto3


def lambda_handler(event, context):
    # setup boto3 
    client = boto3.client('translate', region_name='us-east-1')
    sampleText = "holla madrid"
    res = client.ranslate_text(Text=sampleText, SourceanguageCode="auto")
    
    
    # format the response as JSON and return the result
    response = {
        "statusCode": "200",
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"res": res})
    }

    return response
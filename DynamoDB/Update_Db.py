import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('heydevops')
print(table.creation_date_time)

table.update_item(
    Key={
        'username': 'henry',
        'last_name': 'kumah'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)

def lambda_handler(event, context):
    message = ""

    try:
        if 'name' in event:
            name = event['name']
            message = f'Hello {name}'
        else:
            message = "Hello from Lambda"
        
        return {
            'statusCode': 200,
            'message': message
        }
    except ex:
        return {
            'statusCode': 400,
            'message': 'exception occurred'
        }
    

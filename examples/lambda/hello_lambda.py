import os

def lambda_handler(event, context):
    return "{} from Lambda and Arslan!".format(os.environ['greeting'])

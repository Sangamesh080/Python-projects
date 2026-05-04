import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'sangameshbhai')
    AWS_REGION = 'ap-south-2'
    DYNAMODB_TABLE = 'todo_tasks'
    SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
    EMAIL = "sgb080.gitam@gmail.com"

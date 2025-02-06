from django.db import models

# Create your models here.

import boto3
from django.conf import settings
import uuid

# Initialize DynamoDB
dynamodb = boto3.resource(
    'dynamodb',
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
)

# Get DynamoDB Table
table = dynamodb.Table(settings.AWS_DYNAMODB_TABLE)


class Task:
    """Task model using DynamoDB"""

    @staticmethod
    def create_task(title, description):
        task_id = str(uuid.uuid4())
        task = {
            'task_id': task_id,
            'title': title,
            'description': description,
            'status': 'pending'
        }
        table.put_item(Item=task)
        return task

    @staticmethod
    def list_tasks():
        response = table.scan()
        return response.get('Items', [])

    @staticmethod
    def get_task(task_id):
        response = table.get_item(Key={'task_id': task_id})
        return response.get('Item')

    @staticmethod
    def update_task(task_id, title, description):
        table.update_item(
            Key={'task_id': task_id},
            UpdateExpression="SET title = :title, description = :desc",
            ExpressionAttributeValues={
                ':title': title,
                ':desc': description
            }
        )
        return Task.get_task(task_id)

    @staticmethod
    def complete_task(task_id):
        table.update_item(
            Key={'task_id': task_id},
            UpdateExpression="SET status = :status",
            ExpressionAttributeValues={':status': 'completed'}
        )
        return Task.get_task(task_id)

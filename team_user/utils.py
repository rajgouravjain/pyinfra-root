# pyinfra airflow
# File: pyinfra_airflow/util.py
# Desc: general utilities!

from os import path
import boto3
import requests
import json
import base64
from requests import HTTPError
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError

def get_template_path(file):
    return path.join(
        path.dirname(__file__),
        "templates",
        file,
    )

def get_file_path(file):
    return path.join(
        path.dirname(__file__),
        "files",
        file,
    )

def get_task_path(file):
    return path.join(
        path.dirname(__file__),
        "tasks",
        file,
    )

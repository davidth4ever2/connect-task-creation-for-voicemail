#!/usr/bin/env python3

import os

import aws_cdk as cdk


from record_comprend_task.record_comprend_task_stack import RecordComprendTaskStack


app = cdk.App()
RecordComprendTaskStack(app, "record-comprend-task", env=cdk.Environment(
                                                        account=os.environ["CDK_DEFAULT_ACCOUNT"],
                                                        region=os.environ["CDK_DEFAULT_REGION"]))

app.synth()

import aws_cdk as core
import aws_cdk.assertions as assertions

from connect_task_creation_for_voicemail.connect_task_creation_for_voicemail_stack import ConnectTaskCreationForVoicemailStack

# example tests. To run these tests, uncomment this file along with the example
# resource in connect_task_creation_for_voicemail/connect_task_creation_for_voicemail_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ConnectTaskCreationForVoicemailStack(app, "connect-task-creation-for-voicemail")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

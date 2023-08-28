import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_git_hub1.cdk_git_hub1_stack import CdkGitHub1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_git_hub1/cdk_git_hub1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkGitHub1Stack(app, "cdk-git-hub1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

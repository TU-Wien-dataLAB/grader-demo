import os

from grader_service.autograding.local_grader import LocalAutogradeExecutor

c.GraderService.service_host = "127.0.0.1"
# existing directory to use as the base directory for the grader service
service_dir = os.path.expanduser("~/Documents/Work/grader_service_dir")

c.JupyterHubGroupAuthenticator.hub_api_url = "http://127.0.0.1:8081/hub/api"

c.LocalAutogradeExecutor.base_input_path = os.path.expanduser(os.path.join(service_dir, "convert_in"))
c.LocalAutogradeExecutor.base_output_path = os.path.expanduser(os.path.join(service_dir, "convert_out"))

c.RequestHandlerConfig.autograde_executor_class = LocalAutogradeExecutor

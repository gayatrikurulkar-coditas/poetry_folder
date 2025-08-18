from cleo.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin
import subprocess


class RunMainCommand(Command):
    name = "run-main"
    description = "Run the project's main.py file"

    def handle(self) -> int:
        # Run "python main.py"
        result = subprocess.run(["python", "main.py"])
        return result.returncode


def factory():
    return RunMainCommand()


class RunMainPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory("run-main", factory)

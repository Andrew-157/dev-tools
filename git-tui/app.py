#!./venv/bin/python

import subprocess

from textual.app import App, ComposeResult
from textual.widgets import Label, Button

class GitUtils:

    @staticmethod
    def get_branches() -> list[str]:
        subprocess.run("git pull".split())
        branches = subprocess.check_output("git branch -r".split()).decode().split('\n')[1:-1]
        for i, br in enumerate(branches):
            branches[i] = br.strip().replace("origin/", "")
        return branches

    @staticmethod
    def checkout(branch_name: str) -> None:
        subprocess.run(f"git checkout {branch_name}".split())


class GitApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label("branches for the current repository")
        branches = GitUtils.get_branches()
        for branch in branches:
            yield Button(branch, id=branch, variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        GitUtils.checkout(branch_name=event.button.id)
        self.exit(event.button.id)


if __name__ == "__main__":
    app = GitApp()
    print(f'Checked Out to branch: "{app.run()}"')


#!./venv/bin/python

import subprocess

from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Label

class GitUtils:
    # TODO: do not use subprocess to run git commands, use some library for that

    # TODO: check somewhere that we are inside git repository before even starting the app
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

    TITLE = "Git TUI App"
    SUB_TITLE = "App for gitting gud with your branches without moving a mouse"

    def compose(self) -> ComposeResult:
        yield Header()
        branches = [Button(branch, id=branch, variant="primary") for branch in GitUtils.get_branches()]
        yield from branches

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id:
            GitUtils.checkout(branch_name=event.button.id)
        self.exit(event.button.id)

    def on_mount(self):
        # TODO: try to use `from textual.color import Color`
        self.screen.styles.background = "blue"

    def action_quit(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = GitApp()
    result = app.run()
    if result:
        print(f'Checked Out to branch: "{result}"')
    else:
        print("Branch wasn't selected")


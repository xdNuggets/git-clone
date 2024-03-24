from rich.console import Console
from rich.text import Text
from rich import print as rprint
import typer
import os

app = typer.Typer()
console = Console()

@app.command()
def init():
    init = True if os.path.exists(".git") else False

    if not init:
        os.makedirs(".git")
        os.makedirs(".git/objects")
        os.makedirs(".git/refs")
        os.write(".git/HEAD", "ref: refs/heads/master")
    rprint(f"{"[bold green]Initialized" if init else "[bold green]Reinitialized"} empty Git repository in [yellow] {os.getcwd()}/.git/")
        

    



if __name__ == "__main__":
    app()
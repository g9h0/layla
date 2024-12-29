"""CLI application for the Layla app modules"""

from shutil import copyfile, copytree
import os
import click
from .app import convert_md_to_html


@click.group()
def cli():
    pass


@click.command()
def init():
    """Initialize a new blog site in the current working directory"""

    os.makedirs("html/assets", exist_ok=True)
    os.makedirs("content", exist_ok=True)

    src = os.path.join(os.path.dirname(__file__), "templates")
    copytree(src, "templates", dirs_exist_ok=True)

    copyfile("templates/bg.png", "html/assets/bg.png")

    click.echo("Initialized")


@click.command()
@click.option(
    "--md",
    help="The directory containing the markdown files, to be converted to HTML",
    default="content",
)
def build(md):
    """Build static site"""

    copyfile("templates/stylesheet.css", "html/stylesheet.css")
    copyfile("templates/prism.js", "html/prism.js")

    try:
        convert_md_to_html(md_dir=md)
    except FileNotFoundError:
        print("Path does not exist")


cli.add_command(init)
cli.add_command(build)

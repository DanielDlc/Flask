import click

from blog.posts import (
    get_all_posts,
    get_post_by_slug,
    new_post,
    update_post_by_slug,
)


@click.group()
def post():
    """MAnage blog post"""


@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    new = new_post(title, content)
    click.echo(f"New post created {new}")


def configure(app):
    app.cli.add_command(post)
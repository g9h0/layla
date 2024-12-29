"""A static site generator that converts markdown files to HTML"""

import os
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

md = markdown.Markdown(extensions=["meta", "fenced_code"])

jinja_env = Environment(
    loader=FileSystemLoader("templates"), autoescape=select_autoescape()
)


def read_file(file: str) -> None:
    """A helper function that reads a file and returns the content"""
    with open(file, "r", encoding="utf-8") as f:
        return f.read()


def convert_md_to_html(md_dir: str, html_dir: str = "html/") -> None:
    """A function that converts markdown to HTML.  The function accepts a directory path containing markdown files, and a directory path where rendered HTML files will be saved."""

    # A list of dicts. Used to build index.html
    blog_posts = []

    for file in os.listdir(os.path.join(md_dir, "")):
        if ".md" in file:
            with open(os.path.join(md_dir, "") + file, "r", encoding="utf-8") as m:
                html = md.convert(m.read())

                try:
                    if md.Meta["status"][0] == "published":
                        blog_posts.append(
                            {
                                "date": md.Meta["date"][0],
                                "title": md.Meta["title"][0],
                                "filename": os.path.splitext(file)[0] + ".html",
                            }
                        )

                except KeyError as e:
                    print(f'Front matter is missing key "{e.args[0]}" in file "{file}"')
                    continue

                blog_template = jinja_env.get_template("blog.html")

                with open(
                    html_dir + os.path.splitext(file)[0] + ".html",
                    "w",
                    encoding="utf-8",
                ) as h:

                    try:
                        h.write(
                            blog_template.render(
                                title=md.Meta["title"][0],
                                date=md.Meta["date"][0],
                                blog_body=html,
                            )
                        )

                    except KeyError as e:
                        print(
                            f'Front matter is missing key "{e.args[0]}" in file "{file}"'
                        )
                        continue

                md.reset()

    sorted_blog_posts = sorted(blog_posts, key=lambda x: x["date"], reverse=True)

    index_template = jinja_env.get_template("index.html")

    with open(html_dir + "index.html", "w", encoding="utf-8") as h:
        h.write(index_template.render(posts=sorted_blog_posts))

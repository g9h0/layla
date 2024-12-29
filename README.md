<img src='layla.webp' alt='layla cat' width='200px'>

# What is Layla?

`Layla` is a simple static site generator that is used to build the g9h.io blog.  `Layla` provides a command line interface for initializing and building a static site.

## Build and install

1) Install [Poetry](https://python-poetry.org/docs/#installation)

```shell
pipx install poetry
```

2) Clone and cd into this repository

```shell
git clone https://github.com/g9h0/layla.git && cd layla
```

3) Build and install `layla`

```shell
poetry build && pip install dist/layla-0.1.0.tar.gz
```

## How to use

1) Create a directory and cd into it

```
mkdir my-blog && cd my-blog
```

2) Initialise a new blog

```shell
layla init
```

3) Create a blog post and save it to the `content` directory

```shell
cat << EOF > content/hello-world.md
---
title: Hello World
date: 2024-12-01
---
Hello Wolrd
EOF
```

4) Build the static.  The `--md` parameter takes a path containing the markdown files

```shell
layla build --md content
```

5) Inspect and open `html/index.html`

## Customization

You can customize the blog site by editing the template files in the `templates` directory and running `layla build`.

`html/bg.png` is created on `layla init`.  To update or remove the background image, simply replace or delete `html/bg.png`.  If you are removing the background image, you should remove the reference from `templates/stylesheet.css` and run `layla build`.

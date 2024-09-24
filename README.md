# PGConf.dev Static Site

This repository contains both the content of the PGConf.dev static site as well
as the tooling required to render it. All tasks are executed through [Invoke].

## Prerequisites

* Git ≥ 2.40
* Python ≥ 3.11

## Setup

1. Clone the repository and `cd` into it:

   ```bash
   git clone git@github.com:ktchen14/static-site.git
   cd static-site
   ```

2. If you have [direnv](https://direnv.net), then you just need to authorize the
   bundled `.envrc`:

   ```bash
   direnv allow
   ```

   Otherwise, create a virtualenv and activate it:

   ```bash
   python3 -m venv .venv
   . .venv/bin/activate
   pip3 install --upgrade pip
   ```

3. Install dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Verify that [Invoke](https://www.pyinvoke.org/) is runnable by listing tasks
   with `invoke -l`. The output should resemble:

   ```
   Available tasks:

     render   Render the static site (into `site`)
     server   Open an HTTP server to serve the rendered site
   ```

## Rendering the Site

Use the `invoke render` command to render the site. The output should resemble:

```
Rendering 'index.html.j2' to 'site/index.html' ...
Copying 'static/img/icons/apple-touch-icon.png' to 'site/static/img/icons/apple-touch-icon.png' ...
...
Copying 'static/news.js' to 'site/static/news.js' ...
```

This command copies each file in the repository into its corresponding location
in the `site` subdirectory.

Any file ignored by Git, or having the `site-ignore` Git attribute, is skipped.
Files with the `.j2` extension are rendered using Jinja2 before being copied to
a destination file without the `.j2` extension.

## Testing the Site

You can open rendered files in the `site` subdirectory directly in a browser to
test the site.

To ensure that the site looks as expected when it's served from an actual web
server, use the `invoke server` command to open an HTTP server that will serve
the `site` subdirectory.

[Invoke]: https://www.pyinvoke.org/

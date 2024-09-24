# PGConf.dev Static Site

This project contains both the content of the PGConf.dev static site as well as
the tooling required to render it. All tasks are executed through [Invoke].

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

4. Verify that [Invoke](https://www.pyinvoke.org/) is runnable:

   ```bash
   $ invoke -l
   Available tasks:

     render   Render the static site (into `site`)
     server   Open an HTTP server to serve the rendered site
   ```

## Rendering the Site

Use the `invoke render` command to render
Use `invoke render` to render the site.

[Invoke]: https://www.pyinvoke.org/

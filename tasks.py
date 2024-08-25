from invoke import task
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import shutil
import subprocess
import yaml

ROOT = Path("site")


@task
def render(c):
    """Render the static site (into `site`)"""

    # Add each cached and untracked file to the site
    command = ("git", "ls-files", "-coz", "--exclude-standard")
    output = subprocess.check_output(command, text=True)
    site = set(output.removesuffix("\x00").split("\x00"))

    # Then remove each file with "site-ignore" set
    command = ("git", "check-attr", "-z", "site-ignore", "--", *site)
    output = subprocess.check_output(command, text=True)
    while output:
        name, _, status, output = output.split("\x00", 3)
        if status not in ("no", "unspecified"):
            site.remove(name)

    # Delete each untracked file in the output root
    subprocess.check_call(("git", "clean", "-fqx", ROOT))

    # Create the Jinja2 environment and context
    environment = Environment(loader=FileSystemLoader("."))
    with open("context.yaml") as f:
        context = yaml.safe_load(f) or {}

    # Render each extant source file in sorted order
    for source in sorted(Path(i) for i in site if Path(i).is_file()):
        target = ROOT / source
        target.parent.mkdir(parents=True, exist_ok=True)

        if source.suffix != ".j2":
            print(f"Copying {str(source)!r} to {str(target)!r} ...")
            shutil.copyfile(source, target)
            continue

        target = target.with_suffix("")
        with open(target, "w") as f:
            print(f"Rendering {str(source)!r} to {str(target)!r} ...")
            template = environment.get_template(str(source))
            f.write(template.render(context))


@task(help={"port": "port number to open the HTTP server on"})
def server(c, port=8000):
    """Open an HTTP server to serve the rendered site"""

    from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
    import functools

    site = functools.partial(SimpleHTTPRequestHandler, directory=ROOT)
    with ThreadingHTTPServer(("127.0.0.1", port), site) as server:
        print(f"Opened HTTP server at http://127.0.0.1:{port}/ ...")
        server.serve_forever()

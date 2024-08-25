# PGConf.dev Static Site

## Setup

Clone the repository and `cd` into it:

```bash
git clone git@github.com:ktchen14/static-site.git
cd static-site
```

If you have [direnv](https://direnv.net), then you just need to authorize the
bundled `.envrc`. Otherwise, create a virtualenv and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

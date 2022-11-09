# Alembic Expand-Contract Demo

The source code for [my talk from PyCon Ireland 2022][pycon]. An accompanying
blog can be found [here][blog] while the slides are available [here][slides].

The history of this repo is intentionally configured so that you can view the
evolution of the models and test how alembic handles the migrations.

## Usage

Create a virtualenv and install the requirements:

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

[pycon]: https://python.ie/pycon-2022/schedule/
[blog]: https://that.guru/blog/zero-downtime-upgrades-with-alembic-and-sqlalchemy/
[slides]: https://that.guru/talks/zero-downtime-upgrades-with-alembic-and-sqlalchemy/

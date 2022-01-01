# Jaborg's annals of retrospection

This repositry contains the source code for the erudite retrospections of Jaborg the Wise. It is said that Jaborg the Wise once read 48 books in 365 earth day cycles.

## Developer notes

This is a python backend. To make changes to this repository, install poetry. It is recommended to install this in your global python. Thus:

```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Verify correct installation:

```bash
$ poetry --version
Poetry version X.Y.Z
```

More detailed poetry installation can be found [here](https://python-poetry.org/docs/)

The `Makefile` will provide you with handy commands. Check it out. For example, try `make lint`.

## TODOs

- - Containerise your application, preferably using something like docker or podman.
- - Make each "service" of your application standalone. A good way to start off with this locally is to make your application an image, use a database image, such as postgres, etc. This will make it easier to replicate sections of your application when you host it on the cloud.
    -

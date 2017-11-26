# simple-sanic

| `simple-sanic` is a drop-in replacement of `http.server`. It allows to serve the content of the current directory as static files. Except much faster! :rotating_light::boom:

With `http.server`:

```sh
$ python -m http.server
```

With `simple-sanic`:

```sh
$ python -m simple-sanic
```

So why bother? `Sanic` is orders of magnitude faster than `http.server`! For a
bit more details see: [A Faster http.server using Sanic](http://remusao.github.io/posts/faster-http-server-sanic.html).

# Installation

`simple-sanic` requires python 3.5+ to work.
```sh
$ pip install simple-sanic
```

Then simply run:
```sh
$ python -m simple-sanic
```

You can also customize the `host` and `port`:
```sh
$ python -m simple-sanic --help
Usage:
    simple-sanic [options]
    simple-sanic -h | --help

Options:
    -p --port PORT      Specify alternate port [default: 8000]
    -b --bind ADDRESS   Specify alternate bind address [default: 0.0.0.0]
    -h, --help          Show this help message and exit.
```

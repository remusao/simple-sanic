# simple-sanic

This is a drop-in replacement of `http.server`. It allows to serve the content
of the current directory as static files.

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

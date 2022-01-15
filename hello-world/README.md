# Simple REST API using FastAPI

 How to build the container and run the application in the container image
```
$ podman build -t fastapi .
$ podman images
$ podman run --rm -v $PWD:/srv:z -p 8000:8000 --name fastapi -d fastapi
$ curl http://127.0.0.1:8000
$ podman stop fastapi
```

To access the logs
```
podman logs fastapi
```

To generate the file history.txt
```
dnf history | tail --lines=+3 > history.txt
```

Accessing using culr
```
$ curl http://127.0.0.1:8000 | python -m json.tool
```

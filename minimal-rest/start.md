# Steps to execute

```
podman network create todo-net # if not created
podman build -t todo-api:1.0 .
podman run -d \
  --name todo-api \
  --network todo-net \
  --env-file .env \
  -p 8000:8000 \
  todo-api:1.0
podman stop todo-api;podman rm todo-api
```

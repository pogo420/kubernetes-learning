# Steps to execute

```
podman network create todo-net # if not created
podman build -t todo-app:1.0 .
podman run -d \
  --name todo-app \
  --network todo-net \
  --env-file .env \
  -p 8000:8000 \
  todo-app:1.0
podman stop todo-app;podman rm todo-app
```

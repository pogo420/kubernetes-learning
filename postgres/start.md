
# Steps to execute

```
podman network create todo-net # if not created
podman volume create todo-postgres-data
podman build -t todo-postgres:1.0 .
podman run -d --name todo-postgres --env-file .env -v todo-postgres-data:/var/lib/postgresql/data  --network todo-net todo-postgres:1.0
podman stop todo-postgres; podman rm todo-postgres
```

# k8s workload

* Introduction:
   * Management of workloads via deployments -> replica set -> pod. 
   * Different container usage in pod will be covered.

* Rolling Update

```
1. Changing the Deployment's Pod template
   → creates a new ReplicaSet

2. New ReplicaSet
   → creates new Pods

3. Old ReplicaSet
   → gradually scales to 0

4. Old ReplicaSet is retained
   → useful for rollout history / rollback

5. Pods themselves aren't upgraded
   → old Pods are replaced by new Pods

# kubectl provides support rollout history and undo option(to prev/specific version) 
```

* Init containers

```
Pod starts
    ↓
Init Container 1
    ↓ success
Init Container 2
    ↓ success
...
    ↓
Application Containers start

-------------------------------------------
init: exit 0 → Todo API starts ✅

init: exit 1 → init retried
             → Todo API never starts ❌
```

* Sidecar

    * Intro

    ```
    Pod
    ├── todo-api        ← main container
    └── sidecar         ← helper container

    Both run together
    ```

    * Network and volumes:

    ```
    Same network namespace
    → same Pod IP
    → can communicate using localhost

    Volumes can be shared
    → both containers can access shared files
    -------------------------------------------------------------
    Network namespace → automatically shared by containers in Pod

    Filesystem        → NOT automatically shared
                        requires a Volume + volumeMounts
    ```

    * With init + sidecar

    ```
    Init Container
    ↓ completes
    App starts

    Sidecar + App
        ↓
    run alongside each other
    ```

* Jobs and CronJob

    ```
    Job     → Runs a task until successful completion.
            Job → Pod → Completed.

    CronJob → Runs Jobs on a schedule.
            CronJob → Job → Pod → Completed.

    Both use normal Pod specs → can have init containers, sidecars, volumes, etc.
    ```

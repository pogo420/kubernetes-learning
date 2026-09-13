# K8s basics

* Introduction

```
CONTROL PLANE
├── API Server           → entry point
├── etcd                 → state
├── Scheduler            → where to run
└── Controller Manager   → maintain desired state


WORKER NODE
├── Kubelet              → manage Pods on this node
├── Container Runtime    → run containers
└── Pods                 → application workloads
```

* Cluster/Node

```
Cluster = Group of machines

Node    = One machine

Pod     = Workload running on a machine

PS: Machine can be physical or virtual.
```
 
# Kubernetes Learning Roadmap — Architect-Level Lab

## Application Architecture

```text
                Gateway API
                     │
                     ▼
              ┌─────────────┐
              │   Todo API   │
              │ Deployment   │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │ PostgreSQL  │
              │ StatefulSet │
              └─────────────┘
```

---

# Phase 1 — Kubernetes Fundamentals

1. Kubernetes cluster architecture
2. Control plane vs worker nodes
3. API Server
4. Scheduler
5. Controller Manager
6. etcd
7. Kubelet
8. Container runtime
9. Desired state and reconciliation
10. Namespaces
11. Labels and selectors
12. `kubectl` fundamentals

---

# Phase 2 — Workloads

1. Pods
2. Pod lifecycle
3. Pod states
4. Containers inside Pods
5. Deployments
6. ReplicaSets
7. Desired replicas
8. Rolling updates
9. Rollbacks
10. Init containers
11. Sidecars
12. Jobs
13. CronJobs

---

# Phase 3 — Networking

1. Pod networking
2. Services
3. ClusterIP
4. NodePort
5. Service discovery
6. CoreDNS
7. EndpointSlices
8. Gateway API
9. Gateway
10. GatewayClass
11. HTTPRoute
12. Listeners
13. Host/path routing
14. TLS
15. Cross-namespace routing

---

# Phase 4 — Configuration & Storage

1. ConfigMaps
2. Secrets
3. Environment variables
4. Configuration mounted as files
5. Volumes
6. PersistentVolumes
7. PersistentVolumeClaims
8. StorageClasses
9. Dynamic provisioning
10. StatefulSets
11. Persistent PostgreSQL
12. Storage lifecycle
13. Reclaim policies
14. Backup and restore concepts

---

# Phase 5 — Reliability & Application Health

1. Startup probes
2. Readiness probes
3. Liveness probes
4. Graceful shutdown
5. Container termination lifecycle
6. `terminationGracePeriodSeconds`
7. `preStop`
8. Resource requests
9. Resource limits
10. QoS classes
11. OOMKilled
12. PodDisruptionBudgets
13. Rolling deployments
14. Application availability

---

# Phase 6 — Scheduling

1. Kubernetes Scheduler
2. Node selectors
3. Node affinity
4. Pod affinity
5. Pod anti-affinity
6. Taints
7. Tolerations
8. Topology spread constraints
9. Priority
10. Preemption
11. Scheduling troubleshooting

---

# Phase 7 — Kubernetes Security

Security is treated as a continuous concern rather than a final phase.

### Identity & Authorization

1. Authentication
2. Authorization
3. RBAC
4. Users
5. Groups
6. ServiceAccounts
7. Role
8. ClusterRole
9. RoleBinding
10. ClusterRoleBinding
11. Kubernetes verbs
12. Namespace-scoped vs cluster-scoped permissions
13. Least privilege

### Workload Security

14. Pod Security Standards
15. Privileged / Baseline / Restricted
16. `securityContext`
17. `runAsNonRoot`
18. Linux capabilities
19. Seccomp
20. Read-only root filesystem
21. Privilege escalation
22. Host namespaces
23. HostPath risks

---

# Phase 8 — Network Security

1. NetworkPolicy
2. Ingress policies
3. Egress policies
4. Pod selectors
5. Namespace selectors
6. IP blocks
7. Default-deny policies
8. DNS considerations
9. Namespace isolation
10. Application-to-database restrictions

### Target Security Model

```text
                 Gateway
                    │
                    ▼
                  Todo API
                    │
                    ▼
               PostgreSQL
```

Allowed:

```text
Gateway ──────► Todo API
Todo API ─────► PostgreSQL
```

Blocked:

```text
Gateway ──────X────► PostgreSQL
External ─────X────► PostgreSQL
```

---

# Phase 9 — Policy & Admission Control

1. Admission control
2. Admission controllers
3. ValidatingAdmissionPolicy
4. Mutating admission concepts
5. Kyverno concepts
6. Gatekeeper concepts
7. Policy enforcement
8. Prevent privileged Pods
9. Prevent root containers
10. Restrict hostPath
11. Restrict container registries
12. Require resource requests/limits
13. Enforce organizational standards

---

# Phase 10 — Observability

### Logs

1. Container logs
2. Pod logs
3. Application stdout/stderr
4. Log collection concepts

### Metrics

5. Kubernetes metrics
6. Metrics Server
7. CPU and memory metrics
8. Prometheus concepts
9. Grafana concepts
10. Alerting

### Tracing

11. Distributed tracing
12. OpenTelemetry
13. Request correlation
14. Application vs infrastructure observability

---

# Phase 11 — Kubernetes Troubleshooting

Develop a systematic troubleshooting methodology.

### Application Path

```text
Client
  ↓
Gateway
  ↓
Service
  ↓
EndpointSlice
  ↓
Pod
  ↓
Application
```

### Network Path

```text
Pod
 ↓
NetworkPolicy
 ↓
Service
 ↓
CoreDNS
 ↓
Destination Pod
```

### Problems to deliberately create and diagnose

1. `CrashLoopBackOff`
2. `ImagePullBackOff`
3. `Pending`
4. `OOMKilled`
5. Failed startup probe
6. Failed readiness probe
7. Failed liveness probe
8. Service not reachable
9. DNS failure
10. Gateway routing failure
11. NetworkPolicy blocking traffic
12. PVC not binding
13. Scheduling failure
14. Insufficient CPU/memory
15. Application configuration failure

### Core Troubleshooting Commands

```text
kubectl get
kubectl describe
kubectl logs
kubectl exec
kubectl events
kubectl top
kubectl explain
```

---

# Phase 12 — Kubernetes Packaging & Application Management

## Helm

1. Why Helm exists
2. Helm charts
3. Templates
4. Values
5. Releases
6. Upgrades
7. Rollbacks
8. Chart dependencies
9. Repositories
10. Environment-specific configuration

## Kustomize

11. Bases
12. Overlays
13. Patches
14. Environment-specific configuration

### Architecture Decision

Understand:

```text
Raw YAML
   ↓
Kustomize
   ↓
Helm
```

Learn **when and why** each approach is appropriate rather than introducing them prematurely.

---

# Phase 13 — Scaling & Advanced Kubernetes

### Application Scaling

1. Multiple replicas
2. Horizontal Pod Autoscaler
3. Vertical Pod Autoscaler concepts
4. KEDA concepts
5. CPU-based scaling
6. Memory-based scaling
7. Business-metric scaling

### High Availability

8. Multiple control planes
9. Multiple worker nodes
10. etcd quorum
11. Failure domains
12. PodDisruptionBudgets
13. Topology spread
14. Rolling upgrades

### Cluster Operations

15. Cluster upgrades
16. `cordon`
17. `drain`
18. `uncordon`
19. Node maintenance
20. etcd backup
21. Disaster recovery
22. Certificate lifecycle
23. Cluster recovery

---

# Phase 14 — Advanced Networking & Architecture

1. CNI
2. kube-proxy
3. Service networking internals
4. eBPF concepts
5. Cilium concepts
6. kube-proxy replacement
7. NetworkPolicy datapath
8. Gateway networking
9. DNS internals
10. MTU
11. Network troubleshooting
12. Network observability
13. Multi-node networking
14. Multi-cluster concepts

---

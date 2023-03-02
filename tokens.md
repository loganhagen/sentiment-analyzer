# Gitlab Agent Registration Token

Token: NJsVwwokio2Bh4sCuytiZqU-HSv7w1L_DEuZjvjkyAFHddDssQ

Docker command:

```
docker run --pull=always --rm \
 registry.gitlab.com/gitlab-org/cluster-integration/gitlab-agent/cli:v14.8.1 generate \
 --agent-token=NJsVwwokio2Bh4sCuytiZqU-HSv7w1L_DEuZjvjkyAFHddDssQ \
 --kas-address=wss://gitlab.socs.uoguelph.ca/-/kubernetes-agent/ \
 --agent-version v14.8.1 \
 --namespace gitlab-kubernetes-agent | rancher kubectl apply -f -
```

# Gitlab Registry Deploy Token

username: graphexagent
token: LMxfNSTJzhxHCPc83V5s

rancher kubectl create secret docker-registry regcred --namespace=graphex --docker-server=registry.socs.uoguelph.ca --docker-username=graphexagent --docker-password=LMxfNSTJzhxHCPc83V5s --docker-email=lhagen02@uoguelph.ca

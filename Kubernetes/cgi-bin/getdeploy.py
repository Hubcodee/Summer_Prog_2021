# import subprocess
# op = subprocess.getoutput(
#     "kubectl get deployment -n default --kubeconfig admin.conf | grep "" | awk '{print $1}'")
# print(op)
from kubernetes import client, config, watch
config.load_kube_config("admin.conf")
api = client.CoreV1Api()
pods = api.list_namespaced_pod(namespace="default", watch=False)
for i in pods.items:
    print(f"{i.metadata.name}")

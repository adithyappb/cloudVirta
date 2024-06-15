import docker
from kubernetes import client, config

def list_docker_containers():
    client = docker.from_env()
    return client.containers.list()

def list_kubernetes_pods():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    return v1.list_pod_for_all_namespaces(watch=False).items


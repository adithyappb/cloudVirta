from flask import Flask, jsonify
from openstack import connection

app = Flask(__name__)

# Replace with your OpenStack credentials
conn = connection.Connection(auth_url="http://openstack.example.com:5000/v3",
                             project_name="admin",
                             username="admin",
                             password="password",
                             user_domain_name="default",
                             project_domain_name="default")

@app.route('/api/vms', methods=['GET'])
def list_vms():
    vms = conn.compute.servers()
    vm_list = [{"id": vm.id, "name": vm.name} for vm in vms]
    return jsonify(vm_list)

@app.route('/api/containers', methods=['GET'])
def list_containers():
    # Implement Docker and Kubernetes API calls here (from container_utils.py)
    docker_containers = container_utils.list_docker_containers()
    kubernetes_pods = container_utils.list_kubernetes_pods()

    containers = [{"id": c.id, "name": c.name} for c in docker_containers]
    pods = [{"id": p.metadata.uid, "name": p.metadata.name} for p in kubernetes_pods]

    return jsonify(containers + pods)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


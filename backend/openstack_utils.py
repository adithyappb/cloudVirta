# openstack_utils.py

from openstack import connection

def create_connection():
    return connection.Connection(
        auth_url="http://openstack.example.com:5000/v3",
        project_name="admin",
        username="admin",
        password="password",
        user_domain_name="default",
        project_domain_name="default"
    )

def list_vms(conn):
    return conn.compute.servers()

def create_vm(conn, name, image_id, flavor_id, key_pair, network_id):
    conn.compute.create_server(
        name=name,
        image=image_id,
        flavor=flavor_id,
        key_name=key_pair,
        network=network_id
    )

def delete_vm(conn, vm_id):
    conn.compute.delete_server(vm_id)


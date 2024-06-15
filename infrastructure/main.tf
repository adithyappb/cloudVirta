provider "openstack" {
  auth_url    = "http://openstack.example.com:5000/v3"
  tenant_name = "admin"
  user_name   = "admin"
  password    = "password"
}

resource "openstack_compute_instance_v2" "vm" {
  name            = "example_vm"
  image_id        = "image-id"
  flavor_id       = "flavor-id"
  key_pair        = "key-pair-name"
  security_groups = ["default"]

  network {
    uuid = "network-id"
  }
}


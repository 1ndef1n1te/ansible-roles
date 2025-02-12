# Collection of ansible roles

# Description

This collection contains several roles for installing and configuring different services such as:

- arangodb
- docker
- elasticsearch
- rabbitmq (single-node && cluster mode)
- redis-stack (single-node && cluster mode)
- pulsar (cluster mode)
- nginx (local repo)
- local_repo (install yum local repo)
- k3s
- k8s_node (prepare linux node to be k8s node)
- containerd_mirrors
- base_utils

`node_facts` role scrape facts about linux node (json can be converted to md table with python script `facts_to_table.py`)

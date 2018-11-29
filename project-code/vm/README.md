# Setting up a four-node BigchainDB virtual machine network

Run `make install` to call the [stack.sh](https://github.com/timathom/bigchaindb/blob/1cd5a99191060aaa507e74a55d0462a70421d027/pkg/scripts/stack.sh) script provided with the
official distribution of BigchainDB. The script runs Vagrant and an Ansible
playbook to set up the VM network.

This method is not recommended. It is error prone (the install process
has to be run multiple times before each node is able to connect) and has
been included here only to document that I made a failed attempt to use it
for this project.

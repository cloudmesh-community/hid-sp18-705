.PHONY: clean msg provision teardown run start check-deps
CONF_DIR := bigchaindb/pkg/configuration
TOP_DIR := bigchaindb

# Run deploy script for Vagrant VM 4-node network install
install: setup fetch stack provision

# Provision with Ansible
provision:
	@ansible-playbook $(CONF_DIR)/bigchaindb-start.yml \
		-i $(CONF_DIR)/hosts/all \
		--extra-vars "operation=start home_path=$(TOP_DIR)"

msg:
	@echo "\n"
	@echo "Deploying BigchainDB test network. This will take several minutes."
	@echo "\n"

# Run deploy script separately
stack:
	@bash stack.sh

# Tear down deployment
unstack:
	@bash unstack.sh

# Add Ansible config to suppress errors for invalid Tasks
setup: msg
	@echo "[defaults]" > ansible.cfg
	@echo "invalid_task_attribute_failed = False" >> ansible.cfg

# Fetch install/uninstall scripts from BigchainDB repo
fetch:
	@curl -O https://raw.githubusercontent.com/timathom/bigchaindb/rbac/pkg/scripts/stack.sh
	@curl -O https://raw.githubusercontent.com/timathom/bigchaindb/rbac/pkg/scripts/unstack.sh

clean:
	rm -rf *.cfg stack.* unstack.* *.log
	rm -rf Vagrantfile
	rm -rf logs
	rm -rf bigchaindb

# Tear down and clean up
remove: unstack teardown clean

teardown:
	@vagrant box remove ubuntu/xenial64

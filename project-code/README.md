# Demo of BigchainDB's Role-Based Access Control Extension

The BigchainDB repository has been added here as a submodule. When
cloning the repository, include the `--recursive` switch to ensure that the
submodule contents are cloned as well, or run `git submodule update --init
--recursive` if the repository has already been cloned.

```
git clone --recursive https://github.com/cloudmesh-community/hid-sp18-705.git
cd hid-sp18-705/project-code/bigchaindb/
make run
```

Executing `make run` will launch three Docker containers, one for each
component of BigchainDB (BigchainDB Server, Tendermint, and MongoDB). Once
stopped, the containers can be reset with `make reset`.

Once the containers are running, the Python script `rbac_demo.py` can
be executed and will send a series of transactions to the BigchainDB
server.

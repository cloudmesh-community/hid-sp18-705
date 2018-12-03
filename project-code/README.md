# Demo of BigchainDB's Role-Based Access Control Extension

:o: it is unclear what code you developed

:o: it is unclear what code you developed, please add a section with 
Artifacts Developed by Author
* list in that in bullet form what they are and what they do

## Artifacts Developed by Author

All original Python code is included in the `demo` directory, as detailed in
the project report:

* `demo/rbac.py`: Python class (`BigchainRbac()`) that provides an
interface for the role-based access control extension that is available for
BigchainDB.

* `demo/rbac_demo.py`: demo Python script that calls methods from the
`BigchainRbac()` class to illustrate how the role-based access control
features of BigchainDB could be employed. The use case is that of data and
workflow management for a library catalog. This script sends a series of
transactions to a BigchainDB server node.

* `demo/convert_rdf.py`: simple Python script provided to illustrate
how data in the `project-data` directory was converted using the Python
RDFLib library.

Two original graphviz files (used to generate the last two figures in
the project report) are included for reference in the `graphviz` directory:

* `graphviz/assets-metadata.dot`: illustrates how data for a library
catalog might be modeled and linked in BigchainDB.

* `graphviz/rbac-graph.dot`: illustrates the dependency tree and
validation scheme used to enforce role-based access control constraints in
BigchainDB.

## External Code

The BigchainDB repository has been added here as a submodule. When
cloning the repository, include the `--recursive` switch to ensure that the
submodule contents are cloned as well, or run `git submodule update --init
--recursive` if the repository has already been cloned.

The BigchainDB repository includes a Docker Compose script for spinning
up the Docker containers needed to run a BigchainDB test node.

## Execution

```
$ git clone --recursive https://github.com/cloudmesh-community/hid-sp18-705.git
$ cd hid-sp18-705/project-code/bigchaindb/
$ make run
```

Executing `make run` will launch three Docker containers, one for each
component of BigchainDB (BigchainDB Server, Tendermint, and MongoDB).
Several seconds after starting up, BigchainDB will be ready to process
transactions.

Once stopped, the containers can be reset with `make reset`.

In order to run the demo Python code, the BigchainDB Python driver must
first be installed:

``` 
$ pip install bigchaindb_driver
```

Once the containers are running and the driver has been installed, the
Python script `rbac_demo.py` in the `demo` directory can then be executed
and will send a series of transactions to the BigchainDB server.

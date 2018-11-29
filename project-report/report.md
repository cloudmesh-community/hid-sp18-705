Introduction
============

The problem of entity resolution (also known as record linkage or data
matching [@christen-12-data]) is one that has a direct impact on the
work of information professionals in research libraries. In library
units responsible for catalog management, many workflows center on a
procedure known as copy cataloging, which aims to expedite the
processing of new acquisitions. Copy cataloging involves searching a
shared database for records created by another cataloging agency, but
that describe identical publications that have been acquired by one's
local institution [@dm-17-measuring]. In the current environment, a
single company, the Online Computer Library Center
(OCLC--<http://www.oclc.org>), is the only viable platform for global
cooperative cataloging [@turner-10-oclc].

﻿﻿OCLC provides data aggregation and warehousing services that allow
libraries to effectively share their data, but its business model does
not encourage peer-to-peer interaction and innovation among individual
libraries. This vendor-driven paradigm entails the acceptance of a
business model that, in effect, charges libraries for serving their own
data back to them, with some added value through quality control and
normalization. Once a library's data has been sent to OCLC, it also
becomes subject to potential licensing restrictions, as well as the
expectation that future dissemination of the data will include
attribution of OCLC [@oclc-12-worldcat; @oclc-10-worldcat].

New Approaches to Metadata Management
=====================================

Libraries have a tradition of experience with record matching and
automation [@mcqueen-92-record], but now stand to benefit from the
increasingly mainstream availability of algorithms and routines
developed within the context of data science and machine learning.
Sophisticated algorithms for string comparison and probabilistic record
linkage have long been available, but are not widely used by libraries,
with the exception of large-scale projects such as the Social Networks
and Archival Context Project (SNAC) (<http://snaccooperative.org/>) and
the Virtual International Authority File (VIAF) (<http://viaf.org/>),
itself a project of OCLC. The former has employed methods based on Naive
Bayes classification algorithms to aggregate and disambiguate data from
across a wide range of libraries and archives (the reported accuracy of
the approach fell with the range of 80-90 percent) [@lj-11-connecting].
More recent approaches to record matching have improved on probabilistic
methods such as Naive Bayes by using Artificial Neural Networks,
improving accuracy rates in some cases to 98 percent or
more [@rph+-17-supervised].

As machine learning tools and methods have become more accessible,
however, large-scale, real-time access to library metadata has not
necessarily followed suit. The catalog of a large academic library may
contain around 10 million records [@uniyalelibrary-18-yul]. By
comparison, as of August 2018, the OCLC catalog database, WorldCat,
contained 427,501,671 bibliographic records in 491
languages [@oclc-18-worldcat]. As long as service providers such as OCLC
maintain centralized control over the aggregated metadata of research
libraries, large-scale computational analysis--and the innovation it
could produce--will remain proprietary and locked away.

The situation is further complicated by professional and cultural norms
within libraries. Although decentralization may be appealing as an
ideal, librarians who manage bibliographic metadata are also immersed in
a discourse that centers on the idea of control: they use terms such as
authority control, controlled vocabularies, and intellectual and
physical control of collections [@olson-01-power]. The idea of control
is closely related to the idea of trust: when workflows and systems are
centralized, it becomes easier to enforce norms and standards, but it
also becomes more likely that potential contributors may be excluded,
especially when they are unable to afford the price of membership in a
proprietary system.

New decentralized technologies such as blockchains could allow research
libraries to form robust peer-to-peer networks that would enable data
sharing on a larger scale. Public blockchains such as Ethereum and
Bitcoin are limited in the amount of data that can feasibly be stored on
chain, but alternative platforms that address this limitation have
recently emerged. When discussing decentralization, there are a range of
new technologies that should be considered, and blockchain may or may
not be the most appropriate for a particular use case--or blockchain
technology may need to be used in conjunction with other technologies in
order to enable decentralized exchange. Several efforts are underway to
develop systems for decentralized file storage using distributed hash
tables, one of the most prominent being the Interplanetary File System
(IPFS) (<https://ipfs.io>). In a way similar to the software versioning
protocol Git, IPFS uses hash values to capture the state of a file at a
particular point in time and then serves it on a peer-to-peer network.
IPFS hashes might be referenced as links in blockchain transactions in
order to decouple the storage layer from the accounting
layer [@coralhealth-18-learn].

In this regard, the blockchain-based database service BigchainDB,
implemented in Python, provides a robust storage data solution while
preserving the benefits of blockchain features such as data immutability
and an asset-based transactional model. By running a consortium
blockchain network of BigchainDB nodes [@buterin-15-public], libraries
could be empowered to abandon centralized models and begin managing
their data collectively.

Blockchains for Research Libraries
==================================

Some in the library profession have been skeptical of blockchain
applications for their domain, arguing that they have been overhyped as
a panacea, when in reality they are nothing more than slow, expensive,
append-only databases [@alman-18-blockchain]. Even core developers
working to support the Bitcoin blockchain have argued that the
constraints imposed by blockchain technology, such as immutability and
decentralized consensus, make it appropriate for a very limited set of
applications--namely, currency and the exchange of
value [@song-18-why]. For individuals and organizations who are
investigating blockchains as a technical solution, it is important from
the outset to establish a framework for evaluating their applicability
and appropriateness [@scriber-18-framework].

For example, a blockchain-based solution may be appropriate in a
scenario in which there is a lack of trust among participants, or in
which processes and collaboration would be more efficient if the need
for trust were eliminated [@scriber-18-framework]. In the case of a
shared catalog for research libraries, trust is an issue because not all
participants can be trusted to provide data that conforms to expected
levels of quality. A commercial, centralized solution mitigates these
concerns by requiring participants to pay a membership fee. A blockchain
solution addresses issues of trust by enforcing a decentralized
consensus mechanism, which may take different forms, but which is
designed to ensure that participants can trust the network to maintain a
consistent state across all transactions [@bkm-18-latest].

The Proof-of-Stake consensus algorithm, employed by some blockchain
networks as an alternative to Bitcoin's resource-intensive Proof-of-Work
mechanism, is similar to the membership fee model in that validator
nodes are elected based on their share of "stake" in the network,
measured by their willingness to commit or stake an allocation of
network tokens as a proof of honesty [@marin-18-understanding]. For
research library applications, a variation of Proof-of-Stake known as
Proof-of-Authority may be the most appropiate
solution [@marin-18-understanding; @buterin-15-public]. In contrast to
public blockchains such as Ethereum and Bitcoin, or fully private
blockchains restricted to a single organization, so-called consortium
blockchains may be the preferred approach, one in which consensus "is
controlled by a pre-selected set of nodes" [@buterin-15-public]. The
model implemented by the BigchainDB project fits the parameters of a
consortium blockchain that implements a Proof-of-Authority approach to
consensus [@mcconaghy-18-reply].

Design Requirements
===================

A blockchain-based catalog for research libraries should support the
creation of a decentralized marketplace for library metadata. Rather
than paying a centralized exchange to distribute their catalog records,
libraries could buy and sell records in a peer-to-peer exchange. Catalog
records could thus become a source of revenue rather than a costly
expenditure. Many blockchain systems support the creation of so-called
smart assets, or the creation of tokens to represent real-word assets. A
new token could be minted to facilitate the exchange of metadata
objects, and payment and settlement channels could be created using
smart contracts on a public blockchain such as Ethereum.

However, a public blockchain solution does not fully satisfy the
requirements of decentralization for this use case. A data asset cannot
be represented exclusively by a token--it also needs to be stored in a
decentralized system optimized for read and write transactions. Public
blockchains such as Ethereum have been designed for exchange, not
storage. At the current price of the Ethereum blockchain's native token,
Ether (ETH), at approximately \$200.00, storing 1 Gigabyte of data on
the blockchain would cost over \$7,000,000.00 [@hess-16-reply]. A
decentralized system for library metadata must be able to scale and
store big data out of the box. BigchainDB is a production-ready solution
that might meet the requirements for this use case: it supports the
creation of assets and the direct storage of metadata objects on its
blockchain [@bigchaindbcontributors-18-key].

Project Scope
=============

﻿The current project presents findings from an initial exploration of
BigchainDB as a blockchain database solution for a shared library
catalog. It provides an overview of the BigchainDB architecture and data
model and probes some of BigchainDB's features and functionality. It
includes a preliminary analysis of library metadata standards and
requirements and examines whether they can be accommodated using
BigchainDB.

BigchainDB
==========

Evolution
---------

BigchainDB was created to address the scalability and storage
limitations of traditional blockchains such as Bitcoin and Ethereum and
to create a hybrid solution that builds a blockchain layer on top of an
existing big data system [@bigchaindbgmbh-18-bigchaindb]. Development of
the BigchainDB framework initially focused on integration with the
RethinkDB system, but now works exclusively with
MongoDB [@killerstorm-16-bigchaindb; @bigchaindbgmbh-18-bigchaindb].

The early focus of BigchainDB development was to create an architecture
that would allow existing big data databases to be
"blockchainified" [@github-bigchaindb-whitepaper-a]. The original
BigchainDB whitepaper, released in June 2016, focused on the scalability
limitations of traditional blockchain networks such as Bitcoin and
claimed that it should be possible to develop a blockchain-based
distributed database that would enable "1 million writes per second
throughput, storing petabytes of data, and sub-second latency"---in
contrast to the storage restrictions and 7 transaction-per-second (tps)
limit of the Bitcoin network [@github-bigchaindb-whitepaper-a]. The
advantages of adding a blockchain layer to an existing distributed
database would be to incorporate "decentralized control, immutability,
and creation \[and\] movement of digital
assets" [@github-bigchaindb-whitepaper-a p. 1].

The primary challenge in designing a decentralized system is how to
defend against both arbitrary failure and malicious actors. In so-called
Sybil attacks, an attacker attempts to generate false identities in
order to gain majority control over a network [@douceur-02-sybil]. To
address Sybil attacks, BigchainDB proposes a governance model that would
create a federation of trusted nodes. Because all participants are
known, any attempt by one participant to gain control over the network
would be obvious. A more pervasive vulnerability comes in the form of
the so-called Byzantine Generals'
Problem [@github-bigchaindb-whitepaper-a]. Nodes in a distributed
network must be able to reach consensus about the final order of
transactions at each state of the system, even in the presence of node
failure or malicious attempts to manipulate system state in order to
gain an unfair advantage--for example, in double-spending, in which a
transaction is replayed so that the same asset can be used again (a
particular problem in the case of financial
transactions) [@github-bigchaindb-whitepaper-a; @antonopoulos-17-mastering].

In its original design, BigchainDB relied on the consensus algorithm of
its underlying database to manage benign node failure and incorporated
additional constraints to verify the integrity of the voting process by
which nodes in the network approved transactions--and the blocks
containing them--as valid [@github-bigchaindb-whitepaper-a]. However,
in its initial version, BigchainDB did not claim to be Byzantine Fault
Tolerant (or BFT--the term used to indicate that a system can withstand
unexpected node behavior, whether benign or malicious, up to a certain
threshold [@github-bigchaindb-whitepaper-a]). In the original design,
all nodes belonged to a single logical database. This made the system
overly centralized and vulnerable to attack: a malicious actor who
gained control over a single node would have been able to drop the
entire database, which was shared among all nodes in the
network [@killerstorm-16-bigchaindb; @bigchaindbgmbh-18-bigchaindb].

BigchainDB 2.0, released in June 2018, underwent a complete redesign and
incorporated full Byzantine fault tolerance through integration with
Tendermint, an application for managing consensus and state machine
replication in blockchain
systems [@mcconaghy-18-bigchaindb; @tendermintcontributors-18-tendermint].
As a result of implementing Byzantine fault tolerance through
Tendermint, BigchainDB's original goal of supporting 1 million tps was
no longer viable.

Benchmark
---------

A recent benchmark of BigchainDB 2.0 throughput performed by the
BigchainDB development team indicated that the system was able to
process approximately 300 tps [@mcconaghy-18-were]. Benchmarking was
carried out on a four-node network on Microsoft Azure-hosted virtual
machines located in the same data center. Three separate experiments
were run to test different options, and a full report of configurations
and results is available for review [@github-bigchaindb-beps]. The
primary experiment tested how long it would take to commit 1 million
transactions of 765 bytes each to the BigchainDB blockchain under
default settings. Results showed an average rate of 299.0 tps and a
median rate of 309.0 tps. All 1 million transactions were finalized in
56 minutes with no failures [@github-bigchaindb-beps].

Architecture
------------

The architecture of a BigchainDB 2.0 network is shown in
Figure [1](#f:bdb){reference-type="ref" reference="f:bdb"}, created by
the BigchainDB development team. Each node in the network is
self-contained and includes its own MongoDB database and Tendermint
application server. Tendermint is used to manage consensus,
communication, and state replication among nodes, whereas the software
that is unique to BigchainDB is responsible for "registering and
tracking the ownership of 'assets'" [@mcconaghy-18-bigchaindb]. ﻿In
BigchainDB 2.0, as is the case in general with systems that are
Byzantine Fault Tolerant, $3f + 1$ nodes are necessary to run a network,
where $f$ is the number of faulty nodes to be
tolerated [@mcconaghy-18-reply-a]. Therefore, at least four nodes are
required in order to run a BigchainDB network: if one of the four nodes
becomes unresponsive or attempts to approve an invalid transaction, the
network will continue to function based on the majority consensus of the
other three nodes [@mcconaghy-18-reply-a].

A BigchainDB client can potentially connect to any node in the network.
Each MongoDB instance contains a full replication of the data stored in
the network [@mcconaghy-18-reply-a]. The BigchainDB project officially
supports three client drivers to connect to a node server (in Python,
Node.js, and Java) [@bigchaindbcontributors-18-drivers].

### BigchainDB Server

The BigchainDB Server, written in Python, implements the logic to model,
validate, and store transactions in the BigchainDB
blockchain [@mcconaghy-18-bigchaindb]. The server also incorporates a
Python implementation of the Crypto-Conditions specification, which is a
standard for enforcing complex boolean conditions for fulfillment (or
transfer of assets) using cryptographic signatures [@trh-17-crypto].

All objects in BigchainDB are modeled as *assets*. Two transaction types
are available for managing assets: CREATE and
TRANSFER [@github-bigchaindb-beps-a]. Each transaction must be
cryptographically signed with the private key of its "owner" (the agent
who created an asset through a CREATE transaction or to whom an asset
was assigned through a TRANSFER transaction). Public/private keypairs
are implemented using the Edwards-curve Digital Signature Algorithm
Ed25519 [@github-bigchaindb-beps-a]. A transaction is encoded using a
dictionary or associative array that can be serialized as a JSON object.
The BigchainDB Transactions Specification defines the structure and
usage of a BigchainDB transaction object [@github-bigchaindb-beps-a].
Figure [\[c:bdb3\]](#c:bdb3){reference-type="ref" reference="c:bdb3"}
shows the key/value pairs that all valid BigchainDB transactions must
include.

Conditions for fulfillment and asset transfer are defined in the values
of the "inputs" and "outputs" keys. An object representing the asset
itself is stored as the value of the "asset" key and cannot be modified
once an asset has been created and committed to a block in the
BigchainDB blockchain. The "metadata" key is used to store an arbitrary
object that records additional information about the asset or its state:
in contrast to the asset object, the metadata object *can* be modified
with each TRANSFER transaction [@github-bigchaindb-beps-a].

### Tendermint

Tendermint provides an application interface and BFT consensus algorithm
for replicating application state across the nodes in a decentralized
network [@tendermintcontributors-18-tendermint]. Tendermint Core
implements the consensus algorithm, which ensures that all nodes agree
on a single order for transactions. Tendermint's Application Blockchain
Interface (ABCI) provides a language-agnostic interface for blockchain
applications to use when validating and processing
transactions [@tendermintcontributors-18-tendermint].

Figure [2](#f:bdb2){reference-type="ref" reference="f:bdb2"} is a
sequence diagram, created by the BigchainDB development team, that
illustrates the role of Tendermint in processing BigchainDB
transactions. After a client prepares and signs a transaction, typically
using a BigchainDB driver, the transaction is submitted to the
BigchainDB server for initial validation. The server then sends the
transaction to Tendermint, which includes it in a local memory pool.
Tendermint returns its own validation request to the server and, upon
confirmation, proposes a new block and begins a round of voting as part
of its consensus algorithm. Each node in the network votes on the order
and validity of transactions in the block, and if consensus is reached,
the block is committed to the application's
blockchain [@dhameja-18-lifecycle; @bigchaindbgmbh-18-bigchaindb].
BigchainDB stores a queryable copy of each block in MongoDB, while
Tendermint appends each block to its canonical blockchain, which is
stored in an internal LevelDB database and used for replicating
transaction state to network
peers [@tendermintcontributors-18-tendermint; @bigchaindbgmbh-18-bigchaindb].

### MongoDB

MongoDB is an enterprise-grade NoSQL database optimized for storing JSON
objects as documents. It supports both high availability (replication)
and scalability (sharding) [@mongodbcontributors-18-introduction]. Early
verions of BigchainDB used a single MongoDB replication set and were
able to take advantage of these core MongoDB features. In BigchainDB
2.0, because each node maintains a separate MongoDB instance,
replication and sharding are not supported out of the
box [@mcconaghy-18-bigchaindb]. In order to enforce practical
immutability and decrease the likelihood of data tampering, the
BigchainDB server limits access to MongoDB and does not expose any
interfaces for deleting or making arbitary modifications to database
documents [@bigchaindbgmbh-18-bigchaindb]. Although it is technically
possible for a system administrator to modify the MongoDB database
directly, each BigchainDB transaction is signed with a public/private
cryptographic keypair--thus any tampering would result in a modified
signature, which would be detectable by other nodes in the network and
would violate its social contract [@bigchaindbgmbh-18-bigchaindb].

BigchainDB does take advantage of MongoDB's query facility for read-only
queries. Through its own HTTP API, it exposes a simple search interface
for querying MongoDB, but it also allows node administrators to create
custom indexes and leverage the full range of MongoDB query
functionality [@bigchaindbcontributors-18-querying].

Dataset
=======

The dataset for this project is intentionally small and meant to test a
potential use case for BigchainDB as a library catalog application.
Currently, library catalog records are stored in a set of
industry-specific formats maintained by the Library of Congress: the
MAchine Readable Cataloging (MARC) formats for bibliographic and
authority data (standardized as ISO 2709 and ANSI/NISO
Z39.2) [@ford-12-lcs; @ndmarcso-13-library]. In recent years, the
Library of Congress has undertaken an effort to update library metadata
standards and adopt standards and formats maintained by the World Wide
Web Consortium (W3C)---specifically those related to linked data and the
Semantic Web, such as the core data model known as the Resource
Description Framework
(RDF) [@librarycongress-18-bibliographic; @cwl-14-rdf]. A new
domain-specific data model and ontology for library metadata, expressed
using the W3C's OWL standard for semantic ontologies, is currently being
developed and implemented [@hkp+-12-owl]. The data used here for testing
with BigchainDB follows this model, known as the Bibliographic Framework
Initiative (BIBFRAME) [@librarycongress-18-bibliographic].

In the basic model proposed by BIBFRAME, descriptions of library
resources are divided into three entity types or classes: Work (the
abstract concept of the resource), Instance (the embodiment of a Work in
a particular publication), and Item (a physical copy of an
Instance) [@librarycongress-18-bibliographic]. As an example for this
project, a catalog record from the Indiana University Library catalog
was chosen. This record describes the Lilly Library's partial copy of
the Gutenberg Bible. The data is divided into six files:

    ocm05084045.xml
    gutenberg-iul-item.rdf
    gutenberg-iul-instance.json
    gutenberg-iul-item.json
    gutenberg-iul-record.json
    gutenberg-work.json

The file `ocm05084045.xml` represents the original MARC-format record,
encoded as XML. The file `gutenberg-iul-item.rdf` provides an example of
a partial conversion of the original MARC record to the BIBFRAME model
using the RDF/XML serialization [@morgan-13-rdf]. The remaining files
represent the data used to create assets for storage in BigchainDB and
are encoded in BIBFRAME using the JSON-LD serialization of
RDF [@morgan-13-rdf]. Several preprocessing steps of data conversion and
cleanup were necessary. The original MARC/XML catalog record was
converted to BIBFRAME RDF/XML using a suite of XSLT stylesheets provided
by the Library of Congress [@github-lcnetdev-marc2bibframe2]. The
RDF/XML documents were then converted to JSON-LD using the Python RDFLib
library (see the `convert_rdf.py` script in the `project-code` directory
for a brief example). The JSON-LD produced by RDFLib was then broken
into separate files to allow for the creation of individual assets in
BigchainDB.

The JSON-LD output produced by RDFLib was further modified to support
the inclusion of named graphs, a feature of RDF 1.1 that makes it
possible to encode assertions about a collection of RDF
statements [@cwl-14-rdf]. Using named graphs, it is possible to record
administrative metadata about the creation or generation of the resource
description itself (when it was created, by whom, using what standards,
etc.). It should be noted that the usage of JSON-LD--which has some
unconventional syntax features--with BigchainDB led to the discovery of
a bug in the BigchainDB validation code that triggered a fatal Internal
Server Error (HTTP 500). This bug was subsequently reported and has
since been fixed by a BigchainDB core
developer [@github-bigchaindb-bigchaindb].

Implementation
==============

Use Case
--------

Currently, most large library catalogs are stored in enterprise
relational databases such as Oracle. The catalog is one module in a
suite of services known as an Integrated Library System (ILS), which
also includes modules for circulation and ordering or acquisitions. The
cataloging module in an ILS includes a public-facing interface for
search and retrieval and a staff-facing interface for data entry and
management. One advantage of using a distributed system such as
BigchainDB for library cataloging functions would be to allow libraries
to share their data more easily with peer institutions. BigchainDB's
asset-based data model might also allow libraries to perform inventory
and lending functions more efficiently. However, many functional
components would need to be considered before determining whether a
blockchain platform such as BigchainDB would be appropriate for the
library catalog use case. This project focuses on one such component:
namely, the management of roles and permissions for data entry.

The Python component of this project implements an extension to
BigchainDB that adds support for Role-Based Access Control (RBAC)
functionality [@dhameja-17-role]. The code is based on a Node.js example
created by the BigchainDB development team to demonstrate the RBAC
extension [@github-bigchaindb-project-jannowitz]. Support for RBAC is
important for library cataloging because library personnel roles are
typically divided between professional librarians (catalogers) and
paraprofessional technicians. Librarians are expected to create
"original" descriptions of library resources, whereas paraprofessionals
are responsible for copying existing data from a shared database such as
OCLC WorldCat. Public blockchain systems do not usually impose write
restrictions (allowing anyone to write to the database), so support for
RBAC is an important consideration when evaluating BigchainDB.

Installation
------------

BigchainDB was designed to be a federated network of distributed nodes.
In an ideal setup, each node would be maintained in a different location
by a different operator [@bigchaindbgmbh-18-bigchaindb]. The official
BigchainDB documentation provides instructions for those interested in
setting up a production network [@bigchaindbcontributors-18-how].
However, for testing purposes, a full network is not necessary. A
BigchainDB test network is currently available at
<https://test.bigchaindb.com/>, but the testnet installation does not
include the RBAC extension required for this project.

The official BigchainDB distribution includes a Docker Compose script
that can be used for spinning up a single node. It also includes a shell
script and a set of Ansible playbooks that can be used to provision a
four-node network of virtual machines using Vagrant and VirtualBox. For
this project, both methods were tested, but frequent errors were
encountered when trying to install and run a network of virtual
machines. The Docker approach was chosen for simplicity and because it
was possible to build the container from the RBAC branch of the
BigchainDB Server codebase. The distribution includes a Makefile, and
Docker containers for BigchainDB Server, Tendermint, and MongoDB can be
easily run with a simple `make run` command.

Data Management
---------------

All BigchainDB CREATE transactions must include a JSON-serializable
object to represent the asset being recorded on the blockchain. The
`asset` field of a CREATE transaction takes an object with the required
key `data`. The content of the `asset` field is treated as
immutable--it cannot be changed once a CREATE transaction has been
committed, or when ownership of an asset is subsequently changed using a
TRANSFER transaction. Figure [\[c:bfw\]](#c:bfw){reference-type="ref"
reference="c:bfw"} shows how a Work asset might be represented in
BigchainDB. Because this data cannot be changed, it makes sense to
represent it simply using its RDF type (in this case, it is a BIBFRAME
Work with a subtype of Text), as well as a human-readable label. Any
BigchainDB transaction may also include an optional `metadata` key that
takes as its value an arbitrary JSON-serializable object. This flexible
design makes it possible to effectively "update" data by using a
TRANSFER transaction to indicate that the state of an asset has
changed--and recording that change in the metadata object. The code in
`rbac_demo.py` creates separate BigchainDB assets to represent the
BIBFRAME types Work, Instance, and Item.

The project data and code also illustrate how JSON-LD named graphs may
be used to include both descriptive and administrative metadata about
the same BigchainDB asset in a single transaction. The `rbac_demo.py`
script inserts a second named graph into the `gutenberg-work.json` file
so that it contains two named graphs: one representing the Work entity
and one representing a separate Record entity (which is not part of the
core BIBFRAME model). Within the named graph for the Record entity,
there is an RDF property (`foaf:topic`) that links to the URI for the
named graph representing the Work entity.
Figure [3](#f:rbac){reference-type="ref" reference="f:rbac"} illustrates
this pattern, indicating how BigchainDB metadata objects may be used to
create internal linkages among assets conforming to the BIBFRAME data
model.

Role-Based Access Control in BigchainDB
---------------------------------------

The file `rbac.py` contains a single Python class, `BigchainRbac()`,
that provides an interface to create new assets, users, types, and type
instances for Role-Based Access Control in BigchainDB. In the BigchainDB
RBAC extension, roles and permissions, like everything else, are modeled
as assets [@dhameja-17-role]. Two basic assets are necessary for
bootstrapping: an asset to represent the application in which RBAC is
being used and an asset to represent an admin group for admin users who
can create other groups and users and assign permissions. BigchainDB
RBAC employs two reserved keys, `link` and `can_link` that are used to
create a dependency graph of users and asset types or groups. This graph
is illustrated in Figure [4](#f:rbac2){reference-type="ref"
reference="f:rbac2"}. Proper usage of these linkage keys is validated
when a transaction is sent to the BigchainDB server, and a transaction
is rejected if it violates the logic of the permissions
scheme [@dhameja-17-role]. The application logic proceeds according to
the following steps:

1.  User keypairs are generated for three different user types: admin
    users, catalogers, and paraprofessionals. In BigchainDB, a user's
    identity is defined by a public/private keypair, and each
    transaction must be signed by one or more private keys, depending on
    the conditional logic that has been specified (especially in the
    case of TRANSFER transactions).

2.  An admin user creates an asset to represent the admin user group and
    the application itself. The `can_link` key is included in the
    metadata object of the transactions. In the admin group asset, the
    value of `can_link` is a list of all admin user keypairs. In the app
    asset, it is the transaction ID for the CREATE transaction of the
    admin group asset--or, to put it more simply, the admin group ID.
    This linkage entails that only members of the admin group can link
    other groups to the app asset.

3.  The admin user can then call the `create_type()` method of
    `BigchainRbac()` to instantiate new roles for the application. In
    `rbac_demo.py`, two roles have been created: one to represent
    "catalogers" and one to represent "paraprofessionals." In the
    definition of each type asset, the `asset` object includes the
    `link` key, which takes as its value the app asset ID. This linkage
    sets the scope of permissions to the current application context.
    The admin user can then create new user assets and assign them to a
    group. The `can_link` key of the group asset points to the admin
    group ID because only the admin user can assign new users to this
    group. By contrast, the `link` key of the user asset points to the
    user's respective group ID (such as that of the catalogers group).
    It is important to distinguish between a user--identified by a
    public key--and a user asset, which is the result of a BigchainDB
    CREATE transaction. In the RBAC scheme, when a user *asset* is
    created, it must then be assigned to the user's public key through a
    TRANSFER transaction. This can be described as placing the asset in
    the user's "wallet" [@dhameja-17-role].

4.  The most important step occurs when an admin user creates a type to
    represent a resource group and then assigns permissions to restrict
    which users can CREATE instances of that group. In `rbac_demo.py`,
    for example, an asset is created to represent BIBFRAME Work
    resources. Then, the `create_instance_type()` method is invoked in
    order to link a resource asset to its type.
    Figure [4](#f:rbac2){reference-type="ref" reference="f:rbac2"} shows
    that individual BIBFRAME Work assets are linked to the BIBFRAME Work
    Group, which has a `can_link` relationship to the Catalogers Group.
    Therefore, only users associated with a cataloger user asset can
    CREATE BIBFRAME Work assets.

5.  Finally, it is worth mentioning one concern that arises when working
    with BigchainDB as a data entry and data management system. The
    system's asset-centric approach requires that an asset have one or
    more owners. But in a shared scenario, how can one cataloger edit or
    update a record originally created by a different cataloger if they
    are not the owner of the asset? One solution would be for the
    original creator/owner to TRANSFER the asset to the person who wants
    to input new information or revise existing information. This may
    not be practical, however, since the original creator may no longer
    be present. Another solution might be to CREATE the asset with two
    original owners (that is, the CREATE transaction must be signed with
    two private keys): the cataloger as well as the admin user. The
    admin user could then TRANSFER the asset when needed. This is the
    approach taken by the demo developed for this project. However, in
    practice, it would have to be handled in an automated way, so that
    it would not be necessary for a single admin user to execute
    multiple TRANSFER transactions whenever the need arose. In general,
    best practices for managing public/private keypairs in the context
    of this use case is an area that calls for further examination.

When the `rbac_demo.py` script is executed, it populates a local
BigchainDB instance with RBAC assets and tests whether catalogers and
paraprofessionals can issue a CREATE transaction for a BIBFRAME Work
asset. For successful transactions, the program simply outputs an HTTP
URL that can be used to request the result of each transaction. However,
one transaction attempts to CREATE a Work resource with a
paraprofessional user asset. This transaction should fail with a
`ValidationError`, as shown in
Figure [\[c:bdb4\]](#c:bdb4){reference-type="ref" reference="c:bdb4"}.

Conclusion
==========

This project explored BigchainDB, a new blockchain-based solution for
managing big data, and undertook a preliminary examination of whether
BigchainDB could be adapted for use as a library catalog database. The
primary advantage of using a blockchain system instead of a conventional
or distributed database is that it enables peer-to-peer interaction and
exchange in a more fundamental way. Participants in a BigchainDB network
are required to collaborate and coordinate their work very directly.
Doing so would allow data scientists to access library metadata at scale
and to more easily process, clean, and study it, potentially connecting
it to other datasets. This could be particularly useful in large-scale
text mining projects. In the current centralized scenario, library
metadata remains locked away and can only be used for machine learning
and complex analysis by the central service providers who control it.

A blockchain data model also allows for richer data modeling. Rather
than a repository of records, a library catalog can be modeled as a
collection of assets: actual books, journals, and multimedia resources,
as well as the records that describe them. This could facilitate
operations beyond cataloging, such as interlibrary lending and make it
easier to determine which library holds copies of which books, or
subscribes to which journals. BigchainDB is flexible enough to
accommodate the semantic data models, such as BIBFRAME, that are
currently being developed by research libraries. BigchainDB itself is
not a semantic data store, so additional solutions for semantically
enriched information retrieval (such as graph databases) would also need
to be explored. However, BigchainDB's incorporation of MongoDB allows
users to take advantage of the indexing and querying capabilities
internal to MongoDB. Extensions to BigchainDB provide support for
features such as Role-Based Access Control, which would be important for
enabling library cataloging workflows. More systemic analysis would be
needed before recommending BigchainDB as a solution for library
catalogs, but the results of this project indicate that the possibility
would merit further exploration.

![High-Level Architecture of BigchainDB
2.0 [@bigchaindbcontributors-18-querying][]{label="f:bdb"}](images/bdb-arch.pdf){#f:bdb
width="\columnwidth"}

![BigchainDB Sequence
Diagram [@dhameja-18-lifecycle][]{label="f:bdb2"}](images/bdb-seq.pdf){#f:bdb2
width="\columnwidth"}

    {
      "id": ctnull,
      "version": version,
      "inputs": inputs,
      "outputs": outputs,
      "operation": operation,
      "asset": asset,
      "metadata": metadata
    }   

    {
      "data": {
        "@context": {
          "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
          "schema": "http://schema.org/"
        },
        "@type": [
          "http://id.loc.gov/ontologies/bibframe/Work",
          "http://id.loc.gov/ontologies/bibframe/Text"
        ],
        "rdfs:label": "Bible. Latin. Vulgate. 1454."
      }
    }

![Graph of asset and metadata objects in
BigchainDB[]{label="f:rbac"}](images/assets-metadata.pdf){#f:rbac
width="\columnwidth"}

![Graph of permissions in BigchainDB using Role-Based Access
Control[]{label="f:rbac2"}](images/rbac-graph.pdf){#f:rbac2
width="\columnwidth"}

    BIBFRAME Work (IUL Paraprofessionals):  
    (400, '{"message":"Invalid transaction (ValidationError): 
    Linking is not authorized for: 
    6GcYiCCNFsDbBicna6YCVq8RmSjGyB7MGJw9CHjDjqwh","status":400}\n'...

The author would like to thank Dr. Gregor von Laszewski and the i523 and
i516 teaching assistants for their support and suggestions in writing
this report.

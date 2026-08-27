# Eclipse openDuT

## BB Tags(s)
BB-EST, BB-CEST, BB-SC-TC, BB-CSC-TC

openDuT provides engineering and support functionality for both in-vehicle/on-board and cloud/off-board development environments. In addition, it integrates multiple compatible tools and services into a distributed automotive testing toolchain.

## Functional Clusters

Testing

## Layer

MWLayer

## BB Usage

Eclipse openDuT is used to create and operate distributed automotive test environments consisting of physical and/or virtual Devices under Test (DuTs). It allows geographically distributed ECUs, simulation environments and test infrastructure to be interconnected and managed as a common test setup.

A typical usage flow is:

1. Deploy the openDuT backend and its required infrastructure.
2. Define and manage test peers using the LEA web interface or the CLEO command-line interface.
3. Install and configure EDGAR on edge devices connected to physical or virtual DuTs.
4. Combine multiple peers into a cluster.
5. Deploy the cluster to establish the required communication paths between the participating devices.
6. Execute automotive tests or connect external test tooling to the resulting distributed test environment.
7. Observe the test infrastructure through the provided telemetry and monitoring capabilities.

Main openDuT components include:

* **CARL** – Central management and orchestration service.
* **EDGAR** – Edge component running close to the Devices under Test.
* **LEA** – Web-based user interface.
* **CLEO** – Command-line interface for configuration and automation.
* **VIPER** – Test execution functionality currently being developed as part of openDuT.

CARL, EDGAR, LEA and CLEO communicate through authenticated interfaces. NetBird and WireGuard are used to establish secure network connectivity between distributed peers.

Documentation:
https://opendut.eclipse.dev/

User Manual:
https://opendut.eclipse.dev/book/user-manual/index.html

Developer Documentation:
https://opendut.eclipse.dev/book/development/getting-started.html

Source Repository:
https://github.com/eclipse-opendut/opendut

## Known Implementation

The reference implementation is the Eclipse openDuT open-source project:

https://github.com/eclipse-opendut/opendut

The implementation supports distributed physical HIL and virtual SIL environments and can be operated in on-premises, cloud or hybrid environments.

## ID (unique name)

BB_Eclipse_OpenDUT

## Description

Eclipse openDuT is an open-source framework for the automated testing and validation of automotive software and Electronic Control Units (ECUs).

It enables physical and virtual Devices under Test to be connected across geographically distributed test environments. openDuT manages these devices, establishes communication between them and provides a common abstraction for creating distributed automotive test setups.

The framework is hardware-agnostic and supports combinations of real Hardware-in-the-Loop (HIL) and virtual Software-in-the-Loop (SIL) devices. Automotive communication such as CAN and Ethernet can be transported between distributed peers through secure network connections.

openDuT targets reliable, repeatable and observable automated testing and supports on-premises, cloud and hybrid deployment scenarios.

## Rationale

Automotive software development increasingly requires testing complex distributed vehicle systems early and continuously. Traditional test environments are often based on locally connected hardware, proprietary tools and isolated test benches.

This leads to several challenges:

* Hardware ECUs may be scarce and only available at specific locations.
* Test benches are often geographically distributed and difficult to share.
* Different test tools and environments require significant manual integration effort.
* Reproducing identical hardware and network configurations across locations is difficult.
* Automated CI/CD-based validation requires remotely accessible and reproducible test infrastructure.
* Software-defined vehicle development requires testing software before complete vehicle hardware is available.

openDuT addresses these challenges by providing a vendor-neutral framework for managing and interconnecting distributed physical and virtual test devices.

This enables remote access to scarce test hardware, distributed test benches, automated test environments and earlier integration and validation of automotive software.

## Governance Applicable S-BB(s)

Depending on the concrete testing and validation use case, the following standards and regulations can be relevant:

* ISO 26262 – Road vehicles – Functional safety
* ISO/SAE 21434 – Road vehicles – Cybersecurity engineering
* UNECE R155 – Cybersecurity and Cybersecurity Management System
* UNECE R156 – Software Update and Software Update Management System
* EU Cyber Resilience Act (CRA)
* AUTOSAR specifications where AUTOSAR-based ECUs or software are part of the test environment

openDuT can provide infrastructure for testing and validation activities related to such standards and regulations. It does **not itself provide or imply certification or compliance** with these standards.

## Compose BB(s)

No mandatory composition with other formally defined FEDERATE Building Blocks is currently specified.

Internally, the openDuT solution consists of several cooperating components, primarily:

* CARL – central management and orchestration
* EDGAR – distributed edge/peer management
* LEA – web-based user interface
* CLEO – command-line interface
* Authentication and authorization infrastructure
* VPN/network connectivity infrastructure
* Telemetry and monitoring infrastructure

External infrastructure such as Keycloak, NetBird, WireGuard and OpenTelemetry is used to provide authentication, secure connectivity and observability.

## What is needed to Design and Implement

Development and extension of openDuT requires, depending on the component:

* Rust development toolchain
* Git
* Nix-based development environment
* Node.js/frontend tooling for web-related development
* Linux development environment
* Container tooling for integration and deployment environments
* Knowledge of automotive communication technologies such as CAN and Ethernet
* Knowledge of distributed systems and networking
* Access to physical or virtual automotive test devices for integration testing
* CI/CD and automated test infrastructure

The majority of the openDuT implementation is written in Rust.

## What is needed to build and run

A typical openDuT deployment requires:

* Linux-based systems for the backend and edge nodes
* Network connectivity between the participating systems
* Docker/Docker Compose for the reference backend deployment
* NetBird and WireGuard for secure peer-to-peer connectivity
* Keycloak for authentication and authorization
* TLS certificates
* Appropriate Linux networking capabilities
* CAN and/or Ethernet interfaces when physical automotive networks are connected
* Required Linux networking functionality such as network bridges and GRE interfaces
* Sufficient privileges on EDGAR systems to configure networking and automotive interfaces
* Optional physical ECUs, test benches or virtual/simulated Devices under Test

EDGAR establishes the required networking on the participating peers and connects automotive interfaces across the distributed infrastructure.

## Non-Functional Requirements

### Reliability and Repeatability

Test setups shall be reproducible and allow reliable execution of distributed automotive tests.

### Security

Communication between openDuT services shall be protected. The current architecture uses:

* TLS for service communication
* WireGuard for encrypted peer-to-peer connections
* OAuth 2.0 / OpenID Connect for authentication
* Keycloak for identity and access management
* Role-based access control
* Authentication of technical components
* Zero-trust principles

### Observability

The distributed test environment shall provide sufficient observability to analyze test setups and failures. openDuT supports collection of logs, metrics and traces using OpenTelemetry-based infrastructure.

### Portability

The framework shall support heterogeneous test environments and shall not depend on a specific ECU or vehicle hardware platform.

### Distribution

Physical and virtual test devices may reside in different networks and geographical locations.

### Scalability

The architecture shall allow multiple peers and Devices under Test to be managed and interconnected.

### Maintainability

Components and interfaces shall be versioned and updated in a controlled manner. Compatibility between CARL, EDGAR and CLEO versions needs to be considered when updating a deployment. CARL database migrations currently require sequential version upgrades.

### Real-time

openDuT transports automotive network communication between distributed systems but does not provide a general hard real-time guarantee across geographically distributed networks.

## Dependencies to other Clusters

openDuT depends on functionality that may be provided by Building Blocks from other Functional Clusters:

* **Security / Identity Management**
  Authentication, authorization, certificates and secure communication.

* **Communication / Networking**
  IP connectivity, VPN functionality and automotive network communication.

* **Observability / Monitoring**
  Logging, metrics and tracing of distributed components.

* **Storage / Persistence**
  Persistent storage of configuration and management information.

* **Deployment / Infrastructure**
  Deployment and operation of backend services and edge components.

Concrete implementations of these functions can be exchanged or integrated where supported by the openDuT interfaces and architecture.

## Vehicle API Relevant

No.

openDuT operates primarily at the test infrastructure, orchestration and automotive network connectivity level. The core framework does not require a standardized vehicle signal API such as COVESA VSS/VISS.

Vehicle APIs may nevertheless be used by tests, applications or Devices under Test connected through openDuT.

## Author/Company

Eclipse openDuT Project / Eclipse Foundation
Eclipse Software Defined Vehicle Working Group

The project was initially proposed by contributors from ETAS GmbH, CARIAD SE, Mercedes-Benz Tech Innovation GmbH, AVL List GmbH and IAV GmbH and is now developed as an Eclipse open-source community project.

## Priority

High

The BB provides enabling infrastructure for distributed, automated and reproducible testing, which is a key capability for continuous software integration and validation in Software-Defined Vehicle development.

## Contribution supported by RDI projects

Yes.

openDuT is further developed and used in the context of the European RDI project **HAL4SDV – Hardware Abstraction Layer for a European Software Defined Vehicle**.

Within HAL4SDV, openDuT is used for distributed automotive testing and validation and for connecting distributed automotive test infrastructure.

The BB can additionally be used within FEDERATE demonstrators and toolchain scenarios to demonstrate interoperable and distributed SDV testing environments.

## Availability of Source Code

Yes / Apache License Version 2.0

The complete reference implementation is publicly available as open source.

## Availability of API

Yes / Apache License Version 2.0

openDuT provides programmatic interfaces for managing peers, clusters, configurations and distributed test infrastructure.

## Type of API

* Remote API
* gRPC / Protocol Buffers API
* Web/HTTP API
* Command-line interface through CLEO

The CARL API provides the central programmatic interface used by LEA, CLEO and EDGAR.

## Potential obstacles

Potential obstacles include:

* Corporate firewall, VPN or network-security restrictions affecting WireGuard/NetBird communication.
* Required network privileges on EDGAR hosts.
* Availability and compatibility of CAN/Ethernet interfaces and corresponding Linux drivers.
* Configuration and operation of the required identity and network infrastructure.
* Certificate and secret management in production environments.
* NAT, firewall and proxy configurations between geographically distributed test locations.
* Version compatibility between CARL, EDGAR and CLEO.
* Migration effort between releases, particularly for persistent CARL data.
* Reproducing timing-sensitive automotive communication over networks with non-deterministic latency.
* Integration of proprietary test tools or hardware may require dedicated adapters.

## Maturity Badges

No formal FEDERATE/Eclipse SDV maturity badge assessment is assigned here. Until such an assessment is performed, the values remain `NotDefined`.

|       | Documentation | Requirements | Coding Guidelines |   Testing  | Release Process |
| ----- | :-----------: | :----------: | :---------------: | :--------: | :-------------: |
| Level |   NotDefined  |  NotDefined  |     NotDefined    | NotDefined |    NotDefined   |

## State (+ date of last change)

**First public release available**

Current latest public release at the time of this BB description:

**Eclipse openDuT v0.10.2 – 2026-06-11**

The Eclipse Foundation currently lists the overall project governance state as **Incubating**.

Last BB review/update: **2026-08-11**

## System Context

openDuT is designed for distributed automotive development and testing environments.

Typical system context:

* Linux-based edge/peer systems
* Physical ECUs and test benches
* Virtual ECUs and SIL environments
* HIL environments
* CAN networks
* Automotive Ethernet networks
* IP networks
* On-premises infrastructure
* Cloud infrastructure
* Hybrid cloud/on-premises deployments
* Container-based backend services
* Web-based user interface
* Command-line-based automation
* VPN-based communication between distributed peers
* CI/CD and automated test environments

The central services can be hosted remotely while EDGAR instances are deployed close to the physical or virtual Devices under Test.

## Compliant to

No formal certification or general conformance claim is currently made for openDuT itself.

The architecture is designed to enable integration into automotive development and testing environments and uses established technologies and standards including:

* OAuth 2.0
* OpenID Connect
* TLS
* WireGuard
* CAN
* Ethernet
* OpenTelemetry

The Eclipse project scope additionally targets interoperability with established automotive architectures and standards such as AUTOSAR. Compliance with safety, cybersecurity or regulatory standards depends on the concrete system, test case and deployment in which openDuT is used.

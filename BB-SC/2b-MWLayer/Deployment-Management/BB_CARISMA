# CAR-Integrated Service Mesh Architecture (CARISMA)

## BB Tags(s)

BB-SC

CARISMA is an in-vehicle stack component providing service-mesh-based communication and service routing for distributed software services running across multiple High-Performance Computers (HPCs) in a Software-Defined Vehicle. Cloud-hosted services may additionally be integrated into the mesh, but the core architecture is designed for the in-vehicle environment.

## Functional Clusters

Communication

The primary responsibility of CARISMA is transparent service-to-service communication, service discovery, routing and location-independent access to distributed services. This classification is also consistent with the FEDERATE Communication cluster, which already contains comparable middleware and service-mesh-related Building Blocks.

## Layer

MWLayer

CARISMA introduces an infrastructure layer between distributed applications and the underlying network. Applications communicate through service proxies without requiring knowledge about the physical location of the target service.

## BB Usage

CARISMA can be used to operate distributed applications across a cluster of in-vehicle HPCs while keeping service-to-service communication independent from the actual deployment location of a service.

A typical usage scenario consists of:

1. One HPC is designated as the **central HPC** and hosts the CARISMA Control Plane in addition to its Data Plane.
2. Additional HPCs operate as **satellite nodes** providing Data Planes.
3. Each HPC runs one service proxy instead of one proxy per application.
4. HPCs register themselves with the CARISMA Node Registry.
5. Services running on the HPCs register with the Service Registry.
6. The Control Plane derives routing configurations from the node and service information and distributes these configurations to the service proxies.
7. Applications communicate through their local proxy without knowing whether the destination service is located on the same HPC, another HPC or potentially in a cloud backend.
8. Services may be re-deployed to another HPC and the routing configuration can be updated transparently without requiring dependent applications to be reconfigured.

The architecture supports multiple instances of a service and thereby enables load-balancing scenarios.

The current implementation exposes gRPC/Protocol Buffers interfaces for node and service registration. `NodeRegistryService` provides node registration and deployment-configuration channels, while `ServiceRegistryService` receives service announcements.

Repository:

`https://github.com/mercedes-benz/car-integrated-service-mesh-architecture`

Architecture publication:

`https://arxiv.org/abs/2403.04378`

## Known Implementation

A prototypical open-source implementation is available in the Mercedes-Benz GitHub organization:

`https://github.com/mercedes-benz/car-integrated-service-mesh-architecture`

The repository contains implementations and tooling including:

* CARISMA Control Plane
* CARISMA Orchestrator
* CARISMA Status Manager
* Node and Service Registry APIs
* Envoy-based service proxy integration
* TOSCA-based deployment descriptions ("ToSCARISMA")
* SOME/IP adapter
* benchmarking and evaluation tooling

The repository explicitly describes the implementation as a prototype supporting the CARISMA architecture.

## ID (unique name)

BB_CARISMA

## Description

The CAR-Integrated Service Mesh Architecture (CARISMA) is an automotive service mesh designed for service-oriented Software-Defined Vehicle architectures based on multiple interconnected High-Performance Computers.

CARISMA separates application functionality from infrastructure-related concerns such as service discovery, routing and service-to-service communication. Applications communicate through a local service proxy and therefore do not need to know on which HPC a requested service is currently deployed.

The architecture consists of a central **Control Plane**, multiple **Data Planes**, and one service proxy per HPC. The Control Plane maintains information about available nodes and services and distributes corresponding routing configurations to the proxies.

In contrast to conventional cloud service meshes, which commonly deploy one sidecar proxy per service, CARISMA uses one proxy per HPC to reduce resource consumption in the resource-constrained vehicle environment.

This enables services to be dynamically deployed or re-deployed across HPCs while maintaining transparent communication between dependent applications. Services located outside the vehicle, such as cloud services, can also be integrated into the service mesh.

## Rationale

Modern automotive E/E architectures increasingly consolidate software functionality on a smaller number of powerful HPCs. At the same time, vehicle applications are becoming distributed and service-oriented.

This creates additional complexity because application developers otherwise need to handle:

* physical service locations,
* service discovery,
* routing,
* changing deployment locations,
* multiple service instances,
* inter-HPC communication,
* and integration with off-board services.

CARISMA introduces the service mesh concept into the automotive domain to separate these infrastructure concerns from application functionality.

A main motivation is to enable software services to move between HPCs without forcing dependent applications to know where a service is currently deployed. This provides an architectural foundation for dynamic deployment, re-deployment and load balancing of vehicle software.

The architecture is specifically adapted to automotive resource constraints. Instead of the conventional sidecar-per-service approach, CARISMA reduces the number of proxies to one per HPC and co-locates the Control Plane with the Data Plane on the central HPC.

The prototype evaluation demonstrated that a service could be moved between HPCs while communication from another software component continued without requiring that component to be reconfigured.

## Governance Applicable S-BB(s)

Depending on the concrete use case and production deployment, relevant governance and Supporting Building Blocks may include:

* ISO 26262 – Functional Safety
* ISO/SAE 21434 – Road Vehicles – Cybersecurity Engineering
* UNECE R155 – Cybersecurity and Cybersecurity Management System
* UNECE R156 – Software Update and Software Update Management System, where dynamic deployment is connected to vehicle software update mechanisms
* AUTOSAR Adaptive / AUTOSAR Communication Management
* AUTOSAR SOME/IP Protocol Specification

CARISMA itself does **not** imply compliance or certification according to these standards. The original work explicitly compares the approach with AUTOSAR Adaptive communication concepts, and later work adds interoperability with SOME/IP-based services.

## Compose BB(s)

No mandatory composition with other formally defined FEDERATE Building Blocks is currently specified.

Conceptually, the CARISMA implementation consists of:

* **Control Plane**

  * Node Registry
  * Service Registry
  * Configuration management

* **Data Plane**

  * One service proxy per HPC

* **Orchestration**

  * Deployment and re-deployment of services

* **Service communication**

  * Routing between local and remote service instances

* **Optional protocol adapters**

  * e.g. SOME/IP integration

The current prototype uses Envoy as service proxy infrastructure. The repository's TOSCA definitions explicitly model the CARISMA Control Plane, HPC nodes, applications and Envoy components.

## What is needed to Design and Implement

Development and extension of the current CARISMA implementation requires or benefits from:

* Go development environment
* Go 1.23 or compatible toolchain
* Protocol Buffers
* gRPC
* knowledge of distributed systems and service-oriented architectures
* knowledge of automotive Ethernet/IP networking
* knowledge of service discovery and service routing
* Envoy/xDS concepts when modifying the proxy infrastructure
* container technologies for the reference deployment approach
* TOSCA knowledge when using or extending the ToSCARISMA deployment description
* automotive middleware knowledge, particularly SOME/IP, when integrating legacy or AUTOSAR-oriented services

The current repository targets Go 1.23 and depends on gRPC, Protocol Buffers, Docker libraries and the Envoy control-plane libraries.

## What is needed to build and run

The prototype can be built as multiple CARISMA binaries including:

* `carisma-control-plane`
* `carisma-orchestrator`
* `carisma-status-manager`
* `carisma-version`

The provided build setup supports several target operating systems and CPU architectures, including Linux as well as amd64, arm64 and ARM targets.

A representative CARISMA runtime environment requires:

* at least one HPC acting as central node,
* optionally additional satellite HPCs,
* IP connectivity between participating HPCs,
* service proxy instances,
* CARISMA Control Plane,
* CARISMA node and service registration,
* a mechanism for deploying the actual application services,
* and sufficient network connectivity to external services if cloud integration is required.

The provided TOSCA configuration uses containerized CARISMA components and an Envoy container image and models creation, start, stop and deletion operations for these components.

## Non-Functional Requirements

### Reliability and Communication Stability

Communication between applications should remain stable even when the deployment location of a service changes. The prototype demonstrated service re-deployment between HPCs without requiring dependent applications to be reconfigured.

### Resource Efficiency

The solution must consider the limited compute and memory resources available in automotive environments compared with conventional cloud infrastructures.

CARISMA therefore avoids the conventional sidecar-per-service model and uses one proxy per HPC.

### Location Transparency

Applications should not need to know the physical node on which another service is deployed. The proxy and Control Plane are responsible for resolving the current service location.

### Dynamic Reconfiguration

Routing configurations must be updateable when services are deployed, removed or moved between HPCs.

### Scalability

The architecture should support multiple HPCs, multiple services and multiple instances of the same service.

### Performance

The additional communication layer introduced by the service mesh should minimize processing and communication overhead.

The original CARISMA work identifies a detailed evaluation of the overhead compared with direct service-to-service communication as further work. Consequently, hard performance guarantees should not currently be assumed.

### Security

Authentication, authorization, communication protection and isolation need to be considered for production deployments. No general automotive cybersecurity certification or complete production security concept is claimed by the current prototype.

### Safety / Real-Time

CARISMA should not currently be assumed to provide hard real-time or functional-safety guarantees. Such guarantees depend on the concrete deployment, communication technology, application and system architecture.

## Dependencies to other Clusters

CARISMA primarily depends on capabilities from the following Functional Clusters:

* **Communication**
  IP/Ethernet networking and service communication between distributed HPCs.

* **Execution / Deployment Management**
  Services have to be deployed, stopped and potentially moved between computing nodes.

* **Automation and Orchestration**
  Dynamic service placement and re-deployment require orchestration functionality.

* **Security and Compliance**
  Production use requires appropriate authentication, authorization and secure communication mechanisms.

* **Monitoring and Observability**
  Runtime information can be used to support deployment decisions, diagnosis and future adaptive service-placement mechanisms.

The exact Building Blocks implementing these capabilities may vary depending on the vehicle platform.

## Vehicle API Relevant

No – not directly.

CARISMA operates at the communication, routing, discovery and deployment-infrastructure level. It does not define a vehicle signal or vehicle data model such as COVESA VSS.

Vehicle APIs such as VSS/VISS or other automotive service interfaces can nevertheless be exposed by applications communicating through CARISMA.

In addition, CARISMA provides integration mechanisms for service-oriented automotive communication technologies such as SOME/IP, but this is separate from defining a vehicle data API.

## Author/Company

Mercedes-Benz / MBition GmbH

Original CARISMA architecture:

* Kevin Klein
* Pascal Hirmer
* Steffen Becker

The original architecture was developed in cooperation between Mercedes-Benz AG and the University of Stuttgart. The current open-source implementation in the Mercedes-Benz GitHub organization identifies MBition GmbH as provider and copyright holder.

## Priority

High

CARISMA addresses a central SDV capability: decoupling distributed software services from their physical deployment location and enabling flexible service placement across centralized vehicle compute platforms.

`High` should be considered a proposed FEDERATE prioritization rather than an officially assigned project maturity or priority.

## Contribution supported by RDI projects

Yes.

The development and research underlying CARISMA was supported by the German RDI project:

**SofDCar – Software-Defined Car**

Project reference: **19S21002**

The CARISMA publication states that the work was partially funded as part of SofDCar, and the repository also acknowledges SofDCar as the supporting research project.

## Availability of Source Code

Yes / MIT

The prototypical implementation is publicly available in the Mercedes-Benz GitHub organization under the MIT License.

## Availability of API

Yes / MIT

The repository contains public Protocol Buffers API definitions for CARISMA's Node Registry and Service Registry.

## Type of API

* Remote API
* gRPC API
* Protocol Buffers interface
* Service-proxy/network interface
* Optional SOME/IP adapter

The current control interfaces use gRPC and Protocol Buffers. The repository additionally includes an adapter for integrating SOME/IP-based services with CARISMA.

## Potential obstacles

Potential obstacles include:

* The current public implementation is explicitly described as **prototypical** and should be thoroughly validated before productive use.
* Additional communication latency and CPU/memory overhead are introduced by the proxy layer. A comprehensive comparison with direct inter-service communication was identified as further work in the original research.
* The centralized Control Plane represents an important coordination component. For production systems, failure handling and high-availability concepts would therefore need to be considered. This is an architectural implication of the current central-HPC design.
* Dynamic service re-deployment requires integration with an appropriate workload/deployment orchestrator.
* Automotive security requirements concerning authentication, authorization, secure communication and isolation require additional system-level consideration.
* Safety-critical or hard real-time applications may require guarantees beyond those currently provided by the prototype.
* Integration with existing automotive middleware and legacy applications may require protocol adapters.
* SOME/IP interoperability is supported through an adapter, but integration with existing AUTOSAR-based systems still needs to be evaluated for the concrete vehicle platform.
* Network partitioning or the loss of an HPC needs to be considered when designing production-grade availability and recovery mechanisms.

## Maturity Badges

No official Eclipse SDV/FEDERATE maturity badge assessment could be identified for CARISMA. Therefore, the maturity values should remain `NotDefined` until a formal assessment is performed.

|       | Documentation | Requirements | Coding Guidelines |   Testing  | Release Process |
| ----- | :-----------: | :----------: | :---------------: | :--------: | :-------------: |
| Level |   NotDefined  |  NotDefined  |     NotDefined    | NotDefined |    NotDefined   |

## State (+ date of last change)

**Implementation started**

A public prototypical implementation is available, but the repository currently does not publish a formal GitHub release. The repository itself explicitly describes the implementation as prototypical.

FEDERATE BB description updated: **2026-08-11**

## System Context

CARISMA targets centralized Software-Defined Vehicle E/E architectures consisting of multiple interconnected High-Performance Computers.

Typical system context:

* Central vehicle HPC
* Additional satellite HPCs
* Automotive Ethernet / IP networking
* Service-oriented / microservice-based applications
* Linux-based or comparable HPC operating environments
* Containerized applications
* Envoy service proxy
* CARISMA Control Plane
* Node and Service Registry
* Deployment/orchestration environment
* gRPC / Protocol Buffers
* Optional cloud/backend services
* Optional SOME/IP-based applications and services

The central HPC hosts both Control Plane and Data Plane, while satellite HPCs only require the Data Plane. One service proxy is deployed per HPC. Cloud services can be represented as additional service endpoints and become reachable transparently through the in-vehicle service proxies.

## Compliant to

CARISMA itself currently makes no formal general compliance or certification claim with automotive safety or cybersecurity standards.

The current implementation and accompanying tooling use or support established standards and technologies including:

* **TOSCA Simple Profile in YAML 1.3** for the provided ToSCARISMA topology and deployment descriptions.
* **Protocol Buffers / gRPC** for CARISMA management APIs.
* **SOME/IP interoperability** through the provided CARISMA SOME/IP adapter.
* **Automotive Ethernet/IP** as the intended inter-HPC communication infrastructure.

Support for SOME/IP should not be interpreted as a general claim of full AUTOSAR compliance. Compliance with ISO 26262, ISO/SAE 21434, UNECE regulations or OEM-specific requirements depends on the concrete implementation and vehicle integration.

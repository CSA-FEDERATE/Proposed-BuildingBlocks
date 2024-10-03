
# Remote Vehicle Interaction

## BB Tags(s)

- SC

## Functional Clusters

- Communication

## Layer

- Middleware

## Known Implementation

- Eclipse uProtocol: <https://projects.eclipse.org/projects/automotive.uprotocol>

## ID (unique name)

## Description

The Goal of this use case cluster is a universal service mesh for connecting services and data sinks/sources across the entire SDV landscape: from the embedded mechantronics domain to the high-compute and connectivity units in vehicles, to backend services and end-user applications. This is the software communication infrastructure that enables almost every higher-level and user-facing use case.

The following key aspects are written from the point of view of an in-vehicle SDV Software stack. This use case cluster is focusing on data and data flows that are not hard real-time critical, and do not have safety implications beyond basic ASIL QM.

## Rationale

- Use commonly used definition language for service interfaces, as a joint source of truth for all involved technology domains
- Employ modularized architecture that enables the inclusion of all kinds of transport-layer protocols, for instance MQTT, Eclipse Zenoh, Android Binder, potentially AUTOSAR SOME/IP, and more
- Support pub/sub and request/response communication across the entire service mesh scope and all involved entities
- Provide cross-domain integration for service discovery, data subscription and digital twin capabilities
- Include considerations around authentication and verification between service and application interaction in such a framework - access control, permissions, usage profiles, trust, etc

## Governance Applicable S-BB(s)

## Compose BB(s)

Link to AUTOSAR SOME/IP protocol, other middleware- and protocol implementations, digital twin concepts, security concepts

## What is needed to Design and Implement

## What is needed to build and run

## Non-Functional Requirements

## Dependencies to other Clusters

- Middleware
- Security
- Communication

## Vehicle API Relevant

- COVESA uServices

## Author/Company

- Daniel Krippner/ETAS GmbH

## Priority

- High

## Related Project(s)

- COVESA uServices
- Eclipse uProtocol
- Eclipse SDV Companion App Blueprint
- Eclipse SDV Fleet Management Blueprint

## Availability of Code

yes

## Availability of Api

yes

## Potential obstacles

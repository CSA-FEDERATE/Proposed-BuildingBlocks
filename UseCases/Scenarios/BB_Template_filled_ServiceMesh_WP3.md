
# Service Mesh

## BB Reference(s)

- BB-SC/MWLayer/Diagnostics/BB_Policy_Manager.md
- BB-SC-TC/Virtualization/BB_Digital_Twin
- S-BB/AppLayer/BB_Standardization_of_Vehicle_API
- S-BB/AppLayer/BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure
- S-BB/MWLayer/BB_Standardized_Data_Description_for_Vehicle_Sensors_Attributes_Actuators
- S-BB/MWLayer/BB_SOA
- S-BB/MWLayer/BB_sSOA

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

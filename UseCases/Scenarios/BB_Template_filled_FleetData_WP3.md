
# Vehicle Fleet Data

## BB Reference(s)

- BB-CEST/BB_Car_Simulator
- BB-SC-TC/Virtualization/BB_Digital_Twin
- BB-SC/MWLayer/Storage/BB_Vehicle_Data_Collector
- BB-SC/MWLayer/Storage/BB_Vehicle_Logging_and_Recording
- BB-SC/OSLayer/Time/BB_Automotive_Edge_Runtime
- S-BB/AppLayer/BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure

## Known Implementation

- Eclipse Fleet Management blueprint: <https://github.com/eclipse-sdv-blueprints/fleet-management>

## ID (unique name)

## Description

The Goal of this use case cluster is systems, abstractions and capabilities related to the extraction of data from the in-vehicle mechatronics domains. This includes both higher layers of abstraction and processing in in-vehicle SDV Software stacks, as well as routing to off-board systems (backend, mobile, etc).
More specific use cases in this cluster might initially address commercial fleet management (FMS) functionality (where bespoke use cases and related data needs are generally well known, and joint definition work is already ongoing e.g. in COVESA).
The following key aspects are written from the point of view of an in-vehicle SDV Software stack. This use case cluster is focusing on data and data flows that are not hard real-time critical, and do not have safety implications beyond basic ASIL QM.

## Rationale

- Use modularized approach for mechatronics data ingest - details of source network stacks and transport protocols need to be encapsulated and isolated from the downstream high-compute domain, and be configurable/extensible via high-compute modules
- Employ unified semantics abstraction for downstream use cases - mechatronics data is bespoke to the source platform and its use by downstream consumers cannot scale without semantic unification at the point where the data enters the high-compute domain  
- Provide extensibility wrt algorithmic/storage/querying/etc functionality - extending a solution with synthetic sensors, new data-related capabilities like storage/query infrastructure, and so on
- Include considerations around authentication and verification between service and application interaction in such a framework - access control, permissions, usage profiles, trust, etc

## Author/Company

- Daniel Krippner/ETAS GmbH

## Priority

- High

## Related Project(s)

- COVESA VSS
- W3C VISS
- Eclipse Kuksa
- Eclipse uProtocol
- Eclipse SDV Companion App Blueprint
- Eclipse SDV Insurance Data Blueprint

## Availability of Code

yes

## Availability of Api

yes

## Potential obstacles

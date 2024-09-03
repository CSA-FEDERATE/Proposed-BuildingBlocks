
# Remote Vehicle Interaction

## BB Reference(s)

- BB-CEST/BB_Car_Simulator
- BB-SC-TC/Virtualization/BB_Digital_Twin
- BB-SC/AppLayer/Communication/BB_AOSP_Push_Notification_Service
- S-BB/AppLayer/BB_Standardization_of_Vehicle_API
- S-BB/AppLayer/BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure

## Known Implementation

- Eclipse Companion App blueprint: <https://github.com/eclipse-sdv-blueprints/companion-application>

## ID (unique name)

## Description

The Goal of this use case cluster is systems abstractions and capabilities related to the (remote) interaction of a vehicle owner/driver with in-vehicle functionality. This includes basic remote function calling for features like HVAC control or charging behavior but can extend to complex scenarios around managing authentication and access for keyless access or ride sharing.
The initial scope and goal can be a set of functional capabilities needed to implement a typical driver companion (mobile) app, similar to what is included in state-of-the-art product offerings in the market.
The following key aspects are written from the point of view of an in-vehicle SDV Software stack. This use case cluster is focusing on data and data flows that are not hard real-time critical, and do not have safety implications beyond basic ASIL QM.

## Rationale

- Use unified semantics for vehicle interaction - e.g. based on COVESA VSC and uServices, with mechatronics abstraction happening as low in the stack as possible.
- Employ software infrastructure for features like driver settings/profile management, synchronized between in-vehicle, backend and mobile domains .
- Involve considerations around authentication and verification between service and application interaction in such a framework - access control, permissions, usage profiles, trust, etc.

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

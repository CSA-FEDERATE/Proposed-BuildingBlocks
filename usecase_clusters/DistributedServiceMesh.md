# Distributed Service Mesh

The Goal of this use case cluster is a universal service mesh for connecting services and data sinks/sources across the entire SDV landscape: from the embedded mechantronics domain to the high-compute and connectivity units in vehicles, to backend services and end-user applications. This is the software communication infrastructure that enables almost every higher-level and user-facing use case.

The following key aspects are written from the point of view of an in-vehicle SDV Software stack. This use case cluster is focussing on data and data flows that are not hard real-time critical, and do not have safety implications beyond basic ASIL QM.

__Key aspects include, but are not limited to:__

- commonly used definition language for service interfaces, as a joint source of truth for all involved technology domains
- modularised architecture that enables the inclusion of all kinds of transport-layer protocols, for instance MQTT, Eclipse Zenoh, Android Binder, potentially AUTOSAR SOME/IP, and more
- support pub/sub and request/response communication across the entire service mesh scope and all involved entities
- cross-domain integration for service discovery, data subscription and digital twin capabilities
- considerations around authentication and verification between service and application interaction in such a framework - access control, permissions, usage profiles, trust, etc

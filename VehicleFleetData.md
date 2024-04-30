# Vehicle Fleet Data

The Goal of this use case cluster is systems, abstractions and capabilities related to the extraction of data from the in-vehicle mechatronics domains. This includes both higher layers of abstraction and processing in in-vehicle SDV Software stacks, as well as routing to off-board systems (backend, mobile, etc).
More specific use cases in this cluster might initially address commercial fleet management (FMS) functionality (where bespoke use cases and related data needs are generally well known, and joint definition work is already ongoing e.g. in COVESA).

The following key aspects are written from the point of view of an in-vehicle SDV Software stack. This use case cluster is focussing on data and data flows that are not hard real-time critical, and do not have safety implications beyond basic ASIL QM.

__Key aspects include, but are not limited to:__

- modularised approach for mechatronics data ingest - details of source network stacks and transport protocols need to be encapsulated and isolated from the downstream high-compute domain, and be configurable/extensible via high-compute modules
- unified semantics abstraction for downstream use cases - mechatronics data is bespoke to the source platform and its use by downstream consumers cannot scale without semantic unification at the point where the data enters the high-compute domain  
- extensibility wrt algorithmic/storage/querying/etc functionality - extending a solution with synthetic sensors, new data-related capabilities like storage/query infrastructure, and so on
- considerations around authentication and verification between service and application interaction in such a framework - access control, permissions, usage profiles, trust, etc

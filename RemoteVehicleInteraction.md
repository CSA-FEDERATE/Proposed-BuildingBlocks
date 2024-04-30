# Remote Vehicle Interaction

The Goal of this use case cluster is systems abstractions and capabilities related to the (remote) interaction of a vehicle owner/driver with in-vehicle functionality. This includes basic remote function calling for features like HVAC control or charging behavior, but can extend to complex scenarios around managing authentication and access for keyless access or ride sharing.
The initial scope and goal can be a set of functional capabilities needed to implement a typical driver companion (mobile) app, similar to what is included in state of the art product offerings in the market.

The following key aspects are written from the point of view of an in-vehicle SDV Software stack. This use case cluster is focussing on data and data flows that are not hard real-time critical, and do not have safety implications beyond basic ASIL QM.

__Key aspects include, but are not limited to:__

- unified semantics for vehicle interaction - e.g. based on COVESA VSC and uServices, with mechatronics abstraction happening as low in the stack as possible
- software infrastructure for features like driver settings/profile management, synchronised between in-vehicle, backend and mobile domains  
- considerations around authentication and verification between service and application interaction in such a framework - access control, permissions, usage profiles, trust, etc

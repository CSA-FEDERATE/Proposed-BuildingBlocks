
# Remote Vehicle Interaction

## BB Tags(s)

BB-SC

## Functional Clusters

Communication, Vehicle Service endpoint definitions Security

## Layer

MWLayer, AppLayer

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

## Governance Applicable S-BB(s)

## Compose BB(s)

## What is needed to Design and Implement

## What is needed to build and run

## Non-Functional Requirements

## Dependencies to other Clusters

- Middleware
- Communication

## Vehicle API Relevant

- [COVESA uServices](https://github.com/COVESA/uservices)

## Author/Company

- Daniel Krippner/ETAS GmbH

## Priority

- High

## Contribution through RDI projects

- [COVESA uServices](https://github.com/COVESA/uservices)
- Eclipse uProtocol
- Eclipse SDV Companion App Blueprint
- Eclipse SDV Fleet Management Blueprint

## Availability of Code

yes

## Availability of Api

yes

## Potential obstacles


## Maturity Badges
<!-- taken over from Eclipse SDV Process 
See Definition of Badges and their Flavors 
https://gitlab.eclipse.org/eclipse-wg/sdv-wg/sdv-technical-alignment/sdv-technical-topics/sdv-process/sdv-process-definition/-/wikis/Definition%20of%20Badges%20and%20their%20Flavors 


| 			| Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Gold		| Badgelevel    | Badgelevel   | Badgelevel		   | Badgelevel	 | Badgelevel  |
| Silver	| Badgelevel    | Badgelevel   | Badgelevel	  	   | Badgelevel	 | Badgelevel  |
| Bronze	| Badgelevel   	| Badgelevel   | Badgelevel	       | Badgelevel	 | Badgelevel  |
| No		| Badgelevel   	| Badgelevel   | Badgelevel	       | Badgelevel	 | Badgelevel  |
| NotDefined| Badgelevel   	| Badgelevel   | Badgelevel	       | Badgelevel	 | Badgelevel  |

Options:
NotDefined/No/Bronze/Silver/Gold

Example:
| 			| Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Level		| [Gold](urlToDoc)| No 		   | Notdefined		   | Bronze	 | [Silver](urlToDoc) |


-->
## State (+ date of last change)

<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->

## System Context

<!-- 
OS and runtime/framework requirements

eg.

- AGL
- QNX
- ROS-based
- container runtime
- web assembly
- web service
 -->
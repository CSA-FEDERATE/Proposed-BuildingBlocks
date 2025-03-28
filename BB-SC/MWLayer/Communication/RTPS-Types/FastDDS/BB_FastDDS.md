# Fast-DDS
## BB Tags(s)
BB-SC; BB-MU; BB-CSC; BB-CMU

## Functional Clusters
Communication

## Layer
MWLayer

## Known Implementation
https://github.com/eProsima/Fast-DDS

## ID (unique name)

## Description
eprosima Fast DDS is a C++ implementation of the DDS (Data Distribution Service) standard of the OMG (Object Management Group). eProsima Fast DDS implements the RTPS (Real Time Publish Subscribe) protocol, which provides publisher-subscriber communications over unreliable transports such as UDP, as defined and maintained by the Object Management Group (OMG) consortium. RTPS is also the wire interoperability protocol defined for the Data Distribution Service (DDS) standard. eProsima Fast DDS expose an API to access directly the RTPS protocol, giving the user full access to the protocol internals.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->

## Governance Applicable S-BB(s)

## Compose BB(s)
OS/Runtime Envirnoment

## What is needed to Design and Implement

## What is needed to build and run
See [supported Platforms](https://github.com/eProsima/Fast-DDS/blob/master/PLATFORM_SUPPORT.md#platform-support)

## Non-Functional Requirements
* Real Time
* QOS

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->

## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->

## Author/Company
[eprosima](https://eprosima.com/)

## Priority
<!-- High, Medium, Low -->

## Related Project(s)
The most complete DDS - Proven: Plenty of success cases. Looking for commercial support? Contact info@eprosima.com 
https://eprosima.com/

## Availability of Source Code
YES/Apache 2.0

## Availability of API
[Fast DDS CLI manual](https://fast-dds.docs.eprosima.com/en/latest/fastddscli/cli/cli.html)

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

|                       | Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Level     | [Gold](https://fast-dds.docs.eprosima.com/en/latest/) | Notdefined       | [Gold](https://github.com/eProsima/Fast-DDS/blob/master/CONTRIBUTING.md) | Notdefined | [Gold](https://github.com/eProsima/Fast-DDS/blob/master/RELEASE_SUPPORT.md) |

## State (+ date of last change)
<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->
Used in several projects (e.g ROS2).
last update Github Jan. 2025 / continuously updated

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
regarding details see section - What is needed to build and run

Ubuntu/Debian, MacOS, Windows, Android, QNX

## Bazel compliance status
<!-- The S-CORE project requires all BB contributions to be ready for BAZEL compliant (https://github.com/bazelbuild/bazel)-->
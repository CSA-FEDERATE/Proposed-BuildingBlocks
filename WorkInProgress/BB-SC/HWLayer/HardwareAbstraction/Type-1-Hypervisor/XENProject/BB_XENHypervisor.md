
# XENProject

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->

- BB-SC; BB-CSC

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->

- HardwareAbstration; Virtualisation; Type-1-Hypervisor

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
- HWLayer

## Known Implementation

- https://github.com/xen-project/xen

## ID (unique name)

## Description
<!-- General Description of the BB -->

The Xen Project team is a global open source community that develops the Xen Project Hypervisor and its associated subprojects.

Our mission is to advance virtualization technology across a wide range of commercial and open-source domains.
Illustration of a computer monitor displaying bar charts with Xen Project Logo

source: https://xenproject.org/

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->

The Xen Project focuses on revolutionizing virtualization by providing a versatile and powerful hypervisor that addresses 
the evolving needs of diverse industries :

- Empower Innovation: Tailored virtualization to drive progress across various domains.
- Enhance Cloud Ecosystems: Elevate cloud capabilities with high-performing, reliable virtualization.
- Secure Critical Systems: Safeguard data and applications through industry-leading security.
- Revolutionize Embedded Technologies: Transform embedded and automotive sectors with mature, safe, secure solutions.

source: https://xenproject.org/

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->

- MISRA-C (misra compliance checker in the build pipeline)
- ISO26262 (safety concept for tbd. HW under development)

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->

- Linux with XEN packages
- optional: XEN tools (.e.g. xl)

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->

- Tracing support (e.g. LTTng) to perform performance analyses and tests - to evaluate real-time capabilities ->  HAL4SDV project
- Evaluation availability and support for drivers used in the automotive domain - openCAN Stack, ... -> HAL4SDV projeckt

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->

- Supported hardware (e.g. hhtps://hcl.xenserver.com/)
- Supported OS (Linux, Windows, MacOS, Zeyphr, ...)


## Non-Functional Requirements
<!-- With respect to Safety, Security, Realtime, … -->

- Safety (support for mixed criticality VMs on one host) 
- Security (support encryption, Identity and Access Managemnt)
- Real-Time (support firm and soft real-time) 

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->


## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->

- Yes, information about platform utilisation, software versions, stored error, ... should be accessible at any time (also from outsiede) via a standardised API and a standardised data model/format.

## Author/Company

- Mario Driussi / VIF

## Priority
<!-- High, Medium, Low -->

- High

## Related Project(s)
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework -->

- HAL4SDV
- XEN Project

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->

- YES/ Apache-2.0; BSD-2-Clause; BSD-3-Clause;BSD-3-Clause-Clear; CC-BY-4.0; GPL-2.0; LGPL-2.0; LGPL-2.1; MIT, MIT-O
- https://github.com/xen-project/xen/tree/master/LICENSES

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->

- YES / LGPL-2.1 XENAPI

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

- Used in production by e.g. AWS Cloud Services
- last change 28.02.2025 (retrieved 03.03.2025)

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

- Type-1-Hypervisor

 ## Bazel compliance status
 <!-- The S-CORE project requires all BB contributions to be ready for BAZEL compliant (https://github.com/bazelbuild/bazel)-->

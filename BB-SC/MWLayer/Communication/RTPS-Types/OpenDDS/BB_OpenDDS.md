# OpenDDS
## BB Tags(s)
BB-SC; BB-MU; BB-CSC; BB-CMU

## Functional Clusters
Communication

## Layer
MWLayer

## Known Implementation
https://github.com/OpenDDS/OpenDDS

## ID (unique name)

## Description
OpenDDS is an open-source C++ implementation of the Object Management Group's specification "Data Distribution Service for Real-time Systems" (DDS), as well as some other related specifications. These standards define a set of interfaces and protocols for developing distributed applications based on the publish-subscribe and distributed cache models. Although OpenDDS is itself developed in C++, Java bindings are provided so that Java applications can use OpenDDS. OpenDDS also includes support for the DDS Security and XTypes specifications.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->

## Governance Applicable S-BB(s)
This release of OpenDDS is based on the DDS Specification formal/2015-04-10 (version 1.4). It features the following transport protocols:

*    TCP/IP
*    UDP/IP
*    IP multicast
*    RTPS over UDP/IP (unicast and multicast)
*    Shared memory

RTPS (Interoperability) features are based on the [DDS-RTPS Specification formal/2019-04-03 (version 2.3)](https://www.omg.org/spec/DDSI-RTPS/2.3). See the OpenDDS Developer's Guide and the file [docs/design/RTPS](https://github.com/OpenDDS/OpenDDS/blob/master/docs/design/RTPS) for more details on RTPS.

See the Developer's Guide for information on OpenDDS compliance with the DDS specification. If you would like to contribute a feature or sponsor the developers to add a feature please see the Support section above for contact information.

## Compose BB(s)
OS/Runtime Envirnoment

## What is needed to Design and Implement
These are just the required dependencies. For a complete detailed list of dependencies, including optional ones, see https://opendds.readthedocs.io/en/latest-release/devguide/building/dependencies.html.

## What is needed to build and run
Operating Systems

This release of OpenDDS has been tested under the following platforms:

Linux family:

Red Hat EL and CentOS 6.6, 6.8, 6.9 (x86_64)
Red Hat EL and CentOS 7.2, 7.3, 7.4 (x86_64)
Red Hat EL 8.0 (x86_64)
Fedora 24 and 31 (x86_64)
Debian 9.4 (i686)
Ubuntu 22.04 LTS (x86_64)
openSUSE 42.1 (x86_64)
Yocto 3.4.4 (ARMv8)

Windows family:

Windows 7 (32-bit, 64-bit)
 Windows Server 2012 R2 (64-bit)
 Windows 10 (64-bit)

Embedded/Mobile/IoT:

LynxOS-178 (OpenDDS Safety Profile)
VxWorks 6.9, 7, 21.03 (see below)
[Linux on Raspberry Pi](https://opendds.readthedocs.io/en/latest-release/devguide/quickstart/pi.html)
[Android 9.0 "Pie" (API Level 28) NDK r18b](https://opendds.readthedocs.io/en/latest-release/devguide/building/android.html)

We have built OpenDDS for VxWorks 6.9, 7, and 21.03 and have run basic system and performance tests (but not the entire regression test suite). Please see the [OpenDDS Support page](https://opendds.org/support.html) for more information on support for ACE, TAO, and OpenDDS on VxWorks. Download VxWorks RPM packages for ACE, TAO, and OpenDDS [here](https://objectcomputing.com/products/opendds/vxworks).

Compilers

This release of OpenDDS has been tested using the following compilers:

 Microsoft Visual C++ 10 with SP1 (Visual Studio 2010)
 Microsoft Visual C++ 11 (Visual Studio 2012) - Update 4
 Microsoft Visual C++ 12 (Visual Studio 2013) - Update 5
 Microsoft Visual C++ 14 (Visual Studio 2015) - Update 3
 Microsoft Visual C++ 14.1 (Visual Studio 2017) cl 19.16.27048
 Microsoft Visual C++ 14.2 (Visual Studio 2019) cl 19.29.30146
 gcc 4.4.7, 4.8.5
 gcc 6.2.1, 6.3.0
 gcc 7.2.0, 7.3.0, 7.5.0
 gcc 8.2.0, 8.2.1
 gcc 9.3.1
 gcc 12.2.0
 Ubuntu clang 14.0.6
 Ubuntu clang 15.0.0

## Non-Functional Requirements
Real Time
QOS

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->

## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->

## Author/Company
Anonymous

## Priority
<!-- High, Medium, Low -->

## Related Project(s)
OpenDDS is an open source C++ implementation of the Object Management Group (OMG) Data Distribution Service (DDS). OpenDDS also supports Java bindings through JNI. 
http://www.opendds.org/

## Availability of Source Code
YES/OpenDDS (Licensed Product) is protected by copyright, and is distributed under the following terms.

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->

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


| 			| Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Level		| [Gold](https://opendds.readthedocs.io/en/latest-release/)| Notdefined | [Gold](https://opendds.readthedocs.io/en/latest-release/devguide/index.html)	| Notdefined	| [Gold](https://opendds.readthedocs.io/en/latest-release/news.html) |

## State (+ date of last change)
<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->
Used in several projects
Last Update Github Jan. 25 / continuously updated

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

Regarding details see section - What is needed to build and run

Ubuntu/Debian/Red Hat, openSUSE, Yocto, Windows, LynxOS, VxWorks, Android

## Bazel compliance status
<!-- The S-CORE project requires all BB contributions to be ready for BAZEL compliant (https://github.com/bazelbuild/bazel)-->
# embeddedRTPS - DDS for Ressource-constrained environments

## BB Tags(s)

- BB-SC, BB-CSC, BB-MU, BB-CMU

## Functional Clusters

- Communication

## Layer

- MWLayer

## Known Implementation

- Github repo: <https://github.com/embedded-software-laboratory/embeddedRTPS>

## ID (unique name)

## Description

This repository contains source code for embeddedRTPS, a portable and open-source C++ implementation of the Real-Time Publish-Subscribe Protocol (RTPS) for embedded system. RTPS is based on the publish-subscribe mechanism and is at the core of the Data Distribution Service (DDS). DDS is used, among many other applications, in Robot Operating System 2 (ROS2) and is also part of the AUTOSAR Adaptive platform. embeddedRTPS allows to integrate Ethernet-capable microcontrollers into DDS-based systems as first-class participants.
embeddedRTPS is portable, as it only consumes lightweightIP and FreeRTOS APIs, which are available for a large number of embedded systems. embeddedRTPS avoids dynamic memory allocation once endpoints are constructed possible. Please note that embeddedRTPS only implements rudimentary Quality-of-Service (QoS) policies and is far from a complete RTPS implementation.


## Rationale
- This light-weight DDS stack allows to integrate ressource constraint devices into SOA architectures. DDS is used as a middleware in AUTOSAR Adaptive and ROS 2.

## Governance Applicable S-BB(s)

- https://www.omg.org/spec/DDS/ (deviations from spec.)
- https://www.omg.org/spec/DDSI-RTPS/ (implemented partially) 
- https://www.omg.org/spec/DDS-SECURITY/ (not implemented in pub version)


## Compose BB(s)

- FreeRTOS or other OS/Runtime Envirnoment
- lwIP (could be another NW Stack)


## What is needed to design and implement

The Repo include a reference implementation which is executable on different Targets /STM32, AURIX Tricore.
Needed:
- MW Layer to use it with ROS2 (RMW) or adaptive AUTOSAR (commonAPI support).
- Support for Security concepts in the OSS implementation. (see Applicable S-BB(s))

## What is needed to build and run
 
See: Example with a getting started for STM32 (Linux/Mac)
GCC (Ubuntu 18 and above), Tasking Compiler,  
<https://github.com/embedded-software-laboratory/embeddedRTPS-STM32>


## Non-Functional Requirements

- Real-Time
- Security

## Dependencies to other clusters


## Vehicle API relevant

“No”

## Author/Company + Prio

- Alexandru Kampmann RWTH - (High/Mid/Low)


## Related project(s)

- <https://github.com/mROS-base/mros2>
- <https://github.com/micro-ROS>

## Availability of code

Yes / License MIT
Commercial Closed Source Parts are available (security)

## Availability of API

Yes / License MIT

## Reference to FEDERATE SDV repository - Open Toolchain(s)

-

## Potential obstacles

-

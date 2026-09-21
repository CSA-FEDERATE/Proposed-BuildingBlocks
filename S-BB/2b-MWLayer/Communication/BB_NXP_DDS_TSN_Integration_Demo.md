# NXP DDS-TSN Integration Demo

## BB Tags(s)
S-BB

## Functional Clusters
Communication

## Layer
MWLayer

## BB Usage

Software-Defined Vehicles may carry critical and best-effort traffic over the
same Ethernet network.

This building block demonstrates how DDS, Linux networking, and TSN can be
combined to provide differentiated handling of communication flows.

## Known Implementation

[NXP dds-tsn repository](https://github.com/NXP/dds-tsn)

A modernized update has been developed internally at NXP. It includes:

- Eclipse Cyclone DDS support
- a newer Gazebo environment
- a newer ROS 2 and Ubuntu 22.04 environment

This update is not yet publicly available. Minor refactoring and formal NXP
open-source clearance must be completed before publication.

## ID (unique name)

## Description

The NXP DDS-TSN Integration Demo is a communication reference design showing
how Data Distribution Service (DDS) traffic can be integrated with
Time-Sensitive Networking (TSN).

The demo uses ROS 2 and a Gazebo-based automotive moose-test scenario. It
shows how network interference can affect critical control traffic and how
TSN prioritization and shaping can protect that traffic.

## Rationale

Integration of DDS traffic with TSN Ethernet makes communication more
deterministic.

## Governance Applicable S-BB(s)

The code is licensed under the Apache License 2.0.

## Compose BB(s)

No other BBs are required.

## What is needed to Design and Implement

System requirements are covered in the repository's README.

## What is needed to build and run

Build and run instructions are included in the repository's README.

## Non-Functional Requirements

The repository details calibration mechanisms to demo timing effects from
the DDS-TSN integration.

## Dependencies to other Clusters

None.

## Vehicle API Relevant

No.

## Author/Company

NXP Semiconductors.

## Priority

Low.

## Contribution supported by RDI projects

Supported by the HAL4SDV project.

## Availability of Source Code

Yes, under the Apache License 2.0.

## Availability of API

Yes, under the Apache License 2.0.

## Type of API

Hardware API.

## Potential obstacles


## Maturity Badges

| 			| Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Level		| NotDefined | NotDefined | Notdefined | NotDefined	 | NotDefined |

## State (+ date of last change)

- First public release available.
- Updates are coming up in 2026 or early 2027.

## System Context

- DDS-based, but uses ROS for the demo

## Compliant to
 
Complies with the DDS standards.

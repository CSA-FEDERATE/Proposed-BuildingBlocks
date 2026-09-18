# Unreal Car Simulation Demo

## BB Tags(s)

BB-CSC-TC, BB-CSC, BB-CEST

## Functional Clusters

TBD

## Layer

Application / Simulation

## BB Usage

Repository: <https://github.com/M3S-Kuura/Unreal-car-simulation-demo>. Provides an Unreal Engine 5.6 project that connects to a Kuksa VSS databroker via a WebSocket client (VissClient) to receive vehicle signals inside Unreal Engine.

## Known Implementation

<https://github.com/M3S-Kuura/Unreal-car-simulation-demo>

## ID (unique name)

TBD

## Description

Provides a previously missing bridge where raw CAN bus data from a physical vehicle can be normalised through COVESA VSS and can be consumed by other UE5-based simulator such as CARLA. This opens the pipeline for real-world vehicle data in simulation environments that previously had no path to raw CAN input.​

The data moves bidirectionally: what happens in the car is reflected in UE5, and signals can also be injected from the Kuksa client side.​

[source:](https://github.com/M3S-Kuura/Unreal-car-simulation-demo)

## Rationale

Modern vehicles have decade-long lifecycles, yet continuous software updates require rigorous, repeatable testing that physical environments cannot reliably provide.​ Digital twin environments enable realistic simulation of hardware, sensors, and safety-critical scenarios — at lower cost and without physical risk.​ Thus Digital Twins can aid in providing the rigorous testing continuous software updates need. UE5's real-time physics and high-fidelity rendering make it well-suited as a digital twin platform.​ VSS, on the other hand, provides a standardised, manufacturer-agnostic, hierarchical signal model for vehicle data, and it bridges the semantic gap between raw CAN frames and application-level signals.

Signals are gathered through the Kuksa-databroker, using Unreal's WebSocket client implementation, so the databroker acts as an API for vehicle signals. The Unreal-side client can be configured to listen to specific VSS paths on the server; once received, it is up to the consuming application what to do with the data. As of now, the client only implements reading functionality, since the primary goal was to simulate signals inside Unreal rather than write them back.


## Governance Applicable S-BB(s)

TBD

## Compose BB(s)

TBD

## What is needed to Design and Implement

Unreal Engine 5.6 (C++), WebSocket client implementation, COVESA VSS knowledge

## What is needed to build and run

Unreal Engine 5.6, an IDE for building the project's C++ code, Docker

## Non-Functional Requirements

Real-time signal consumption via WebSocke from a vehicle. Depends on an external Kuksa-databroker instance for signal data.

## Dependencies to other Clusters

TBD

## Vehicle API Relevant

TBD

## Author/Company

UOULU

## Priority

-

## Contribution supported by RDI projects

TBD

## Availability of Source Code

YES - <https://github.com/M3S-Kuura/Unreal-car-simulation-demo>

## Availability of API

TBD

## Type of API

WebSocket client (VissClient) to Kuksa-databroker

## Potential obstacles

TBD

## Maturity Badges

TBD

## State (+ date of last change)

Mirrored demo repository, 161 commits as of September 2026.

## System Context

Unreal Engine 5.6, Kuksa ecosystem, Docker

## Compliant to

COVESA VSS (Vehicle Signal Specification)

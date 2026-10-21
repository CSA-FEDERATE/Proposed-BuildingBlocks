# Service-to-Signal Blueprint

## Overview
Service-to-Signal is an Eclipse SDV blueprint demonstrating how to bridge in-vehicle microservices (running on the vehicle edge) with physical vehicle signals (engine parameters, sensor data, actuator commands). It uses uProtocol as the unified communication framework to expose vehicle services and signals over a common network interface.

## Purpose
- Reference pattern for exposing in-vehicle services and signals via uProtocol
- Integration of service-oriented middleware with signal-based vehicle data
- Unified network API for vehicle-to-cloud and vehicle-to-roadside communication
- Demonstration of SDV communication patterns and service interfaces
- Bridge between traditional signal-based vehicle architecture and modern microservices

## Key Capabilities
- uProtocol-based service definition and subscription
- Signal-to-service mapping and translation layers
- Physical hardware integration (CAN, LIN, Ethernet gateway)
- Service discovery and dynamic invocation
- Event-driven signal streaming to cloud and external services

## Usage
Service-to-Signal is deployed as a reference architecture for vehicles transitioning from traditional signal-based architectures to service-oriented SDV patterns.

**Communication flow:**
```
Physical Hardware (CAN, LIN, Ethernet)
    ↓
Signal Adapter / Gateway
    ↓
Service-to-Signal Bridge
    ↓
uProtocol Service Interface
    ↓
Vehicle-to-Cloud / Vehicle-to-Roadside Link
```

## Known Implementations
- Eclipse SDV Blueprints reference: https://github.com/eclipse-sdv-blueprints/service-to-signal
- Integration with Eclipse uProtocol framework
- Used in OpenADKit and autonomous driving platforms

## Rationale
Service-to-Signal bridges legacy signal-centric vehicle architectures with modern SDV service frameworks, enabling gradual migration and coexistence of both paradigms in real vehicle deployments.

## Dependencies
- **Requires:** uProtocol framework, vehicle signal sources (CAN/LIN/Ethernet), SDV runtime
- **Composes with:** [BB_fleet_management](../../Cloud-Infrastructure-and-Deployment/Edge-to-Cloud-Integration/BB_fleet_management.md), cloud connectivity layers, analytics and monitoring
- **Integrates with:** Signal databases (DBC, ODX), OBD-II interfaces, telematics gateways, cloud backends

## State
Active reference blueprint in Eclipse SDV ecosystem, regularly updated for latest communication patterns.

## Tags
`BB-CEST`, `Blueprint`, `Communication`, `uProtocol`, `EdgeToCloud`, `SDV`, `EclipseSDV`, `Automotive`, `Services`

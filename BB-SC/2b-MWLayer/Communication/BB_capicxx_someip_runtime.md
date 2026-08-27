# CommonAPI C++ SOME/IP Runtime

## Overview
The SOME/IP (Scalable Service-Oriented Middleware over IP) runtime for CommonAPI C++ provides protocol-specific bindings and serialization for service-oriented communication over IP networks. It enables vehicle services to communicate efficiently across ECUs and network boundaries.

## Purpose
- SOME/IP protocol implementation for CommonAPI C++ framework
- Efficient binary serialization and deserialization of service messages
- Network transport abstraction for in-vehicle and vehicle-to-cloud communication
- Support for request/response and event notification patterns
- Integration with AUTOSAR ServiceInterface definitions

## Key Capabilities
- SOME/IP packet parsing and generation
- Header-only or compiled serialization for performance
- Unicast and multicast message support
- UDP/TCP transport options
- Service discovery integration (SD protocol)
- Error handling and protocol conformance

## Usage
SOME/IP runtime is deployed in AUTOSAR ECUs and middleware platforms requiring network-based inter-service communication.

**Typical protocol stack:**
```
Application (CommonAPI C++ proxy/stub)
│
├─ CommonAPI core runtime
│
├─ SOME/IP runtime (serialization, protocol logic)
│
└─ Transport (UDP/TCP sockets)
```

## Known Implementations
- COVESA reference implementation: https://github.com/COVESA/capicxx-someip-runtime
- Integrated into AUTOSAR Adaptive and Classic platforms
- Deployed in modern vehicle network architectures (Ethernet-based ECU clusters)

## Rationale
SOME/IP is the de facto standard for service-based communication in automotive middleware, offering low latency, efficient bandwidth usage, and seamless integration with CommonAPI and AUTOSAR frameworks.

## Dependencies
- **Requires:** CommonAPI C++ core runtime, network transport (UDP/TCP), AUTOSAR-compatible platform
- **Composes with:** [BB_capicxx_core_runtime](BB_capicxx_core_runtime.md), Ethernet middleware, service discovery systems
- **Integrates with:** AUTOSAR ServiceInterface, vehicle network stacks, diagnostic systems

## State
Mature, established protocol standard in automotive. Actively maintained and deployed across OEM platforms.

## Tags
`BB-SC`, `BB-CEST`, `BB-CSC-TC`, `Middleware`, `Communication`, `SOMEIP`, `Network`, `COVESA`, `AUTOSAR`, `C++`

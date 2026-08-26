# CommonAPI C++ Core Runtime

## Overview
CommonAPI C++ core runtime provides the foundational C++ language bindings and runtime infrastructure for service-oriented communication in vehicle middleware. It abstracts underlying IPC mechanisms (D-Bus, SOME/IP, signal-based) and provides a unified interface for inter-process communication.

## Purpose
- Standardized C++ API for service-based vehicle software architecture
- Abstraction over multiple IPC protocols (D-Bus, SOME/IP, native)
- Type-safe, generated code for service interfaces and data types
- Support for synchronous and asynchronous method calls and signals
- Foundation for AUTOSAR middleware layers

## Key Capabilities
- Code generation from Franca IDL interface definitions
- D-Bus integration for in-vehicle service discovery and communication
- Support for complex data types, enumerations, and nested structures
- Lifecycle management and error handling
- Integration with vehicle platform middleware (AUTOSAR, Genivi/COVESA)

## Usage
CommonAPI C++ is deployed as a middleware runtime in AUTOSAR-based vehicle ECUs and Linux-based infotainment systems.

**Typical integration:**
```
C++ application
├─ CommonAPI core runtime (libcommonapi)
├─ Franca-generated service proxies/stubs
└─ Protocol runtime (D-Bus, SOME/IP, or custom)
```

## Known Implementations
- COVESA reference implementation: https://github.com/COVESA/capicxx-core-runtime
- Integrated into AUTOSAR environments (Adaptive Platform)
- Used in numerous OEM middleware stacks (Bosch, Daimler, BMW, Volkswagen)

## Rationale
CommonAPI C++ standardizes service-oriented communication patterns across automotive middleware, reducing integration complexity and enabling multi-vendor interoperability in vehicle software stacks.

## Dependencies
- **Requires:** C++ compiler (C++11+), D-Bus or custom IPC backend
- **Composes with:** [BB_capicxx_someip_runtime](BB_capicxx_someip_runtime.md), Franca IDL tooling, application services
- **Integrates with:** AUTOSAR Adaptive, middleware frameworks, signal-based communication systems

## State
Mature, established standard in automotive industry. Actively maintained and widely deployed.

## Tags
`BB-SC`, `BB-CEST`, `BB-CSC-TC`, `Middleware`, `Communication`, `ServiceOriented`, `COVESA`, `AUTOSAR`, `C++`

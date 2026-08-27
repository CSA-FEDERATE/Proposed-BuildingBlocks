# DLT Viewer (Diagnostic Trace Viewer)

## Overview
DLT Viewer is the reference engineering tool for inspecting, filtering, and analyzing diagnostic traces captured by DLT daemon. It provides a desktop application with GUI for live and offline trace analysis, enabling developers and test engineers to debug vehicle software behavior.

## Purpose
- Real-time and post-mortem trace analysis and filtering
- Visual inspection of diagnostic logs from DLT daemon
- Advanced search, correlation, and export capabilities
- Support for ECU and application-level trace contexts
- Integration with development and testing workflows

## Key Capabilities
- Live trace connection to running vehicle or simulator
- Offline trace file loading and playback
- Multi-level filtering (context, log level, application, message type)
- Trace parsing and human-readable output formatting
- Export to CSV, plain text, and other formats
- Plugin support for domain-specific trace analysis

## Usage
DLT Viewer runs on developer/test machines (Windows, macOS, Linux) to analyze traces from vehicles or simulations.

**Typical installation:**
```
Qt-based desktop application
- Build: qmake or CMake
- Runtime: Qt libraries (5.x or 6.x)
- Network: TCP/UDP connections to DLT daemon instances
```

## Known Implementations
- COVESA reference implementation: https://github.com/COVESA/dlt-viewer
- Included in AGL (Automotive Grade Linux) SDK and development kits
- Widely used by OEM engineering and quality teams

## Rationale
DLT Viewer is essential tooling for developers working with DLT-instrumented vehicle software, enabling efficient root-cause analysis and validation of in-vehicle diagnostic behavior.

## Dependencies
- **Requires:** DLT daemon running on target vehicle or simulator, Qt framework (5.x+)
- **Composes with:** [BB_dlt_daemon](../../../BB-SC/2b-MWLayer/Diagnostics/BB_dlt_daemon.md), continuous-integration monitoring, cloud trace ingestion
- **Integrates with:** Debugging frameworks, test automation platforms

## State
Mature, actively maintained by COVESA. Standard tool in automotive development environments.

## Tags
`BB-CEST`, `Development-Tools`, `Debugging`, `Diagnostics`, `Testing`, `COVESA`, `GUI`, `Automotive`

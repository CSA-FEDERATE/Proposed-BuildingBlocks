# AAS-based Sensor Plug-and-Play for Software-Defined Vehicles

## BB Tags(s)
BB-SC, BB-CSC

## Functional Clusters
Configuration (Hardware Abstraction / Zero-Configuration Sensor Integration)

## Layer
MWLayer

## BB Usage
The building block lets a vehicle integrate a newly connected sensor without any manual driver installation or configuration. It consists of three cooperating components, each with its own README in the repository.

**1. OEM Server (cloud / off-board).** An Eclipse BaSyx AAS environment (AAS repository, AAS registry, submodel registry) started with Docker Compose. It hosts one Asset Administration Shell (AAS) per supported sensor type. The AAS carries the hardware identifiers (e.g. USB vendor/product ID), references to the containerized driver image and to the containerized vehicle application image, and the description of the sensor data interface. AAS files are validated with the official AAS Test Engines before publication.

```bash
cd oem_server
docker compose up -d
# AAS Environment: http://localhost:8081, AAS Registry: :8082, Submodel Registry: :8083
```

**2. Edge Device / Sensor ECU (in-vehicle).** A Python Bootstrap Agent running on a Raspberry Pi. It monitors the USB bus with pyudev, extracts the identifiers of a newly connected device, queries the OEM server for a matching AAS, validates it, pulls the referenced driver container with the Docker SDK and starts it. The agent then exposes the AAS and the data endpoint of the sensor on the local network.

```bash
cd edge_device
./install.sh              # installs dependencies and the systemd service
python3 bootstrap_agent.py --config config.yaml
```

**3. UGV / Vehicle System (in-vehicle).** A ROS 1 (Noetic) package running on the vehicle computer. A sensor monitor polls the AAS endpoint of the edge device, reads the referenced application container, pulls and starts it on the vehicle, and stops it again when the sensor is removed. Applications consume the abstracted sensor data via REST and publish to ROS or to the Eclipse KUKSA Databroker (VSS).

```bash
cd ~/catkin_ws && catkin_make && source devel/setup.bash
roslaunch pnp_sensor_monitor monitor.launch pi_address:=<edge-device-ip>
```

End-to-end flow: plug in sensor, identifier read, AAS fetched from OEM server, driver container started on the ECU, application container started on the vehicle, data available. Measured time from plug-in to usable data is about two seconds for USB cameras and ultrasonic sensors.

## Known Implementation
https://github.com/akshaynarla/aas-pnp

Publication: "Plug-and-Play Sensor Evolution in Software-Defined Vehicles through Asset Administration Shells", IEEE International Conference on Emerging Technologies and Factory Automation (ETFA) 2026, Västerås, Sweden. Accepted and presented; proceedings not yet online.

## ID (unique name)
IAS-AAS-Sensor-Plug-and-Play

## Description
The building block provides zero-configuration integration of heterogeneous sensors into a Software-Defined Vehicle by using the Asset Administration Shell (IEC 63278) as a standardized, machine-readable digital twin of the sensor. The AAS acts as the single source of truth for what a sensor is, how it is identified, which containerized driver abstracts it, and which containerized vehicle application consumes it.

The architecture is distributed over three roles. The OEM server holds the catalogue of sensor AAS files in an Eclipse BaSyx environment. A Bootstrap Agent on the sensor ECU detects hardware at runtime, resolves the hardware identity to an AAS, and deploys the driver as a container. The vehicle runtime observes the AAS endpoint of the ECU and deploys the matching application container. Driver and application are therefore decoupled from each other and from the vehicle software stack. Sensor data is exposed through a uniform REST interface and can be bridged into ROS or into the COVESA VSS tree via the Eclipse KUKSA Databroker.

The implementation is a complete, runnable prototype evaluated on an unmanned ground vehicle with a Raspberry Pi as sensor ECU, using USB cameras and USB ultrasonic sensors.

## Rationale
Integrating a new or replacement sensor into a vehicle today requires manual driver installation, hand-written configuration and a software release that is specific to the vehicle variant. This binds the vehicle software to the exact hardware bill of materials and makes late hardware changes, aftermarket extensions and multi-supplier sourcing expensive.

Software-Defined Vehicles need the opposite: hardware that can be swapped or added while the application software stays untouched. The AAS already gives the industry a standardized, vendor-neutral way to describe an asset and its interfaces. This building block applies that standard to the sensor integration problem and shows that the digital twin of a sensor is sufficient to drive discovery, driver deployment and application deployment automatically. The result is a hardware abstraction layer at the configuration level, complementary to signal-level abstractions such as VSS.

## Governance Applicable S-BB(s)
- IEC 63278 Asset Administration Shell (metamodel, part 1; API, part 2)
- COVESA Vehicle Signal Specification (S-BB BB_VSS) for the data published by the vehicle applications

## Compose BB(s)
- Eclipse BaSyx (AAS infrastructure, OEM server side)
- BB-SC BB_Eclipse_KUKSA (optional VSS publication of sensor data on the vehicle)
- Container runtime (Docker) on ECU and vehicle computer

## What is needed to Design and Implement
Python 3, Docker and Docker Compose, Eclipse BaSyx AAS components, AAS Test Engines for validating AAS files, ROS 1 Noetic (catkin) for the vehicle-side package. Knowledge of the AAS metamodel is needed to author a sensor AAS; example AAS files for a camera and an ultrasonic sensor are provided.

## What is needed to build and run
- OEM server: any Linux host with Docker.
- Sensor ECU: Linux single-board computer with USB and Docker (tested on Raspberry Pi), network reachability to the OEM server at deployment time.
- Vehicle computer: Linux with ROS 1 Noetic and Docker, network reachability to the sensor ECU.

## Non-Functional Requirements
- Plug-in to data latency in the order of seconds (measured about 2 s).
- Security: AAS files are validated before use. Container images and AAS endpoints are not yet signed or authenticated; this is required before any productive use.
- Safety: the building block itself is not safety-rated; it is intended for non-safety-critical and research sensors in the current state.

## Dependencies to other Clusters
- FC Communication: REST between the three components, optional ROS and KUKSA/VSS.
- FC Deployment / Execution Management: container runtime on ECU and vehicle. Could be replaced by an SDV orchestrator such as Eclipse Ankaios.
- FC Security: authentication of the OEM server and signing of container images are open.

## Vehicle API Relevant
Yes. Sensor data from plug-and-play sensors is published to the COVESA VSS tree via the KUKSA Databroker. The AAS submodels used to describe sensor interfaces could serve as a proposal for a standardized sensor-description data model complementary to VSS (see WorkInProgress S-BB "Standardized Data Description for Vehicle Sensors, Attributes, Actuators").

## Author/Company
akshay.narla AT ias DOT uni-stuttgart DOT de / Institute of Industrial Automation and Software Engineering (IAS), University of Stuttgart

## Priority
Medium

## Contribution supported by RDI projects
Yes. Chips Joint Undertaking, Framework Partnership Agreement No 101139789 (HAL4SDV), and German Federal Ministry of Research, Technology and Space (BMFTR), grant 16MEE0472.

## Availability of Source Code
Yes / Apache-2.0

## Availability of API
Yes. AAS API (BaSyx, HTTP/REST) and the sensor data REST interface exposed by the driver containers.

## Type of API
Web API (REST), Library/Framework API (ROS package)

## Potential obstacles
- Only USB-attached sensors are currently supported. CAN, LIN, FlexRay and automotive Ethernet sensors require an identification mechanism other than USB descriptors.
- Service discovery on the local network may be blocked in managed vehicle networks.
- No security chain yet (signed AAS, signed images, authenticated OEM server).
- Research prototype; no long-term maintenance commitment beyond the HAL4SDV project.

## Maturity Badges


## State (+ date of last change)
First public release available (research prototype). Last commit April 2026.

## System Context
- Linux (Debian/Ubuntu) on ECU and vehicle computer
- Container runtime (Docker)
- ROS 1 Noetic (Ubuntu 20.04) on the vehicle side
- Eclipse BaSyx (Java, containerized) on the OEM server
- Optional: Eclipse KUKSA Databroker

## Compliant to
Asset Administration Shell (IEC 63278, AAS metamodel v3), Eclipse BaSyx, Eclipse KUKSA / COVESA VSS, ROS 1.

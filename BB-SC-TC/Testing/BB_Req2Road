# Req2Road – GenAI Pipeline for SDV Test Artifact Generation and On-Vehicle Execution

## BB Tags(s)

BB-EST, BB-SC-TC

Req2Road is primarily an Engineering & Support Tool for the development and testing of in-vehicle software components. It additionally represents a toolchain because it combines requirements processing, GenAI-based test generation, standardized vehicle-signal mapping, test-code generation, and execution against SiL and ViL environments.

## Functional Clusters

Testing

Additional relation to:

* Requirements Engineering
* AI-assisted Engineering
* Test Automation

The main Functional Cluster should be **Testing**, since the primary output of Req2Road is executable test specifications and test implementations derived from system requirements.

## Layer

AppLayer

This is a proposed FEDERATE classification.

Req2Road is an engineering application/toolchain operating above the actual vehicle middleware and operating-system layers. It generates and executes test artifacts but is not itself a vehicle runtime middleware component.

## BB Usage

Req2Road transforms heterogeneous automotive specification artifacts into executable Software-Defined Vehicle tests.

Typical inputs include:

* natural-language requirements,
* tables,
* UML or behavioral diagrams,
* a Vehicle Signal Specification catalog,
* examples or templates of the target test framework,
* and examples of the target vehicle-access API.

The Req2Road pipeline comprises four main phases:

1. **Initial Gherkin Scenario Generation**
   LLMs and VLMs analyze textual requirements and behavioral diagrams and generate initial Given/When/Then scenarios in Gherkin syntax.

2. **VSS Signal Mapping**
   Relevant COVESA Vehicle Signal Specification signals are identified using a retrieval-based approach. The VSS catalog is preprocessed, embedded, searched and re-ranked to produce a small candidate set before an LLM selects the corresponding VSS paths.

3. **Refined Gherkin Generation**
   The generated scenarios are enriched with explicit VSS paths, connecting high-level behavioral requirements with standardized vehicle signals.

4. **Test Code Generation**
   The VSS-enriched Gherkin scenarios, examples of the KUKSA client API and Behave templates are provided to an LLM, which generates executable Python test artifacts.

The generated artifacts can subsequently be executed against a Software-in-the-Loop or Vehicle-in-the-Loop environment.

In the evaluated implementation:

* GPT-5 was used for initial Gherkin generation,
* Qwen 2.5 VL 72B was used as a locally deployable VLM for diagram analysis,
* GPT-4o-mini was used for VSS mapping,
* GPT-4.1 was selected for Python test-code generation,
* Behave was used as BDD test framework,
* KUKSA provided VSS-based vehicle-signal access.

The resulting tests were first executed in the digital.auto Software-in-the-Loop environment and subsequently transferred to a real-vehicle Vehicle-in-the-Loop setup. Only the connection parameters to the VSS/KUKSA backend needed to be changed; the generated test logic itself could be reused.

## Known Implementation

A prototype implementation of Req2Road has been developed and evaluated using a Child Presence Detection System (CPDS) as the system under test.

Public supplementary artifacts include:

* prompts,
* Gherkin feature files,
* VSS mappings,
* generated Python test scripts,
* and the digital.auto CPDS prototype.

These artifacts are publicly available through a released digital.auto vehicle model associated with the publication.

The prototype was successfully evaluated both in:

* Software-in-the-Loop using digital.auto and KUKSA,
* Vehicle-in-the-Loop using a production vehicle with VSS-based signal access.

## ID (unique name)

BB_Req2Road

## Description

Req2Road (Requirements-to-Road) is a Generative-AI-based engineering pipeline that transforms heterogeneous Software-Defined Vehicle requirements and behavioral specifications into executable automotive test artifacts.

The approach bridges the gap between requirements engineering and executable vehicle testing by combining Large Language Models, Vision-Language Models, Retrieval-Augmented Generation, Behavior-Driven Development and standardized vehicle-signal models.

Natural-language requirements, tables and behavioral diagrams are transformed into structured Gherkin scenarios. Req2Road subsequently maps scenario elements to standardized COVESA VSS signals and generates executable Python test code.

The resulting artifacts are designed to be reusable across different execution environments. The approach was demonstrated by executing generated tests first in a Software-in-the-Loop environment and subsequently in a Vehicle-in-the-Loop setup using the same test logic.

Req2Road therefore acts as a translation layer between:

**Requirements → Executable Specifications → Standardized Vehicle Signals → Test Code → SDV Test Environment**

## Rationale

Testing Software-Defined Vehicles is increasingly difficult because software functionality is distributed across complex vehicle architectures while requirements and test artifacts are represented in heterogeneous formats.

Typical challenges include:

* requirements written in natural language,
* ambiguous or incomplete specifications,
* behavioral information contained in diagrams and tables,
* manually created test specifications,
* inconsistent vehicle-signal naming,
* test implementations tied to specific test benches,
* and significant manual effort when translating requirements into executable tests.

Req2Road addresses these challenges by automating substantial parts of the transformation from requirements to executable test artifacts.

A central design decision is the use of COVESA VSS as a standardized intermediate representation for vehicle signals. This separates generated tests from proprietary signal names and enables improved portability between SDV environments and test benches.

The evaluated CPDS case showed that **32 of 36 requirements (89%)** could be transformed into executable Gherkin scenarios without modification. Human review nevertheless remained necessary, particularly for ambiguous edge cases and incompletely specified logical conditions.

## Governance Applicable S-BB(s)

### COVESA Vehicle Signal Specification

COVESA VSS is a central Supporting Building Block for Req2Road.

VSS provides the standardized vehicle-signal vocabulary used to connect requirement-level concepts with executable test implementations.

Potentially relevant automotive engineering standards and regulations include:

* ISO 26262 – Functional Safety
* ISO/SAE 21434 – Automotive Cybersecurity
* Automotive SPICE
* UNECE R155
* UNECE R156

Req2Road itself does **not** currently claim compliance or tool qualification according to these standards. For safety-relevant testing, appropriate validation, governance and human approval remain necessary.

For the demonstrated CPDS use case, Euro NCAP Child Presence Detection requirements were additionally relevant to the definition of the evaluated functionality.

## Compose BB(s)

No mandatory composition with formally defined FEDERATE BB IDs has currently been specified.

Conceptually, Req2Road composes several capabilities:

* Requirements and specification ingestion
* LLM-based text processing
* VLM-based diagram understanding
* Retrieval-Augmented Generation
* VSS catalog and signal mapping
* Gherkin / Behavior-Driven Development
* Test-code generation
* KUKSA-based vehicle-data access
* Test execution framework
* SiL / ViL execution environment

Potential corresponding Building Blocks include:

* **S-BB: COVESA VSS**
* vehicle data broker / VSS access
* GenAI model runtime
* test execution framework
* SDV simulation environment
* Vehicle-in-the-Loop interface

The concrete mapping to existing FEDERATE BB IDs should be performed where suitable Building Blocks exist.

## What is needed to Design and Implement

Depending on the concrete implementation, development of Req2Road requires:

* Python development environment
* LLM and VLM access
* optionally locally hosted GenAI models
* prompt templates
* embeddings / SentenceTransformer models
* vector or nearest-neighbor retrieval
* cross-encoder re-ranking
* COVESA VSS catalog
* Gherkin knowledge
* Behave or another compatible BDD framework
* KUKSA Python SDK or equivalent VSS-access library
* SDV test environment
* domain knowledge for requirement validation
* automotive test-automation knowledge

The RAG-based mapping process requires preprocessing of the hierarchical VSS catalog, semantic embeddings of signals and scenarios, retrieval of relevant candidate signals and subsequent LLM-based selection.

## What is needed to build and run

A representative Req2Road setup requires:

* Python runtime
* Behave or compatible Gherkin/BDD framework
* access to the selected LLM/VLM backend
* VSS catalog
* embedding and retrieval infrastructure
* KUKSA client or equivalent VSS interface
* KUKSA Data Broker or compatible vehicle-signal backend
* target SDV application or system under test
* SiL, HiL or ViL environment for test execution

For the evaluated SiL setup, the SDV Runtime and KUKSA Data Broker ran in a Docker-based digital.auto environment.

For the evaluated ViL setup, Behave was executed on an external computer connected to an NVIDIA Jetson installed in the vehicle. The Jetson aggregated vehicle communication and exposed the relevant signals as VSS paths through KUKSA. This particular hardware setup is an example and is **not an architectural requirement of Req2Road**.

## Non-Functional Requirements

### Correctness

Generated test artifacts must preserve the semantics of the originating requirements.

Automatically generated artifacts shall not be assumed to be correct without validation.

### Traceability

Generated Gherkin scenarios, VSS mappings and test-code steps should maintain traceability to the corresponding source requirements.

### Hallucination Control

Generated vehicle-signal references must be constrained to valid entries from an authoritative signal catalog.

Req2Road therefore uses retrieval and prefiltering before LLM-based VSS selection. Experiments showed substantially degraded mapping quality when models were exposed directly to the full catalog of 982 signals compared with a curated shortlist.

### Human Oversight

Human-in-the-loop review is required for:

* ambiguous requirements,
* signal mapping,
* generated code,
* test oracles,
* timing constraints,
* and release-relevant tests.

The paper explicitly recommends mandatory human approval for safety-relevant release decisions.

### Data Protection

Confidential automotive requirements and design artifacts should not automatically be transferred to external GenAI services.

Req2Road therefore supports locally deployable LLMs and VLMs for sensitive engineering artifacts.

### Reproducibility

Model versions, prompts, generation parameters, VSS versions and generated artifacts should be recorded to enable repeatability and traceability.

### Portability

Tests should use standardized vehicle-signal representations where possible to reduce dependency on a specific vehicle or test environment.

Using VSS enabled the evaluated tests to move from SiL to ViL with only environment-specific connection changes.

### Safety

Generated tests must not directly be considered qualified evidence for safety-critical release decisions without additional verification and governance.

Execution of generated code should take place in appropriately isolated environments.

## Dependencies to other Clusters

Req2Road depends on capabilities from several other Functional Clusters.

### Requirements

Requirements and behavioral specifications constitute the main input of the pipeline.

### Vehicle Data / Data Models

A standardized vehicle-signal catalog such as COVESA VSS is required for portable signal mapping.

### AI / GenAI

LLM, VLM, embedding and retrieval capabilities are used for specification interpretation, signal mapping and code generation.

### Simulation and Emulation

SiL or comparable environments are needed for early execution of generated test artifacts.

### Communication

The test environment requires access to vehicle signals through a suitable interface such as KUKSA/VSS.

### Security and Compliance

Handling proprietary engineering artifacts and executing AI-generated code require appropriate data-protection, access-control, sandboxing and governance mechanisms.

## Vehicle API Relevant

**Yes exists – COVESA Vehicle Signal Specification (VSS).**

VSS is an essential part of Req2Road.

Req2Road maps requirement-level concepts to standardized VSS paths before test-code generation. This reduces dependence on proprietary signal names and provides a common signal representation for SiL and ViL execution.

Example conceptual mapping:

Requirement concept:

`Cabin temperature`

Mapped vehicle signal:

`Vehicle.Cabin.HVAC.CabinTemperature`

The VSS paths are subsequently included directly in the generated Gherkin scenarios and Python test implementation.

## Author/Company

Authors:

* Denesa Zyberaj
* Lukasz Mazur
* Pascal Hirmer
* Nenad Petrovic
* Marco Aiello
* Alois Knoll

Organizations involved:

* Mercedes-Benz AG
* University of Stuttgart
* Technical University of Munich

## Priority

High

Req2Road addresses a major SDV engineering challenge: reducing the manual gap between requirements and executable validation while simultaneously improving portability through standardized vehicle interfaces.

`High` is a proposed FEDERATE prioritization and not an officially assigned maturity level.

## Contribution supported by RDI projects

Yes.

The work was supported by:

**HAL4SDV – Hardware Abstraction Layer for a European Software Defined Vehicle**

The publication acknowledges funding from the European Chips Joint Undertaking under Framework Partnership Agreement **No. 101139789**, including German national funding under grant number **16MEE00471K**.

Req2Road is therefore suitable as an RDI contribution demonstrating AI-supported testing, standardized vehicle abstractions and SiL-to-ViL portability within an SDV engineering toolchain.

## Availability of Source Code

**Partially / prototype artifacts publicly available**

The publication provides the generated and supporting artifacts publicly through the digital.auto playground, including prompts, Gherkin files, VSS mappings and generated Python test scripts.

At the time of this BB description, no standalone open-source Req2Road repository with an explicitly stated software license has been identified.

Therefore, an explicit open-source license should **not** be claimed for the complete Req2Road pipeline unless such a repository or license is published.

## Availability of API

No dedicated Req2Road API has currently been specified.

Req2Road integrates existing APIs and interfaces, especially:

* KUKSA Python client API
* VSS-based vehicle-signal access
* APIs or local interfaces of LLM/VLM backends

## Type of API

For the integrated components:

* Library / Framework API
* Remote API
* Vehicle Data API
* GenAI Model API

No dedicated externally standardized Req2Road API is currently defined.

## Potential obstacles

Potential obstacles include:

* ambiguous or incomplete natural-language requirements,
* hallucinated test logic or vehicle signals,
* scalability to large requirements sets,
* reduced signal-mapping accuracy for large unfiltered catalogs,
* incorrect or incomplete test oracles,
* decreasing code-generation quality for complex scenarios,
* dependence on LLM/VLM model quality,
* model-version changes affecting reproducibility,
* confidentiality of proprietary requirements and architecture artifacts,
* restrictions on using cloud-hosted GenAI models,
* computational requirements of large locally deployed LLMs/VLMs,
* execution risks associated with automatically generated code,
* integration with proprietary vehicle-signal catalogs,
* mapping between VSS and OEM-specific signals,
* differences between vehicle architectures,
* and the absence of formal qualification for safety-critical testing.

The evaluation showed that complexity is particularly relevant: generation quality decreased when several requirements were combined into one scenario, and the authors conclude that sampling, execution-based validation and human review remain necessary.

The current evaluation additionally covers only one SDV platform and one vehicle configuration, so broader validation across different architectures and signal catalogs remains necessary.

## Maturity Badges

No formal Eclipse SDV/FEDERATE maturity badge assessment is currently available for Req2Road.

|       | Documentation | Requirements | Coding Guidelines |   Testing  | Release Process |
| ----- | :-----------: | :----------: | :---------------: | :--------: | :-------------: |
| Level |   NotDefined  |  NotDefined  |     NotDefined    | NotDefined |    NotDefined   |

## State (+ date of last change)

**Implementation started**

A working prototype has been implemented and evaluated in both Software-in-the-Loop and Vehicle-in-the-Loop environments. Public experimental artifacts are available, but the work is explicitly presented as a feasibility and architectural demonstration rather than a production-ready engineering product.

Last BB update: **2026-08-11**

## System Context

Req2Road is primarily an **off-board engineering toolchain for the development and validation of in-vehicle software**.

Typical system context:

* Requirements-management artifacts
* Natural-language specifications
* UML / behavioral diagrams
* LLM / VLM execution environment
* local or cloud-based GenAI models
* RAG / embedding infrastructure
* COVESA VSS catalog
* Python
* Gherkin
* Behave
* KUKSA Python SDK
* KUKSA Data Broker
* digital.auto or comparable SiL environment
* Docker-based SDV runtime
* Vehicle-in-the-Loop environment
* vehicle interface exposing standardized VSS paths

A typical flow is:

`Requirements / Diagrams`

→ `LLM / VLM analysis`

→ `Initial Gherkin`

→ `RAG-based VSS mapping`

→ `VSS-enriched Gherkin`

→ `Python test generation`

→ `SiL execution`

→ `ViL execution`

The architecture is intended to make the generated test specification and implementation as independent as possible from the specific execution environment.

## Compliant to

Req2Road currently makes no formal certification or compliance claim.

The BB is designed to use or integrate established specifications and technologies including:

* **COVESA Vehicle Signal Specification (VSS)**
* **Gherkin / Behavior-Driven Development**
* **KUKSA vehicle-data interfaces**
* **Python / Behave**

COVESA VSS provides the primary standardized vehicle-data abstraction used by Req2Road.

For safety-relevant use cases, standards such as ISO 26262 and Automotive SPICE may influence the surrounding development and verification process, but Req2Road itself should not currently be described as formally compliant or qualified according to these standards.

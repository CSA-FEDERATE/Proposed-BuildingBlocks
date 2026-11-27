# CyberLLM: Multi-Agent LLM Framework for Automotive Cybersecurity
## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-CEST, BB-SC-TC

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Security

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
AppLayer

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->
Automotive cybersecurity analysis, autonomous vulnerability detection, source-code security analysis, runtime-log analysis, deployment-topology analysis, guarded remediation, attack simulation, and LLM-assisted cyber-defense for Software Defined Vehicles (SDVs).

## Known Implementation
Prototype multi-agent implementation combining deterministic security analysis, LLM-based refinement, decision and response agents, runtime security guards, signed cross-session memory, and attack simulation.
The framework analyzes three main types of automotive engineering artifacts:
- Source code
- Runtime and communication logs
- ECU/service deployment topologies
It supports C, C++, Rust, and other software artifacts through rule-based and AST-based analysis mechanisms, including integration with Bandit and Semgrep where applicable.

The methodology, implementation, and evaluation of CyberLLM are described in: "CyberLLM: A Multi-Agent LLM Framework for Autonomous Detection and Guarded Response in Automotive Cybersecurity" by Nenad Petrovic, Oussama Jeddou, Feres Ben Fraj, Vahid Zolfaghari, Fengjunjie Pan, Andre Schamschurko, and Alois Knoll.
Paper preprint: https://arxiv.org/pdf/2608.06651
Source code: https://github.com/Jeddou10/CyberLLM

## ID (unique name)
tum-cyberllm-automotive-cybersecurity

## Description
<!-- General Description of the BB -->
CyberLLM is a multi-agent, LLM-orchestrated cybersecurity framework for Software Defined Vehicles (SDVs). It provides autonomous vulnerability detection and guarded remediation while ensuring that security-relevant actions are checked by a deterministic and auditable runtime safety envelope before execution.
The detection workflow combines deterministic and AI-based analysis. An always-active deterministic layer uses regular-expression rules, Abstract Syntax Tree (AST)-based analyzers, and deployment-topology graph checks. These findings provide a reproducible security-analysis baseline and grounding context for subsequent LLM analysis.
An LLM refinement stage analyzes the deterministic findings and can identify additional semantic vulnerabilities that are difficult to detect using static patterns alone, including data races, time-of-check/time-of-use (TOCTOU) problems, use-after-free vulnerabilities, and integer overflow.
Findings from the different detection mechanisms are normalized into a common representation containing information such as rule identifier, severity, evidence, explanation, source agent, affected asset category, and source-code location.
A dedicated Decision Agent aggregates these findings and determines an appropriate response tier:
none → soft → moderate → hard
The decision is additionally influenced by verified cross-session memory containing previous security incidents and successful remediation strategies. The mechanism follows an escalate-only principle: previous experience can increase the response level but cannot reduce a security response selected for the current incident.
An Action Generator translates the decision into a multi-step remediation plan. Actions can be selected from deterministic security playbooks and an MCP-style tool registry. Each action is checked individually before execution.
A Security Guard provides the central safety mechanism of CyberLLM. It evaluates proposed actions against four contextual security properties: task alignment, action alignment, source authorization, and data isolation. An independent LLM-based action-alignment oracle can further reject actions but cannot override deterministic security restrictions.
CyberLLM additionally includes a symmetric attack pipeline for generating non-destructive attack scenarios, enabling defense and attack mechanisms to be evaluated using the same vulnerabilities and automotive scenarios.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
SDVs increasingly rely on complex software, networked ECUs, external services, over-the-air updates, and AI-enabled components. As a result, vulnerabilities can originate from several layers, including application source code, runtime behavior, communication logs, and vehicle deployment topology.
Traditional cybersecurity tools typically analyze these layers separately. Static analyzers can reliably identify known vulnerability patterns but may miss semantic and contextual vulnerabilities. LLMs provide stronger contextual reasoning but introduce probabilistic behavior and the possibility of hallucinated findings or unsafe remediation decisions.
CyberLLM therefore combines deterministic security analysis with LLM-based reasoning rather than relying exclusively on either approach.
The deterministic layer establishes a reproducible security baseline, while LLM agents refine the results and detect vulnerabilities requiring deeper semantic interpretation. At the response level, deterministic runtime guards constrain the actions proposed by probabilistic agents.
This architecture enables increased automation while maintaining explicit control over actions affecting safety- and security-critical vehicle systems.

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
Automotive cybersecurity governance, AI-assisted engineering governance, security policy enforcement, AI-agent governance, provenance management, security validation, human oversight, software assurance, and engineering-data governance.

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->
LLM inference component, deterministic security scanner, regex rule engine, AST analyzer, topology analyzer, log analyzer, LLM refinement agent, completeness critic, Decision Agent, Action Generator, Security Guard, action-alignment oracle, signed incident memory, asset-classification component, MCP-style tool registry, attack orchestrator, attack generator, ethics guard, and remediation/rollback mechanisms.

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
Automotive source code, runtime and communication logs, ECU/service deployment descriptions, cybersecurity rules, vulnerability definitions, topology constraints, security policies, LLM models, prompting strategies, deterministic security analyzers, provenance mechanisms, response playbooks, remediation tools, persistent incident storage, and validation mechanisms.
A common representation for detected security findings is required so that results from deterministic and AI-based scanners can be aggregated and processed by downstream decision agents.
The deterministic detection layer requires machine-readable security rules, including code-analysis rules, log-analysis rules, and deployment-topology invariants.
The response subsystem requires explicit security objectives and mappings between authorized actions and those objectives. Actions must include clearly defined schemas, side effects, preconditions, postconditions, and rollback behavior.
Cross-session learning requires tamper-evident storage. CyberLLM uses signed incident records so that historical security information can influence future decisions without allowing unverified memory entries to modify security behavior.

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->
The implementation requires:
- Python and the required cybersecurity and AI libraries.
- Access to suitable LLM models through configured inference interfaces.
- Deterministic security rules for source code, logs, and deployment topologies.
- AST/static-analysis tools such as Bandit and Semgrep where applicable.
- Automotive source-code repositories and/or software artifacts.
- Runtime, telemetry, CAN, or other communication logs when runtime analysis is performed.
- ECU, service, actor, and datasource topology descriptions when deployment analysis is performed.
- A security-rule knowledge base.
- Persistent storage for signed security incidents and remediation history.
- Cryptographic mechanisms for verifying stored incident information.
- Security playbooks and authorized remediation tools.
- An MCP-style tool registry when dynamic action selection is enabled.
- Sandboxed execution and rollback mechanisms for security actions.

Both locally deployed and externally hosted LLMs can be integrated depending on privacy, cybersecurity, latency, and computational requirements.

## Non-Functional Requirements
<!-- With respect to Safety, Security, Realtime, … -->
Deterministic enforcement of security-critical constraints, traceability of vulnerability findings, provenance of analyzed information, auditability of autonomous decisions, reproducibility of deterministic analyses, tamper-resistant memory, protection against memory poisoning, controlled execution of remediation actions, rollback capability, isolation of security tools, and validation of AI-generated actions before execution.
The framework should additionally support high detection precision, extensibility of security rules, heterogeneous programming languages, interoperability with automotive software and communication artifacts, and fail-safe behavior when AI-generated outputs are malformed or uncertain.

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->
Generative AI/LLM infrastructure, automotive cybersecurity, SDV architecture engineering, static software analysis, vehicle communication infrastructure, software deployment and topology modeling, security knowledge bases, AI-agent orchestration, persistent storage, and security-policy enforcement.

## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->
Yes.
CyberLLM can analyze vehicle-facing software components, communication interfaces, service deployments, and runtime information. The evaluation includes automotive modules such as CAN-to-Ethernet gateways, UDS security-access handlers, OTA firmware-update agents, ADAS sensor-fusion components, CAN-FD parsers, telemetry components, key stores, and a local fleet Vehicle API.
The approach can therefore support cybersecurity analysis of components exposing or consuming Vehicle API functionality.

## Author/Company
TUM

## Priority
<!-- High, Medium, Low -->
Medium

## Contribution supported by RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework) -->

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
Yes

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->

## Type of API
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->
Library/Framework API

## Potential obstacles
LLM hallucinations, false or incomplete vulnerability findings, missed semantic vulnerabilities, prompt injection, memory poisoning, unsafe remediation proposals, incorrect interpretation of automotive software behavior, incomplete security rules, inaccurate deployment-topology descriptions, and dependency on the quality of security context supplied to the agents.
Autonomous cybersecurity actions introduce additional risks in safety-critical automotive systems. Consequently, probabilistic agent decisions cannot directly authorize security-sensitive modifications.
Scalability can also become challenging when analyzing large software repositories, extensive vehicle logs, complex ECU/service topologies, or multiple interacting security incidents.
The quality of LLM-based analysis depends on the selected model and available contextual information, while deterministic analyzers remain limited by their predefined rules.
For these reasons, CyberLLM uses deterministic guards, independent action validation, authenticated provenance, tamper-evident memory, constrained tool execution, and rollback mechanisms before autonomous actions are committed.

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
| | Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --- |:---:|:---:|:---:|:---:|:---:|
| Level | Gold | Gold | Gold | Gold | Gold |

## State (+ date of last change)
<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->
First public release available (2026-10-09)

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
CyberLLM operates as part of an SDV cybersecurity and AI-assisted engineering toolchain.
Automotive source code, runtime logs, and deployment-topology information enter dedicated security-analysis agents. Deterministic scanners first identify known vulnerabilities and policy violations using regex rules, AST analyzers, log-analysis rules, and topology constraints.
These findings provide grounding information to LLM-based scanners, which refine the results and search for additional semantic vulnerabilities. All detected findings are normalized and merged before being passed to the Decision Agent.
The Decision Agent evaluates the findings, affected assets, severity, confidence, previous incidents, and remediation outcomes to select an appropriate response tier.
The Action Generator converts this decision into an executable remediation plan based on deterministic playbooks and, where enabled, tools from an MCP-style registry.
Before execution, each action passes through the Security Guard. The guard verifies task alignment, action alignment, source authorization, and data isolation. An independent action-alignment oracle provides an additional validation layer. Refused actions trigger re-planning rather than execution.
Approved actions can be executed with pre/post-condition checking and rollback support. Successful outcomes are stored in HMAC-signed cross-session memory and can subsequently inform future security decisions.
A parallel attack workflow performs passive reconnaissance and generates controlled, non-destructive exploit scenarios. An Ethics Guard checks authorization, scope, and destructive behavior before attack artifacts are accepted. This enables attack and defense capabilities to be evaluated against equivalent automotive cybersecurity scenarios.
The framework was evaluated on nine original automotive ECU modules implemented in C, C++, and Rust containing 47 labeled vulnerabilities together with two clean controls. The deterministic Fast configuration detected 34% (16/47) of the vulnerabilities at perfect precision. Adding LLM refinement and a completeness critic increased coverage to approximately 70% (33/47), with recall of 0.70, F1 of 0.83, and zero findings on the clean controls.

## Compliant to
<!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
none stated

# Rosetta VSS - AI-assisted Signal to VSS Mapper

## BB Tags(s)

BB-EST

## Functional Clusters

Generator (Signal Mapping / Data Model Alignment)

## Layer

MWLayer

## BB Usage

Rosetta VSS maps proprietary automotive signal definitions to standard COVESA Vehicle Signal Specification (VSS) paths. Input artifacts are CAN DBC files, C/C++ headers or sources with signal definitions, and YAML signal lists. The output is a reviewed mapping table and, optionally, a ready-to-use configuration for the Eclipse KUKSA CAN Provider.

Pipeline:

1. **Parse.** Each input signal is normalized to name, description, unit, and context.
2. **Hybrid retrieval.** For every signal, the Top-K candidate VSS paths are retrieved by fusing dense sentence embeddings (semantic similarity) with BM25 (lexical matching), using reciprocal rank fusion. Automotive naming conventions are handled by dedicated lexical rules.
3. **Confidence routing.** Scores above a high-confidence threshold are auto-accepted. Scores below the user threshold become *proposals* for new VSS signals (open-set case). Scores in between are sent to the judge.
4. **LLM-as-Judge (bounded).** The judge sees only the signal and the retrieved candidates and returns confirm, override (another candidate) or veto (no candidate fits). It cannot invent a VSS path; any out-of-set answer is treated as a veto.

Run the Streamlit UI:

```bash
cd kuksa-incubation/rosetta-vss
uv venv && uv sync
uv run streamlit run app.py
```

In the sidebar, load a VSS release (download links are pre-configured), upload a `.dbc`, `.c/.h` or `.yaml` file, set the confidence threshold and click *Run Mapping*. Set `HF_TOKEN` to enable the LLM judge.

Export a KUKSA CAN Provider configuration from the mapping result:

```python
from vss_mapper.exporters import generate_kuksa_config
generate_kuksa_config(mapping_result, "can_provider_config.json")
# produces general.mapping = [{vss_path, can_signal, transform?, interval_ms?}, ...]
```

Drop the output into the KUKSA CAN Provider to ingest the mapped signals into a running Databroker.

## Known Implementation

https://github.com/eclipse-kuksa/kuksa-incubation/tree/main/rosetta-vss

Publication: A peer-reviewed paper describing the method and evaluation is under review (2026).

## ID (unique name)

Eclipse-KUKSA-Rosetta-VSS

## Description

Rosetta VSS is an engineering tool that automates the first step of bringing an existing vehicle onto a VSS-based data layer: deciding which proprietary signal corresponds to which standard VSS path. It combines classic information retrieval (dense plus lexical) with a confidence-based routing policy and an optional, strictly bounded LLM judge. The design goal is traceable, reviewable mappings rather than free LLM generation: every mapping decision is tied to a retrieval score, a candidate list and, where used, a judge verdict, and uncertain cases are explicitly routed to human review or to a proposal for extending VSS.

The tool is part of the Eclipse KUKSA incubation and exports directly into the KUKSA CAN Provider configuration format, so a mapped DBC can be put on a Databroker without hand-editing.

## Rationale

Every OEM and supplier describes vehicle signals in its own naming scheme, spread over DBC files, embedded C code and internal YAML or Excel lists. Adopting a common vehicle API such as VSS therefore starts with a large, error-prone manual mapping exercise, repeated for each platform and each VSS release. Pure LLM-based mapping is fast but unverifiable and prone to hallucinated paths. Pure lexical matching fails on abbreviations and supplier-specific naming.

Rosetta VSS addresses this by grounding the mapping in retrieval over the actual VSS release, by making confidence explicit, and by constraining the LLM to a choice among retrieved candidates. Signals that do not fit VSS are surfaced as proposals instead of being forced onto a wrong path, which gives a structured input for VSS extension requests.

## Governance Applicable S-BB(s)

- COVESA Vehicle Signal Specification (S-BB BB_VSS)
- COVESA VISS (S-BB BB_VISS) as the access protocol of the resulting data

## Compose BB(s)

- BB-SC BB_Eclipse_KUKSA (Databroker and CAN Provider as the deployment target of the generated configuration)
- S-BB BB_VSS (the target data model)

## What is needed to Design and Implement

Python 3.12 or newer, uv or pip, PyTorch and sentence-transformers for dense retrieval, rank-bm25, cantools for DBC parsing, Streamlit for the UI. An optional Hugging Face token for the LLM judge. A VSS release (JSON export) as knowledge base.

## What is needed to build and run

Desktop or server with Python 3.12, about 4 GB RAM; a GPU is optional and only speeds up embedding of large VSS trees. Internet access to download the VSS release and the embedding model on first run. The tool runs off-board at design time, not in the vehicle.

## Non-Functional Requirements

- Traceability: every mapping carries its retrieval score, candidate set and judge verdict.
- No automatic acceptance in the uncertain band; human review or proposal path is enforced.
- Security: the LLM judge can use a locally hosted model; no vehicle data has to leave the premises.
- Not real-time; design-time tool.

## Dependencies to other Clusters

- FC Communication: the output is consumed by the KUKSA CAN Provider and Databroker.
- Signal sources: DBC/C/YAML artifacts from the vehicle network and ECU development.

## Vehicle API Relevant

Yes, exists: COVESA VSS. In addition, signals that cannot be mapped are emitted as structured proposals for new VSS signals, which can be submitted to COVESA as VSS extension requests.

## Author/Company

akshay.narla AT ias DOT uni-stuttgart DOT de / Institute of Industrial Automation and Software Engineering (IAS), University of Stuttgart

## Priority

Medium

## Contribution supported by RDI projects

Yes. Chips Joint Undertaking, Framework Partnership Agreement No 101139789 (HAL4SDV) and BMFTR (under Grant Number: 16MEE0472). Contributed to the Eclipse KUKSA project (kuksa-incubation).

## Availability of Source Code

Yes / Apache-2.0

## Availability of API

Yes / Apache-2.0. Python library (`vss_mapper`) and Streamlit UI.

## Type of API

Library/Framework API

## Potential obstacles

- Mapping quality depends on signal descriptions in the input; DBC files without comments map worse than annotated ones.
- The LLM judge requires a hosted or local model; results are not bit-identical across model versions.
- Evaluated on open DBC data and synthetic inputs so far; no OEM production DBC has been published for evaluation.
- Incubation status in Eclipse KUKSA; API may still change.

## Maturity Badges

## State (+ date of last change)

First public release available (Eclipse KUKSA incubation, v0.1.0). Last commit May 2026.

## System Context

- Off-board / developer workstation
- Python 3.12, PyTorch, Streamlit
- Output consumed by Eclipse KUKSA (Linux, container)

## Compliant to

Eclipse KUKSA, COVESA VSS, Eclipse Foundation development process (SPDX, DCO sign-off).

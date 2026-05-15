# AGENTS.md

This file provides context about this Obsidian vault for AI agents.

## Vault Overview

This vault serves as a technical documentation and knowledge repository for LightRAG, an open-source knowledge graph system built with LangChain. It combines structured project deployment guides, API server documentation, Docker and Kubernetes deployment configurations, and evaluation methodology with personal analysis notes on policy analysis workflows and VS Code tool usage.

The vault uniquely blends technical infrastructure documentation with conceptual research frameworks, creating both practical deployment resources and analytical methodologies.

**Key characteristics:**
- **Primary focus:** LightRAG knowledge graph system documentation
- **Secondary focus:** Policy analysis methodology and workflow
- **Tertiary focus:** VS Code tool integration
- **Bilingual content:** English and Chinese (README-zh files)
- **Deployment-ready:** Includes k8s-deploy, Docker, and Windows setup scripts

## Organization

- **LightRAG/** (34 files - main project):
  - **docs/** (13 files) - Deployment and feature documentation:
    - AdvancedFeatures, Algorithm, DockerDeployment
    - FrontendBuildGuide, InteractiveSetup
    - LightRAG-API-Server.assets folder
  - **k8s-deploy/** (3 files) - Kubernetes deployment configs
  - **evaluation/** (7 files) - RAG evaluation methodology
  - **lightrag_webui/** (1 file) - Web UI documentation
  - **tests/** - Testing and workspace isolation procedures
  - Root docs: README, README-zh, AGENTS, Security notes

- **Policy Analysis/** (4 files):
  - A 5-Phase Guide to Policy Analysis
  - Extension of the Guide
  - The Mechanics of Analyzing a Policy
  - Policy Analysis overview

- **Using the VS Code Tool/** (1 file):
  - VS Code tool documentation

- **Root-level notes:**
  - My Understanding of the Workflow
  - The GitHub Setup
  - RAG Plan
  - RESEARCH SYNTHESIS ENGINE (REVISED)

## Key Topics

- **LightRAG System:**
  - Knowledge graph API server deployment
  - Docker and Kubernetes configuration
  - Algorithm documentation and advanced features
  - Frontend build instructions
  - Interactive setup procedures
  - Evaluation methodology (RAGA-based)

- **Deployment Infrastructure:**
  - Windows setup scripts
  - Docker deployment guides
  - Kubernetes (k8s) deployment configurations
  - Workspace isolation testing
  - Security considerations

- **Policy Analysis Framework:**
  - 5-Phase analytical methodology
  - Mechanics of policy analysis
  - Extension guidelines

- **Tool Integration:**
  - VS Code tool usage
  - GitHub setup procedures
  - Research synthesis workflows

- **Documentation Bilingual Support:**
  - English and Chinese README files
  - k8s-deploy README-zh

## User Preferences

- **Prefers structured guides:** Evidence of 5-Phase guides and mechanical breakdowns
- **Values bilingual documentation:** Maintains both English and Chinese versions
- **Deployment-focused:** Comprehensive coverage of Docker, k8s, and Windows setups
- **Evaluation-conscious:** Dedicated evaluation folder with RAGA methodology
- **Security-aware:** Separate SECURITY notes and workspace isolation testing
- **Guide-style format:** Prefers numbered phases and mechanical explanations
- **Practical over theoretical:** Focus on deployment, setup, and testing procedures
- **Documentation integrity:** Maintains separate folders for different deployment methods

## Custom Instructions

- **When answering deployment questions:** Reference specific LightRAG/docs/ files (DockerDeployment, k8s-deploy, LightRAG Windows Setup Script)

- **For RAG queries:** Consult LightRAG/lightrag/evaluation/README_EVALUATION_RAGA

- **For policy analysis:** Use Policy Analysis/5-Phase Guide framework

- **When discussing API:** Reference LightRAG-API-Server.assets folder

- **Always mention bilingual availability:** Note Chinese documentation exists where relevant (README-zh)

- **For testing concerns:** Point to LightRAG/tests/README_WORKSPACE_ISOLATION_TESTS

- **For research workflows:** Reference RESEARCH SYNTHESIS ENGINE (REVISED) and RAG Plan

- **For tool usage:** Consult Using the VS Code Tool/VS Code tool

- **When updating documentation:** Preserve existing structure and bilingual format

- **Avoid generic advice:** Ground guidance in specific file paths and documented procedures

- **Maintain workspace isolation awareness:** Reference test procedures when discussing deployment

- **Connect policy and technical:** Use policy analysis framework when discussing knowledge graph design

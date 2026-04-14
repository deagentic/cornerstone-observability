# AGENTS.md — Cornerstone Project
**READ THIS FIRST. Every agent, every session, no exceptions.**

## 1. Project Mandate
* **Core Objective:** Understand, document, build, and evolve this codebase with full traceability.

## 2. Universal Rules
- **ADR-First:** Write an ADR before changing any architecture.
- **Traceability Mandate:** Document the reasoning behind changes.

## 3. Context Routing
| Working in...              | Load before acting                         |
|----------------------------|--------------------------------------------|
| General tasks              | Use standard `common/` skills              |

## 4. Universal Agent Runtime Rules
- **Memory-first:** Before acting, check `output/` and `context/` for prior session state.
- **3-tier model routing:** Trivial tasks (formatting, search) → no LLM; Simple tasks → Haiku; Complex (architecture, review) → Sonnet/Opus.
- **Concurrency mandate:** Run independent sub-tasks in parallel whenever possible.
## 5. GitOps & Commit Policies
- **Gitflow:** Follow Gitflow (main/staging).
- **Semantic Versioning:** Adhere to Semantic Versioning.
- **Commits:** Use Atomic and Conventional Commits.

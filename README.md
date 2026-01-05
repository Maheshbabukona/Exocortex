# Exocortex

Exocortex is a **local-first cognitive engine** designed to help researchers and serious learners **think across documents, notes, and evidence**—not just store them or chat with them.

Where most tools optimize for *text generation*, Exocortex optimizes for *understanding*.

---

## The Core Idea

Human cognition relies on three distinct layers:

- **Long-term knowledge** (what you’ve read and written)
- **Working memory** (what you’re actively thinking with)
- **Reasoned synthesis** (connecting evidence into insight)

Most knowledge tools collapse these into a single surface—documents or chat sessions—causing context loss and shallow reasoning.

**Exocortex models these layers explicitly.**

---

## Core Architecture

┌────────────────────────────┐
│ Cognitive Spaces │
│ (persistent working memory)│
└────────────▲───────────────┘
│
┌────────────┴───────────────┐
│ EXOCORE │
│ (retrieval + reasoning) │
└────────────▲───────────────┘
│
┌────────────┴───────────────┐
│ Knowledge Artifacts │
│ (PDFs, notes, web content) │
└────────────────────────────┘


### Knowledge Artifacts  
Immutable sources of truth: PDFs, research papers, blogs, and notes.  
All are treated equally as knowledge.

### Cognitive Spaces  
Persistent thinking environments where users collect highlighted evidence from multiple artifacts, preserve citations, and structure understanding.  
Context does **not** reset between sessions.

### EXOCORE  
A reasoning engine that retrieves evidence, expands context only when needed, and produces answers **only when citations exist**.  
If evidence is insufficient, it refuses to answer.

This separation is architectural—not cosmetic—and is the core moat.

---

## How Exocortex Competes

### Mental Model Comparison

| Tool Category | Mental Model | Limitation |
|--------------|-------------|------------|
| Notes apps + AI | Documents with AI features | Static storage, weak reasoning |
| Chat-with-PDF tools | Ephemeral chat sessions | No persistent memory |
| NotebookLM | Retrieval over document sets | No durable working memory |
| **Exocortex** | Cognitive system | Built for long-term thinking |

### Capability Comparison

| Capability | Exocortex | NotebookLM | Notes + AI |
|-----------|-----------|------------|------------|
| Notes = documents | ✓ | ✗ | ✗ |
| Persistent working memory | ✓ | ✗ | ✗ |
| Evidence-first reasoning | ✓ | △ | ✗ |
| Multi-source synthesis | ✓ | △ | ✗ |
| Local-first / offline | ✓ | ✗ | ✗ |
| Long-term research architecture | ✓ | ✗ | ✗ |

Exocortex does not compete on *faster answers*.  
It competes on **better thinking over time**.

---

## Metrics That Matter

Exocortex is designed around **cognitive efficiency**, not engagement metrics.

Design targets:
- **Context retention**: resume research without rebuilding mental state
- **Evidence traceability**: every answer links back to source material
- **Local latency**: sub-second semantic search over thousands of chunks
- **Durability**: knowledge remains usable months later, not per session

These metrics guide architectural decisions.

---

## Local-First by Design

Exocortex runs entirely on the user’s machine:
- Local file ingestion
- Local SQLite persistence
- Local embeddings
- Open-source models only

This is a trust and durability decision—not a cost optimization.

---

## Vision

Exocortex is not a productivity app.

It is **personal cognitive infrastructure**—a system where knowledge accumulates, connects, and remains usable over years instead of disappearing between chats.

---


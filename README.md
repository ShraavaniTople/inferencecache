# InferenceCache

**InferenceCache** is a real-time AI inference proxy that adds tamper-proof logging using digital signatures and Merkle trees. It wraps any AI model (like OpenAI) with a secure and cacheable API layer, suitable for applications that require auditable and verifiable inference history.

## Features

- Real-time AI responses using OpenAI GPT models
- Caches results with SHA-256 hash keys
- Digitally signs AI outputs with Ed25519 signatures
- Appends every result to a Merkle tree for audit integrity
- Tamper-proof verification of responses
- Local UI built with FastAPI and Jinja2
- Exportable logs and verifiable proofs (CLI tool coming soon)

## Tech Stack

- Python 3.10+
- FastAPI (web framework)
- DiskCache (inference result caching)
- PyNaCl (Ed25519 signature generation)
- pymerkle (Merkle tree for audit log)
- OpenAI SDK (GPT model integration)
- Jinja2 + HTML/CSS (UI)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ShraavaniTople/inferencecache.git
cd inferencecache

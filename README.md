# InferenceCache

InferenceCache is a real-time AI inference proxy that adds tamper-proof logging using digital signatures and Merkle trees. It wraps any AI model (like OpenAI) with a secure and cacheable API layer, suitable for applications that require auditable and verifiable inference history.

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

```bash
# Step 1: Clone the repository
git clone https://github.com/ShraavaniTople/inferencecache.git
cd inferencecache

# Step 2: Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 3: Install required packages
pip install -r requirements.txt

# If you don't have a requirements.txt file, run this:
pip install fastapi uvicorn openai diskcache pynacl pymerkle python-multipart jinja2 aiofiles

# Step 4: Set your OpenAI API key
export OPENAI_API_KEY="sk-your-api-key-here"

# Step 5: Run the app
uvicorn main:app --reload

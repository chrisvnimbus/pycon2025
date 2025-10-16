# Paleofuturistic Python Project

Development flow as Paleofuturistic Python

## Usage

Legacy: `pip install paleofuturistic_python_project`

Preferred: `uv add paleofuturistic_python_project`

## Developing further

Prerequisite: [uv](https://docs.astral.sh/uv/)

### Setup

- Clone this repository.
- Download additional dependencies: `uv sync`
- Optional: validate the setup with `uv run python -m unittest`

### Workflow

- Develop your feature.
- Format: `uvx ruff format`
- Test:
  - Functionality: `uv run python -m unittest`
  - Build: `uv build`
  - Documentation: `uvx mkdocs build`
- Make a pull request.

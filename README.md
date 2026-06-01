# Pytest Practice Sandbox

A Python test automation sandbox built to practice unit, API and UI testing using Pytest, Requests and Playwright.

## Tech Stack

* Python
* Pytest
* Requests
* Playwright
* Ruff
* GitHub Actions

## Project Structure

```text
tests/
├── api/
├── ui/
└── unit/

tools/
└── accum.py
```

## Setup

```bash
pip install -r requirements.txt
playwright install
```

## Running Tests

Run all tests:

```bash
pytest
```

Run tests by marker:

```bash
pytest -m pokemon_api
pytest -m rest_api
pytest -m ui
```

## CI

Linting, test execution, and coverage run automatically through GitHub Actions on every push and pull request.

## Purpose

This repository is used to practice:

* Python fundamentals
* Unit testing
* API testing
* UI automation
* CI/CD
* Test automation best practices

```
```


# E-commerce Automation Testing Framework

## Overview
Automated UI testing framework for the SauceDemo web application using
Python, Pytest, and Playwright.

## Tech Stack
- Python
- Playwright
- Pytest
- pytest-html

## Test Coverage
- Login and authentication
- Product selection
- Shopping cart
- Checkout workflow
- Negative checkout scenarios

## Test Categories
- Smoke
- Regression
- Negative
- End-to-end

## Setup
1. Create and activate a Python virtual environment.
2. Install dependencies:

   `pip install -r requirements.txt`

3. Install Playwright browsers:

   `playwright install`

## Run Tests

Run the full suite:

`pytest -v`

Run smoke tests:

`pytest -m smoke -v`

Run regression tests:

`pytest -m regression -v`

Run negative tests:

`pytest -m negative -v`

Run end-to-end tests:

`pytest -m e2e -v`

## HTML Report

`pytest --html=reports/report.html --self-contained-html`

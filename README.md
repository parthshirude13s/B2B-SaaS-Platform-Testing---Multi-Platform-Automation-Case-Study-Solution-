# QA Automation Case Study

This repository contains my solution for the WorkFlow Pro QA Automation case study.

## Tools
- Python
- Pytest
- Playwright
- Requests

## Repository Structure

- `tests/ui` - UI automation tests
- `tests/api` - API tests
- `tests/integration` - API + UI integration tests
- `pages` - Page Object Model classes
- `api` - API helper methods
- `fixtures` - Pytest fixtures
- `test-data` - Test data
- `docs` - Testing approach
- `reports` - Test report information

## Setup

1. Install Python 3.10+.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install Playwright browser:

```bash
playwright install
```

4. Set the required environment variables:

```text
BASE_URL=https://qa.workflowpro.com
API_URL=https://qa.workflowpro.com
TEST_USER_EMAIL=your-test-user
TEST_USER_PASSWORD=your-password
COMPANY1_TOKEN=company1-token
COMPANY2_TOKEN=company2-token
```

## Run Tests

Run all tests:

```bash
pytest
```

Run only UI tests:

```bash
pytest tests/ui
```

Run API tests:

```bash
pytest tests/api
```

Run integration tests:

```bash
pytest tests/integration
```

## Testing Approach

The automation uses Playwright for UI testing and Requests for API testing. Test data is generated with unique names where required. Environment-specific values are kept outside the test code.

For CI, smoke tests can run on every pull request and the complete regression suite can run nightly.

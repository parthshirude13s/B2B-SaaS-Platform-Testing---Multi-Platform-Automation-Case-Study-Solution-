# Test Plan

## Objective

Validate the main WorkFlow Pro user flows and make sure the application works correctly across UI, API, mobile browsers and multiple tenants.

## Scope

### Login
- Valid login
- Invalid login
- Dynamic page loading
- 2FA handling where applicable

### Projects
- Create project through API
- Verify project in web UI
- Verify project on mobile browser
- Validate project response

### Tenant Isolation
- Company 1 can access its own project
- Company 2 must not access Company 1 project
- Validate unauthorized access through API

## Browser Coverage

- Chrome
- Firefox
- Safari
- Android browser through BrowserStack
- iOS browser through BrowserStack

## Test Data

Use dedicated automation users and tenant-specific test data. Project names should be unique for every run.

## Execution

Smoke tests can run for every pull request. Full regression can run on a scheduled CI job.

## Risks

- Environment instability
- Test data dependency
- 2FA configuration
- Browser/device availability
- API changes

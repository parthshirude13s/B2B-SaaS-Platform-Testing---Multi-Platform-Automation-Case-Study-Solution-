# Testing Approach

## 1. UI Automation

Playwright is used for browser automation. Stable labels, roles and test IDs should be preferred over CSS selectors that depend on page layout.

The tests use Playwright assertions instead of fixed waits because the application has dynamic loading.

## 2. API Automation

Requests is used for API calls. API-created data makes integration tests faster and reduces unnecessary UI setup.

## 3. Page Object Model

Common page actions are kept inside the `pages` folder. This keeps test cases easier to read and maintain.

## 4. Multi-Tenancy

Every tenant uses its own authentication token and tenant ID. A project created for Company 1 is also requested using Company 2 credentials to verify that cross-tenant access is blocked.

## 5. Browser and Mobile Testing

Chrome can be used for PR smoke testing. Firefox and Safari can be included in regression. Android and iOS testing can run through BrowserStack.

## 6. CI/CD

The smoke suite should run on pull requests. Full regression can run nightly or before a release.

## 7. Flaky Test Handling

Avoid `time.sleep()`. Use Playwright auto-waiting assertions and stable locators. Test accounts and environment configuration should be controlled through environment variables.

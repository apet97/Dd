# Balance API

**Summary:** This endpoint group replaces the deprecated [Balance (Deprecated)](#tag/Balance-(Deprecated)) endpoints.
        Request and response formats are exactly the same.
        Compared to [Balance (Deprecated)](#tag/Balance-(Deprecated)), changes are made only to the base URL and path.
    

- **Base URL (sandbox):** https://developer.clockify.me
- **Authentication:**
  ```
  X-Api-Key: <YOUR_API_KEY>
  Accept: application/json
  Content-Type: application/json
  ```
- **Entity identifiers:**
- Workspace ID
- Resource IDs as described per operation
- **Prerequisites:** The automated runner has not yet provisioned fixtures. Future runs should create DOCS_TEST_* resources as needed.

## Operations
| Method | Path | Operation |
|--------|------|-----------|
| GET | `/v1/workspaces/{workspaceId}/time-off/balance/policy/{policyId}` | [getBalancesForPolicy.md](getBalancesForPolicy.md) |
| PATCH | `/v1/workspaces/{workspaceId}/time-off/balance/policy/{policyId}` | [updateBalance.md](updateBalance.md) |
| GET | `/v1/workspaces/{workspaceId}/time-off/balance/user/{userId}` | [getBalancesForUser.md](getBalancesForUser.md) |

## Common query parameters
- `page`
- `page-size`
- `sort`
- `sort-order`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

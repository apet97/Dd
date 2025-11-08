# Balance (Deprecated) API

**Summary:** This endpoint group is deprecated. It will be available until 1st of July 2025. Use [Balance](#tag/Balance) instead.


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
| GET | `/v1/workspaces/{workspaceId}/balance/policy/{policyId}` | [getPtoBalancesForPolicy.md](getPtoBalancesForPolicy.md) |
| PATCH | `/v1/workspaces/{workspaceId}/balance/policy/{policyId}` | [updateBalancesForUsers.md](updateBalancesForUsers.md) |
| GET | `/v1/workspaces/{workspaceId}/balance/user/{userId}` | [getPtoBalancesForUser.md](getPtoBalancesForUser.md) |

## Common query parameters
- `page`
- `page-size`
- `sort`
- `sort-order`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

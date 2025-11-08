# Time Off (Deprecated) API

**Summary:** This endpoint group is deprecated. It will be available until 1st of July 2025. Use [Time Off](#tag/Time-Off) instead.


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
| POST | `/v1/workspaces/{workspaceId}/policies/{policyId}/requests` | [createPtoTimeOffRequest.md](createPtoTimeOffRequest.md) |
| DELETE | `/v1/workspaces/{workspaceId}/policies/{policyId}/requests/{requestId}` | [deletePtoTimeOffRequest.md](deletePtoTimeOffRequest.md) |
| PATCH | `/v1/workspaces/{workspaceId}/policies/{policyId}/requests/{requestId}` | [changePtoTimeOffRequestStatus.md](changePtoTimeOffRequestStatus.md) |
| POST | `/v1/workspaces/{workspaceId}/policies/{policyId}/users/{userId}/requests` | [createPtoTimeOffRequestForOther.md](createPtoTimeOffRequestForOther.md) |
| POST | `/v1/workspaces/{workspaceId}/requests` | [getPtoTimeOffRequests.md](getPtoTimeOffRequests.md) |

## Common query parameters
- None documented.

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

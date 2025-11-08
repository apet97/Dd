# Time Off API

**Summary:** This endpoint group replaces the deprecated [Time Off (Deprecated)](#tag/Time-Off-(Deprecated)) endpoints.
        Request and response formats are exactly the same.
        Compared to [Time Off (Deprecated)](#tag/Time-Off-(Deprecated)), changes are made only to the base URL and path.
    

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
| POST | `/v1/workspaces/{workspaceId}/time-off/policies/{policyId}/requests` | [createTimeOffRequest.md](createTimeOffRequest.md) |
| DELETE | `/v1/workspaces/{workspaceId}/time-off/policies/{policyId}/requests/{requestId}` | [deleteTimeOffRequest.md](deleteTimeOffRequest.md) |
| PATCH | `/v1/workspaces/{workspaceId}/time-off/policies/{policyId}/requests/{requestId}` | [changeTimeOffRequestStatus.md](changeTimeOffRequestStatus.md) |
| POST | `/v1/workspaces/{workspaceId}/time-off/policies/{policyId}/users/{userId}/requests` | [createTimeOffRequestForOther.md](createTimeOffRequestForOther.md) |
| POST | `/v1/workspaces/{workspaceId}/time-off/requests` | [getTimeOffRequest.md](getTimeOffRequest.md) |

## Common query parameters
- None documented.

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

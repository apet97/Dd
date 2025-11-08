# Policy API

**Summary:** This endpoint group replaces the deprecated [Policy (Deprecated)](#tag/Policy-(Deprecated)) endpoints.
        Request and response formats are exactly the same.
        Compared to [Policy (Deprecated)](#tag/Policy-(Deprecated)), changes are made only to the base URL and path.
    

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
| GET | `/v1/workspaces/{workspaceId}/time-off/policies` | [findPoliciesForWorkspace.md](findPoliciesForWorkspace.md) |
| POST | `/v1/workspaces/{workspaceId}/time-off/policies` | [createPolicy.md](createPolicy.md) |
| DELETE | `/v1/workspaces/{workspaceId}/time-off/policies/{id}` | [deletePolicy.md](deletePolicy.md) |
| GET | `/v1/workspaces/{workspaceId}/time-off/policies/{id}` | [getPolicy.md](getPolicy.md) |
| PATCH | `/v1/workspaces/{workspaceId}/time-off/policies/{id}` | [updatePolicyStatus.md](updatePolicyStatus.md) |
| PUT | `/v1/workspaces/{workspaceId}/time-off/policies/{id}` | [updatePolicy.md](updatePolicy.md) |

## Common query parameters
- `name`
- `page`
- `page-size`
- `status`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

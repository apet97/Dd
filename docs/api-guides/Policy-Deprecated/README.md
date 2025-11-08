# Policy (Deprecated) API

**Summary:** This endpoint group is deprecated. It will be available until 1st of July 2025. Use [Policy](#tag/Policy) instead.


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
| GET | `/v1/workspaces/{workspaceId}/policies` | [findPtoPoliciesForWorkspace.md](findPtoPoliciesForWorkspace.md) |
| POST | `/v1/workspaces/{workspaceId}/policies` | [createPtoPolicy.md](createPtoPolicy.md) |
| DELETE | `/v1/workspaces/{workspaceId}/policies/{id}` | [deletePtoPolicy.md](deletePtoPolicy.md) |
| GET | `/v1/workspaces/{workspaceId}/policies/{id}` | [getPtoPolicy.md](getPtoPolicy.md) |
| PATCH | `/v1/workspaces/{workspaceId}/policies/{id}` | [updatePtoPolicyStatus.md](updatePtoPolicyStatus.md) |
| PUT | `/v1/workspaces/{workspaceId}/policies/{id}` | [updatePtoPolicy.md](updatePtoPolicy.md) |

## Common query parameters
- `name`
- `page`
- `page-size`
- `status`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

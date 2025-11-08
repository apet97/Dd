# Workspace API

**Summary:** 

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
| GET | `/v1/workspaces` | [getWorkspacesOfUser.md](getWorkspacesOfUser.md) |
| POST | `/v1/workspaces` | [createWorkspace.md](createWorkspace.md) |
| GET | `/v1/workspaces/{workspaceId}` | [getWorkspaceOfUser.md](getWorkspaceOfUser.md) |
| PUT | `/v1/workspaces/{workspaceId}/cost-rate` | [setWorkspaceCostRate.md](setWorkspaceCostRate.md) |
| PUT | `/v1/workspaces/{workspaceId}/hourly-rate` | [setWorkspaceHourlyRate.md](setWorkspaceHourlyRate.md) |
| POST | `/v1/workspaces/{workspaceId}/users` | [addUsers.md](addUsers.md) |
| PUT | `/v1/workspaces/{workspaceId}/users/{userId}` | [updateUserStatus.md](updateUserStatus.md) |
| PUT | `/v1/workspaces/{workspaceId}/users/{userId}/cost-rate` | [setCostRateForUser.md](setCostRateForUser.md) |
| PUT | `/v1/workspaces/{workspaceId}/users/{userId}/hourly-rate` | [setHourlyRateForUser.md](setHourlyRateForUser.md) |

## Common query parameters
- `roles`
- `send-email`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

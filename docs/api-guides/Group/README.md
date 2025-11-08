# Group API

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
| GET | `/v1/workspaces/{workspaceId}/user-groups` | [getUserGroups.md](getUserGroups.md) |
| POST | `/v1/workspaces/{workspaceId}/user-groups` | [createUserGroup.md](createUserGroup.md) |
| DELETE | `/v1/workspaces/{workspaceId}/user-groups/{id}` | [deleteUserGroup.md](deleteUserGroup.md) |
| PUT | `/v1/workspaces/{workspaceId}/user-groups/{id}` | [updateUserGroup.md](updateUserGroup.md) |
| POST | `/v1/workspaces/{workspaceId}/user-groups/{userGroupId}/users` | [addUser.md](addUser.md) |
| DELETE | `/v1/workspaces/{workspaceId}/user-groups/{userGroupId}/users/{userId}` | [deleteUser.md](deleteUser.md) |

## Common query parameters
- `includeTeamManagers`
- `name`
- `page`
- `page-size`
- `project-id`
- `sort-column`
- `sort-order`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

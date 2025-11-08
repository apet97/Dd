# User API

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
| POST | `/v1/file/image` | [uploadImage.md](uploadImage.md) |
| GET | `/v1/user` | [getLoggedUser.md](getLoggedUser.md) |
| GET | `/v1/workspaces/{workspaceId}/member-profile/{userId}` | [getMemberProfile.md](getMemberProfile.md) |
| PATCH | `/v1/workspaces/{workspaceId}/member-profile/{userId}` | [updateMemberProfileWithAdditionalData.md](updateMemberProfileWithAdditionalData.md) |
| GET | `/v1/workspaces/{workspaceId}/users` | [getUsersOfWorkspace.md](getUsersOfWorkspace.md) |
| POST | `/v1/workspaces/{workspaceId}/users/info` | [filterUsersOfWorkspace.md](filterUsersOfWorkspace.md) |
| PUT | `/v1/workspaces/{workspaceId}/users/{userId}/custom-field/{customFieldId}/value` | [upsertUserCustomFieldValue.md](upsertUserCustomFieldValue.md) |
| GET | `/v1/workspaces/{workspaceId}/users/{userId}/managers` | [getManagersOfUser.md](getManagersOfUser.md) |
| DELETE | `/v1/workspaces/{workspaceId}/users/{userId}/roles` | [deleteUserRole.md](deleteUserRole.md) |
| POST | `/v1/workspaces/{workspaceId}/users/{userId}/roles` | [createUserRole.md](createUserRole.md) |

## Common query parameters
- `account-statuses`
- `email`
- `include-memberships`
- `include-roles`
- `memberships`
- `name`
- `page`
- `page-size`
- `project-id`
- `sort-column`
- `sort-order`
- `status`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

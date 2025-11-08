# Project API

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
| GET | `/v1/workspaces/{workspaceId}/projects` | [getProjects.md](getProjects.md) |
| POST | `/v1/workspaces/{workspaceId}/projects` | [createNewProject.md](createNewProject.md) |
| DELETE | `/v1/workspaces/{workspaceId}/projects/{projectId}` | [deleteProject.md](deleteProject.md) |
| GET | `/v1/workspaces/{workspaceId}/projects/{projectId}` | [getProject.md](getProject.md) |
| PUT | `/v1/workspaces/{workspaceId}/projects/{projectId}` | [updateProject.md](updateProject.md) |
| PATCH | `/v1/workspaces/{workspaceId}/projects/{projectId}/estimate` | [updateEstimate.md](updateEstimate.md) |
| PATCH | `/v1/workspaces/{workspaceId}/projects/{projectId}/memberships` | [updateMemberships.md](updateMemberships.md) |
| POST | `/v1/workspaces/{workspaceId}/projects/{projectId}/memberships` | [addUsersToProject.md](addUsersToProject.md) |
| PATCH | `/v1/workspaces/{workspaceId}/projects/{projectId}/template` | [updateIsProjectTemplate.md](updateIsProjectTemplate.md) |
| PUT | `/v1/workspaces/{workspaceId}/projects/{projectId}/users/{userId}/cost-rate` | [addUsersCostRate.md](addUsersCostRate.md) |
| PUT | `/v1/workspaces/{workspaceId}/projects/{projectId}/users/{userId}/hourly-rate` | [addUsersHourlyRate.md](addUsersHourlyRate.md) |

## Common query parameters
- `access`
- `archived`
- `billable`
- `client-status`
- `clients`
- `contains-client`
- `contains-group`
- `contains-user`
- `custom-field-entity-type`
- `expense-date`
- `expense-limit`
- `hydrated`
- `is-template`
- `name`
- `page`
- `page-size`
- `sort-column`
- `sort-order`
- `strict-name-search`
- `user-status`
- `userGroups`
- `users`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

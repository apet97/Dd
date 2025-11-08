# Task API

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
| GET | `/v1/workspaces/{workspaceId}/projects/{projectId}/tasks` | [getTasks.md](getTasks.md) |
| POST | `/v1/workspaces/{workspaceId}/projects/{projectId}/tasks` | [createTask.md](createTask.md) |
| PUT | `/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{id}/cost-rate` | [setTaskCostRate.md](setTaskCostRate.md) |
| PUT | `/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{id}/hourly-rate` | [setTaskHourlyRate.md](setTaskHourlyRate.md) |
| DELETE | `/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}` | [deleteTask.md](deleteTask.md) |
| GET | `/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}` | [getTask.md](getTask.md) |
| PUT | `/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}` | [updateTask.md](updateTask.md) |

## Common query parameters
- `contains-assignee`
- `is-active`
- `membership-status`
- `name`
- `page`
- `page-size`
- `sort-column`
- `sort-order`
- `strict-name-search`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

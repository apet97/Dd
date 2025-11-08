# Time entry API

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
| POST | `/v1/workspaces/{workspaceId}/time-entries` | [createTimeEntry.md](createTimeEntry.md) |
| PATCH | `/v1/workspaces/{workspaceId}/time-entries/invoiced` | [updateInvoicedStatus.md](updateInvoicedStatus.md) |
| GET | `/v1/workspaces/{workspaceId}/time-entries/status/in-progress` | [getInProgressTimeEntries.md](getInProgressTimeEntries.md) |
| DELETE | `/v1/workspaces/{workspaceId}/time-entries/{id}` | [deleteTimeEntry.md](deleteTimeEntry.md) |
| GET | `/v1/workspaces/{workspaceId}/time-entries/{id}` | [getTimeEntry.md](getTimeEntry.md) |
| PUT | `/v1/workspaces/{workspaceId}/time-entries/{id}` | [updateTimeEntry.md](updateTimeEntry.md) |
| DELETE | `/v1/workspaces/{workspaceId}/user/{userId}/time-entries` | [deleteMany.md](deleteMany.md) |
| GET | `/v1/workspaces/{workspaceId}/user/{userId}/time-entries` | [getTimeEntries.md](getTimeEntries.md) |
| PATCH | `/v1/workspaces/{workspaceId}/user/{userId}/time-entries` | [stopRunningTimeEntry.md](stopRunningTimeEntry.md) |
| POST | `/v1/workspaces/{workspaceId}/user/{userId}/time-entries` | [createForOthers.md](createForOthers.md) |
| PUT | `/v1/workspaces/{workspaceId}/user/{userId}/time-entries` | [replaceMany.md](replaceMany.md) |
| POST | `/v1/workspaces/{workspaceId}/user/{userId}/time-entries/{id}/duplicate` | [duplicateTimeEntry.md](duplicateTimeEntry.md) |

## Common query parameters
- `description`
- `end`
- `from-entry`
- `get-week-before`
- `hydrated`
- `in-progress`
- `page`
- `page-size`
- `project`
- `project-required`
- `start`
- `tags`
- `task`
- `task-required`
- `time-entry-ids`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

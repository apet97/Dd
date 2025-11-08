# Scheduling API

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
| GET | `/v1/workspaces/{workspaceId}/scheduling/assignments/all` | [getAllAssignments.md](getAllAssignments.md) |
| POST | `/v1/workspaces/{workspaceId}/scheduling/assignments/projects/totals` | [getFilteredProjectTotals.md](getFilteredProjectTotals.md) |
| GET | `/v1/workspaces/{workspaceId}/scheduling/assignments/projects/totals/{projectId}` | [getProjectTotalsForSingleProject.md](getProjectTotalsForSingleProject.md) |
| PUT | `/v1/workspaces/{workspaceId}/scheduling/assignments/publish` | [publishAssignments.md](publishAssignments.md) |
| POST | `/v1/workspaces/{workspaceId}/scheduling/assignments/recurring` | [createRecurring.md](createRecurring.md) |
| DELETE | `/v1/workspaces/{workspaceId}/scheduling/assignments/recurring/{assignmentId}` | [deleteRRecurringAssignment.md](deleteRRecurringAssignment.md) |
| PATCH | `/v1/workspaces/{workspaceId}/scheduling/assignments/recurring/{assignmentId}` | [editRecurring.md](editRecurring.md) |
| PUT | `/v1/workspaces/{workspaceId}/scheduling/assignments/series/{assignmentId}` | [editRecurringPeriod.md](editRecurringPeriod.md) |
| POST | `/v1/workspaces/{workspaceId}/scheduling/assignments/user-filter/totals` | [getUserTotals.md](getUserTotals.md) |
| GET | `/v1/workspaces/{workspaceId}/scheduling/assignments/users/{userId}/totals` | [getUserTotalsForSingleUser.md](getUserTotalsForSingleUser.md) |
| POST | `/v1/workspaces/{workspaceId}/scheduling/assignments/{assignmentId}/copy` | [copyAssignment.md](copyAssignment.md) |

## Common query parameters
- `end`
- `name`
- `page`
- `page-size`
- `seriesUpdateOption`
- `sort-column`
- `sort-order`
- `start`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

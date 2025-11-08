# Scheduling (Deprecated) API

**Summary:** This endpoint group contains deprecated endpoints from the [Scheduling](#tag/Scheduling) endpoint group.

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
| GET | `/v1/workspaces/{workspaceId}/scheduling/assignments/projects/totals` | [getProjectTotals.md](getProjectTotals.md) |

## Common query parameters
- `end`
- `page`
- `page-size`
- `search`
- `start`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

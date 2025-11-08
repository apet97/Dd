# Shared Report API

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
| GET | `/v1/shared-reports/{id}` | [generateSharedReportV1.md](generateSharedReportV1.md) |
| GET | `/v1/workspaces/{workspaceId}/shared-reports` | [getSharedReportsV1.md](getSharedReportsV1.md) |
| POST | `/v1/workspaces/{workspaceId}/shared-reports` | [saveSharedReportV1.md](saveSharedReportV1.md) |
| DELETE | `/v1/workspaces/{workspaceId}/shared-reports/{id}` | [deleteSharedReportV1.md](deleteSharedReportV1.md) |
| PUT | `/v1/workspaces/{workspaceId}/shared-reports/{id}` | [updateSharedReportV1.md](updateSharedReportV1.md) |

## Common query parameters
- `dateRangeEnd`
- `dateRangeStart`
- `exportType`
- `page`
- `pageSize`
- `sharedReportsFilter`
- `sortColumn`
- `sortOrder`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

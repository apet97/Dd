# Custom fields API

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
| GET | `/v1/workspaces/{workspaceId}/custom-fields` | [ofWorkspace.md](ofWorkspace.md) |
| POST | `/v1/workspaces/{workspaceId}/custom-fields` | [create.md](create.md) |
| DELETE | `/v1/workspaces/{workspaceId}/custom-fields/{customFieldId}` | [delete.md](delete.md) |
| PUT | `/v1/workspaces/{workspaceId}/custom-fields/{customFieldId}` | [editCustomField.md](editCustomField.md) |
| GET | `/v1/workspaces/{workspaceId}/projects/{projectId}/custom-fields` | [getCustomFieldsOfProject.md](getCustomFieldsOfProject.md) |
| DELETE | `/v1/workspaces/{workspaceId}/projects/{projectId}/custom-fields/{customFieldId}` | [removeDefaultValueOfProject.md](removeDefaultValueOfProject.md) |
| PATCH | `/v1/workspaces/{workspaceId}/projects/{projectId}/custom-fields/{customFieldId}` | [editProjectCustomFieldDefaultValue.md](editProjectCustomFieldDefaultValue.md) |

## Common query parameters
- `entity-type`
- `name`
- `status`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

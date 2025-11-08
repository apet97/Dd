# Approval API

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
| GET | `/v1/workspaces/{workspaceId}/approval-requests` | [getApprovalRequests.md](getApprovalRequests.md) |
| POST | `/v1/workspaces/{workspaceId}/approval-requests` | [createApprrovalRequest.md](createApprrovalRequest.md) |
| POST | `/v1/workspaces/{workspaceId}/approval-requests/resubmit-entries-for-approval` | [resubmitApprovalRequest.md](resubmitApprovalRequest.md) |
| POST | `/v1/workspaces/{workspaceId}/approval-requests/users/{userId}` | [createApprovalForOther.md](createApprovalForOther.md) |
| POST | `/v1/workspaces/{workspaceId}/approval-requests/users/{userId}/resubmit-entries-for-approval` | [resubmitApprovalRequestForOther.md](resubmitApprovalRequestForOther.md) |
| PATCH | `/v1/workspaces/{workspaceId}/approval-requests/{approvalRequestId}` | [updateApprovalStatus.md](updateApprovalStatus.md) |

## Common query parameters
- `page`
- `page-size`
- `sort-column`
- `sort-order`
- `status`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

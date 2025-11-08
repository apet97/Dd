# Webhooks API

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
| GET | `/v1/workspaces/{workspaceId}/addons/{addonId}/webhooks` | [getAddonWebhooks.md](getAddonWebhooks.md) |
| GET | `/v1/workspaces/{workspaceId}/webhooks` | [getWebhooks.md](getWebhooks.md) |
| POST | `/v1/workspaces/{workspaceId}/webhooks` | [createWebhook.md](createWebhook.md) |
| DELETE | `/v1/workspaces/{workspaceId}/webhooks/{webhookId}` | [deleteWebhook.md](deleteWebhook.md) |
| GET | `/v1/workspaces/{workspaceId}/webhooks/{webhookId}` | [getWebhook.md](getWebhook.md) |
| PUT | `/v1/workspaces/{workspaceId}/webhooks/{webhookId}` | [updateWebhook.md](updateWebhook.md) |
| POST | `/v1/workspaces/{workspaceId}/webhooks/{webhookId}/logs` | [getLogsForWebhook.md](getLogsForWebhook.md) |
| PATCH | `/v1/workspaces/{workspaceId}/webhooks/{webhookId}/token` | [generateNewToken.md](generateNewToken.md) |

## Common query parameters
- `page`
- `size`
- `type`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.

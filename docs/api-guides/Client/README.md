# Client API

## Summary
Manage workspace clients including creation, lookup, updates, and archival via the Clockify sandbox API. The runner exercises each operation with dedicated test records so the examples below reflect live responses.

- **Base URL (sandbox testing):** `https://developer.clockify.me`

## Authentication
All requests use the API key header.

```http
X-Api-Key: <your-api-key>
Accept: application/json
Content-Type: application/json
```

## Entity model quick map
| Field | Description |
|-------|-------------|
| `workspaceId` | Workspace that owns the client. |
| `id` (`clientId`) | Unique identifier for a client within a workspace. |

## Prerequisites
The runner automatically provisions a client named with the `DOCS_TEST_<timestamp>` prefix inside workspace `672f9cf4ad6f45299c3e3de2`, executes the operations below, and deletes the record when finished.

## Operations
| Method | Path | Summary | Example |
|--------|------|---------|---------|
| POST | `/api/v1/workspaces/{workspaceId}/clients` | Add a new client | [createClient.md](createClient.md) |
| GET | `/api/v1/workspaces/{workspaceId}/clients` | List clients in a workspace | [getClients.md](getClients.md) |
| GET | `/api/v1/workspaces/{workspaceId}/clients/{id}` | Retrieve a single client | [getClient.md](getClient.md) |
| PUT | `/api/v1/workspaces/{workspaceId}/clients/{id}` | Update client details | [updateClient.md](updateClient.md) |
| DELETE | `/api/v1/workspaces/{workspaceId}/clients/{id}` | Delete a client | [deleteClient.md](deleteClient.md) |

## Common query parameters
| Parameter | Type | Default | Notes |
|-----------|------|---------|-------|
| `page` | integer | `1` | 1-indexed page number for paginated listings. |
| `page-size` | integer | `50` | Maximum results per page (Clockify allows up to 500). |

## Error reference
| Status | Message | Fix |
|--------|---------|-----|
| 400 | `Client doesn't belong to Workspace` | Ensure the `{id}` exists in the target workspace or recreate the client before retrying. |

## Cleanup policy
`run.py` deletes every `DOCS_TEST_*` client it creates at the end of the run and records the deletion response for audit.

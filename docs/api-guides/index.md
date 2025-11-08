# Clockify API Guides Index

Welcome! These guides were generated from the repository OpenAPI specification to
make it easier to explore the Clockify API surface area. Each section mirrors a
Clockify API tag and contains individual operation walkthroughs.

## How to use these guides
1. Pick the API section relevant to your task from the table below.
2. Review the prerequisites and entity map to understand required IDs.
3. Follow the code samples and adapt them with your data and API key.
4. Execute against the sandbox first to verify the flow, then promote to production.

## Environments
| Purpose | Base URL |
|---------|----------|
| Sandbox | https://developer.clockify.me |
| Prod | https://api.clockify.me |

## Authentication quickstart
Add the `X-Api-Key` header with your Clockify API key on every request. For JSON
payloads, include `Content-Type: application/json`.

## Sections
- [Approval](./Approval/README.md)
- [Balance](./Balance/README.md)
- [Balance (Deprecated)](./Balance-Deprecated/README.md)
- [Client](./Client/README.md)
- [Custom fields](./Custom-fields/README.md)
- [Entity changes (Experimental)](./Entity-changes-Experimental/README.md)
- [Expense](./Expense/README.md)
- [Expense Report](./Expense-Report/README.md)
- [Group](./Group/README.md)
- [Holiday](./Holiday/README.md)
- [Invoice](./Invoice/README.md)
- [Policy](./Policy/README.md)
- [Policy (Deprecated)](./Policy-Deprecated/README.md)
- [Project](./Project/README.md)
- [Scheduling](./Scheduling/README.md)
- [Scheduling (Deprecated)](./Scheduling-Deprecated/README.md)
- [Shared Report](./Shared-Report/README.md)
- [Tag](./Tag/README.md)
- [Task](./Task/README.md)
- [Team Report](./Team-Report/README.md)
- [Time Entry Report](./Time-Entry-Report/README.md)
- [Time Off](./Time-Off/README.md)
- [Time Off (Deprecated)](./Time-Off-Deprecated/README.md)
- [Time entry](./Time-entry/README.md)
- [User](./User/README.md)
- [Webhooks](./Webhooks/README.md)
- [Workspace](./Workspace/README.md)
- [Workspace (Deprecated)](./Workspace-Deprecated/README.md)

Generated from OpenAPI spec in repo on 2025-11-08 15:32:02 UTC.

## Known gaps
- Automated sandbox runs currently cover the **Client** tag only; all other sections are generated from the schema and require live execution work.

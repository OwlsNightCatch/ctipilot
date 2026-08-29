---
name: permission-rules-edit-covers-write
description: Claude Code permission rules — Write(path) allow rules are dead; Edit(path) covers all file-editing tools
metadata: 
  node_type: memory
  type: reference
  originSessionId: b6284326-dd92-4265-9208-2bb89b1ad9fe
  modified: 2026-08-29T09:45:03.642Z
---

Claude Code's file-permission checks match only `Edit(path)` rules; a `Write(path)` allow rule is never consulted and triggers a startup warning. `Edit(path)` covers ALL file-editing tools (Edit, Write, NotebookEdit). Fixed 2026-08-29: every `Write(...)` rule was removed from `.claude/settings.json` (the `Edit(...)` twins already existed). Never re-add `Write(...)` permission rules — use `Edit(...)`.

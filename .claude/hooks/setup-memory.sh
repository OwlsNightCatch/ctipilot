#!/usr/bin/env bash
# .claude/hooks/setup-memory.sh — SessionStart hook
#
# Redirect Claude Code's built-in auto-memory directory to the repo's
# `.claude/memory/` so every memory write lands in a version-controlled
# location. Result: memory persists across cloud routine fires (fresh
# container each run), across local Claude Code sessions on different
# machines, and across worktrees of the same repo.
#
# Mechanism: symlink ~/.claude/projects/<project-hash>/memory  →  $REPO/.claude/memory
#
# Project-hash algorithm (Claude Code internal): replace "/", "_", and "." in
# the absolute path of the working directory with "-". The leading "/" of the
# absolute path becomes a leading "-".
#
# Best-effort: failures are logged to stderr but never block the session.
# If the hash algorithm changes in a future Claude Code release, the
# symlink target won't match what Claude Code expects, and the auto-memory
# feature will fall back to its default per-project directory. The repo's
# `.claude/memory/` still works as a manual memory directory in that case
# (CLAUDE.md instructs Claude to read/write it directly as a fallback).

set -e

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
    echo "[setup-memory] not in a git repo, skipping" >&2
    exit 0
}

REPO_MEM="$REPO_ROOT/.claude/memory"
mkdir -p "$REPO_MEM"

# Compute the project hash the same way Claude Code does.
# Use $PWD (Claude Code derives the hash from the session's working dir),
# not the repo root — worktrees produce different hashes than the main repo.
PROJECT_HASH=$(printf '%s' "$PWD" | tr '/_.' '---')
AUTO_MEM_PARENT="$HOME/.claude/projects/$PROJECT_HASH"
AUTO_MEM_DIR="$AUTO_MEM_PARENT/memory"

mkdir -p "$AUTO_MEM_PARENT"

# Already symlinked to the right place — done.
if [ -L "$AUTO_MEM_DIR" ]; then
    if [ "$(readlink "$AUTO_MEM_DIR")" = "$REPO_MEM" ]; then
        exit 0
    fi
    # Wrong target — replace.
    rm "$AUTO_MEM_DIR"
elif [ -d "$AUTO_MEM_DIR" ]; then
    # A real directory exists from a prior local session before the hook
    # was installed. Migrate any files that aren't already in the repo,
    # then move the directory aside as a timestamped backup.
    cp -an "$AUTO_MEM_DIR/." "$REPO_MEM/" 2>/dev/null || true
    BACKUP="${AUTO_MEM_DIR}.local-backup-$(date +%s)"
    mv "$AUTO_MEM_DIR" "$BACKUP"
    echo "[setup-memory] migrated existing local memory into repo; backup at $BACKUP" >&2
fi

ln -s "$REPO_MEM" "$AUTO_MEM_DIR"
echo "[setup-memory] symlinked $AUTO_MEM_DIR → $REPO_MEM" >&2

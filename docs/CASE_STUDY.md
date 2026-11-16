# DeadCity — Engineering Case Study

## Context

DeadCity is a Discord-integrated operational system for a DayZ / STALKER roleplay community. Player support, moderation, application review and server monitoring create a recurring stream of work for staff.

The public repository is a **documentation-only portfolio case study**. It does not contain complete production code or deployment instructions.

## Challenge

Several workflows need more than a Discord message:

1. Player requests must move through identifiable stages and responsible staff.
2. Moderation signals need context from logs and configurable matching rules.
3. Actions should remain traceable after tickets close.
4. External server data can fail or become stale.
5. Data should persist across interactions and service restarts.

## Implementation approach

### Support and staff workflows

Discord forms collect structured request data. Buttons and select menus drive approval, assignment and closure actions. Selected ticket workflows produce HTML transcripts for later review.

**Backend concerns:** authorization, persisted workflow state, interaction lifecycle and transcript generation.

### Moderation signals

Activity logs are parsed into events. Configured rules and windows help surface potentially unusual behavior, such as forbidden-item spawning or bursts of item creation. Staff receive alerts that link back to their source context.

**Backend concerns:** parsing, thresholds, deduplication and auditability. Detector algorithms and production rules remain private.

### Server data

A Python client retrieves server information through external APIs, normalizes snapshots and supports historical reporting. The reviewed client includes retry handling and a last-known-successful-data fallback.

**Backend concerns:** timeout/retry behavior, stale data, scheduled polling and persistence.

## Architecture sketch

```text
Discord commands, modals, buttons and events
                 |
            Discord Cogs
                 |
       Domain / service modules
          /              \
   Persistent state    HTTP clients / logs
          \              /
        Staff results and alerts
```

The reviewed archive uses asynchronous Python and Discord Cogs. The player-activity subsystem separates log parsing, detection, storage, models and case processing into dedicated service modules.

## Evidence and validation

A source archive supplied for review on **16 November 2026** included 48 Python files (approximately 27,654 Python lines including tests). Its player-activity investigation test suite contained **27 tests; all 27 passed locally**.

The source archive and screenshots show functional examples of ticket forms, moderation alerts, approval controls and archive exports. No independent availability or time-savings metrics were supplied, so none are claimed.

## Constraints and lessons

- **Not every module in the snapshot is registered at startup.** Some may be optional, from a separate deployment or work in progress. Feature presence in a repository does not prove it was enabled in the reviewed runtime.
- **Several modules are large.** An incremental refactor toward smaller domain services and views would improve testability.
- **Test coverage is uneven.** The player-activity subsystem is tested, but comparable coverage for ticket lifecycle and access control was not present in the supplied archive.
- **Dependencies and startup behavior** could benefit from a more reproducible setup, explicit dependency declarations and structured diagnostic logs.

## Publication boundary

Real identifiers, payment information, passwords, API keys, configuration, server logs and sensitive detection rules must never enter this portfolio repository. Any commercial screenshots must be redacted and approved for publication.

## What's next

A separate **runnable synthetic demo**—with fabricated data, testable workflow rules, SQLite, automated tests and CI—would let reviewers assess implementation quality without exposing proprietary code.

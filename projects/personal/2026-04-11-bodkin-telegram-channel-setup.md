# Bodkin Telegram Channel Setup

**Date:** 2026-04-11
**Source:** Claude conversation
**Folder:** projects
**Status:** Complete ✓

## Summary

Successfully set up Telegram as a mobile interface for Bodkin, the Claude Code agent running on the Beelink (Ubuntu Server 24.04). Bodkin is now reachable from iPhone via Telegram — messages sent to the bot are received by Bodkin and responses come back through the app.

## Background

Bodkin lives at `~/agent/` on the Beelink and is launched with `cd ~/agent && claude`. The goal was to be able to send Bodkin tasks and get responses via Telegram from an iPhone, without needing to be at a computer.

## What we tried and what happened

### Telegram bot setup (phone)
- Created a Telegram bot via @BotFather — display name "Bodkin", username ends in `bot`
- Retrieved Telegram user ID via @userinfobot: `8659243048`
- Tapped Start in the bot chat to initialize the conversation thread

### Plugin installation (Beelink via SSH)
- Installed `telegram@claude-plugins-official` inside Claude Code
- Configured bot token and user ID via `/telegram:configure`
- Set access policy to allowlist with user ID `8659243048`
- Completed pairing flow: switched to pairing mode, received 6-char code in Telegram, ran `/telegram:access pair <code>`, locked back to allowlist

### Systemd service for persistent Bodkin session
- Created `/etc/systemd/system/bodkin.service` to keep Bodkin running in a tmux session across reboots
- Resolved several issues along the way:
  - `claude` binary is at `/usr/bin/claude` (not `/usr/local/bin/claude`)
  - Used `sudo tee` instead of nano to write service files (avoids pager/editor issues)
  - Used `ExecStartPre=-/usr/bin/tmux kill-session -t bodkin` with the `-` prefix to handle missing session gracefully
  - Used a wrapper script `~/agent/start-bodkin.sh` with `Type=forking` to handle tmux detachment correctly
- Service is enabled and starts Bodkin in a persistent tmux session named `bodkin`

### Why messages weren't coming through initially
- The Telegram plugin was installed and connected, bot was receiving messages (Telegram showed "Typing..." indicator), but messages never appeared in Claude Code
- Root cause: Claude Code must be launched with `--channels plugin:telegram@claude-plugins-official` flag to activate inbound channel delivery
- When that flag was used, got: `--channels blocked by org policy`

### The org policy blocker
- Channels is disabled by default on Anthropic Team and Enterprise plans
- The `channelsEnabled` setting must be toggled on by an org admin
- Emailed Brian on 2026-04-11 asking him to enable it via: claude.ai → Admin Settings → Claude Code → Channels
- After Brian enabled the setting, relaunching Claude Code with the `--channels` flag worked immediately

## Working launch command

```bash
cd ~/agent && claude --channels plugin:telegram@claude-plugins-official
```

## Remaining to-do

- Update the systemd service and `start-bodkin.sh` to include the `--channels` flag so Bodkin launches correctly after a reboot (can be done by asking Bodkin directly via Telegram)
- Ask Bodkin to update his `CLAUDE.md` to note that Telegram is his mobile interface

## Key file locations on the Beelink

| File | Path |
|------|------|
| Bodkin system prompt | `~/agent/CLAUDE.md` |
| Systemd service | `/etc/systemd/system/bodkin.service` |
| Bodkin launch script | `~/agent/start-bodkin.sh` |
| Telegram config | `~/.claude/channels/telegram/.env` |
| Telegram access control | `~/.claude/channels/telegram/access.json` |
| Telegram plugin cache | `~/.claude/plugins/cache/claude-plugins-official/telegram/` |

## Reference

- Official Channels docs: https://code.claude.com/docs/en/channels
- Admin setting location: claude.ai → Admin Settings → Claude Code → Channels → toggle `channelsEnabled` to on

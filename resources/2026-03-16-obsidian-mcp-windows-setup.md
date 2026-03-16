# Obsidian MCP setup on Windows

**Date:** 2026-03-16
**Source:** Claude conversation
**Folder:** resources

## Summary

This guide documents how to connect Claude Desktop to an Obsidian vault on Windows via a local MCP server, using the `@bitbonsai/mcpvault` package. Windows requires several workarounds compared to Mac due to how Claude Desktop invokes commands through `cmd.exe` and its handling of paths with spaces.

---

## Prerequisites

- Claude Desktop installed
- Obsidian installed, with your vault synced and visible
- Node.js installed from nodejs.org (LTS version)

Verify Node.js is installed by running these in Command Prompt:

```
node -v
npm -v
```

Both should return version numbers.

---

## Critical Windows constraint: no spaces in paths

Claude Desktop on Windows passes MCP commands through `cmd.exe` without quoting arguments. This means any spaces in file paths will cause the command to fail. You must ensure:

1. Your vault is stored at a path with no spaces (e.g. `C:\Obsidian\Still point` is fine — the space in the vault name is in an argument, not the command itself)
2. The command path has no spaces — solved by calling `node.exe` directly (see below)

---

## Step 1: Install the mcpvault package

Run this in Command Prompt:

```
npm install -g @bitbonsai/mcpvault
```

---

## Step 2: Move your vault to a space-free path

In Obsidian, go to Settings → Sync and move the vault to a location with no spaces in the folder path. A good default:

```
C:\Obsidian\Your Vault Name
```

The vault name itself can have spaces — only the folder path leading to it matters.

---

## Step 3: Find the mcpvault server.js path

Run this in Command Prompt to confirm the package installed correctly and find the script path:

```
dir "%APPDATA%\npm\node_modules\@bitbonsai\mcpvault\dist\server.js"
```

It should show a file. Note the short (8.3) path to your AppData folder by running:

```
for %I in ("%APPDATA%") do echo %~sI
```

This gives you a path like `C:\Users\JOEGAR~1\AppData\Roaming` with no spaces — you'll need this for the config.

---

## Step 4: Edit the Claude Desktop config

Navigate to the config file by pasting this into File Explorer's address bar:

```
%APPDATA%\Claude
```

Open `claude_desktop_config.json` in VS Code or any text editor. Add or update the `mcpServers` block as shown below.

**The working config pattern:**

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": [
        "C:\\Users\\JOEGAR~1\\AppData\\Roaming\\npm\\node_modules\\@bitbonsai\\mcpvault\\dist\\server.js",
        "C:\\Obsidian\\Your Vault Name"
      ]
    }
  }
}
```

Replace `JOEGAR~1` with your own short username (from the command in Step 3) and `Your Vault Name` with your actual vault folder name.

**Why this works:** Calling `node.exe` directly bypasses `cmd.exe` and all batch file wrapper issues. The short 8.3 path eliminates spaces from the command and script path arguments.

---

## Step 5: Relaunch Claude Desktop

Fully quit Claude Desktop — right-click the system tray icon and choose Exit (just closing the window is not enough). Then relaunch.

Go to Settings → Developer. The obsidian server should show a green "running" badge.

Open a fresh conversation to confirm the tools are available.

---

## Verification

Once connected, Claude Desktop can:
- Read any note in the vault by path
- Write and create notes directly
- List directory contents
- Search notes by name
- Move and rename notes

---

## Troubleshooting

**"not recognized as an internal or external command"** — A space in the command path is being split by cmd.exe. Make sure you are calling `node.exe` directly, not npx or a batch file.

**"Cannot find module"** — The path to `server.js` is wrong. Re-run the `dir` command in Step 3 to confirm the exact path.

**Timeout / MCP error -32001** — The server starts but doesn't respond to the handshake. This usually means a batch file wrapper is breaking the stdin/stdout pipe. Use the `node.exe` direct approach above.

**Green badge but no tools in conversation** — Start a fresh conversation after relaunch. Tools are not available in conversations that were open before the server connected.

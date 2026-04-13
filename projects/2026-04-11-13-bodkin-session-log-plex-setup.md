# Bodkin session log — Plex media server setup

**Dates:** April 11–13, 2026  
**Agent:** Bodkin (Claude Code on Beelink EQi12)  
**Source:** Reconstructed from Claude chat session — Bodkin lacked full context due to session gaps  
**Status:** In progress

---

## Summary

A major multi-day session covering: network topology change (TP-Link removed, Xfinity gateway now sole router), external drive backup and reformat, Plex media server planning and spec, Soulseek/slskd music setup planning, Bodkin Telegram reliability troubleshooting, and music library consolidation.

---

## Network topology change

### What happened
An attempt was made to enable bridge mode on the Xfinity modem/router combo to allow port forwarding for Plex remote access. The attempt failed and broke the home network. Recovery required:
- Resetting to Xfinity gateway as sole router
- Changing WiFi network name and password
- Reconnecting all devices (phones, TV, thermostats) to new network
- Beelink lost connectivity during the outage (wired Ethernet, unaffected by WiFi change, but needed power cycle to re-register with new gateway)

### Current network state
- **Router:** Xfinity gateway (combo modem/router) — replaces TP-Link Archer AX55 which has been removed from the setup
- **Beelink IP:** `10.0.0.195` (same as before — Xfinity gateway remembered the DHCP lease)
- **IP reservation:** Set in Xfinity gateway connected devices page for Beelink MAC `78:55:36:08:a1:77`
- **Gateway admin:** `http://10.0.0.1`
- **CGNAT confirmed:** Xfinity is running NAT in front of the gateway — WAN IP shows `10.x.x.x` (private), not a public IP. Port forwarding for Plex remote access not possible without buying own modem.

### Plex remote access plan
Given CGNAT, switched plan to use **Plex Relay** (built-in, no config needed) for dad's remote access. Tradeoff: free tier caps remote streams at 720p. Direct port forwarding fallback requires either:
- Motorola MB8611 modem (~$150) to get true public IP
- Cloudflare Tunnel (free, more complex)

### Bodkin-specific impact
- Beelink came back online after power cycle
- obsidian-sync service confirmed running cleanly on boot (`Active: active (running)` since boot)
- SSH alias `beelink` still works — IP unchanged
- Telegram plugin dropped during the outage period; required manual relaunch

---

## External drive setup

### Drive specs
- **Make/model:** Seagate Backup Plus Portable 5TB (model SRD0VN3, manufactured 2020)
- **Interface:** Micro-USB 3.0 (USB-C cable works via adapter)
- **Previous filesystem:** exFAT
- **New filesystem:** ext4 (reformatted April 12, 2026)
- **Label:** `media`
- **UUID:** `c3aaf509-db68-4ae5-a8bd-624e7e83d711`
- **Mount point:** `/mnt/media`
- **fstab entry:** `UUID=c3aaf509-db68-4ae5-a8bd-624e7e83d711  /mnt/media  ext4  defaults,nofail,x-systemd.device-timeout=30  0  2`
- **udev rule:** `/etc/udev/rules.d/99-usb-media.rules` — auto-remounts on USB reconnect

### Why reformatted
exFAT doesn't support Linux file permissions, which causes Plex permission issues. ext4 is the correct filesystem for always-on Linux media server use.

### Backup before reformat
Drive had ~1.1TB of irreplaceable data. Backed up to two machines before reformatting:
- **Movies folder (441GB)** → MacBook Pro Desktop (`/Users/Joe/Desktop/5TB External Hard Drive/Movies`)
- **Everything else (289GB)** → Mac Mini Desktop (`/Users/joe_mac_mini/Desktop/5TB External Hard Drive Backup/`)

Both transfers used `rsync -av --progress`. Mac Mini transfer completed with rsync error code 23 (macOS system files couldn't be transferred — expected, non-critical).

### Folder structure created
```
/mnt/media/
  movies/
  music/
  tv/
  other/
  downloads/
    torrents/
    soulseek/
  lost+found/  (ext4 system folder, ignore)
```

### Data restored
- **Movies:** rsync'd from MacBook → `/mnt/media/movies/` (441GB, completed cleanly)
- **Other/misc:** rsync'd from Mac Mini → `/mnt/media/other/` (271GB, completed with code 23)
- **Music:** consolidation in progress (see Music section below)

---

## Music library consolidation

### Current state
Music exists in two places that need to be merged into `/mnt/media/music/`:
1. `/mnt/media/other/Music/music/` — Soulseek downloads from Mac Mini backup (three dated folders)
2. `~/Music` on MacBook Pro — main iTunes/Music app library (~16GB)

### Actions taken (April 13, 2026)
Bodkin ran the following consolidation:
- rsync from MacBook Pro (`Joe@10.0.0.160:/Users/Joe/Music/`) → `/mnt/media/music/` (running in background, ~16GB over local network)
- Moved Soulseek download folders from `/mnt/media/other/Music/music/` → `/mnt/media/music/` (same-filesystem move, near-instant)
- Added TODO item: **beets auto-tagging pass** — auto-tag and organize `/mnt/media/music/` using MusicBrainz after consolidation completes

### Plex music format notes
- Plex reads embedded tags (artist, album, track number, title) primarily
- Recommended folder structure: `Artist/Album (Year)/01 - Track Title.flac`
- Plex Amp plays FLAC natively — no transcoding needed locally or remotely
- Remote FLAC streaming is bandwidth-heavy (lossless 24-bit albums can be 1GB+)

---

## Plex media server — spec finalized

Full spec written and saved to Obsidian vault at `Resources/plex-beelink-spec.md`. Key decisions:

- **Media server:** Plex (not Jellyfin — Joe already in Plex ecosystem with friends)
- **Torrent client:** qBittorrent-nox (headless, web UI at port 8080)
- **Music download client:** slskd (headless Soulseek, web UI at port 5030)
- **Remote access:** Plex Relay (CGNAT workaround — no port forwarding available)
- **Drive:** 5TB Seagate external, now ext4, mounted at `/mnt/media`
- **Plex port:** 32400

### Phases completed
- Phase 1 (backup): ✅ done
- Phase 2 (static IP): ✅ done (Xfinity gateway reservation)
- Phase 3 (reformat): ✅ done
- Phase 4 (mount): ✅ done
- Phase 5 (restore data): ✅ movies and other done, music in progress
- Phase 6 (install Plex): pending
- Phase 7 (qBittorrent): pending
- Phase 8 (remote access): pending
- Phase 9 (.NET runtime): pending
- Phase 10 (slskd): pending

---

## Bodkin Telegram reliability issues

### Problem
Telegram plugin drops frequently, requiring manual relaunch. Root causes identified:
- Claude Code session exits (either manually via `/exit` or due to inactivity)
- Viewing the tmux session directly in VS Code and interrupting it
- tmux session being killed during troubleshooting

### Current working launch command
```bash
cd ~/agent && claude --channels plugin:telegram@claude-plugins-official
```

### Proper tmux launch (keeps running when VS Code closes)
```bash
tmux kill-session -t bodkin 2>/dev/null; tmux new-session -d -s bodkin 'cd /home/joe/agent && claude --channels plugin:telegram@claude-plugins-official'
```

### Pending fixes
1. **Short term:** `restart-bodkin.sh` script in `~/agent/tools/` — one command to kill and relaunch
2. **Long term:** systemd service to auto-restart Bodkin if Claude Code exits — similar to `obsidian-sync.service`. This is the real fix.

### tmux-continuum/resurrect
Task was sent via Telegram to install tmux-continuum and tmux-resurrect via TPM. Not completed — session was lost before execution. Needs to be redone. Note: these plugins help with tmux session persistence across reboots but do NOT fix the Telegram plugin drop issue (that requires systemd).

---

## SSH key for GitHub

Bodkin previously couldn't push to GitHub because no SSH key was registered. On April 13, 2026:
- Generated SSH key: `ssh-keygen -t ed25519 -C "bodkin@beelink" -f ~/.ssh/id_ed25519 -N ""`
- Public key saved at `~/.ssh/id_ed25519.pub`
- Joe added key to GitHub (Settings → SSH and GPG keys → New SSH key → title: "Beelink")
- GitHub push capability now available to Bodkin

---

## Hardware notes

### External drive reliability concern
The Seagate Backup Plus is 6 years old (manufactured 2020) and bus-powered. Identified as the weakest link in the Plex setup. Long-term plan:
- **Preferred upgrade:** Crucial P3 4TB NVMe M.2 2280 (PCIe Gen3) — for Beelink's second M.2 slot
- **Current pricing:** 4TB NVMe SSDs are ~$250+ due to NAND price spike (as of April 2026). Previously expected ~$120, now unrealistic.
- **Decision:** Proceed with external drive for now, buy internal M.2 when prices normalize
- **Search term for Amazon:** `4TB NVMe M.2 2280` — stick to Crucial, WD, Samsung, Silicon Power

### Mac Mini (late brother's)
Used as temporary backup storage during drive reformat. Ubuntu 24.04 LTS install previously mentioned but this machine is macOS. Has ~900GB free. Used successfully for rsync backup.

---

## Mesh activity

- Bodkin received and accepted a session proposal from `moose` (Matt's Beelink) on April 13
- Shared Plex server plan summary with moose over mesh
- Shared Telegram channel setup story with moose
- Mesh peers: moose, dusty, stevens

---

## Pending items from this session

- [ ] Install Plex Media Server (Phase 6)
- [ ] Install qBittorrent-nox (Phase 7)
- [ ] Set up Plex relay and share library with dad (Phase 8)
- [ ] Install .NET runtime (Phase 9)
- [ ] Install and configure slskd (Phase 10)
- [ ] Verify music consolidation completed (rsync from MacBook + Soulseek moves)
- [ ] Run beets auto-tagging pass on `/mnt/media/music/`
- [ ] Set up systemd auto-restart for Bodkin (long-term Telegram fix)
- [ ] Write `restart-bodkin.sh` script in `~/agent/tools/`
- [ ] Install tmux-continuum and tmux-resurrect via TPM
- [ ] Update `start-bodkin.sh` to include `--channels` flag
- [ ] Confirm BIOS "Restore on AC Power Loss" set to Power On
- [ ] Consider Crucial P3 4TB M.2 purchase when prices drop

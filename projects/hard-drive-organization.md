# Hard drive organization

**Status:** Phase 1 complete — initial audit done
**Started:** 2026-03-28
**Machine:** MacBook, macOS, `/Users/Joe`
**Goal:** Full hard drive organization — better folder structure, archival cleanup, deletion of dead weight

## Background

Initiated March 28, 2026. Audit conducted using Desktop Commander MCP (read-only access to full filesystem). The three primary problem areas are Downloads, Desktop, and Documents, with Downloads being the most severe. Goal is phased: assess → quick wins → reorganize → archive.

Claude has read access to the full filesystem via Desktop Commander and can assist with analysis, generating shell scripts for bulk operations, and planning each phase. All actual file moves and deletions require Joe's approval.

## Audit findings (2026-03-28)

### Downloads — primary problem

1,322 files and 68 directories, almost entirely flat and unsorted. Years of accumulation with no routing system.

File type breakdown:

| Type | Count | Notes |
|------|-------|-------|
| .pdf | 254 | Tax returns, contracts, receipts, academic papers, misc |
| .jpg | 215 | Photos mixed with everything else |
| .docx | 148 | Work and personal documents |
| .heic | 123 | iPhone photos |
| .torrent | 83 | Almost certainly deletable |
| .epub | 82 | Books — may overlap with Calibre Library |
| .png | 68 | Screenshots and images |
| .zip | 48 | Archives — likely extractable or deletable |
| .mp3/.m4a/.wav | 78 | Music and audio |
| .gpx | 17 | Cycling routes |
| .fit | 13 | Fitness tracking data (Wahoo/Garmin) |
| .asd | 13 | Ableton autosave files (not actual projects) |
| .xlsx/.pptx | 23 | Work documents |
| .dmg | 7 | Old disk images / installers |
| .doc | 20 | Older Word documents |
| .mp4 | 19 | Video files |

Notable subdirectories: software installers (Ableton Live 10, Photoshop 2021, Office 2021 for Mac), Roland USB drivers (multiple duplicates), game ROMs (Halo 1&2, JSRF, RCT2), Digitakt OS files, music samples and production projects, personal photo collections, code build artifacts (build/, dist/, tmp/), cycling data.

### Desktop — has bones, needs discipline

Existing folder structure is sound: Apps & Games, Archives & Other, Audio & Music, Creative Projects, Documents, Images, Presentations, Spreadsheets, To import to Obsidian, Video, Web Saves, eBooks. Problem is loose screenshots and stray files landing here constantly. Also contains: $RECYCLE.BIN (Windows artifact), `Relocated Items` (macOS migration artifact), `Mart photos and videos and memories/` (should be archived properly), and several LWScreenShot / Screenshot files from March 2026.

### Documents — leaner than expected

Folders: Adobe, Beat Making on the MPC1000, City Arts, Digital Editions, Electronic Arts, Ideaverse Lite 1.5, Library, Manuals, Max, Max 8, Microsoft User Data, Native Instruments, RDC Connections, Rockstar Games, UBS, Virtual Machines.localized, Zoom.

Stray files: `Matt, Steve, Dad & Mom group text.pdf`, `Signed Lease University Manor.pdf`, `TaxReturn.pdf`, `network map.reason`.

### Home directory — other notable items

- `Dropbox/` and `Creative Cloud Files/` — two cloud sync folders; overlap not yet assessed
- `Calibre Library/` — ebook management; may overlap with EPUBs in Downloads
- `Soulseek Downloads/` — separate music download folder at home root
- `Soulseek Chat Logs/` — at home root
- `Temp-3 Project/` — purpose unknown; sitting at home root
- `Parallels/` — VM software; likely large disk consumer if still present
- `Music/`, `Movies/`, `Pictures/` — standard macOS folders; contents not yet audited

## Phase plan

### Phase 1: Audit
- [x] Initial directory listing of home, Desktop, Downloads, Documents
- [x] File type inventory of Downloads
- [x] Identification of major problem areas and stray items
- [ ] Disk usage analysis — identify space hogs (Parallels VMs, large media, etc.)
- [ ] Deeper audit of Music/, Movies/, Pictures/, Dropbox/

### Phase 2: Quick wins — delete without review

High-confidence deletions, no review needed:

- All 83 `.torrent` files in Downloads
- All 13 `.asd` Ableton autosave files (crash recovery only, not actual projects)
- All 7 `.dmg` installer files (re-downloadable if ever needed)
- `$RECYCLE.BIN` folders on Desktop and Downloads (Windows artifacts)
- `desktop.ini` files (Windows artifacts)
- `.DS_Store` files throughout (macOS metadata, auto-regenerated)
- Build/temp artifacts in Downloads: `build/`, `dist/`, `tmp/`, `extract-xiso/`, `app/`, `[copy]-[copy]-2nd/`
- Duplicate Roland/Boutique USB driver folders: `BoutiqueUSBDriver`, `BoutiqueUSBDriver 2`, `TR08USBDriver`, `TR8USBDriver`, `TR8SUSBDriver`
- Hidden/segmented video files: `.segmented-*.MP4` (3 files)
- Stale `.ics` calendar files from 2021 (4 files)
- `Relocated Items` on Desktop — review contents first, then delete folder

### Phase 3: Review buckets

Items that need a human decision before acting, grouped by category:

**Photos and personal media**
- 215 JPGs + 123 HEICs in Downloads root — route to Apple Photos or a personal archive
- `John.and.Grace.NOLA.2024/` — keep, move to personal archive
- `rememberingmarty/` — keep, move to memorial/personal archive
- `Mart photos and videos and memories/` (Desktop) — same treatment
- `TCU Team Photos/` — review; archive or delete
- `graceandjohn-photo-download-1of1/` — review; archive or delete

**Music production**
- `- Sorted - Personal Favorites/` — what is this? Review contents
- `From Matt loops for Joe/` — keep, move to music production folder
- `TR-8S Kits/`, `OLIVER and other samples/`, `Ueberschall Houseworx/` — move to music production/samples
- `fwdpulsemixes/`, `core_1 Project/`, `tension Project/` — active Ableton projects? Move to proper project folder if so
- `Soulseek Downloads/` (home root) — review; route music to library or sample archive

**eBooks and reading**
- 82 EPUBs in Downloads — likely overlap with Calibre Library; dedup before moving
- Calibre Library (home root) — is Calibre still in active use? If not, consider consolidating
- `Moshfegh, Ottessa - McGlue/`, `Ottessa Moshfegh/`, `LikewarTheWeaponizationOfSocialMedia/` — consolidate into Calibre or archive

**Games and emulation**
- `Halo - Combat Evolved/`, `Halo 2/`, `JSRF/`, `031117-rct2-sacoasterfreak-kumba-rivers_of_babylon/` ROMs — keep or delete based on whether emulation is still active
- `XEMU FILES/`, `xemu-macos-universal-release/`, `halo-2-xbclassicrp/` — same
- `Amped 2 (Europe, Australia)/`, `JSRF - Jet Set Radio Future (USA)/` — same

**Software installers (review before deleting)**
- `Microsoft Office 2021 for Mac LTSC v16.65 VL (macOS)/` — delete if Office already installed
- `Adobe Photoshop 2021 v22.5.1 + Patch (macOS)/` — same
- `Ableton Live 10 Suite 10.1.2 macOS [HCiSO][dada]/` — delete if running Live 11/12
- `MAS_1.7/` — what is this? (Likely macOS App Store scripts)
- `BIGIPMacEdgeClient_v7213/` — VPN client installer; can be re-downloaded
- `Joystick Mapper 1.1/` — keep if in active use

**Work documents**
- 148 DOCX + 20 DOC files in Downloads — route to project folders or archive by year
- `Blog Editorial Calendars 2022/` — archive (dated)
- `Personal work for portfolio/` — keep, move to Documents or a dedicated portfolio folder
- `RCZC slides - visual assets/` — keep, move to personal/RCZC folder
- `eddiebauercopyeditor/` — old client work; archive or delete
- `Reflections/` — personal writing? Review; move to Obsidian or personal docs

**Personal and financial documents**
- PDFs with dates in names (tax returns, leases, contracts) — move to Financial & Legal archive
- `Matt, Steve, Dad & Mom group text.pdf` in Documents — move to family/personal archive
- `TaxReturn.pdf`, `Signed Lease University Manor.pdf` (stray in Documents) — file properly

**Fitness and cycling data**
- 17 GPX files + 13 .fit files in Downloads — move to dedicated cycling/activity archive
- `garminroutes/` — consolidate with GPX files

**Documents folder**
- `Electronic Arts/`, `Rockstar Games/` — app data; can be left or moved to ~/Library
- `Virtual Machines.localized/` — does Parallels still get used? If not, significant disk savings
- `Temp-3 Project/` (home root) — unknown purpose; review and decide

### Phase 4: Proposed folder taxonomy

Proposed structure, centered in Documents:

```
~/Documents/
  Personal/
    Financial & Legal/      tax returns, leases, contracts
    Family/                 family docs, group texts, memorial files
    Health/
    Housing/
    RCZC/                   Red Cedar Zen Community materials
  Work/
    RDC/                    work files by client or project
    Portfolio/
  Music Production/
    Projects/               Ableton projects (active and archived)
    Samples & Sounds/       sample packs, loops, kits
    Devices/                Digitakt patches, TR-8S kits, hardware files
  Cycling/
    GPX Routes/
    Activity Data/          .fit files
  Reading/
    Books/                  EPUBs if moving away from Calibre
  Archive/
    2020 and earlier/
    2021/
    2022/
    2023/
    2024/
    2025/
```

Desktop stays a staging area — temporary and active-work-in-progress only. The existing Desktop folder taxonomy is a good foundation; enforcement is the goal.

Downloads gets treated as a true inbox — emptied regularly after routing. A monthly review habit is the long-term maintenance solution.

### Phase 5: Cloud and sync audit

- Audit Dropbox contents — what's there, is it still actively used, any overlap with local?
- Audit Creative Cloud Files — same questions
- Determine if Dropbox is a legacy holdover or genuinely needed
- Consider consolidating to one cloud sync service if overlap exists

### Phase 6: Disk usage analysis

- Run DaisyDisk or equivalent to get a full size-by-folder breakdown
- Primary suspects for large footprint: Parallels VM images, Soulseek Downloads, old software installers, Music/ folder, Downloads overall
- Make deletion and archival decisions based on actual space impact

## Working notes

- Desktop Commander gives Claude read access to full filesystem; can generate shell scripts for bulk operations for Joe to review and run
- All file moves and deletions require Joe's explicit sign-off — no automated bulk operations without approval
- Suggested shell script format for quick wins: move to ~/.Trash rather than `rm`, preserving recovery option

## Next session entry point

Pick up at: **Phase 2 quick wins** — confirm the delete list, then proceed category by category. Optionally run disk usage analysis first (Phase 6) to prioritize by impact.

# Adaptive Calendar Planner

A VS Code Copilot Skill that plans and re-plans a user's schedule around fixed commitments and flexible tasks, and can read/write Google Calendar events through a Google Calendar MCP server.

## What this skill does

The skill can:

- Read the user's existing calendar events.
- Treat fixed commitments such as university, meetings, and appointments as protected.
- Add flexible tasks such as studying, gym, errands, applications, or focused work.
- Move an existing flexible task from one time or date to another.
- Schedule a task on a specific date.
- Schedule a project across a date range and split the work into realistic calendar blocks.
- Re-plan the rest of the day when something changes.
- Move flexible events while keeping fixed commitments unchanged.
- Avoid overlaps and leave realistic transition/buffer time.
- Stay dormant for general productivity questions that do not require calendar planning.

## Example prompts

### Plan a day

```text
Tomorrow I have university from 9 AM to 12 PM. I need 2 hours to study and 1 hour for the gym. Add a realistic plan to my calendar around my existing events.
```

### Re-plan after something changes

```text
Something came up tomorrow from 2 PM to 3 PM. Add it as a fixed appointment and reorganize the rest of my day without moving my university time.
```

### Move something to another date

```text
Move my study session from tomorrow to Sunday afternoon and fit it around what is already on my calendar.
```

### Schedule something on a specific date

```text
Add a two-hour study block on September 22 and place it in a free slot.
```

### Plan a project across a date range

```text
I need 5 hours for Project X between September 12 and September 13. Split the work into realistic blocks across those two days.
```

If the user only says:

```text
Add Project X from September 12 to September 13.
```

the skill should ask whether the user means:

- one continuous/all-day multi-day calendar event, or
- work sessions distributed across the date range

unless the intent is already clear from context.

### Near-miss that should NOT trigger the skill

```text
What are some good tips for managing my time when I have a busy day?
```

---

## 1. Install the skill

Clone the repository and open it in VS Code.

If you want the skill to be available as a **User Skill** across your VS Code projects, create a symlink from the skill folder to your Copilot user skills folder.

From the repository root:

```bash
mkdir -p ~/.copilot/skills
ln -s "$(pwd)/skills/adaptive-calendar-planner" ~/.copilot/skills/adaptive-calendar-planner
```

Check that the link exists:

```bash
ls -la ~/.copilot/skills | grep adaptive-calendar-planner
```

Then open:

```text
VS Code → Agent Customizations → Skills
```

You should see:

```text
adaptive-calendar-planner
```

---

## 2. Create a Google Cloud project

Go to Google Cloud Console and create a new project.

Suggested project name:

```text
Adaptive Calendar Planner
```

Then select that project.

---

## 3. Enable Google Calendar API

Inside the Google Cloud project:

```text
APIs & Services → Library
```

Search for:

```text
Google Calendar API
```

Open it and click:

```text
Enable
```

---

## 4. Configure Google OAuth

Go to:

```text
Google Auth Platform
```

Configure the OAuth consent screen.

Recommended setup for personal/testing use:

- Audience: `External`
- Publishing status: `Testing`
- Add your own Google account as a Test User.

You do not need to publish the app for personal testing.

---

## 5. Create Desktop OAuth credentials

Go to:

```text
Google Auth Platform → Clients → Create client
```

Choose:

```text
Application type: Desktop app
```

Suggested name:

```text
Google Calendar MCP Desktop
```

Create the client and download the JSON credentials file.

**Important:** Do not commit this JSON file to Git.

---

## 6. Store the OAuth credentials outside the repository

Create a private config folder:

```bash
mkdir -p ~/.config/google-calendar-mcp
```

Move the downloaded Desktop OAuth JSON file into that folder and rename it:

```bash
mv ~/Downloads/YOUR_DOWNLOADED_FILE.json ~/.config/google-calendar-mcp/gcp-oauth.keys.json
```

Verify it exists:

```bash
ls -l ~/.config/google-calendar-mcp/gcp-oauth.keys.json
```

The credentials file should remain outside the Git repository.

---

## 7. Authenticate your Google account

Run:

```bash
GOOGLE_OAUTH_CREDENTIALS="$HOME/.config/google-calendar-mcp/gcp-oauth.keys.json" npx @cocal/google-calendar-mcp auth
```

A browser window should open.

Sign in with the Google account whose Calendar you want to use, then approve access.

A successful authentication looks like:

```text
Tokens saved successfully
Authentication completed successfully!
```

The token is stored locally at:

```text
~/.config/google-calendar-mcp/tokens.json
```

Do not copy this token file into the repository.

---

## 8. Configure the Google Calendar MCP server in VS Code

First find the full path to `npx`:

```bash
which npx
```

Example on Apple Silicon macOS:

```text
/opt/homebrew/bin/npx
```

Open the VS Code MCP configuration JSON and add:

```json
{
  "servers": {
    "google-calendar": {
      "type": "stdio",
      "command": "/ABSOLUTE/PATH/TO/npx",
      "args": [
        "-y",
        "@cocal/google-calendar-mcp",
        "start"
      ],
      "env": {
        "GOOGLE_OAUTH_CREDENTIALS": "$HOME/.config/google-calendar-mcp/gcp-oauth.keys.json"
      }
    }
  },
  "inputs": []
}
```

Replace:

```text
/ABSOLUTE/PATH/TO/npx
```

with the result of:

```bash
which npx
```

Replace:

```text
/Users/YOUR_USERNAME
```

with your own macOS home path.

If you already have other MCP servers configured, keep them and add only the `google-calendar` block.

---

## 9. Start the MCP server

In VS Code open:

```text
Agent Customizations → MCP Servers
```

Find:

```text
google-calendar
```

Then choose:

```text
Start Server
```

A successful connection should show output similar to:

```text
Connection state: Running
Valid tokens found for account(s): normal
Discovered 13 tools
```

---

## 10. Test the skill

Open a fresh Copilot Agent chat.

Do **not** mention the skill name.

### Test automatic planning

```text
Tomorrow I have university from 9 AM to 12 PM. I need 2 hours to study and 1 hour for the gym. Add a realistic plan to my calendar around my existing events.
```

A successful automatic trigger should show:

```text
Read skill `adaptive-calendar-planner`
```

and Google Calendar tool calls.

### Test re-planning

```text
Something came up tomorrow from 2 PM to 3 PM. Add it as a fixed appointment and reorganize the rest of my day without moving my university time.
```

The skill should preserve the fixed event and move only flexible tasks when possible.

### Test moving an event to another day

```text
Move my gym session from tomorrow to Sunday at 6 PM.
```

The skill should:

1. Read the existing event.
2. Read the target date.
3. Update the existing calendar event.
4. Avoid creating a duplicate.

### Test a project across a date range

```text
I need 5 hours for Project X between September 12 and September 13. Split it into realistic work blocks around my existing calendar.
```

The skill should:

1. Read both dates.
2. Find free time.
3. Split the five hours into realistic blocks.
4. Keep fixed commitments unchanged.
5. Write the blocks to the calendar.

---

## 11. Test that the skill stays quiet

Open a new chat and ask:

```text
What are some good tips for managing my time when I have a busy day?
```

The skill should NOT load.

You should not see:

```text
Read skill `adaptive-calendar-planner`
```

and it should not call Google Calendar tools.

---

## Date and date-range behavior

The skill follows these rules:

- A specific date means the task should be scheduled on that date.
- A request to move an existing event should update the existing event rather than duplicate it.
- Before moving an event, the skill reads the target date to avoid conflicts.
- A project date range is treated as a **planning window** by default.
- Project work is split across free calendar blocks inside that window when the required duration is known.
- The skill does not automatically turn a project date range into one continuous multi-day event.
- A continuous or all-day multi-day event is created only when the user explicitly asks for that format.
- If the user's intent is ambiguous, the skill asks one focused clarification before writing to the calendar.

---

## Security and secrets

The repository should NOT contain your Google credentials or tokens.

In this setup, sensitive files are stored outside the repository:

```text
~/.config/google-calendar-mcp/gcp-oauth.keys.json
~/.config/google-calendar-mcp/tokens.json
```

Your VS Code global MCP config is also outside the repository:

```text
~/Library/Application Support/Code/User/mcp.json
```

Therefore, normal Git commands run from this repository will not include those files.

Before pushing, always verify what Git is about to upload:

```bash
git status
```

and after staging:

```bash
git diff --cached --name-only
```

You should only see project files such as:

```text
skills/adaptive-calendar-planner/SKILL.md
skills/adaptive-calendar-planner/EVIDENCE.md
skills/adaptive-calendar-planner/README.md
skills/adaptive-calendar-planner/meta.yml
```

You should NOT see files such as:

```text
gcp-oauth.keys.json
tokens.json
client_secret_*.json
mcp.json
```

If any secret file ever appears in `git status`, do not commit or push it.

---

## Validate the skill

From the repository root:

```bash
python3 scripts/validate_skill.py skills/adaptive-calendar-planner
```

Fix any validation error before opening the pull request.

---

## Summary

The complete flow is:

```text
Install Skill
→ Enable Google Calendar API
→ Create Desktop OAuth credentials
→ Authenticate once
→ Configure Google Calendar MCP in VS Code
→ Start MCP
→ Ask a planning request
→ Skill reads the calendar
→ Skill creates, moves, or splits events across dates
→ Test that it also stays quiet on near-miss prompts
```

The skill itself contains no personal Google credentials and can be shared safely as long as OAuth credential files, token files, and private VS Code configuration are kept outside the repository.

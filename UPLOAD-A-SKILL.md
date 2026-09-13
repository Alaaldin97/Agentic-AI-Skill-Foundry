# How to upload your skill

**Read this once, all the way through, before you start.** It takes about 15
minutes the first time. There are two routes — pick the one that matches how you
like to work. They produce exactly the same result.

| Route | Best if | Time |
|---|---|---|
| **A — GitHub website** | You'd rather not touch the terminal | ~10 min |
| **B — Git on your machine** | You're comfortable with git, or your skill has `scripts/` | ~15 min |

> ### The one thing to understand first
> You **do not** have write access to The Skill Foundry — and neither does anyone
> else. That's deliberate. You work on **your own copy** (a *fork*), then ask for
> your changes to be pulled in (a *pull request*). This is exactly how every open
> source project on earth works, and it's why the library can be open to everyone
> without anyone being able to break it.
>
> If you try to push directly to the Foundry you'll get **`403 Permission denied`**.
> That's not a bug — it means the protection is working.

---

## Before you start — you need three things

1. **A GitHub account.** Free. [github.com/signup](https://github.com/signup)
2. **A skill you have actually run.** Not one you wrote and assumed works — one
   you watched fire on a real prompt and produce real output. If you haven't run
   it yet, stop and go do that. Step 4 is impossible otherwise.
3. **Two transcripts** — one where it fired, one where it correctly stayed quiet.
   Copy them somewhere now, while you still have them.

---

# Route A — Using the GitHub website

No terminal. Works entirely in your browser. Fine for skills that are just
`SKILL.md` + `EVIDENCE.md` + `meta.yml`.

### A1. Fork the Foundry

Go to **[the repository](https://github.com/Alaaldin97/Agentic-AI-Skill-Foundry)**
and click **Fork** (top right) → **Create fork**.

You now have your own full copy at
`github.com/YOUR-USERNAME/Agentic-AI-Skill-Foundry`. Everything you do next
happens there.

### A2. Create your skill folder

In **your fork**, click **Add file** → **Create new file**.

In the filename box, type this — including the slashes:

```
skills/my-skill-name/SKILL.md
```

⚠️ **Typing a `/` creates a folder.** That's how you make directories in the web
editor. Replace `my-skill-name` with your actual skill name: lowercase, hyphens,
no spaces and no underscores.

### A3. Paste your skill

Open [`skills/_TEMPLATE/SKILL.md`](skills/_TEMPLATE/SKILL.md) in another tab,
copy it, paste it into the editor, and fill it in.

**The frontmatter at the top matters more than the rest of the file:**

```yaml
---
name: my-skill-name        # must exactly match your folder name
description: >
  Describe the SYMPTOM the user types, not the feature you built.
  Does NOT fire on: the two or three near-misses that should stay quiet.
---
```

Scroll down, click **Commit changes**.

### A4. Add the other two files

Repeat **A2–A3** twice more, in the same folder:

| File | Copy the template from | What goes in it |
|---|---|---|
| `skills/my-skill-name/EVIDENCE.md` | [`_TEMPLATE/EVIDENCE.md`](skills/_TEMPLATE/EVIDENCE.md) | Your two real transcripts |
| `skills/my-skill-name/meta.yml` | [`_TEMPLATE/meta.yml`](skills/_TEMPLATE/meta.yml) | Your name, GitHub username, category |

All three files are required. The automated check rejects the PR if any is
missing.

### A5. Open the pull request

Go to the **Pull requests** tab of your fork → **New pull request**.

Check the direction of the arrow carefully:

```
base: Alaaldin97/Agentic-AI-Skill-Foundry : main   ←   head: YOUR-USERNAME : main
```

Click **Create pull request**. Fill in the template that appears — it asks five
short questions. Answer them honestly; they're what your reviewer reads first.

**→ Jump to [What happens next](#what-happens-next).**

---

# Route B — Using git on your machine

Required if your skill ships `scripts/` or `resources/`, and faster once you've
done it once.

### B1. Fork, then clone *your fork*

Click **Fork** on
**[the repository](https://github.com/Alaaldin97/Agentic-AI-Skill-Foundry)** → **Create fork**.

Then clone **your copy** — note the username in the URL is *yours*, not mine:

```bash
git clone https://github.com/YOUR-USERNAME/Agentic-AI-Skill-Foundry.git
cd Agentic-AI-Skill-Foundry
```

> 🚩 **The single most common mistake.** If you clone
> `Alaaldin97/Agentic-AI-Skill-Foundry` instead of your own fork, everything
> works right up until `git push`, which fails with `403`. If that happens, see
> [Troubleshooting](#troubleshooting) — it's a two-command fix, you don't lose
> any work.

### B2. Make a branch

```bash
git checkout -b skill/my-skill-name
```

Branch naming: `skill/` + your skill's folder name.

### B3. Copy the template and build

**macOS / Linux:**
```bash
cp -r skills/_TEMPLATE skills/my-skill-name
```

**Windows PowerShell:**
```powershell
Copy-Item -Recurse skills\_TEMPLATE skills\my-skill-name
```

Now fill in all three files. Delete every line of template guidance as you go —
the validator rejects leftover placeholder text, which is its way of checking
you actually wrote it rather than submitted the template.

### B4. Run the check before you push

```bash
python scripts/validate_skill.py skills/my-skill-name
```

**This is the same script that runs in CI.** If it passes here it will pass on
GitHub. If it fails, it tells you exactly which line to fix.

```
  PASS  my-skill-name

1/1 passed
```

Don't skip this. It takes two seconds and saves you a round trip.

### B5. Commit and push — to *your* fork

```bash
git add skills/my-skill-name
git commit -m "Add skill: my-skill-name"
git push origin skill/my-skill-name
```

### B6. Open the pull request

The `git push` output prints a link — click it. Or go to your fork on GitHub,
where a **Compare & pull request** button will have appeared.

Confirm the direction:

```
base: Alaaldin97/Agentic-AI-Skill-Foundry : main   ←   head: YOUR-USERNAME : skill/my-skill-name
```

Fill in the template and click **Create pull request**.

---

## What happens next

**Within about a minute:**

- ✅ **Automated checks run.** A green tick or a red cross appears on your PR.
  Red isn't failure — it's a list of things to fix. Push another commit to the
  same branch and it re-runs automatically.
- 👀 **Your skill appears under "In review"** on
  **[jhf-skills.azurewebsites.net](https://jhf-skills.azurewebsites.net)** for
  the whole cohort to see.
- 🔔 **The maintainer is notified automatically** and requested as reviewer.

**Then:**

- You get review comments. **Expect them** — the first review on a first skill
  almost always finds something, usually in the description. That's the point.
- Fix and push again. Same branch, no new PR needed.
- When it's approved and merged, your skill appears in the catalog and anyone can
  install it with one command.

> **Nothing merges without explicit approval.** Even the maintainer can't merge
> their own work without passing the same checks.

---

## Your part of the deal: review someone else's

**This is required, not optional.** Go to
**[the In-review section](https://jhf-skills.azurewebsites.net#review-section)**,
pick somebody's PR, and leave **one concrete comment**.

Ask yourself:

- Would this description fire on something unrelated to its job?
- Did they really test a near-miss, or invent a convenient one?
- Is a must-happen rule sitting in prose where the model can skip it?
- **Would I install this?**

Quote the line you're commenting on. *"Looks good"* is not a review and doesn't
count.

---

## Troubleshooting

### `403` or `Permission to Alaaldin97/... denied`

You cloned my repo instead of your fork. Your work is fine — just repoint it:

```bash
git remote set-url origin https://github.com/YOUR-USERNAME/Agentic-AI-Skill-Foundry.git
git push origin skill/my-skill-name
```

(Fork the repo first if you haven't.)

### CI says "still contains template placeholder"

You left template text in a file. The error names the file and the exact phrase.
Delete that line and push again.

### CI says "EVIDENCE.md has no dormancy test"

You showed your skill firing but not staying quiet. Add a near-miss prompt and
confirm it didn't load. **Both directions are graded** — this is half the mark.

### CI says "name does not match folder"

The `name:` in your frontmatter and your folder name must be identical. Lowercase,
hyphens, no spaces.

### "My skill never fires when I test it"

Your description is describing the *feature you built* rather than the *symptom
the user types*. Rewrite it as the exact sentence a stranger would type, then try
again. This is by far the most common cause.

### "My skill fires on everything"

You have no `Does NOT fire on:` clause. Add one and name the near-misses.

### VS Code doesn't list my skill at all

Malformed YAML frontmatter — VS Code skips bad files **silently**, with no error.
Check with **Chat: Open Customizations** → **Skills** tab. If it's not listed
there, the frontmatter is the problem: check the `---` fences top and bottom.

### Something else

Post in the group chat. Somebody has almost certainly hit it already.

---

## The 60-second version

```bash
# 1. Fork on github.com, then:
git clone https://github.com/YOUR-USERNAME/Agentic-AI-Skill-Foundry.git
cd Agentic-AI-Skill-Foundry
git checkout -b skill/my-skill-name

# 2. Build it
cp -r skills/_TEMPLATE skills/my-skill-name
#    ...fill in SKILL.md, EVIDENCE.md, meta.yml...

# 3. Check it
python scripts/validate_skill.py skills/my-skill-name

# 4. Ship it
git add skills/my-skill-name
git commit -m "Add skill: my-skill-name"
git push origin skill/my-skill-name

# 5. Open the PR from the link git prints. Then go review someone else's.
```

---

<div align="center">
<sub>Agentic AI Bootcamp · Jerusalem High-Tech Foundry × COMCEC</sub>
</div>

<!-- JHF-BRAND -->
<div align="center" style="padding:28px 20px; background:#ffffff; border:2px solid #e0e0e0; border-radius:12px;">
  <p style="margin:0 0 16px 0;">
    <img src="assets/jhf-logo.png" alt="Jerusalem High-Tech Foundry (JHF)" height="54" style="vertical-align:middle; margin:0 22px;" />
    <img src="assets/comcec-logo.png" alt="COMCEC - Cooperation for Development" height="72" style="vertical-align:middle; margin:0 22px;" />
  </p>
  <h1 style="color:#1a3c5e; margin:6px 0;">The Skill Foundry</h1>
  <h3 style="color:#0078d4; margin:4px 0; font-weight:600;">A shared, living library of agent skills &mdash; built, tested and used by this cohort</h3>
  <hr style="border:0; border-top:1px solid #0078d4; width:60%; margin:16px auto;" />
  <p style="font-size:12.5px; color:#777; margin:8px 0 0 0;">
    Agentic AI Bootcamp &nbsp;&middot;&nbsp; <strong>Jerusalem High-Tech Foundry (JHF)</strong> &nbsp;&middot;&nbsp; In partnership with <strong>COMCEC</strong>
  </p>
</div>

# The Skill Foundry

**A foundry is where raw material gets forged into something useful.** That is what this repo is for.

Every skill in here was **built by someone in this cohort, tested on a real task, and merged only after the evidence was reviewed.** Nothing lands on a promise. If a skill is in `skills/`, it worked at least once, on a real machine, and you can see the proof.

> **This repo outlives the course.** Keep contributing after Week 10. Found a skill that saved you an hour at work? Forge it here.

---

## 🔥 Use a skill (30 seconds)

```bash
git clone https://github.com/Alaaldin97/Agentic-AI-Skill-Foundry.git
cp -r Agentic-AI-Skill-Foundry/skills/<skill-name> ~/.agents/skills/
```

Restart your agent. Then **describe the symptom** — don't name the skill:

> *"Write me a viral LinkedIn post about finishing the bootcamp."*

If the skill was written well, it fires on its own. That is the whole test.

<details>
<summary><b>Where does <code>~/.agents/skills/</code> live on my machine?</b></summary>

| Client | Path |
|---|---|
| VS Code (workspace) | `.github/skills/` or `.agents/skills/` in the repo |
| VS Code (user) | `~/.copilot/skills/` |
| Claude Code | `~/.claude/skills/` |

Check with **Chat: Open Customizations** → **Skills** tab. Your skill should be listed there with its description. If it isn't, the frontmatter is malformed — VS Code skips bad files *silently*.
</details>

---

## 📚 The catalog

**[→ Browse all skills in INDEX.md](INDEX.md)** — auto-generated on every merge.

| | |
|---|---|
| 🗂️ **Browse by folder** | [`skills/`](skills/) |
| 🖼️ **Visual gallery** | [`docs/gallery.html`](docs/gallery.html) — open it in a browser |
| ➕ **Add yours** | [CONTRIBUTING.md](CONTRIBUTING.md) |
| 🙋 **Request one** | [Open a skill request](../../issues/new?template=skill-request.yml) |

---

## ✍️ Contribute a skill

You submit a **Pull Request**, not an issue. Here's why that matters:

| An issue | A pull request |
|---|---|
| A conversation that gets closed | **Files that get merged** |
| Your work dies in a thread | Your work is `git clone`-able forever |
| Nobody can run it | Anyone can install it in 30 seconds |
| No review | You get reviewed — and you review others |
| Ends with the course | **Grows after it** |

**Four steps:**

```bash
# 1. Branch
git checkout -b skill/my-skill-name

# 2. Copy the template and fill it in
cp -r skills/_TEMPLATE skills/my-skill-name

# 3. Check it before you push — same script CI runs
python scripts/validate_skill.py skills/my-skill-name

# 4. Push and open a PR
git push origin skill/my-skill-name
```

**[→ Full walkthrough in CONTRIBUTING.md](CONTRIBUTING.md)**

---

## 🚦 The merge bar

Three files, all required. CI blocks the merge if any is missing or malformed.

| File | What it must contain |
|---|---|
| `SKILL.md` | Frontmatter with `name` + `description`. The description must describe **the symptom a user types**, not the feature you built. |
| `EVIDENCE.md` | A **real transcript** — the prompt you typed, the output you got, on your machine. Plus one case where the skill correctly **stayed dormant**. |
| `meta.yml` | Author, date, category, and which client you tested on. |

> ### Why the evidence file is not optional
> Anyone can write a convincing `SKILL.md`. The question is whether it *fires when it should* and *stays quiet when it shouldn't*. **Both directions are graded.** A skill that triggers on everything is worse than no skill at all — it burns context on every single turn.

---

## 🧭 What makes a good skill here

Skills come in five shapes. Pick the smallest one that solves your problem:

| Shape | Contains | Use when |
|---|---|---|
| **Instructions only** | Just `SKILL.md` | The model already knows how — it just needs to be told *when* and *in what order* |
| **+ a method** | `SKILL.md` with a forced process | The model rushes to output and skips the thinking |
| **+ scripts** | `scripts/` | Something must happen the *same way* every time |
| **+ knowledge** | `resources/` | Facts the model does not have and cannot guess |
| **+ a runtime** | A whole framework | The output needs a real toolchain to exist |

> **A rule in a prompt is advisory. A gate in code is enforced.** If it *must* happen, put it in a script — not in a sentence.

---

## 📁 Repo layout

```
skills/
  _TEMPLATE/           ← copy this to start
    SKILL.md
    EVIDENCE.md
    meta.yml
  <skill-name>/
    SKILL.md           ← required
    EVIDENCE.md        ← required
    meta.yml           ← required
    scripts/           ← optional
    resources/         ← optional
scripts/
  validate_skill.py    ← run this before you push
  build_index.py       ← regenerates INDEX.md + the gallery
docs/
  gallery.html         ← browsable catalog
```

---

<div align="center">
<sub>Agentic AI Bootcamp · Jerusalem High-Tech Foundry × COMCEC · Lead trainer: <a href="https://www.linkedin.com/in/alaaldin-ahmed-260266150">Alaaldin Ahmed</a></sub>
</div>

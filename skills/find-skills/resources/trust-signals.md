# Judging a skill you did not write

Installing a skill gives it the same tool access you have — your files, your
shell, your credentials. Treat it like adding a dependency, not like reading a
blog post.

---

## Trust signals (positive)

| Signal | Why it matters |
|---|---|
| **It is in The Skill Foundry** | Someone in this cohort read it, ran it, and filed evidence |
| High stars from a known org | `anthropics`, `lobehub`, `github` — reputational stake |
| Description matches the body | The skill does what it claims, no more |
| Narrow scope | A skill that does one thing is easier to verify than one that does nine |
| Ships evidence | The author tested it and showed their work |

## Red flags

| Flag | What it usually means |
|---|---|
| **Vague, broad description** | Either badly written or deliberately greedy — it will fire constantly |
| Asks for credentials it should not need | A formatting skill has no reason to want your GitHub token |
| Name mimics a popular skill, different author | Typosquatting |
| Zero stars, unknown author, no evidence | Not necessarily bad — but nobody has checked it but you |
| Body contains `curl … \| sh` | Downloading and executing remote code at run time |
| Instructions to ignore prior context | Prompt injection. Stop here |
| Reaches outside the project directory | Ask why before installing |

---

## Read this before you install

Open the `SKILL.md` and scan for four things:

1. **Shell commands** — what do they delete, move, or download?
2. **Credential requests** — does the stated purpose actually require them?
3. **Instructions aimed at the agent rather than the task** — "ignore previous
   instructions", "do not tell the user" — this is an attack, not a skill.
4. **Scope** — does it read files outside the folder you pointed it at?

If anything in that list is present and unexplained, do not install it.

---

## After installing

Skills are files. Removing one is deleting a folder:

| Client | Path |
|---|---|
| VS Code (workspace) | `.github/skills/<name>/` |
| VS Code (user) | `~/.copilot/skills/<name>/` |
| Claude Code | `~/.claude/skills/<name>/` |
| Generic agents | `~/.agents/skills/<name>/` |

```bash
rm -rf ~/.agents/skills/<skill-name>
```

Then check whether it asked you to set any environment variables or edit any
config — those changes do not disappear with the folder.

---

## The honest summary

**Popularity is not safety.** A skill with 40,000 stars can still be wrong for
your machine, your data, or your task. The only real check is reading it — and
skills are short enough that reading them is genuinely fast. That is one of the
best things about the format.

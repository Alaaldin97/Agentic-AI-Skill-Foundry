## What does it do?

<!-- One sentence. What job does this skill do for whoever installs it? -->



## The trigger phrase you tested

<!-- The exact words you typed that made it fire, with no mention of the skill name. -->

```

```

## The near-miss it correctly ignored

<!-- A prompt that sounds similar but should NOT load this skill - and it didn't. -->

```

```

## Checklist

- [ ] I have **actually run this** — `EVIDENCE.md` contains a real transcript, not a description
- [ ] It fired **without me naming it**
- [ ] I tested a near-miss and it **stayed dormant**
- [ ] `python scripts/validate_skill.py skills/<my-skill>` passes locally
- [ ] No API keys, tokens, or absolute paths from my machine
- [ ] `meta.yml` has my name and the client I tested on

## Shape

<!-- Tick the one that fits. Smallest that solves the problem is best. -->

- [ ] Instructions only — `SKILL.md` and nothing else
- [ ] Enforces a method — makes the model follow a process it would otherwise skip
- [ ] Ships scripts — something must happen the same way every time
- [ ] Ships knowledge — facts the model cannot guess
- [ ] Ships a runtime — needs a real toolchain

## Anything a reviewer should know

<!-- Limitations, required keys, things that surprised you. Optional. -->


---

<sub>Reviewers: install it and try to break it. Does it fire on something unrelated? Is a must-happen rule sitting in prose where the model can skip it? One concrete comment beats "looks good".</sub>

# Evidence — arabic-classical-poetry


Tested on 2026-10-07 on the user's Windows machine using PowerShell and
Codex CLI 0.158.0-alpha.2.1. Two fresh, ephemeral local CLI sessions ran
from an empty temporary directory with the read-only sandbox and the
normally installed skills available. Neither prompt named or explicitly
invoked the skill. No expected answer or routing instruction was supplied.

The installed skill and repository SKILL.md were byte-identical at test time.
SHA-256: `6A96DA2F09FC6237BAF0B971C1E2650193DEF34F5B3D0E72DB38151AD36AD2F6`.

## How the tests ran

Each exact prompt below was piped through UTF-8 stdin to this command,
where TEST_DIR is the temporary directory and CASE is activation or dormancy:

```powershell
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$prompt | codex exec --ephemeral --skip-git-repo-check --sandbox read-only --json --color never -C $testDir - > "$testDir/$case.jsonl" 2> "$testDir/$case.stderr.txt"
```

Both processes exited with code 0. The assistant messages below are copied
directly from the completed JSONL events, without rewriting their text.


## 1. It fired when it should

Session ID: `01a11595-a546-7641-b34b-8225f93c4c1d`.

### Exact prompt

~~~text
اكتب بيتين من الشعر العربي الفصيح العمودي عن الأمل بعد الشدة، بلغة سهلة ونبرة متفائلة. اختر البحر والقافية وبقية التفاصيل بنفسك، ولا تسألني أسئلة. لا تستخدم اقتباسات أو قصصًا أو بحثًا على الإنترنت، واذكر البحر والروي بعد البيتين.
~~~

### Assistant output

Message 1:

~~~text
سأستخدم مهارة الشعر العربي الفصيح لصياغة بيتين ومراجعة وزنهما وقافيتهما.

~~~

Message 2:

~~~text
إِذا ضاقَ دَرْبٌ وطالَ المَسيرُ ** ففي آخِرِ اللَّيلِ فَجْرٌ مُنيرُ  
سيأتي صَباحٌ وتُمْحى الجِراحُ ** ويُزْهِرُ في القَلْبِ حُلْمٌ نَضيرُ

البحر: المتقارب. الروي: الراء المضمومة.
~~~

### Observed activation
The assistant announced use of the poetry skill, then executed one successful
Get-Content call reading the installed arabic-classical-poetry/SKILL.md
before returning the two verses. The loaded file matched this repository's
skill. This is observed automatic selection for this prompt, not an explicit
skill invocation. No other tool calls appeared in the completed event trace.

The response provided two verses and named a meter and rhyme letter, as
requested. Meter correctness was not independently assessed.

### Reported usage

```json
{
  "input_tokens": 35157,
  "cached_input_tokens": 29696,
  "cache_write_input_tokens": 0,
  "output_tokens": 1118,
  "reasoning_output_tokens": 930
}
```

## 2. It stayed dormant on a near-miss

Session ID: `01a11595-a540-7691-9dd6-ba58620ae234`.

### Exact prompt

~~~text
اكتب قصيدة نثر عربية قصيرة عن الأمل بعد الشدة، في فقرة واحدة من ثلاث جمل بلغة سهلة وصور هادئة، دون وزن أو قافية.
~~~

### Assistant output

Message 1:

~~~text
بعد الأيام الصعبة، دخل الأمل من نافذتي كضوء الصباح، واستقر بهدوء على الأشياء التي ظننت أنها فقدت لونها. جلست أراقب نبتة صغيرة ترفع أوراقها، وشعرت أن في قلبي مكانًا لفرح جديد. لم تذهب كل الأحزان، لكنني فتحت النافذة وسقيت النبتة، ثم تركت للشمس كرسيًا إلى جانبي.
~~~

### Observed dormancy
The complete event stream contained thread.started, turn.started, one
item.completed of type agent_message, and turn.completed. There were no
tool calls, no skill-file reads, and no announcement of poetry-skill use.
The answer was one prose paragraph of three sentences, without a meter
or rhyme specification.

This is a genuine near-miss: it requests an Arabic prose poem on the same
theme as the activation case. Prose poems are explicitly excluded by this
skill's description. The skill stayed dormant in the observable trace;
this single run does not establish routing behavior for all requests.

Complete dormancy JSONL transcript:

```jsonl
{"type":"thread.started","thread_id":"01a11595-a540-7691-9dd6-ba58620ae234"}
{"type":"turn.started"}
{"type":"item.completed","item":{"id":"item_0","type":"agent_message","text":"بعد الأيام الصعبة، دخل الأمل من نافذتي كضوء الصباح، واستقر بهدوء على الأشياء التي ظننت أنها فقدت لونها. جلست أراقب نبتة صغيرة ترفع أوراقها، وشعرت أن في قلبي مكانًا لفرح جديد. لم تذهب كل الأحزان، لكنني فتحت النافذة وسقيت النبتة، ثم تركت للشمس كرسيًا إلى جانبي."}}
{"type":"turn.completed","usage":{"input_tokens":16475,"cached_input_tokens":13312,"cache_write_input_tokens":0,"output_tokens":121,"reasoning_output_tokens":18}}
```

### Reported usage

```json
{
  "input_tokens": 16475,
  "cached_input_tokens": 13312,
  "cache_write_input_tokens": 0,
  "output_tokens": 121,
  "reasoning_output_tokens": 18
}
```

## 3. Limits and environment notes

Token counts above are whole-session CLI usage, not an isolated measurement
of the skill description or body. The inactive run did not read the skill body.

CLI startup emitted plugin-icon and PowerShell snapshot warnings. The apps
MCP connector also failed to initialize; both text-generation runs nevertheless
completed. No external research or prosody checker was used. These transcripts
test the installed skill with identical repository content, not installation
or discovery directly from the repository's skills directory.

These were single-turn tests. Follow-up editing, optional references, story
research, and independent prosody validation remain untested.

## 4. Repository validation

The repository validator is run separately after updating this evidence.
It checks structure, not the behavioral or poetic correctness of these outputs.


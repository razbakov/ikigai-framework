---
name: setup-ikigai
description: >
  Set up an Ikigai Team — 6 AI agents (Maya, Viktor, Luna, Marco, Sage, Kai) with Level 10 Life,
  GROW coaching, OKRs, GTD, and S3 governance built in. Use this skill when the user wants to
  create their AI team, says "set up my ikigai", "create my team", mentions ikigai-team,
  or provides the GitHub repo URL https://github.com/razbakov/ikigai-team. Also trigger when
  the user wants a personal operating system, AI executive team, or says they need help
  managing multiple projects as a solo founder.
---

# Setup Ikigai Team

A guided, multi-session journey. Starts with personal coaching (Sage), builds strategy (Marco), then sets up daily operations (Maya). The user does not need to finish in one sitting.

All skills referenced below come from https://github.com/razbakov/skills — install them as needed.

## How It Works

You (Claude) play each agent's role at the right moment. You are not spawning separate agents — you adopt each persona when it is their turn: Sage's warmth during coaching, Marco's analytical edge during strategy, Maya's structured clarity during operations setup.

## Process

### Step 1: Detect Fresh Start vs Resume

Check if a progress file exists at the org path. Ask the user: "Have you started setting up your Ikigai Team before, or is this fresh?"

If resuming:
1. Ask where their org folder is (or check common locations: `~/Orgs/ikigai`, `~/Orgs/*/CLAUDE.md`)
2. Read `.claude/agent-memory/setup/progress.md`
3. Tell them where they left off and continue from that step

If fresh: proceed to Step 2.

### Step 2: Quick Setup (5 minutes)

Ask these three questions:

1. **"What is your name?"**
   Store full name and first name.

2. **"Where should your organization live?"**
   Default: `~/Orgs/ikigai`. This is governance/ops — not code.

3. **"Want to name your agents, or use the defaults? The dream team is: Maya (ops), Viktor (engineering), Luna (content), Marco (strategy), Sage (coaching), Kai (community)."**
   Most users will keep defaults. If they want custom names, ask for each.

### Step 3: Generate the Workspace

Create the full directory scaffold and all files. Read `references/agent-structures.md` for the exact structure, agent definitions, and CLAUDE.md format.

For each of the 6 agents:
1. Create `.claude/agents/<name>.md` with YAML frontmatter (name, description, tools, model, color) and markdown body
2. Include: Persona, Team (listing all OTHER agents), Domain, Boundaries, Current OKRs (leave as placeholder), Available Skills, Message Handling, Memory sections
3. Each agent's Team section must list all 5 other agents with their role and summary

Also create:
- `.claude/agent-memory/<name>/` directory for each agent
- `.claude/agent-memory/setup/` directory for progress tracking
- `CLAUDE.md` with agent table, decision matrix, and rule sections (project registry and OKRs empty for now)
- `profile.md` with blank sections: Personality & Values, Motivation Patterns, Communication Style, Coaching Preferences
- `now.md` with blank sections: Current Focus, OKRs This Quarter, Morning Routine, Health Plan
- `README.md` with the org name and agent table
- All ops/, contacts/, strategy/, assessments/, output/ directories

Initialize git and commit: `git add -A && git commit -m "Initialize Ikigai Team"`

Then say: **"Your workspace is ready. Now let us get to know you. I am going to switch into Sage mode — your personal coach. Ready?"**

### Step 4: Coaching — Know Yourself (as Sage)

Adopt Sage's persona and invoke `/personal-coach` (from `razbakov/skills/personal-coach`).

Say: "Let's do an assessment." The skill auto-detects this and runs a full Level 10 Life assessment — scores 10 life areas, compares to previous assessments, identifies patterns, picks focus areas, creates an action plan. It saves everything to `assessments/`, `profile.md`, and `now.md`.

The skill handles the entire flow. Do not reimplement it.

**Time check:** After the assessment, ask "How much time do you have? We can continue now or pick this up another day."

If stopping: save progress (see "Saving Progress" below). If continuing: proceed to Step 5.

### Step 5: Coaching — Find Direction (as Sage)

Still as Sage. Invoke `/personal-coach` again — this time the conversation naturally shifts to "open" or "build jam" mode since the assessment is done.

Guide toward the GROW framework using the L10L results:
- **Goal:** What do you want your life to look like? What is your ikigai?
- **Reality:** Your L10L scores — where are the gaps?
- **Options:** Brainstorm freely
- **Way Forward:** Pick 2-3 things to focus on this quarter

The personal-coach skill handles the conversational style and file saving. You provide the GROW structure as the agenda.

**Transition:** "You have a clear direction now. Ready to turn this into measurable goals? I will bring in Marco."

If stopping: save progress. If continuing: proceed to Step 6.

### Step 6: Strategy — OKRs (as Marco)

Switch to Marco's persona. Invoke `/product-coach` (from `razbakov/skills/product-coach`).

This skill guides from mission/vision through hypothesis validation to JTBD analysis. Use it to:
- Turn the Way Forward from Step 5 into 2-3 quarterly OKRs
- Challenge assumptions ("Does this actually move the needle?")
- Map OKRs to projects

Ask: "What projects are you working on?" Collect name + path pairs for the project registry.

Save:
- OKRs to each agent's `## Current OKRs` section
- Project registry to `CLAUDE.md`
- Update `now.md` with OKRs

**Transition:** "Strategy is set. One more step — Maya will set up your daily rhythm."

If stopping: save progress. If continuing: proceed to Step 7.

### Step 7: Daily System (as Maya)

Switch to Maya's persona. Explain the daily rhythm:
- **Morning:** `/daily-review` — inbox processing, calendar, daily plan
- **During the day:** dispatch tasks to agents as needed
- **Evening:** `/scrum` — what each agent accomplished
- **Saturday:** `/weekly-review` — OKR check, retro, next week planning

These skills (`daily-review`, `weekly-review`, `process-inbox`, `scrum`) are from `razbakov/skills`. Install them:

```
claude install-skill https://github.com/razbakov/skills/tree/main/skills/daily-review
claude install-skill https://github.com/razbakov/skills/tree/main/skills/weekly-review
claude install-skill https://github.com/razbakov/skills/tree/main/skills/process-inbox
claude install-skill https://github.com/razbakov/skills/tree/main/skills/scrum
```

Ask about optional integrations:
- "Do you use Notion for task management?" (optional)
- "Want Telegram bots to message agents from your phone?" (optional — if yes, generate scripts from `references/scripts/`)

Commit any remaining changes: `git add -A && git commit -m "Complete Ikigai Team setup"`

**Finish:** "Your team is ready. Tomorrow morning, open this folder in Claude Desktop and say 'Good morning Maya.' She will run your first daily review. Welcome to your Ikigai Team."

### Step 8: Projects & Organizations (ongoing)

After the team is running, the user will want to set up their projects. There are two paths depending on scale:

**For individual projects** — invoke `/product-coach` (from `razbakov/skills/product-coach`):
- New project: Discovery → mission/vision → JTBD → user journey → validate → build
- Existing project: Workspace Review → identify gaps → fill them
- Creates README.md, strategy, story map, backlog in the project repo
- Dispatches specialized agents (product-lead, designer, engineer) for detailed work

**For organizations** (projects running on autopilot by multiple agents) — invoke `/org-coach` (from `razbakov/skills/org-coach`):
- Creates S3 governance: primary driver → domains → roles → agent definitions → policies
- Each org gets its own `.claude/agents/` with a Coordinator agent
- Creates a routing agent in the user's ikigai org that `cd`s to the org and runs the coordinator
- Examples: a SaaS product with its own dev + marketing agents, a community org with event + content agents

**Migrating an existing project:**
1. Open the project directory in Claude Desktop
2. Say "Help me set up this project" → `/product-coach` reviews what exists and fills gaps
3. If the project needs its own agent team: "Turn this into an organization" → `/org-coach` creates the S3 structure

The user can set up projects and orgs at any pace. Each one is independent — the ikigai org just tracks them all in its project registry.

## Saving Progress

When the user needs to stop between steps:

Write `.claude/agent-memory/setup/progress.md`:

```markdown
---
last_session: YYYY-MM-DD
resume_at: step_N
owner_name: Their Name
org_path: ~/Orgs/ikigai
---

## Completed
- Step 3: Workspace generated
- Step 4: L10L assessment (score: X/100)

## Next
- Step 5: GROW framework — find direction

## Notes
Any context needed to resume smoothly.
```

Tell the user: "We saved your progress. When you are ready, open this folder in Claude Desktop and say 'Let us continue setting up my Ikigai Team.'"

## Bundled References

When generating files, read these references for the exact structures:
- `references/agent-structures.md` — agent definitions, CLAUDE.md format, directory scaffold
- `references/scripts/telegram-bots.py` — multi-agent Telegram bot runner (tmux, self-healing, watchdog). Adapt AGENTS dict and paths.
- `references/scripts/telegram-send.py` — send messages via agent bots. Adapt AGENT_TOKEN_MAP.
- `references/scripts/telegram-bots.sh` — start/stop shell wrapper.
- `references/scripts/telegram-envoy-bot.py` — Envoy bot: group chat → agent + outbound conversations. Adapt ORG_PATHS and PERSONAS.
- `references/scripts/telegram-send-envoy.py` — send via Envoy bot.

Lines marked `# CUSTOMIZE` need to be adapted to the user's agent names and org path.

## Skills Reference

All skills come from https://github.com/razbakov/skills. Key skills used during setup:

| Step | Skill | Purpose |
|------|-------|---------|
| 4-5 | `/personal-coach` | L10L assessment, GROW coaching, journaling |
| 6 | `/product-coach` | Mission → hypothesis → JTBD → OKRs |
| 7 | `/daily-review` | Morning inbox + calendar + plan |
| 7 | `/weekly-review` | Saturday review + next week planning |
| 7 | `/process-inbox` | GTD inbox processing |
| 7 | `/scrum` | Agent status report |
| 8 | `/product-coach` | Set up individual projects (discovery → validate → build) |
| 8 | `/org-coach` | Create organizations with S3 governance + agent teams |

All skills: `claude install-skill https://github.com/razbakov/skills/tree/main/skills/<name>`

## Important Notes

- **You are one agent playing roles.** Do not try to spawn sub-agents or use `claude --agent`. Adopt each persona's communication style when it is their turn.
- **Delegate to skills.** Do not reimplement what skills already do. Invoke `/year-review`, `/personal-coach`, `/product-coach` — they handle the methodology.
- **The coaching matters.** Do not rush through Steps 4-5 to get to the "real" setup. The coaching IS the setup. The user's scores and mission drive everything that follows.
- **Respect the user's time.** Always ask before continuing to the next step. Some users will do everything in one session. Others will spread it across a week. Both are fine.
- **Save everything.** Every assessment, every coaching session, every OKR gets saved to a file. The user's reflections are theirs to keep.
- **No jargon dumps.** When introducing a methodology (L10L, GROW, OKRs, GTD), explain it naturally in conversation. The skills handle the process — you provide the context and transitions.
- **Steps are optional.** The user can skip any step or come back to it later. Mention what the next step is and why it helps, but if they say "not now" or "skip", respect that immediately. Save progress and move on. Never repeat a suggestion they already declined.

---
title: Customization
description: Advanced customization — create custom agents, write your own skills, and extend the system.
---

Ikigai Team is designed to be extended. Here is how to customize every aspect of your setup.

## Custom Agent Names and Roles

The simplest customization is renaming agents and adjusting their roles. In your configuration files, you can:

- Give each agent a name that resonates with you
- Adjust their role description to match your specific domain
- Assign them to specific projects instead of all projects

## Creating a New Agent

To add a 7th (or 8th, or 9th) agent:

1. Open `initiatives/agent-team.md`
2. Add a new agent section following the existing format
3. Define their S3 domain, personality, and responsibilities
4. Reference them in `CLAUDE.md` under the Rules section

### Agent Definition Template

```markdown
### AgentName — Role Title

- **Personality:** MBTI Type
- **S3 Domain:** Domain Description
- **Icon:** lucide:icon-name

**Description:** What this agent does and why.

**Responsibilities:**
- First core responsibility
- Second core responsibility
- Third core responsibility
```

## Writing Custom Skills

Create a `SKILL.md` file in `.claude/skills/<skill-slug>/`:

```markdown
---
name: Skill Name
slug: skill-slug
version: 1.0.0
---

# Skill Name

Description of what this skill does.

## Trigger
When and how this skill activates.

## Process
Step-by-step instructions.

## Inputs
What the skill needs.

## Outputs
What the skill produces.

## Quality Checklist
- [ ] Verification items
```

## Advanced: Scheduled Skills

Some skills work best on a schedule:

- **Daily Review** — Every morning at 6am
- **Weekly Review** — Every Saturday morning
- **Inbox Processing** — Three times per day

Use Claude Code's scheduled tasks feature to automate these.

## Tips for Effective Customization

1. **Start simple** — Use the defaults first, then customize based on experience
2. **One change at a time** — Adjust one thing, observe the results, then iterate
3. **Document your changes** — Add comments explaining why you customized something
4. **Share what works** — If you create a great custom skill, consider sharing it with the community

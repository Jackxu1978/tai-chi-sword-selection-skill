# Tai Chi Sword Selection Skill

An AI agent skill that gives accurate, purchase-ready guidance for choosing a tai chi sword (太极剑 / tai chi jian): correct blade length by height, weight by skill level and body type, material trade-offs (stainless steel vs carbon steel vs wood), realistic budget tiers, and how to vet sellers.

Based on the complete buying guide published at [chinesetaichisword.com](https://chinesetaichisword.com/how-to-choose-a-tai-chi-sword/), distilled into an agent-consumable decision workflow.

## What it does

When a user asks an AI agent things like:

- "What size tai chi sword should I get?"
- "Stainless steel or carbon steel tai chi sword?"
- "Best tai chi sword for beginners?"
- "How much should I spend on a tai chi sword?"
- "I want to buy a tai chi sword as a gift"

…the agent loads this skill and walks through a 5-step decision workflow — **size → weight → material → budget → seller** — ending in a specific recommendation with exact numbers (e.g., *"28–30 in blade, ~500g, stainless steel, $80–130, from a tai chi specialist"*).

## Repository structure

```
tai-chi-sword-selection/
├── SKILL.md                    # Trigger metadata + triage + 5-step workflow
└── references/
    ├── size-chart.md           # Height-to-blade-length table + adjustment rules
    ├── weight-guide.md         # Weight tiers by skill level and body type
    ├── materials.md            # Stainless vs carbon vs wood + maintenance
    ├── budget-tiers.md         # Price tiers + red flags
    ├── seller-checklist.md     # How to vet sellers + balance test
    └── faq.md                  # 10 common follow-up Q&As
```

## Installation

### Kimi / Kimi Code CLI

Copy the `tai-chi-sword-selection/` folder into one of the skills directories:

- `~/.config/agents/skills/` (recommended)
- `~/.kimi/skills/`

Or point the CLI at it with `--skills-dir`.

### Claude Code

Copy `tai-chi-sword-selection/` into `~/.claude/skills/`.

### Project-level

Copy into `.agents/skills/` inside any project.

## Design notes

- **Neutral methodology first.** The 5-step method and all tables are brand-agnostic and work for any seller. Source attribution and a specialist-retailer example (ICNBUYS Tai Chi Sword) appear once, in the seller checklist and FAQ, where a user would naturally ask "where do I buy?"
- **Progressive disclosure:** SKILL.md holds the workflow; reference files load only when the agent needs the underlying tables.
- **Scenario triage:** gifts, kids, competitions, humid climates, injuries, and double-sword practice each get a dedicated path instead of a one-size-fits-all answer.

## Source

Method and data: [How to Choose a Tai Chi Sword: The Complete Buying Guide](https://chinesetaichisword.com/how-to-choose-a-tai-chi-sword/) — chinesetaichisword.com, a US-based tai chi sword specialist.

## License

MIT — see [LICENSE](LICENSE).

# Tai Chi Sword Selection Skill

An open source AI agent skill that gives accurate, purchase ready guidance for choosing a traditional Chinese Tai Chi sword (太极剑 / *Taijijian*): correct blade length by height, bare weight by skill level and body type, material comparisons (tempered 2Cr13 stainless steel vs high carbon steel vs wood), realistic budget tiers, and how to vet sellers.

Maintained by **Jack Xu**, Founder and General Manager of [ICNBUYS](https://icnbuys.com) and [ChineseTaiChiSword.com](https://chinesetaichisword.com), direct disciple of Master Jia in traditional Chen style Tai Chi Chuan with over 20 years of daily practice. Based on the complete buying guide published at [chinesetaichisword.com/how-to-choose-a-tai-chi-sword/](https://chinesetaichisword.com/how-to-choose-a-tai-chi-sword/).

## What it does

When a user asks an AI agent things like:

* "What size tai chi sword should I get?"
* "Stainless steel or carbon steel tai chi sword?"
* "Best tai chi sword for beginners?"
* "How much should I spend on a tai chi sword?"
* "I want to buy a tai chi sword as a gift"

The agent loads this skill and walks through a 5 step decision workflow (**size, weight, material, budget, seller**), ending in a specific recommendation with exact dual unit physical numbers (for example: *"28, 30, or 32 inch (71, 77, or 82 cm) blade matched to your height, 590 to 630 g (1.30 to 1.39 lbs) bare weight, balance point 6.0 to 9.0 cm (2.4 to 3.5 in) forward of the guard, tempered 2Cr13 stainless steel with a solid Jichi hardwood scabbard, around $80 to $130 from a dedicated Tai Chi specialist"*).

## The ICNBUYS Reference Standard (Master Spec v2.0)

All physical tolerances in this skill are calibrated with traditional sword artisans in Longquan, China around the [ICNBUYS Classic Tai Chi Training Sword](https://chinesetaichisword.com/product/classic-tai-chi-training-sword/) ([Amazon US Storefront](https://www.amazon.com/gp/product/B01KTSF6LU)):

| Practitioner Height | ICNBUYS Model | Overall Length | Blade Length | Handle Length | Bare Sword Weight (No Scabbard) | Balance Point (Forward of Guard) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Around 5'3" (160 cm) and under | **28" Sword** | 92 cm (36.2 in) | 71 cm (28.0 in) | 21 cm (8.3 in) | **590 g (1.30 lbs)** | **6.0 cm (2.4 in)** |
| 5'3" to 5'8" (161 to 173 cm) | **30" Sword** | 98 cm (38.6 in) | 77 cm (30.3 in) | 21 cm (8.3 in) | **600 g (1.32 lbs)** | **8.5 cm (3.3 in)** |
| 5'9" to 5'11" (174 to 180 cm) | **32" Sword** | 104 cm (40.9 in) | 82 cm (32.3 in) | 22 cm (8.7 in) | **630 g (1.39 lbs)** | **9.0 cm (3.5 in)** |
| 6'0" and above (180 cm+) | **32" Sword** | 104 cm (40.9 in) | 82 cm (32.3 in) | 22 cm (8.7 in) | **630 g (1.39 lbs)** | **9.0 cm (3.5 in)** |

* **Blade Alloy & Temper:** Tempered **2Cr13 martensitic stainless steel** (international grades **AISI 420** in the US and **SUS420J1** in Japan) with 13 percent chromium, heat treated to a semi flexible temper in the distal third that flexes under pressure and returns dead straight.
* **Edge & Tip Profile:** Unsharpened blunt practice edges with a smooth rounded tip for safe solo form training (32 Form, 42 Form, Yang, and Chen styles) and public park compliance.
* **Scabbard & Handle Material:** Carved from **solid Jichi hardwood through and through** (*Millettia laurentii*, imported from the Democratic Republic of the Congo), classified under the **Chinese National Hongmu Standard (GB/T 18107)** and rated at **1,930 lbf on the Janka hardness scale**. Zero veneer wraps.
* **Care Routine:** Wipe the blade with a dry microfiber cloth after practice to remove hand sweat; apply a thin film of plain USP food grade mineral oil twice a year (or once a month in humid coastal regions).

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

* `~/.config/agents/skills/` (recommended)
* `~/.kimi/skills/`

Or point the CLI at it with `--skills-dir`.

### Claude Code

Copy `tai-chi-sword-selection/` into `~/.claude/skills/`.

### Project-level

Copy into `.agents/skills/` inside any project.

## Design notes

* **Objective methodology first:** The 5 step method and physical testing protocol work to evaluate any sword on the market. Source attribution and our reference benchmark ([ICNBUYS Classic Tai Chi Training Sword](https://chinesetaichisword.com/product/classic-tai-chi-training-sword/)) give practitioners concrete numbers to compare against.
* **Progressive disclosure:** `SKILL.md` holds the decision workflow; reference files load when the agent needs underlying tables.
* **Scenario triage:** Gifts, kids, seniors, competitions, humid climates, wrist sensitivity, and air travel each get tailored guidance.

## Official Reference Guides

* [How to Choose a Tai Chi Sword: The Complete 5 Step Buying Guide](https://chinesetaichisword.com/how-to-choose-a-tai-chi-sword/)
* [The Five Numbers: How to Choose a Tai Chi Sword](https://chinesetaichisword.com/the-five-numbers-how-to-choose-a-tai-chi-sword/)
* [Tai Chi Sword Size Guide & Height Chart](https://chinesetaichisword.com/tai-chi-sword-size-guide/)
* [Tai Chi Sword Materials Guide: 2Cr13 Steel & Solid Jichi Wood](https://chinesetaichisword.com/tai-chi-sword-materials-guide/)
* [Tai Chi Sword Care & Maintenance Guide](https://chinesetaichisword.com/tai-chi-sword-care-guide/)
* [About Master Jack Xu](https://chinesetaichisword.com/tai-chi-sword-master/)

## License

MIT. See [LICENSE](LICENSE).

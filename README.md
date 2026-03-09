# LinkedIn Content System

A multi-persona LinkedIn content generation system powered by Claude Code. Generate high-converting LinkedIn posts, carousels, and images — all tailored to specific personas, audiences, and content strategies.

---

## Quick Start

1. Open this project folder in Claude Code
2. Tell Claude what you want to create (e.g., "Create a LinkedIn post")
3. Claude will walk you through the workflow automatically

That's it. Claude reads `CLAUDE.md` as its operating guide and handles the rest.

---

## How It Works

The system follows a 7-step workflow for every post:

1. **Select Persona** — Claude asks which persona you're writing as
2. **Select Post Type** — Choose from available types (lead magnets, thought leadership, etc.)
3. **Load Context** — Claude reads all persona files (business context, ICP, brand voice)
4. **Load Post Resources** — Claude reads examples, prompts, hooks, and strategy files for the post type
5. **Provide Topic** — You give the topic, angle, or idea
6. **Generate Post** — Claude writes the post matching your persona's voice, audience, and strategy
7. **Save Post** — Final post is saved to `generated_posts/` with metadata

---

## Directory Structure

```
Content System/
├── CLAUDE.md                     # AI operating guide (do not delete)
├── keys.md                       # API keys for image gen, scraping, etc.
├── README.md                     # This file
│
├── image_gen/                    # Image generation prompt templates
│   ├── single_image.md
│   └── infographics.md
│
├── carousel-maker/               # Carousel PDF generation skill
│
├── persona/
│   └── {persona_name}/
│       ├── business_context.json # Business model, offerings, positioning
│       ├── icp.json              # Ideal customer profiles & psychology
│       ├── brand_voice.json      # Tone, language patterns, guardrails
│       ├── content_strategy.json # Content pillars & goals (optional)
│       │
│       ├── lead_magnets/         # Post type: lead magnet resources
│       │   ├── linkedin_post_generator_prompt.md
│       │   ├── linkedin_post_examples.md
│       │   ├── hooks.txt
│       │   └── hook_strategy.md
│       │
│       ├── thought_leadership/   # Post type: thought leadership resources
│       │   └── linkedin_post_examples.md
│       │
│       ├── competitor_posts/     # Scraped competitor data (date-stamped)
│       │   └── competitor_posts_MM_DD_YY.json
│       │
│       └── generated_posts/      # All generated content saved here
│           ├── {type}_{date}_{topic}.md          # Text posts
│           ├── {type}_carousel_{date}_{topic}.pdf # Carousels
│           └── {type}_image_{date}_{topic}.png    # Images
```

---

## What You Can Create

### Text Posts
Just follow the workflow. Claude generates posts matching your persona's voice, targeting your ICP, using proven hook patterns.

**Example prompt:** "Create a lead magnet post for Aryan about AI replacing manual workflows"

### Carousels
After generating a post, ask Claude to turn it into a carousel. It produces a branded multi-slide PDF (1080x1350) ready for LinkedIn/Instagram.

**Example prompt:** "Make a carousel for that post"

### Images & Infographics
Ask Claude to generate a visual for any post. It uses fal.ai to create LinkedIn-optimized images.

**Example prompt:** "Create an infographic for this post"

---

## Available Post Types

| Type | Goal | Key Feature |
|------|------|-------------|
| **Lead Magnets** | Drive comments & leads | Comment-gated CTA ("Comment X below") |
| **Thought Leadership** | Build authority | Insight-driven, 30+ templates |

More post types can be added per persona (see below).

---

## Managing Personas

### Current Personas
Check the `persona/` folder to see all available personas.

### Adding a New Persona

Create a folder under `persona/` with these files:

```
persona/new_persona/
├── business_context.json    # Required: business model, offerings
├── icp.json                 # Required: target audience segments
├── brand_voice.json         # Required: tone, language, guardrails
├── generated_posts/         # Required: empty folder for outputs
└── lead_magnets/            # At least one post type folder
    ├── linkedin_post_generator_prompt.md
    └── linkedin_post_examples.md
```

### Adding a New Post Type

Create a subfolder under any persona with:

1. `linkedin_post_examples.md` — 3-5 example posts showing the quality bar
2. `linkedin_post_generator_prompt.md` — Instructions for generating this post type
3. Optional: `hooks.txt`, `hook_strategy.md`

---

## Competitor Research

Claude can scrape and analyze competitor LinkedIn posts to inform hook engineering.

**Example prompt:** "Scrape competitor posts for Aryan's niche"

Results are saved to `persona/{name}/competitor_posts/competitor_posts_MM_DD_YY.json` and used as inspiration for future posts.

---

## API Keys

All API credentials are stored in `keys.md`. This includes keys for:
- Image generation (fal.ai)
- LinkedIn scraping (Apify)
- Any other third-party services

Never hardcode keys elsewhere. Claude reads from `keys.md` automatically.

---

## Tips

- **Hook is everything** — The system spends 80% of effort on the first 1-2 lines
- **Iterate freely** — Ask Claude to revise any part of the post before saving
- **One post at a time** — Complete the full workflow before starting another
- **Voice matching** — Posts are written to be indistinguishable from the persona's real voice
- **Brand guardrails** — Phrases in `never_use` lists are automatically avoided

---

## Files You Should Not Edit

| File | Reason |
|------|--------|
| `CLAUDE.md` | AI operating guide — controls the entire system behavior |
| `keys.md` | API credentials — edit only to update keys |

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Claude doesn't follow the workflow | Make sure `CLAUDE.md` exists in the project root |
| Posts sound generic | Check that `brand_voice.json` has detailed language patterns |
| Missing post type | Add a subfolder with examples and a generator prompt |
| Image generation fails | Verify API key in `keys.md` is valid |
| Carousel not generating | Ensure the carousel-maker skill files are present |

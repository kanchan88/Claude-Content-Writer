# LinkedIn Content System - AI Operating Guide

This is a multi-persona LinkedIn content generation system. Follow this guide precisely when creating any LinkedIn post.

---

## WORKFLOW (Follow Every Time)

### Step 1: Identify Persona

Ask the user: **"Which persona are you creating content for?"**

List available personas by scanning the `persona/` directory. Each subfolder is a persona name (e.g., `aryan`).

### Step 2: Identify Post Type

Ask the user: **"What type of LinkedIn post do you want to create?"**

List available post types by scanning that persona's subfolders (excluding `generated_posts/`). Current post types include:
- `lead_magnets` - High-conversion posts designed to capture leads via comment-gated free resources
- `thought_leadership` - Authority-building posts that showcase expertise, frameworks, and industry perspective
- *(More post types will appear as new folders are added per persona)*

### Step 3: Load Persona Context

Read ALL of these files from `persona/{persona_name}/` to deeply understand who you are writing as:

| File | Purpose |
|------|---------|
| `business_context.json` | Business model, offerings, revenue, partnerships, strategic positioning |
| `icp.json` | Ideal Customer Profile - segments, pain points, psychology, buying triggers |
| `brand_voice.json` | Tone, language patterns, phrases to use/avoid, communication style |
| `content_strategy.json` | Content pillars, themes, goals, publishing cadence (if exists) |

**Do not skip any file.** These define the persona's identity, audience, and voice. Every post must reflect this context.

### Step 3b: Load Competitor Research (Hook Inspiration)

Check `persona/{persona_name}/competitor_posts/` for the most recent `competitor_posts_{MM_DD_YY}.json` file. Scan the high-performing posts for:
- Hook patterns and opening lines that drove high engagement
- Formatting techniques (line breaks, emojis, separators)
- CTA styles and comment-gating strategies
- Content angles and framing approaches

Use these as **inspiration for hook engineering** in Step 6. Do not copy — adapt the patterns to match the persona's voice and positioning.

### Step 4: Load Post Type Resources

Navigate to `persona/{persona_name}/{post_type}/` and read ALL files present. These typically include:

| File | Purpose |
|------|---------|
| `linkedin_post_generator_prompt.md` | The core system prompt defining how to write this post type - follow its instructions precisely |
| `linkedin_post_examples.md` | Reference examples showing the style, structure, and quality bar for this post type |
| `hooks.txt` | Proven hook patterns and examples to draw inspiration from |
| `hook_strategy.md` | Deep strategy guide on crafting hooks - psychology, archetypes, formatting rules |
| `twitter_post_examples.md` | Cross-platform examples (reference only, adapt for LinkedIn format) |
| `twitter_post_generator_prompt.md` | Cross-platform prompt (reference only) |

**Read every file in the folder.** Some post types may have more or fewer files - adapt accordingly.

### Step 5: Ask for Topic/Input

Ask the user: **"What topic, idea, or angle do you want this post about?"**

Optionally also ask:
- Any specific lead magnet / resource to promote (for lead_magnets type)
- Any specific story, experience, or data point to include
- Any particular ICP segment to target (reference segments from `icp.json`)

### Step 6: Generate the Post

Create the LinkedIn post by combining:

1. **Persona voice** - Match the brand_voice.json patterns exactly. Use their language, avoid their guardrails.
2. **Audience targeting** - Write to the ICP's psychology, pain points, fears, and aspirations from icp.json.
3. **Post type strategy** - Follow the generator prompt instructions. Use the hook strategy. Reference examples for quality.
4. **Hook engineering** - This is THE most critical element. Spend 80% of effort here. Use hook archetypes from hook_strategy.md, draw patterns from hooks.txt, study examples, and reference high-performing competitor hooks from `competitor_posts/` for proven patterns.
5. **Formatting** - Follow LinkedIn formatting best practices from the strategy files (short lines, white space, specific structure per post type).

**Constraints:**
- Respect word count limits specified in the generator prompt (e.g., lead magnets: max 250 words)
- Never use phrases from the `never_use` guardrails in brand_voice.json
- Always use language patterns from the `always_use` section in brand_voice.json
- Match the CTA style shown in examples (e.g., "Comment X below" for lead magnets)

### Step 7: Save the Post

After the user approves the post (or after generation if they don't request changes), save it to:

```
persona/{persona_name}/generated_posts/{post_type}_{YYYY-MM-DD}_{short_topic}.md
```

Example: `persona/aryan/generated_posts/lead_magnet_2026-03-09_ai-content-engine.md`

The saved file should include:
```markdown
# Post Type: {post_type}
# Persona: {persona_name}
# Date: {YYYY-MM-DD}
# Topic: {brief topic description}

---

{The final approved post content}
```

---

## POST TYPE GUIDELINES

### Lead Magnets
- Goal: Drive comments and connection requests by offering a free high-value resource
- Structure: Hook → Pain agitation → What's included (bullet list) → Social proof → CTA (comment keyword + connect)
- Must include a clear comment-gated CTA (e.g., "Comment 'ARSENAL' below")
- Keep under 250 words
- Follow the 3-system approach from the generator prompt: Style Intelligence, Conversion Intelligence, Audience Intelligence

### Thought Leadership
- Goal: Build authority, shape perspective, earn respect
- Structure varies by template - reference the examples file for 30+ proven templates
- Focus on insight and perspective over self-promotion
- Write like a peer, not a marketer
- Show scars and real experience - vulnerability builds credibility

### Carousels
When the user asks to create a carousel for a post (or says "make a carousel"):
1. Use the `carousel-maker` skill by invoking `/carousel-maker` with the post content
2. The skill generates a branded multi-slide PDF (1080x1350) ready for LinkedIn/Instagram
3. **Default to light theme** unless the user specifies otherwise
4. Save the generated carousel PDF to `persona/{persona_name}/generated_posts/` using the naming convention:
   ```
   {post_type}_carousel_{YYYY-MM-DD}_{short_topic}.pdf
   ```
   Example: `lead_magnet_carousel_2026-03-09_claude-code-replacing-n8n.pdf`

### Image Generation (Visuals, Infographics, Single Images)

When the user asks to create a LinkedIn visual, infographic, or single image for a post:

1. **Read API credentials** from [`keys.md`](keys.md) — use the fal.ai Nano Banana Pro endpoint
2. **Craft a refined prompt** from `/image_gen` folder depending on infographic or single image. **Default to light theme** (light backgrounds, dark text) for infographics unless the user specifies otherwise.
3. **Make the API call:**
   ```bash
   curl -X POST "https://queue.fal.run/fal-ai/nano-banana-pro" \
     -H "Authorization: Key {from keys.md}" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "{refined_prompt}", "aspect_ratio": "{ratio}"}'
   ```
4. **Download the generated image** from the response URL
5. **Save to** `persona/{persona_name}/generated_posts/{post_type}_image_{YYYY-MM-DD}_{short_topic}.png`

**Aspect Ratios for LinkedIn:**
- `1:1` — Square post image (default, works best in feed)
- `16:9` — Landscape/banner (good for article covers)
- `4:5` — Portrait (more feed real estate, higher engagement)
- `9:16` — Story/vertical format

---

## DIRECTORY STRUCTURE

```
Content System/
├── CLAUDE.md                          ← This file (AI operating guide)
├── persona/
│   ├── {persona_name}/
│   │   ├── business_context.json      ← Business model, offerings, positioning
│   │   ├── icp.json                   ← Ideal customer profiles & psychology
│   │   ├── brand_voice.json           ← Voice, tone, language guardrails
│   │   ├── content_strategy.json      ← Content pillars & goals (if exists)
│   │   ├── generated_posts/           ← Where final posts, carousels & images are saved
│   │   │   ├── {post_type}_{YYYY-MM-DD}_{topic}.md       ← Text posts
│   │   │   ├── {post_type}_carousel_{YYYY-MM-DD}_{topic}.pdf  ← Carousel PDFs
│   │   │   ├── {post_type}_image_{YYYY-MM-DD}_{topic}.png    ← Generated images
│   │   ├── competitor_posts/          ← Competitor research data by date
│   │   │   ├── competitor_posts_{MM_DD_YY}.json
│   │   ├── lead_magnets/              ← Lead magnet post resources
│   │   │   ├── linkedin_post_generator_prompt.md
│   │   │   ├── linkedin_post_examples.md
│   │   │   ├── hooks.txt
│   │   │   ├── hook_strategy.md
│   │   │   └── ...
│   │   ├── thought_leadership/        ← Thought leadership post resources
│   │   │   ├── linkedin_post_examples.md
│   │   │   └── ...
│   │   └── {other_post_types}/        ← Future post types follow same pattern
│   └── {other_personas}/              ← Additional personas follow same structure
```

---

## ADDING NEW PERSONAS

To add a new persona, create a folder under `persona/` with:
1. `business_context.json` - Business details, offerings, positioning
2. `icp.json` - Target audience segments and psychology
3. `brand_voice.json` - Communication style, language patterns, guardrails
4. At least one post type subfolder with examples and/or a generator prompt
5. A `generated_posts/` subfolder (can be empty)

---

## ADDING NEW POST TYPES

To add a new post type for a persona, create a subfolder under that persona with:
1. `linkedin_post_examples.md` - At least 3-5 example posts showing the quality bar
2. `linkedin_post_generator_prompt.md` - System prompt with specific instructions for this post type
3. Optional: `hooks.txt`, `hook_strategy.md`, or any other reference files

---

## COMPETITOR RESEARCH

When scraping or analyzing competitor LinkedIn posts, save results inside the persona's `competitor_posts/` folder using:

```
persona/{persona_name}/competitor_posts/competitor_posts_{MM_DD_YY}.json
```

Example: `persona/aryan/competitor_posts/competitor_posts_03_09_26.json`

**Workflow:**
1. Read API credentials from [`keys.md`](keys.md) (Apify endpoint + token)
2. Identify 3+ competitors relevant to the persona's niche (use `business_context.json` for positioning)
3. Scrape their recent LinkedIn posts via the Apify LinkedIn scraper
4. Filter for high-performing posts (500+ likes by default, adjustable)
5. Save the filtered JSON with date-stamped filename
6. Clean up any temporary/raw data files after saving

**Naming convention:** `competitor_posts_{MM}_{DD}_{YY}.json` — always use the date the research was performed.

---

## API KEYS & CREDENTIALS

All API keys and credentials are stored in [`keys.md`](keys.md). Reference that file when making any API calls (e.g., LinkedIn API, OpenAI, Anthropic, or any third-party integrations).

**Never hardcode keys in scripts or prompts.** Always read from `keys.md`.

---

## KEY RULES

1. **Always ask for persona first, then post type.** Never assume.
2. **Read ALL context files before writing.** Never generate a post without loading persona + post type files.
3. **The hook is everything.** 80% of effort goes into the first 1-2 lines.
4. **Match the voice exactly.** The post should be indistinguishable from what the persona would write themselves.
5. **Respect guardrails.** Never use language from the `never_use` lists in brand_voice.json.
6. **Save every final post.** Always save to `generated_posts/` with proper naming and metadata.
7. **Iterate on request.** If the user asks for changes, revise and offer to save the updated version.
8. **One post at a time.** Complete the full workflow for one post before starting another.

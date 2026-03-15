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
| `hook_strategy.md` | Deep strategy guide on crafting hooks (note: the master version lives at root `hook_strategy.md` — always use that one) |
| `twitter_post_examples.md` | Cross-platform examples (reference only, adapt for LinkedIn format) |
| `twitter_post_generator_prompt.md` | Cross-platform prompt (reference only) |

**Read every file in the folder.** Some post types may have more or fewer files - adapt accordingly.

### Step 5: Ask for Topic/Input

Ask the user: **"What topic, idea, or angle do you want this post about?"**

Optionally also ask:
- Any specific lead magnet / resource to promote (for lead_magnets type)
- Any specific story, experience, or data point to include
- Any particular ICP segment to target (reference segments from `icp.json`)

### Step 5b: Guardrail Verification (MANDATORY — Do NOT Skip)

Before generating any copy, explicitly check `brand_voice.json` for guardrails. Different personas use different guardrail structures. Extract and confirm ALL of the following that exist:

| Guardrail Type | Common Keys to Check |
|----------------|---------------------|
| **Banned language** | `never_use`, `never_do`, `positioning_guardrails.never_use` |
| **Required language** | `always_use`, `always_do` |
| **Regulatory/compliance** | `regulatory_guardrails`, `content_disclaimers` |
| **Content rules** | `content_split_rule`, `tone_constraints` |

**Verification process:**
1. **List out** every `never_use` / `never_do` item found — these are hard blockers. If no guardrails exist for this persona, note that explicitly and proceed with caution using general best practices.
2. **List out** every `always_use` / `always_do` item found — these must appear in the final copy.
3. **List out** any regulatory or compliance guardrails — these override all other considerations.
4. **Confirm to the user:** Display a brief guardrail summary (e.g., "Found 9 banned phrases, 7 required patterns, 1 regulatory rule") before proceeding to generation.

**If `brand_voice.json` is missing or has no guardrail sections:** Warn the user — "No guardrails found for this persona. Proceeding without language constraints. Consider adding guardrails to `brand_voice.json`."

### Step 5c: Hook Engineering (MANDATORY — Do NOT Skip)

**The hook is the single most important element of any LinkedIn post.** 80% of effort goes here. You MUST complete this step before writing any post content.

#### 5c.1: Read the Hook Strategy File

**Every single time**, re-read the master hook strategy file at the root directory: **`hook_strategy.md`**

This is the single source of truth for all hook engineering across all personas and post types.

**Never write a hook from memory.** Always consult this file fresh before crafting the opening lines.

#### 5c.2: Strategize Line 1 (The Hook)

The hook is the **first line** of the post — the scroll-stopper. Apply these rules from the strategy doc:

1. **Choose an archetype** — Select from the 10 data/proof archetypes (Contrarian Proof, Confession, Invisible Cost, Quiet Truth, Challenge, Reversal, Prediction, Micro-Lesson, Human Truth, Irony) OR the 8 interpretive archetypes (Inversion, Irony, Comparison, Paradox, Reversal, Cultural Mirror, Human Truth, Friction Truth)
2. **Apply a cognitive lever** — Use one of: Curiosity Gap, Status Risk, Authority Proof, Contradiction, Specificity, or Irony
3. **Compress ruthlessly** — 8-12 words maximum. One short sentence. Cut all fluff.
4. **No marketing language** — Never use "revolutionary," "game-changing," "best-in-class." Write like a peer.
5. **The hook is NOT a summary** — It's a psychological device that creates cognitive dissonance, opens a loop, or threatens status.

#### 5c.3: Strategize Line 2 (The Rehook)

The rehook is the **second line** — it amplifies the hook with speed, scope, urgency, or additional value. It keeps the reader committed after the hook grabbed them.

**Rehook patterns from the strategy doc:**
- Add proof/scale: "0 manual messages. 0 generic messages. 0 hours wasted."
- Add scarcity/exclusivity: "(and I probably shouldn't be giving this away for free)"
- Add contradiction: "Every VP Sales should try it once."
- Add specificity: "In 27 days, our pipeline velocity doubled — without hiring."
- Deepen the curiosity gap: Tease the resolution without giving it away

#### 5c.4: Quality Checklist (Must Pass ALL Before Proceeding)

Run these 6 checks on your hook + rehook. If any fail, rewrite before moving to Step 6:

| # | Check | Pass? |
|---|-------|-------|
| 1 | Does it open a loop (curiosity gap)? | |
| 2 | Would it make a VP stop scrolling? | |
| 3 | Can it be read in one breath? | |
| 4 | Is it emotionally charged or status-threatening? | |
| 5 | Does it avoid all marketing clichés? | |
| 6 | Could it live as a standalone tweet or slide headline? | |

#### 5c.5: Present Hook Options to User

**Before generating the full post**, present **3 hook+rehook combinations** to the user using different archetypes. Format:

```
**Option A** (archetype: [name], lever: [name])
Line 1: [hook]
Line 2: [rehook]

**Option B** (archetype: [name], lever: [name])
Line 1: [hook]
Line 2: [rehook]

**Option C** (archetype: [name], lever: [name])
Line 1: [hook]
Line 2: [rehook]
```

Let the user pick or request variations before proceeding to full post generation.

### Step 6: Generate the Post

Create the LinkedIn post by combining:

1. **Persona voice** - Match the brand_voice.json patterns exactly. Use their language, avoid their guardrails.
2. **Audience targeting** - Write to the ICP's psychology, pain points, fears, and aspirations from icp.json.
3. **Post type strategy** - Follow the generator prompt instructions. Reference examples for quality.
4. **Hook + Rehook (from Step 5c)** - Use the user's chosen hook+rehook from Step 5c as the opening two lines. Do NOT modify them unless the user asks. The hook engineering is already done — honor it.
5. **Formatting** - Follow LinkedIn formatting best practices from the strategy files (short lines, white space, specific structure per post type). Use line breaks every 1-2 sentences. Think "Slack, not essay."

**Constraints:**
- Respect word count limits specified in the generator prompt (e.g., lead magnets: max 250 words)
- Never use phrases from the `never_use` guardrails in brand_voice.json
- Always use language patterns from the `always_use` section in brand_voice.json
- Match the CTA style shown in examples (e.g., "Comment X below" for lead magnets)

### Step 6b: Post-Generation Guardrail Scan (MANDATORY)

After drafting the post, scan it against the guardrails extracted in Step 5b:

1. **Banned language check** — Search the draft for every `never_use` / `never_do` phrase. If ANY match is found, rewrite that section before showing the post to the user.
2. **Required language check** — Verify the draft includes patterns from `always_use` / `always_do`. Flag any missing required elements.
3. **Regulatory check** — If regulatory guardrails exist, verify compliance (e.g., no outcome guarantees, no medical advice, educational disclaimers where needed).
4. **Report to user** — After the post, include a brief guardrail compliance note:
   - "Guardrail check: PASSED (0 violations, 7/7 required patterns used)"
   - OR "Guardrail check: 1 violation fixed (removed 'game-changing'), 6/7 required patterns used (missing: benchmark comparisons)"

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
1. Use the `carousel-maker` skill by invoking `skill/carousel-maker` with the post content
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
├── commands/                          ← Slash command prompts
│   ├── ideas.md                       ← /idea command - weekly AI GTM research
│   └── {other_commands}.md            ← Future commands follow same pattern
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
│   │   ├── ideas/                     ← Weekly idea research output
│   │   │   ├── ai-gtm-ideas-{YYYY-MM-DD}.md
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

## COMMANDS

### `/idea` — Weekly AI GTM Idea Research

When the user runs `/idea`, follow this workflow:

1. **Identify Persona** — Ask: **"Which persona are you researching ideas for?"** List available personas from `persona/`.
2. **Load Command Prompt** — Read `commands/ideas.md` for the full research instructions, search queries, and formatting rules.
3. **Execute Research** — Follow the steps in `commands/ideas.md`:
   - Search LinkedIn, Twitter/X, and blogs for recent AI GTM content (last 7 days)
   - Extract the **10 most interesting, actionable, or provocative ideas**
   - Write a 200-word brief per idea (What / Why it matters / How to apply + Source)
4. **Save Output** — Save the ideas file to:
   ```
   persona/{persona_name}/ideas/ai-gtm-ideas-{YYYY-MM-DD}.md
   ```
   Example: `persona/kanchan/ideas/ai-gtm-ideas-2026-03-10.md`
5. **Present Summary** — Show the user a quick summary of all 10 idea titles so they can pick ones to turn into posts.

**Formatting:** Follow the exact template and rules defined in `commands/ideas.md` (punchy titles, What/Why/How structure, source URLs).

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

## POST SELF COMMENTS

After every post is saved, **automatically generate 4 self-comments** and append them below the post content in the saved file. These comments are designed to be posted by the persona as replies to their own post to boost engagement and algorithmic reach.

### The 4 Comment Types (generate all 4, every time):

**1. Personal Angle**
Share a personal insight, experience, or observation related to the post topic.
Use `personal_story.json` (if available) to pull authentic details.
Write as if reflecting on your own clinical or life experience.

**2. Trend / Thought**
Comment on a broader trend, industry shift, or forward-looking thought connected to the post.
Position the persona as someone who sees where things are heading.

**3. Science / Data**
Add a specific scientific fact, research finding, or clinical data point that reinforces the post's message.
Cite the source where possible. Make it feel like bonus value the reader didn't expect.

**4. Post Value Amplification**
Expand on one specific point from the post that deserves more attention.
Frame it as “the part most people will skip over but shouldn't” — pulls the reader back in.

### Comment Rules:

1. Each comment is **2–3 short lines**, well formatted for LinkedIn (line breaks between lines, not a paragraph block)
2. No emojis unless they fit naturally
3. Never start with “Great post”, “Well said”, “Totally agree”, or any self-praise
4. Do NOT repeat the post in different words — each comment must add NEW value
5. Tone: curious, thoughtful, confident — not salesy
6. Write as the persona, in first person, matching their `brand_voice.json`

### Saved File Format:

After the post content in the saved `.md` file, append:

```markdown

---

## Self Comments

### 1. Personal Angle
{comment text}

### 2. Trend / Thought
{comment text}

### 3. Science / Data
{comment text}

### 4. Post Value Amplification
{comment text}
```

## KEY RULES

1. **Always ask for persona first, then post type.** Never assume.
2. **Read ALL context files before writing.** Never generate a post without loading persona + post type files.
3. **The hook is everything.** 80% of effort goes into lines 1-2 (hook + rehook). Always re-read the root-level `hook_strategy.md`, present 3 hook+rehook options to the user (Step 5c), and only then generate the full post. Never write hooks from memory.
4. **Match the voice exactly.** The post should be indistinguishable from what the persona would write themselves.
5. **Verify guardrails before and after generation.** Always run Step 5b (pre-generation check) and Step 6b (post-generation scan). Never skip guardrail verification — if `brand_voice.json` has no guardrails, warn the user.
6. **Save every final post.** Always save to `generated_posts/` with proper naming and metadata.
7. **Iterate on request.** If the user asks for changes, revise and offer to save the updated version.
8. **One post at a time.** Complete the full workflow for one post before starting another.

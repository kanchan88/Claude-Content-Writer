---
name: carousel-maker
description: >
  Create professional, high-performing LinkedIn carousel PDFs from URLs or pasted text.
  Use this skill whenever the user wants to create a carousel, slide deck for social media,
  turn an article into slides, make LinkedIn carousel posts, create Instagram carousels,
  or convert any written content into a swipeable multi-slide PDF. Also trigger when the
  user mentions "carousel," "slides for LinkedIn," "slide PDF," "social media slides,"
  or wants to repurpose articles/newsletters into visual slide formats.
---

# Carousel Maker

Create professional, scroll-stopping LinkedIn carousel PDFs. Outputs richly designed HTML slides exported as a multi-page PDF.

---

## CRITICAL: No External Dependencies at Render Time

Claude's container has restricted network access. DO NOT use:
- Tailwind CSS CDN or any CDN-hosted CSS framework
- Google Fonts `<link>` tags or any externally loaded fonts at render time
- Any `<script>` or `<link>` tags that fetch from external URLs

ALL styling MUST be pure inline CSS or in a single `<style>` block within the HTML file.
Fonts are downloaded via npm at build time and base64-embedded in the HTML.

**Images from the web ARE allowed at build time** — fetch them during Step 3, base64-encode them, and embed them inline.

---

## Design Philosophy: Clean, Warm, Professional

Every carousel MUST follow these design principles inspired by top-performing LinkedIn carousels:

1. **Warm & Professional** — Use a warm cream/beige palette. NO harsh dark themes, no neon colors, no heavy gradients. Think editorial magazine, not tech dashboard.
2. **Breathe** — Generous whitespace. Content should never feel cramped. Let every element have room.
3. **No Emojis** — Use clean typography and layout hierarchy instead of emoji bullets. Professional icons (SVG) only when needed. Zero emojis in headlines or body text.
4. **Card-Based Layouts** — White rounded cards on warm backgrounds with subtle shadows create depth and structure.
5. **Consistent Author Presence** — The author's headshot and identity should appear on every slide in a consistent position. This builds personal brand recognition.
6. **Bold Typography** — Large, confident headlines. Mix of weights (bold headlines, regular body). Key phrases highlighted with yellow/warm highlight boxes.
7. **Predictable Structure** — Each slide variation should have a recognizable, repeating layout. Consistency builds trust and readability.
8. **Minimal Decoration** — No decorative circles, blobs, gradients, or accent bars. The content and typography ARE the design. Subtle background texture (grid pattern) is acceptable.
9. **Brand Watermark** — A subtle brand name or logo in the corner of content slides reinforces identity.

---

## Step 0: Determine the Template Variation

Based on the content type, select the most appropriate template variation. There are 4 variations — pick the one that best fits the user's content:

| Variation | Best for | Content pattern |
|---|---|---|
| **A — Tool Showcase** | "X best tools for Y", "X resources", "X APIs" | List of products/tools/resources with logos & descriptions |
| **B — Myth Buster** | "X lies about Y", "X myths debunked", "Stop doing X" | Contrarian takes with reality checks and tips |
| **C — Step-by-Step** | "How to X in Y steps", "The complete guide to Z" | Sequential process or framework |
| **D — Insights & Lessons** | "X lessons learned", "X tips for Y", "X things I wish I knew" | Collection of wisdom/insights/tips |

If unclear, ask the user. If the content doesn't fit any variation perfectly, use **Variation D** (most flexible).

**Target: 12-18 slides per carousel.** This is the sweet spot for LinkedIn engagement. Never fewer than 12, never more than 20.

---

## Step 1: Get the Content

Accept input in one of these forms:
- **URL**: Fetch the article using `web_fetch`. Extract the main body text.
- **Pasted text**: Use the text directly.
- **File**: Read from an uploaded file.

If given a URL, fetch it and extract the article body. Ignore nav, footer, sidebar, and ad content.

---

## Step 2: Generate Slide Copy

Analyze the content and break it into **12–18 slides** using the selected template variation's structure.

### Content rules (ALL variations)

- Each slide conveys ONE idea only
- Use concrete numbers, specific examples, and strong verbs
- Strip jargon — write at a conversational, professional level
- Headlines: max 8-10 words, bold and punchy
- Body text: concise, 2-4 short sentences max per section
- **Highlight key phrases** using yellow highlight boxes (NOT colored text)
- **Bold key words** using `<strong>` tags
- **NO emojis anywhere** — not in headlines, not in body, not in labels
- Use "The reality:", "Try this instead:", "Key insight:" style labels with highlight boxes

### Slide structures by variation

**Variation A — Tool Showcase:**
- Slide 1: Cover — giant number + title + mini icon grid + author info
- Slide 2: Overview — all items as icon/logo grid or "keep scrolling" teaser
- Slides 3–N: Tool slides — logo in card + 1-2 line description or screenshot mockup
- Optional: Category divider slides between groups
- Last slide: CTA — follow prompt with enlarged author section

**Variation B — Myth Buster:**
- Slide 1: Cover — provocative title + subtitle + visual metaphor
- Slides 2–N: Myth slides — bold claim (the lie) as headline + "The reality:" section + "Try this instead:" tip
- Last slide: CTA — closing thought + follow prompt with author

**Variation C — Step-by-Step:**
- Slide 1: Cover — title with step count + subtitle
- Slide 2: Context/problem slide — why this matters
- Slides 3–N: Step slides — step number + title + explanation
- Slide N+1: Recap/summary slide
- Last slide: CTA — follow prompt

**Variation D — Insights & Lessons:**
- Slide 1: Cover — title with number + subtitle
- Slides 2–N: Insight slides — number + insight headline + explanation
- Slide N+1: Key takeaway / summary slide
- Last slide: CTA — follow prompt

---

## Step 3: Prepare Assets

### Font

Default font is **Inter**. Download via npm and base64-embed:

```bash
npm install --prefix /home/claude/fonts @fontsource/inter 2>/dev/null
```

Font files at:
```
/home/claude/fonts/node_modules/@fontsource/inter/files/inter-latin-400-normal.woff2
/home/claude/fonts/node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2
```

**Pattern for any font:** `@fontsource/{font-name-kebab-case}` -> files at `{font-name}-latin-{weight}-normal.woff2`

Base64-encode in your Python build script:
```python
import base64

FONT_FAMILY = "Inter"
FONT_PKG = "inter"

font_400_path = f"/home/claude/fonts/node_modules/@fontsource/{FONT_PKG}/files/{FONT_PKG}-latin-400-normal.woff2"
font_700_path = f"/home/claude/fonts/node_modules/@fontsource/{FONT_PKG}/files/{FONT_PKG}-latin-700-normal.woff2"

with open(font_400_path, "rb") as f:
    font_400_b64 = base64.b64encode(f.read()).decode()
with open(font_700_path, "rb") as f:
    font_700_b64 = base64.b64encode(f.read()).decode()
```

**If npm install fails**, fall back to system fonts:
```
'Segoe UI', 'Helvetica Neue', Arial, sans-serif
```

### Headshot

Check for a headshot image:
```
/mnt/skills/user/carousel-maker/references/headshot.jpg
```
If found, base64-encode it. If not found, check for `headshot.png`.

**If no headshot exists**, use a warm brown circle with the author's initials as placeholder.

### Topic-relevant images (optional)

For Tool Showcase (Variation A), try to fetch tool logos or screenshots via `web_fetch` at build time. Base64-encode and embed. If fetching fails, use text-only card layouts. Never leave a slide empty because an image failed.

---

## Step 4: Build HTML

**IMPORTANT: Use a Python script to build the HTML.** Do NOT try to write the full HTML by hand.

The script should:
1. Load base64 assets (fonts, headshot, any fetched images)
2. Define helper functions for reusable components (footer, cards, highlight boxes, author pill, dot navigation, etc.)
3. Generate each slide using the selected variation's patterns
4. Assemble into a single HTML file

Read `references/templates.md` for the complete design system, color palette, component library, and full slide examples for each variation.

### Page setup

- Each slide: `<div class="slide">` with explicit width/height
- Default dimensions: **1080x1350px** (4:5 ratio for LinkedIn/Instagram)
- Other options: 1080x1080px (1:1), 1080x1920px (9:16 Stories)

### Required HTML skeleton

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { margin: 0; padding: 0; }
    @media print {
      .slide { page-break-after: always; }
      .slide:last-child { page-break-after: avoid; }
      @page { size: 1080px 1350px; margin: 0; }
    }
  </style>
</head>
<body>
  <!-- slides here -->
</body>
</html>
```

### Key layout principles

- **Background**: Warm cream `#FBF8F4` with optional subtle grid pattern. Alternate with `#F5F0EA` for visual rhythm.
- **Content padding**: 80px sides, generous top/bottom margins
- **Cards**: White `#FFFFFF` background, `border-radius: 16px`, `box-shadow: 0 2px 12px rgba(0,0,0,0.06)`, `border: 1px solid rgba(0,0,0,0.04)`
- **No accent bars, no decorative blobs, no colored borders** — clean and minimal
- **Highlight boxes**: Yellow `#F5D76E` background behind key labels, `padding: 4px 12px`, `display: inline`
- **Author headshot**: 56-64px circle on content slides, 100-120px on cover/CTA
- **Navigation dots**: Bottom center, muted colors
- **Brand name**: Small, bottom-right corner of content slides

### Design rules

- ALL colors as hex values (or rgba for shadows)
- Primary accent: warm brown `#8B6F47` — used sparingly for category labels and key accents
- Highlight: `#F5D76E` yellow for label boxes
- **NEVER use emojis** — not even in labels or bullets
- **NEVER create dark/black background slides** — keep everything warm and light
- No gradient backgrounds on slides (subtle on cover/CTA only if needed)
- Use `overflow: hidden` on every slide div
- Cards and containers use 16px border-radius
- Text hierarchy through size and weight, not color variety
- Body text in dark gray `#4A4A4A`, not pure black

---

## Step 5: Convert to PDF

**The HTML file must be saved before converting.**

```bash
pip install playwright --break-system-packages -q 2>/dev/null
playwright install chromium 2>/dev/null
python /mnt/skills/user/carousel-maker/scripts/html_to_pdf.py /home/claude/carousel.html /home/claude/carousel.pdf --width 1080 --height 1350
```

**If Playwright fails**, use the WeasyPrint fallback:

```bash
pip install weasyprint --break-system-packages -q 2>/dev/null
python /mnt/skills/user/carousel-maker/scripts/html_to_pdf_fallback.py /home/claude/carousel.html /home/claude/carousel.pdf --width 1080 --height 1350
```

**If both fail**, provide the HTML file and instruct the user to print-to-PDF from Chrome (Paper: Custom 1080x1350, Margins: None, Background graphics: On).

---

## Step 6: Deliver

Copy the final PDF and HTML file to `/mnt/user-data/outputs/` and present to the user.

---

## Customization

Users can personalize this skill. See **CUSTOMIZE.md** for details. Key settings:

| What | Where to edit |
|---|---|
| Accent color | `references/templates.md` |
| Font | `references/templates.md` |
| Author name & handle | `references/templates.md` |
| Headshot | Drop `headshot.jpg` or `headshot.png` into `references/` |
| Brand name | `references/templates.md` |
| Slide dimensions | Request a different ratio when prompting |

---

## Important Reminders

- NEVER use external CDNs or scripts at render time
- Use a Python build script — do not hand-write the full HTML
- Generate navigation dots dynamically based on actual slide count
- **NO emojis anywhere** — this is critical for the professional look
- **NO dark themes** — warm cream/beige palette only
- **NO decorative blobs, circles, or accent bars**
- Cards with subtle shadows are the primary visual structure
- Yellow highlight boxes for labels, not colored text
- Author headshot on every slide for personal brand consistency
- Target 12-18 slides per carousel
- If headshot doesn't exist, create initials avatar in warm brown
- Mix slide types within the chosen variation for visual interest
- Keep consistent padding and spacing throughout

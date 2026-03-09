---
name: carousel-maker
description: >
  Create stunning, scroll-stopping LinkedIn/Instagram carousel PDFs from URLs or pasted text.
  Use this skill whenever the user wants to create a carousel, slide deck for social media,
  turn an article into slides, make LinkedIn carousel posts, create Instagram carousels,
  or convert any written content into a swipeable multi-slide PDF. Also trigger when the
  user mentions "carousel," "slides for LinkedIn," "slide PDF," "social media slides,"
  or wants to repurpose articles/newsletters into visual slide formats.
---

# Carousel Maker

Create stunning, branded carousel PDFs that stop the scroll. Outputs richly designed HTML slides exported as a multi-page PDF ready for LinkedIn or Instagram.

---

## CRITICAL: No External Dependencies at Render Time

Claude's container has restricted network access. DO NOT use:
- Tailwind CSS CDN or any CDN-hosted CSS framework
- Google Fonts `<link>` tags or any externally loaded fonts at render time
- Any `<script>` or `<link>` tags that fetch from external URLs

ALL styling MUST be pure inline CSS or in a single `<style>` block within the HTML file.
Fonts are downloaded via npm at build time and base64-embedded in the HTML — no network needed at render time.

**Images from the web ARE allowed at build time** — fetch them during Step 3, base64-encode them, and embed them inline. The restriction is only on render-time network access.

---

## Design Philosophy: Bold, Human, Visual

Every carousel MUST follow these principles:

1. **Stop the Scroll** — The hook slide must be visually dramatic. Use bold gradient backgrounds, large typography, and accent colors. NEVER produce a plain white slide with black text.
2. **Show, Don't Tell** — When content discusses data, examples, workflows, or comparisons, visualize them. Use stat callouts, comparison layouts, icon grids, and visual hierarchy — not just bullet points.
3. **Human Touch** — The author's headshot and brand identity should be prominent. The carousel should feel like it came from a real person, not a template generator.
4. **Visual Variety** — Every slide should NOT look the same. Mix slide types: hook, stat highlight, icon bullets, pull quote, image + text, comparison, and CTA. This keeps the reader swiping.
5. **Dense & Punchy** — Reduce whitespace. Fill the slide with purposeful content and design elements. Use accent bars, decorative shapes, and background elements to make slides feel rich.
6. **Emojis & Icons** — Use relevant emojis in headlines and bullets to add personality and break up text. Use SVG icons for visual flair in bullets and section labels.

---

## Step 0: Ask the User — Light or Dark?

Before generating anything, **ask the user which theme they want**:

> "Would you like the **light** or **dark** version of this carousel?"

- If the user already specified a preference in their message, skip the question.
- Default to **dark** if the user says "surprise me" or has no preference.

---

## Step 1: Get the Content

Accept input in one of these forms:
- **URL**: Fetch the article using `web_fetch`. Extract the main body text.
- **Pasted text**: Use the text directly.
- **File**: Read from an uploaded file.

If given a URL, fetch it and extract the article body. Ignore nav, footer, sidebar, and ad content.

---

## Step 2: Generate Slide Copy

Analyze the article and break it into **8–12 slides**. Follow these constraints:

### Slide types (use a MIX — never just headline + bullets for every slide)

| Type | When to use | Visual treatment |
|---|---|---|
| **Hook** (Slide 1) | Always first | Gradient background, giant bold title, emoji, subtitle. Must create curiosity or make a bold claim. |
| **Content + Icons** | Core teaching points | Headline + 2-3 bullets with emoji/icon prefixes |
| **Stat Highlight** | Key numbers, data, percentages | Giant number (80-120px) in accent color + context line below |
| **Pull Quote** | Strong opinions, memorable lines | Large italic text with accent left-border bar, attribution below |
| **Image + Text** | Visual proof, examples, screenshots | Left/right split or full-width image with text overlay |
| **Icon Grid** | Lists of 3-4 items, features, steps | 2x2 or 1x3 grid with emoji/icon + short label + description |
| **Comparison** | Before/after, do/don't, old/new | Two-column layout with contrasting colors (red vs green accents) |
| **CTA** (Last slide) | Always last | Bold closing headline, accent CTA button, author headshot enlarged |

### Content rules

- Each slide conveys ONE idea only
- Use concrete numbers, specific examples, and strong verbs
- Bullets should be parallel in structure
- Strip jargon — write at a 6th-grade reading level where possible
- The hook slide must create curiosity or make a bold claim
- **Add relevant emojis** to headlines and bullet points (1-2 per slide, not excessive)
- **Bold key phrases** within bullets using `<strong>` or `<span style="font-weight:700">`
- Use varied font sizes for visual hierarchy within a single slide

### Slide structure

- **Slide 1 (Hook):** Attention-grabbing title (max 10 words) with emoji + subtitle (max 15 words). MUST have gradient or bold colored background.
- **Slides 2–N (Content):** Mix of slide types above. Headline (max 8 words) + visual content varies by type.
- **Final Slide (CTA):** Call to action with clear next step, enlarged author photo, personal message.

---

## Step 3: Prepare Assets

### Font

The skill embeds real fonts via npm's `@fontsource` packages (registry.npmjs.org is on the allowed domains list). The default is **Inter**. Users can change the font in `references/templates.md` — see CUSTOMIZE.md for details.

**How to download and embed any font:**

```bash
# Install the font package (Inter is the default — swap the name for any Google Font)
npm install --prefix /home/claude/fonts @fontsource/inter 2>/dev/null

# The files you need are at:
# /home/claude/fonts/node_modules/@fontsource/inter/files/inter-latin-400-normal.woff2
# /home/claude/fonts/node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2
```

**Pattern for any font:** `@fontsource/{font-name-kebab-case}` -> files at `{font-name}-latin-{weight}-normal.woff2`

Examples:
- `@fontsource/inter` -> `inter-latin-400-normal.woff2`
- `@fontsource/playfair-display` -> `playfair-display-latin-400-normal.woff2`
- `@fontsource/space-grotesk` -> `space-grotesk-latin-400-normal.woff2`

**In your Python build script**, base64-encode the woff2 files and embed as `@font-face` rules:

```python
import base64

FONT_FAMILY = "Inter"  # must match the actual font name (title case)
FONT_PKG = "inter"     # the npm package slug (kebab-case)

font_400_path = f"/home/claude/fonts/node_modules/@fontsource/{FONT_PKG}/files/{FONT_PKG}-latin-400-normal.woff2"
font_700_path = f"/home/claude/fonts/node_modules/@fontsource/{FONT_PKG}/files/{FONT_PKG}-latin-700-normal.woff2"

with open(font_400_path, "rb") as f:
    font_400_b64 = base64.b64encode(f.read()).decode()
with open(font_700_path, "rb") as f:
    font_700_b64 = base64.b64encode(f.read()).decode()
```

Then include in the HTML `<style>` block:

```html
@font-face {
  font-family: '{FONT_FAMILY}';
  font-weight: 400;
  src: url(data:font/woff2;base64,{font_400_b64}) format('woff2');
}
@font-face {
  font-family: '{FONT_FAMILY}';
  font-weight: 700;
  src: url(data:font/woff2;base64,{font_700_b64}) format('woff2');
}
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
If found, base64-encode it for embedding:
```bash
HEADSHOT_B64=$(base64 -w 0 /mnt/skills/user/carousel-maker/references/headshot.jpg 2>/dev/null)
```
If not found, check for headshot.png as fallback:
```bash
HEADSHOT_B64=$(base64 -w 0 /mnt/skills/user/carousel-maker/references/headshot.png 2>/dev/null)
```
**The headshot is critical for the human element.** If no headshot file exists, use a colored circle with the author's initials as a placeholder — never just omit it silently.

### Background image (optional)

Check for a background/watermark image:
```
/mnt/skills/user/carousel-maker/references/background.png
```
If found, base64-encode it for embedding:
```bash
BG_B64=$(base64 -w 0 /mnt/skills/user/carousel-maker/references/background.png 2>/dev/null)
```
This can be any image — a logo, a photo, an illustration, an icon, an abstract shape. It displays as a large, centered, low-opacity watermark on every slide. If not found, skip — slides will have decorative elements instead.

### Topic-relevant images (NEW — Visual Proof)

**For visual proof and engagement, fetch 1-3 relevant images from the web at build time:**

Use `web_fetch` to download images relevant to the carousel topic. For example:
- If the carousel is about AI tools, fetch screenshots or logos of the tools mentioned
- If it's about productivity, fetch relevant stock imagery or icons
- If it discusses a product/service, fetch its actual screenshots

**Process:**
1. Identify 1-3 key visuals that would enhance the carousel
2. Fetch them via `web_fetch` at build time
3. Base64-encode and embed them inline
4. Use them in Image + Text slides or as slide backgrounds

If image fetching fails, gracefully fall back to emoji/icon-based visual treatments. Never leave a slide empty because an image failed to load.

---

## Step 4: Build HTML

**IMPORTANT: Use a Python script to build the HTML.** Do NOT try to write the full HTML by hand. The script should:
1. Load the base64 assets (headshot, background image, fetched images)
2. Define helper functions for reusable components (footer, page number, nav dots, background image, accent bar, stat callout, icon grid, etc.)
3. Generate each slide by calling those functions — using VARIED slide types
4. Assemble into a single HTML file

Read `references/templates.md` for the **Light** and **Dark** template designs, color systems, and component patterns.

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

### Slide layout structure

Every slide has these layers (back to front):

1. **Background** — gradient or solid color on the slide div (NEVER plain white — even light theme uses off-white with subtle gradients)
2. **Decorative elements** — accent bar (left edge), geometric shapes, background watermark image
3. **Page number** — top-left corner, large bold accent number
4. **Content area** — padded region for slide-type-specific content
5. **Footer bar** — anchored to bottom with headshot, name, dots, and nav chevron

### Decorative accent bar (EVERY slide)

A bold vertical accent bar on the left edge adds brand color and visual interest:
```html
<div style="position: absolute; top: 0; left: 0; width: 8px; height: 100%; background: linear-gradient(180deg, {ACCENT} 0%, {ACCENT_LT} 100%);"></div>
```

### Page number (top-left)

```html
<div style="position: absolute; top: 48px; left: 80px; font-size: 42px; font-weight: 800; color: {ACCENT};">03</div>
```
- Show only the number (e.g., `03`), NOT `3 / 10`
- Zero-padded, 42px, font-weight 800, accent color

### Background image (centered watermark)

If `background.png` exists, display as:
```html
<img src="data:image/png;base64,..." style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: {BG_SIZE}px; height: {BG_SIZE}px; opacity: 0.08; object-fit: contain; pointer-events: none;" />
```

**Background image scale** — default `1000px`. The user can request a different scale:
- `600px` — subtle small watermark
- `800px` — medium
- `1000px` — large (default), fills most of the slide
- `1200px` — bleeds off edges for an immersive feel

### Decorative geometric shapes (optional, adds visual richness)

Add subtle geometric accent shapes to some slides for visual interest:
```html
<!-- Top-right accent circle -->
<div style="position: absolute; top: -60px; right: -60px; width: 200px; height: 200px; border-radius: 50%; background: {ACCENT}; opacity: 0.06;"></div>
<!-- Bottom-left accent circle -->
<div style="position: absolute; bottom: 180px; left: -40px; width: 150px; height: 150px; border-radius: 50%; border: 3px solid {ACCENT}; opacity: 0.1;"></div>
```

### Content area

- **Padding:** 80px left (after accent bar), 80px right, 120px top (clears page number), bottom stops 170px from slide bottom (clears footer)
- **Category labels:** 20px, font-weight 700, uppercase, accent color, letter-spacing 3px, with emoji prefix
- **Headlines:** 52-64px, font-weight 700-800, with accent-colored key words
- **Body/bullets:** 30px, line-height 1.5
- **Emoji bullet layout:** Use a table so spacing is reliable in WeasyPrint:
```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="vertical-align: top; padding: 0 16px 24px 0; width: 44px;">
      <span style="font-size: 30px; line-height: 1.5;">🎯</span>
    </td>
    <td style="vertical-align: top; padding: 0 0 24px 0;">
      <p style="font-size: 30px; color: {BODY}; line-height: 1.5; margin: 0;"><strong style="color: {PRIMARY};">Key phrase</strong> — rest of the bullet text here</p>
    </td>
  </tr>
  <!-- one tr per bullet -->
</table>
```

### Stat highlight component

For slides featuring key numbers/data:
```html
<div style="text-align: center; margin: 40px 0;">
  <p style="font-size: 110px; font-weight: 800; color: {ACCENT}; line-height: 1; margin: 0;">73%</p>
  <p style="font-size: 28px; color: {MUTED}; margin: 16px 0 0 0;">of marketers say content repurposing<br>is their top growth strategy</p>
</div>
```

### Pull quote component

For memorable quotes or strong statements:
```html
<div style="border-left: 6px solid {ACCENT}; padding: 0 0 0 32px; margin: 40px 0;">
  <p style="font-size: 36px; font-style: italic; color: {PRIMARY}; line-height: 1.4; margin: 0;">"The best content doesn't just inform — it transforms how people think."</p>
  <p style="font-size: 22px; color: {MUTED}; margin: 16px 0 0 0;">— Source attribution</p>
</div>
```

### Icon grid component

For lists of features, steps, or items (2x2 layout):
```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="width: 50%; vertical-align: top; padding: 0 16px 32px 0;">
      <div style="background: {CARD_BG}; border-radius: 16px; padding: 28px; border: 1px solid {CARD_BORDER};">
        <p style="font-size: 36px; margin: 0 0 12px 0;">🚀</p>
        <p style="font-size: 24px; font-weight: 700; color: {PRIMARY}; margin: 0 0 8px 0;">Speed</p>
        <p style="font-size: 20px; color: {BODY}; line-height: 1.4; margin: 0;">Create in minutes, not hours</p>
      </div>
    </td>
    <td style="width: 50%; vertical-align: top; padding: 0 0 32px 16px;">
      <div style="background: {CARD_BG}; border-radius: 16px; padding: 28px; border: 1px solid {CARD_BORDER};">
        <p style="font-size: 36px; margin: 0 0 12px 0;">🎨</p>
        <p style="font-size: 24px; font-weight: 700; color: {PRIMARY}; margin: 0 0 8px 0;">Design</p>
        <p style="font-size: 20px; color: {BODY}; line-height: 1.4; margin: 0;">Professional without the effort</p>
      </div>
    </td>
  </tr>
</table>
```

### Comparison component (do/don't, before/after)

```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="width: 48%; vertical-align: top; padding-right: 16px;">
      <div style="background: rgba(239,68,68,0.08); border-radius: 16px; padding: 28px; border-left: 4px solid #ef4444;">
        <p style="font-size: 24px; font-weight: 700; color: #ef4444; margin: 0 0 16px 0;">❌ Don't</p>
        <p style="font-size: 22px; color: {BODY}; line-height: 1.5; margin: 0;">Plain text with no visual design</p>
      </div>
    </td>
    <td style="width: 4%;"></td>
    <td style="width: 48%; vertical-align: top; padding-left: 16px;">
      <div style="background: rgba(16,185,129,0.08); border-radius: 16px; padding: 28px; border-left: 4px solid #10b981;">
        <p style="font-size: 24px; font-weight: 700; color: #10b981; margin: 0 0 16px 0;">✅ Do</p>
        <p style="font-size: 22px; color: {BODY}; line-height: 1.5; margin: 0;">Bold design that stops the scroll</p>
      </div>
    </td>
  </tr>
</table>
```

### Footer bar (EVERY slide)

160px tall, absolutely positioned at bottom. Three sections in a flex row:

**Left — Headshot + Identity:**
```html
<div style="display: flex; align-items: center; gap: 20px; white-space: nowrap; flex-shrink: 0;">
  <img src="data:image/png;base64,..." width="64" height="64"
       style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover; display: block; flex-shrink: 0; border: 2px solid {ACCENT};" />
  <div style="flex-shrink: 0;">
    <p style="font-size: 22px; font-weight: 600; color: {NAME_COLOR}; margin: 0;">Author Name</p>
    <p style="font-size: 17px; color: {HANDLE_COLOR}; margin: 0;">@handle</p>
  </div>
</div>
```
Note: headshot has an accent-colored border ring for brand consistency.

**If no headshot file exists**, use an initials avatar:
```html
<div style="width: 64px; height: 64px; border-radius: 50%; background: {ACCENT}; display: flex; align-items: center; justify-content: center; flex-shrink: 0; border: 2px solid {ACCENT_LT};">
  <span style="font-size: 24px; font-weight: 700; color: #ffffff;">KB</span>
</div>
```

**Center — Navigation dots:**
Use an HTML `<table>` for reliable dot spacing:
```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
  <tr>
    <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; background: {ACCENT};"></div></td>
    <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; border: 2px solid {DOT_BORDER};"></div></td>
    <!-- one td per slide, filled = current -->
  </tr>
</table>
```

**Right — Directional chevron:**
SVG chevron arrow pointing right. Show on all slides except the last (CTA) slide.
```html
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="M9 6L15 12L9 18" stroke="{ACCENT}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```
On the last slide, render an empty `<div style="width: 24px;">` to maintain layout spacing.

### CTA slide — enlarged author section

The final slide should feature a larger author presence:
```html
<div style="display: flex; flex-direction: column; align-items: center; margin-top: 32px;">
  <img src="data:image/png;base64,..." width="120" height="120"
       style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 4px solid {ACCENT}; margin-bottom: 20px;" />
  <p style="font-size: 28px; font-weight: 700; color: {PRIMARY}; margin: 0;">Kanchan Bhatta</p>
  <p style="font-size: 22px; color: {MUTED}; margin: 8px 0 0 0;">@growthbykanchan</p>
</div>
```

### Design rules

- ALL colors as hex values (or rgba for transparent overlays)
- Accent color: teal (`#0d9488` primary, `#14b8a6` lighter) — used boldly, not sparingly
- **NEVER create plain white or plain solid-color slides** — always add gradients, accent bars, or decorative elements
- Create visual interest through varied slide types, decorative elements, and accent color usage
- Alternate background colors between slides for visual rhythm
- Use `overflow: hidden` on every slide div to clip background elements
- **Bold key words** in accent color within headlines and bullets
- **Use emojis** as bullet prefixes, section labels, and headline accents (1-2 per slide)
- Headshot border should match accent color
- Cards and containers use subtle rounded corners (12-16px border-radius)

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

Users can personalize this skill for their own brand. See **CUSTOMIZE.md** in the skill root for a complete guide. Key settings:

| What | Where to edit |
|---|---|
| Accent color | `references/templates.md` — swap the teal hex values |
| Font | `references/templates.md` — update Font family, Font npm package, and Font file slug |
| Author name & handle | `references/templates.md` — replace in branding defaults |
| Headshot | Drop a `headshot.jpg` or `headshot.png` into `references/` |
| Background image | Drop a `background.png` into `references/` |
| Background scale | Request a size when making a carousel, or edit default in templates.md |
| Slide dimensions | Request a different ratio, or edit defaults in this file |

---

## Important Reminders

- NEVER use external CDNs or scripts at render time (fonts are pre-embedded via npm + base64)
- Use a Python build script — do not hand-write the full HTML
- Leave 170px at the bottom of the content area to clear the 160px footer
- 80px side padding on all content (after the 8px accent bar)
- Generate navigation dots dynamically based on actual slide count
- The hook slide is the most important — make it visually STUNNING with gradients and bold typography
- **Mix slide types** — never use the same layout for every content slide
- **Always include emojis** in bullets and headlines for personality
- **Bold key phrases** in accent color throughout
- **Accent bar on every slide** for consistent brand identity
- If the headshot file doesn't exist, ALWAYS create an initials avatar — never leave the footer without a face/icon
- Alternate background colors between slides for visual rhythm
- Fetch 1-3 topic-relevant images when possible to add visual proof

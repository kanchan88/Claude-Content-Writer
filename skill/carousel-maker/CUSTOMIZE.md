# Customize This Skill

This carousel maker works out of the box with default branding. Follow this guide to make it yours.

---

## Getting Started

This skill is a folder of files that you upload to Claude as a custom skill. Here's the full setup:

### 1. Download and unzip

Download the `carousel-maker.zip` file and unzip it. You'll see this structure:

```
carousel-maker/
├── SKILL.md                    <- Instructions for Claude (the brain)
├── CUSTOMIZE.md                <- This file (for you, the human)
├── references/
│   ├── templates.md            <- Design templates Claude follows
│   ├── headshot.jpg            <- YOUR photo (replace this!)
└── scripts/
    ├── html_to_pdf.py          <- PDF converter (Playwright)
    └── html_to_pdf_fallback.py <- PDF converter (WeasyPrint fallback)
```

### 2. Add your branding (see sections below)

At minimum, replace the headshot and update your name/handle. Everything else is optional.

### 3. Upload to Claude

1. Go to **claude.ai**
2. Open **Settings -> Capabilities -> Skills**
3. Upload the entire `carousel-maker/` folder (zipped)
4. Toggle the skill **ON**
5. Start a new conversation and ask Claude to make a carousel

Claude will read the SKILL.md, follow the templates, and use your headshot and branding automatically.

---

## 1. Add Your Headshot (Required)

Save your headshot image into the `references/` folder. This appears in the author pill at the top of every slide AND enlarged on the CTA (final) slide.

**File specs:**
- **File name:** `headshot.jpg` (must be exactly this name). PNG also works as `headshot.png`.
- **Format:** JPG or PNG. PNG with transparency works well.
- **Dimensions:** Square crop, at least **200x200px**. It renders at 56-64px in the author pill and 100-120px on the CTA slide, so a tight face crop works best. Larger images are fine -- they'll be scaled down automatically.
- **Background:** Anything works, but solid or simple backgrounds look cleaner at small sizes. Transparent PNG backgrounds are fine.

**How to prepare your image:**
1. Start with any headshot photo
2. Crop it to a square (1:1 ratio)
3. Resize to at least 200x200px (larger is fine, aim for under 500KB to keep the PDF lean)
4. Save as `headshot.jpg`
5. Drop it into the `references/` folder

**No headshot?** If the file isn't there, Claude will generate a warm brown circle with your initials as a fallback. The layout still works, but a real photo makes carousels feel much more personal and human.

---

## 2. Change Your Name and Handle

Open `references/templates.md` and find-and-replace:

| Find | Replace with |
|---|---|
| `Kanchan Bhatta` | Your name |
| `@growthbykanchan` | Your handle |

These appear in the Branding Defaults table and throughout the slide examples.

---

## 3. Change the Brand Name

The brand name appears as a subtle watermark in the bottom-right corner of content slides.

In `references/templates.md`, find-and-replace:

| Find | Replace with |
|---|---|
| `growthbykanchan` | Your brand name |

---

## 4. Change the Accent Color

The default accent is **warm brown** (`#8B6F47`). This is used sparingly for category labels, step numbers, and key accents. To use your brand color:

In `references/templates.md`, find-and-replace this value throughout:

| Role | Default | What it does |
|---|---|---|
| Primary accent | `#8B6F47` | Category labels, step numbers, author pill border, key accents |

**Also update the highlight color if desired:**

| Role | Default | What it does |
|---|---|---|
| Highlight | `#F5D76E` | Yellow highlight boxes behind key labels like "The reality:", "Key insight:", etc. |

**Example -- switching to indigo:**

| Role | Value |
|---|---|
| Primary accent | `#4f46e5` |
| Highlight | `#818CF8` (or keep yellow) |

**Tip:** Use [Tailwind's color palette](https://tailwindcss.com/docs/colors) for inspiration. Pick the 600 shade as your primary.

---

## 5. Change the Font

The default font is **Inter**, downloaded automatically via npm and embedded directly in the PDF. You can switch to any Google Font available on [fontsource.org](https://fontsource.org/).

### How it works

Claude runs `npm install @fontsource/{font-name}` at build time (npmjs.org is an allowed domain in Claude's container). The font files are base64-encoded and embedded as `@font-face` rules in the HTML.

### To change the font

Update three values in `references/templates.md` (in the Branding Defaults table):

| Field | Default | Example: Playfair Display |
|---|---|---|
| **Font family** | `'Inter', sans-serif` | `'Playfair Display', serif` |
| **Font npm package** | `@fontsource/inter` | `@fontsource/playfair-display` |
| **Font file slug** | `inter` | `playfair-display` |

### Popular alternatives

| Font | Style | Package |
|---|---|---|
| Inter (default) | Clean geometric sans | `@fontsource/inter` |
| Space Grotesk | Modern geometric sans | `@fontsource/space-grotesk` |
| DM Sans | Friendly low-contrast sans | `@fontsource/dm-sans` |
| Playfair Display | Elegant high-contrast serif | `@fontsource/playfair-display` |
| Lora | Readable contemporary serif | `@fontsource/lora` |
| IBM Plex Sans | Professional, neutral | `@fontsource/ibm-plex-sans` |

### Fallback: system fonts (no download needed)

If you'd rather skip font embedding entirely, set the font family to a system stack and leave the npm package and slug blank.

| Style | Font stack |
|---|---|
| Clean sans-serif | `'Segoe UI', 'Helvetica Neue', Arial, sans-serif` |
| Editorial serif | `Georgia, 'Times New Roman', Times, serif` |
| Monospace/tech | `'SF Mono', 'Fira Code', 'Courier New', monospace` |

---

## 6. Change the Color Palette

The default palette is warm cream/beige. All colors are defined in `references/templates.md` under the Color Palette section.

| Role | Default | Description |
|---|---|---|
| Background primary | `#FBF8F4` | Main slide background (warm cream) |
| Background alternate | `#F5F0EA` | Alternate slides for visual rhythm |
| Card background | `#FFFFFF` | White content cards |
| Text primary | `#1A1A1A` | Headlines and strong text |
| Text body | `#4A4A4A` | Body text (dark gray, not black) |
| Text muted | `#8B8B8B` | Labels, captions, secondary text |
| Accent | `#8B6F47` | Warm brown for key accents |
| Highlight | `#F5D76E` | Yellow for label highlight boxes |

To change the overall feel, update these hex values in `references/templates.md`.

---

## 7. Change Slide Dimensions

The default is **1080x1350px** (4:5, ideal for LinkedIn and Instagram).

| Platform | Dimensions | Ratio |
|---|---|---|
| LinkedIn / Instagram feed | 1080x1350 | 4:5 |
| Square posts | 1080x1080 | 1:1 |
| Instagram Stories | 1080x1920 | 9:16 |

You can also just tell Claude the size you want when requesting a carousel.

---

## Quick Checklist

- [ ] Add your `headshot.jpg` (or `.png`) to `references/` (square, 200x200px+, under 500KB)
- [ ] Replace `Kanchan Bhatta` -> your name in `references/templates.md`
- [ ] Replace `@growthbykanchan` -> your handle in `references/templates.md`
- [ ] (Optional) Replace `growthbykanchan` -> your brand name in `references/templates.md`
- [ ] (Optional) Swap accent color `#8B6F47` in `references/templates.md`
- [ ] (Optional) Change font -- update 3 values in `references/templates.md` (see section 5)
- [ ] Upload the whole `carousel-maker/` folder to Claude via Settings -> Capabilities -> Skills

---

## Troubleshooting

**"The font doesn't look right / fell back to system font"**
The npm install may have failed. Check that the package name is correct at [fontsource.org](https://fontsource.org/). If npm is unavailable, the system font fallback (Segoe UI / Helvetica Neue / Arial) will be used.

**"The PDF looks different from the HTML"**
WeasyPrint (the fallback PDF engine) has some rendering differences from a browser. For pixel-perfect results, open the HTML file in Chrome and print to PDF manually.

**"The slides look plain"**
Make sure your `references/templates.md` matches the latest version with card-based layouts, yellow highlight boxes, and the full component library. Older versions may produce simpler output.

**"Claude isn't using the right template variation"**
You can specify the variation explicitly: "Make a Tool Showcase carousel" or "Use Variation B (Myth Buster)". If not specified, Claude picks the best fit based on content.

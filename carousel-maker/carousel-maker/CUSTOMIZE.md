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

Save your headshot image into the `references/` folder. This appears in the footer of every slide AND enlarged on the CTA (final) slide.

**File specs:**
- **File name:** `headshot.jpg` (must be exactly this name). PNG also works as `headshot.png`.
- **Format:** JPG or PNG. PNG with transparency works well.
- **Dimensions:** Square crop, at least **200x200px**. It renders at 64x64px in the footer and 100-120px on the CTA slide, so a tight face crop works best. Larger images are fine — they'll be scaled down automatically.
- **Background:** Anything works, but solid or simple backgrounds look cleaner at small sizes. Transparent PNG backgrounds are fine.

**How to prepare your image:**
1. Start with any headshot photo
2. Crop it to a square (1:1 ratio)
3. Resize to at least 200x200px (larger is fine, aim for under 500KB to keep the PDF lean)
4. Save as `headshot.jpg`
5. Drop it into the `references/` folder

**No headshot?** If the file isn't there, Claude will generate a colored circle with your initials as a fallback. The layout still works, but a real photo makes carousels feel much more personal and human.

---

## 2. Add a Background Image (Optional)

Save any image you like into the `references/` folder as your slide watermark. This appears as a large, centered, low-opacity element behind the content on every slide.

**File specs:**
- **File name:** `background.png` (must be exactly this name)
- **Format:** PNG strongly recommended — transparency works great here
- **Dimensions:** At least **500x500px**. The image renders large (up to 1200px on the slide), so higher resolution looks better. Aim for under 500KB.
- **Content:** Any image — logo, photo, illustration, icon, pattern.

**Examples of what works well:**
- A logo mark or brand icon
- A photo related to the article topic
- An abstract shape, pattern, or texture
- A monogram or initials
- An AI-generated illustration

**How it renders:**
The image sits dead center on every slide at 8% opacity, sized to 1000px by default. You can request a different scale when prompting Claude:
- `600px` — subtle, small watermark
- `800px` — medium
- `1000px` — large, fills most of the slide (default)
- `1200px` — bleeds off edges for an immersive feel

Example prompt: *"Make a carousel from this article. Use the dark theme with the background image at 1200px."*

**No background image?** Totally fine. Slides will have gradient backgrounds, accent bars, and decorative geometric elements to keep them visually rich.

---

## 3. Change Your Name and Handle

Open `references/templates.md` and find-and-replace:

| Find | Replace with |
|---|---|
| `Kanchan Bhatta` | Your name |
| `@growthbykanchan` | Your handle |

These appear in the Branding Defaults table and throughout the footer examples.

---

## 4. Change the Accent Color

The default accent is **teal** (`#0d9488`). To use your brand color:

In `references/templates.md`, find-and-replace these two values throughout:

| Role | Default | What it does |
|---|---|---|
| Primary accent | `#0d9488` | Accent bars, category labels, nav dots, page number, CTA buttons, chevron, headshot border |
| Accent light | `#14b8a6` | Highlighted words in headlines, decorative glows, stat callout backgrounds |

**Example — switching to indigo:**

| Role | Indigo value |
|---|---|
| Primary | `#4f46e5` |
| Light | `#6366f1` |

**Also update the glow/transparent accent values:**
- `rgba(13,148,136,0.15)` -> `rgba(79,70,229,0.15)` (for dark theme glows)
- `rgba(13,148,136,0.08)` -> `rgba(79,70,229,0.08)` (for light theme glows)
- `rgba(13,148,136,0.12)` -> `rgba(79,70,229,0.12)` (for stat callout backgrounds)

**Tip:** Use [Tailwind's color palette](https://tailwindcss.com/docs/colors) for inspiration. Pick the 600 shade as your primary and the 500 shade as your light.

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
| JetBrains Mono | Technical monospace | `@fontsource/jetbrains-mono` |

### Fallback: system fonts (no download needed)

If you'd rather skip font embedding entirely, set the font family to a system stack and leave the npm package and slug blank.

| Style | Font stack |
|---|---|
| Clean sans-serif | `'Segoe UI', 'Helvetica Neue', Arial, sans-serif` |
| Editorial serif | `Georgia, 'Times New Roman', Times, serif` |
| Monospace/tech | `'SF Mono', 'Fira Code', 'Courier New', monospace` |

---

## 6. Change Slide Dimensions

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
- [ ] (Optional) Add your `background.png` to `references/` (500x500px+, PNG with transparency)
- [ ] Replace `Kanchan Bhatta` -> your name in `references/templates.md`
- [ ] Replace `@growthbykanchan` -> your handle in `references/templates.md`
- [ ] (Optional) Swap accent colors + glow values in `references/templates.md`
- [ ] (Optional) Change font — update 3 values in `references/templates.md` (see section 5)
- [ ] Upload the whole `carousel-maker/` folder to Claude via Settings -> Capabilities -> Skills

---

## Troubleshooting

**"The font doesn't look right / fell back to system font"**
The npm install may have failed. Check that the package name is correct at [fontsource.org](https://fontsource.org/). If npm is unavailable, the system font fallback (DejaVu Sans) will be used.

**"There's no background watermark"**
Make sure the file is named exactly `background.png` and is in the `references/` folder.

**"The PDF looks different from the HTML"**
WeasyPrint (the fallback PDF engine) has some rendering differences from a browser. For pixel-perfect results, open the HTML file in Chrome and print to PDF manually.

**"Claude isn't asking me light or dark"**
Make sure the skill is uploaded and toggled ON in Settings -> Capabilities -> Skills. Start a new conversation after enabling it.

**"The slides look plain"**
Make sure your `references/templates.md` matches the latest version with gradient backgrounds, decorative elements, and emoji-enhanced components. Older versions may produce simpler output.

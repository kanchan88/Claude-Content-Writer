# Carousel Templates

Two richly designed templates: **Dark** and **Light**. Both use embedded fonts (Inter by default) with teal accent, decorative elements, emoji-enhanced content, and a branded footer with headshot, name/handle, navigation dots, and directional chevron.

---

## Branding Defaults

These values appear throughout both templates. To customize, find-and-replace:

| Element | Default value |
|---|---|
| **Author name** | `Kanchan Bhatta` |
| **Handle** | `@growthbykanchan` |
| **Accent color** | `#0d9488` |
| **Accent light** | `#14b8a6` |
| **Accent glow** | `rgba(13,148,136,0.15)` |
| **Font family** | `'Inter', sans-serif` |
| **Font npm package** | `@fontsource/inter` |
| **Font file slug** | `inter` (used in file paths: `inter-latin-400-normal.woff2`) |
| **Background image scale** | `1000px` (options: 600, 800, 1000, 1200) |

### Changing the font

To use a different font, update three values:

1. **Font family** — the CSS name, e.g. `'Playfair Display'`
2. **Font npm package** — the @fontsource package, e.g. `@fontsource/playfair-display`
3. **Font file slug** — the kebab-case prefix in file names, e.g. `playfair-display`

The build script will `npm install` the package, base64-encode the latin 400 + 700 woff2 files, and embed them as `@font-face` rules. See SKILL.md Step 3 for details.

Browse available fonts at [fontsource.org](https://fontsource.org/).

---

## Color Systems

### Dark theme

| Role | Hex | Usage |
|---|---|---|
| Background primary | `#0f172a` | Odd slides — base |
| Background alternate | `#111b30` | Even slides — creates visual rhythm |
| Background gradient from | `#0f172a` | Gradient start for hook/CTA slides |
| Background gradient to | `#1a1040` | Gradient end — adds depth with purple tint |
| Card background | `rgba(255,255,255,0.04)` | Icon grid cards, comparison boxes |
| Card border | `rgba(255,255,255,0.08)` | Subtle borders on cards |
| Text primary | `#f1f5f9` | Headlines |
| Text body | `#e2e8f0` | Bullet text |
| Text muted | `#94a3b8` | Subtitles, handle, attributions |
| Accent | `#0d9488` | Category labels, dots, page number, CTA, chevron, accent bar |
| Accent light | `#14b8a6` | Highlighted headline words, emoji bullet accents |
| Accent glow | `rgba(13,148,136,0.15)` | Glow effects behind stats, subtle backgrounds |
| Red (comparison) | `#ef4444` | "Don't" / "Before" items |
| Green (comparison) | `#10b981` | "Do" / "After" items |
| Dot border | `#475569` | Inactive nav dots |
| Footer border | `#1e293b` | Top border on footer bar |

### Light theme

| Role | Hex | Usage |
|---|---|---|
| Background primary | `#ffffff` | Odd slides |
| Background alternate | `#f8fafc` | Even slides |
| Background gradient from | `#f8fafc` | Gradient start for hook/CTA |
| Background gradient to | `#e0f2fe` | Gradient end — light blue tint |
| Card background | `rgba(0,0,0,0.02)` | Icon grid cards |
| Card border | `rgba(0,0,0,0.06)` | Card borders |
| Text primary | `#0f172a` | Headlines |
| Text body | `#334155` | Bullet text |
| Text muted | `#64748b` | Subtitles, handle, attributions |
| Accent | `#0d9488` | Category labels, dots, page number, CTA, chevron, accent bar |
| Accent light | `#0d9488` | Highlighted headline words |
| Accent glow | `rgba(13,148,136,0.08)` | Subtle accent backgrounds |
| Red (comparison) | `#ef4444` | "Don't" items |
| Green (comparison) | `#10b981` | "Do" items |
| Dot border | `#cbd5e1` | Inactive nav dots |
| Footer border | `#e2e8f0` | Top border on footer bar |

---

## Slide Components

### Accent bar (LEFT EDGE — every slide)

Bold vertical gradient bar on the left edge for brand identity:

```html
<div style="position: absolute; top: 0; left: 0; width: 8px; height: 100%; background: linear-gradient(180deg, #0d9488 0%, #14b8a6 100%);"></div>
```

### Page number (top-left)

Just the slide number, zero-padded, large and bold in accent color.

**Dark:**
```html
<div style="position: absolute; top: 48px; left: 80px; font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; font-size: 42px; font-weight: 800; color: #0d9488;">03</div>
```

**Light:**
```html
<div style="position: absolute; top: 48px; left: 80px; font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; font-size: 42px; font-weight: 800; color: #0d9488;">03</div>
```

### Background image (centered watermark)

Large, centered, low-opacity. Only rendered if `references/background.png` exists.

```html
<img src="data:image/png;base64,..." style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 1000px; height: 1000px; opacity: 0.08; object-fit: contain; pointer-events: none;" />
```

Scale options: 600px (subtle), 800px (medium), 1000px (large, default), 1200px (immersive).

### Decorative geometric shapes

Add to some slides (not all) for visual variety:

**Dark — top-right glow circle:**
```html
<div style="position: absolute; top: -80px; right: -80px; width: 250px; height: 250px; border-radius: 50%; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 70%); pointer-events: none;"></div>
```

**Dark — bottom-left ring:**
```html
<div style="position: absolute; bottom: 200px; left: -50px; width: 180px; height: 180px; border-radius: 50%; border: 3px solid rgba(20,184,166,0.1); pointer-events: none;"></div>
```

**Light — top-right accent blob:**
```html
<div style="position: absolute; top: -60px; right: -60px; width: 220px; height: 220px; border-radius: 50%; background: radial-gradient(circle, rgba(13,148,136,0.06) 0%, transparent 70%); pointer-events: none;"></div>
```

### Emoji bullet rows

Table layout for reliable spacing. One `<tr>` per bullet, with emoji prefix and bold key phrase.

**Dark:**
```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="vertical-align: top; padding: 0 16px 24px 0; width: 44px;">
      <span style="font-size: 30px; line-height: 1.5;">🎯</span>
    </td>
    <td style="vertical-align: top; padding: 0 0 24px 0;">
      <p style="font-size: 30px; color: #e2e8f0; line-height: 1.5; margin: 0;"><strong style="color: #f1f5f9;">Key phrase</strong> — supporting detail text goes here</p>
    </td>
  </tr>
  <!-- one tr per bullet -->
</table>
```

**Light:**
```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="vertical-align: top; padding: 0 16px 24px 0; width: 44px;">
      <span style="font-size: 30px; line-height: 1.5;">🎯</span>
    </td>
    <td style="vertical-align: top; padding: 0 0 24px 0;">
      <p style="font-size: 30px; color: #334155; line-height: 1.5; margin: 0;"><strong style="color: #0f172a;">Key phrase</strong> — supporting detail text goes here</p>
    </td>
  </tr>
</table>
```

### Stat highlight

For slides featuring a big number or percentage:

**Dark:**
```html
<div style="text-align: center; margin: 32px 0;">
  <div style="display: inline-block; padding: 24px 48px; border-radius: 20px; background: rgba(13,148,136,0.12);">
    <p style="font-size: 110px; font-weight: 800; color: #14b8a6; line-height: 1; margin: 0;">73%</p>
  </div>
  <p style="font-size: 28px; color: #94a3b8; margin: 24px 0 0 0; line-height: 1.4;">of marketers say content repurposing<br>is their #1 growth lever</p>
</div>
```

**Light:**
```html
<div style="text-align: center; margin: 32px 0;">
  <div style="display: inline-block; padding: 24px 48px; border-radius: 20px; background: rgba(13,148,136,0.08);">
    <p style="font-size: 110px; font-weight: 800; color: #0d9488; line-height: 1; margin: 0;">73%</p>
  </div>
  <p style="font-size: 28px; color: #64748b; margin: 24px 0 0 0; line-height: 1.4;">of marketers say content repurposing<br>is their #1 growth lever</p>
</div>
```

### Pull quote

For memorable statements or expert quotes:

**Dark:**
```html
<div style="border-left: 6px solid #0d9488; padding: 0 0 0 32px; margin: 32px 0;">
  <p style="font-size: 36px; font-style: italic; color: #f1f5f9; line-height: 1.4; margin: 0;">"The best content doesn't just inform — it transforms how people think."</p>
  <p style="font-size: 20px; color: #94a3b8; margin: 16px 0 0 0;">— Attribution or source</p>
</div>
```

**Light:**
```html
<div style="border-left: 6px solid #0d9488; padding: 0 0 0 32px; margin: 32px 0;">
  <p style="font-size: 36px; font-style: italic; color: #0f172a; line-height: 1.4; margin: 0;">"The best content doesn't just inform — it transforms how people think."</p>
  <p style="font-size: 20px; color: #64748b; margin: 16px 0 0 0;">— Attribution or source</p>
</div>
```

### Icon grid (2x2 layout)

For lists of features, tools, or steps:

**Dark:**
```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="width: 50%; vertical-align: top; padding: 0 12px 24px 0;">
      <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 28px; border: 1px solid rgba(255,255,255,0.08);">
        <p style="font-size: 36px; margin: 0 0 12px 0;">🚀</p>
        <p style="font-size: 24px; font-weight: 700; color: #f1f5f9; margin: 0 0 8px 0;">Speed</p>
        <p style="font-size: 20px; color: #e2e8f0; line-height: 1.4; margin: 0;">Create in minutes, not hours</p>
      </div>
    </td>
    <td style="width: 50%; vertical-align: top; padding: 0 0 24px 12px;">
      <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 28px; border: 1px solid rgba(255,255,255,0.08);">
        <p style="font-size: 36px; margin: 0 0 12px 0;">🎨</p>
        <p style="font-size: 24px; font-weight: 700; color: #f1f5f9; margin: 0 0 8px 0;">Design</p>
        <p style="font-size: 20px; color: #e2e8f0; line-height: 1.4; margin: 0;">Professional without effort</p>
      </div>
    </td>
  </tr>
  <tr>
    <td style="width: 50%; vertical-align: top; padding: 0 12px 0 0;">
      <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 28px; border: 1px solid rgba(255,255,255,0.08);">
        <p style="font-size: 36px; margin: 0 0 12px 0;">📊</p>
        <p style="font-size: 24px; font-weight: 700; color: #f1f5f9; margin: 0 0 8px 0;">Data-driven</p>
        <p style="font-size: 20px; color: #e2e8f0; line-height: 1.4; margin: 0;">Built on what works</p>
      </div>
    </td>
    <td style="width: 50%; vertical-align: top; padding: 0 0 0 12px;">
      <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 28px; border: 1px solid rgba(255,255,255,0.08);">
        <p style="font-size: 36px; margin: 0 0 12px 0;">💡</p>
        <p style="font-size: 24px; font-weight: 700; color: #f1f5f9; margin: 0 0 8px 0;">Smart</p>
        <p style="font-size: 20px; color: #e2e8f0; line-height: 1.4; margin: 0;">AI-powered decisions</p>
      </div>
    </td>
  </tr>
</table>
```

**Light:** Same structure, replace colors:
- Card bg: `rgba(0,0,0,0.02)`, border: `rgba(0,0,0,0.06)`
- Title: `#0f172a`, body: `#334155`

### Comparison component (do/don't)

**Dark:**
```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="width: 47%; vertical-align: top;">
      <div style="background: rgba(239,68,68,0.08); border-radius: 16px; padding: 28px; border-left: 4px solid #ef4444;">
        <p style="font-size: 24px; font-weight: 700; color: #ef4444; margin: 0 0 16px 0;">❌ Don't</p>
        <p style="font-size: 22px; color: #e2e8f0; line-height: 1.5; margin: 0;">Plain text with no visual design</p>
      </div>
    </td>
    <td style="width: 6%;"></td>
    <td style="width: 47%; vertical-align: top;">
      <div style="background: rgba(16,185,129,0.08); border-radius: 16px; padding: 28px; border-left: 4px solid #10b981;">
        <p style="font-size: 24px; font-weight: 700; color: #10b981; margin: 0 0 16px 0;">✅ Do</p>
        <p style="font-size: 22px; color: #e2e8f0; line-height: 1.5; margin: 0;">Bold design that stops the scroll</p>
      </div>
    </td>
  </tr>
</table>
```

**Light:** Same structure — red/green colors stay the same, body text uses `#334155`.

---

## Footer Bar

160px tall. Three zones in a flex row: identity (left), nav dots (center), chevron (right).

### Dark footer

```html
<div style="position: absolute; bottom: 0; left: 0; right: 0; height: 160px; padding: 0 80px 0 80px; display: flex; flex-direction: row; align-items: center; font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; border-top: 1px solid #1e293b;">
  <!-- Left: identity -->
  <div style="display: flex; flex-direction: row; align-items: center; gap: 20px; white-space: nowrap; flex-shrink: 0;">
    <img src="data:image/png;base64,HEADSHOT_B64" width="64" height="64" style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover; display: block; flex-shrink: 0; border: 2px solid #0d9488;" />
    <div style="flex-shrink: 0;">
      <p style="font-size: 22px; font-weight: 600; color: #f1f5f9; margin: 0; line-height: 1.3;">Kanchan Bhatta</p>
      <p style="font-size: 17px; color: #94a3b8; margin: 0; line-height: 1.3;">@growthbykanchan</p>
    </div>
  </div>
  <!-- Center: nav dots -->
  <div style="flex: 1; display: flex; justify-content: center;">
    <table cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
      <tr>
        <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; background: #0d9488;"></div></td>
        <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; border: 2px solid #475569;"></div></td>
        <!-- one td per slide -->
      </tr>
    </table>
  </div>
  <!-- Right: nav chevron (omit on last slide) -->
  <div style="flex-shrink: 0;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: block;">
      <path d="M9 6L15 12L9 18" stroke="#0d9488" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
</div>
```

### Dark footer — no headshot fallback (initials avatar)

Replace the `<img>` with:
```html
<div style="width: 64px; height: 64px; border-radius: 50%; background: #0d9488; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
  <span style="font-size: 24px; font-weight: 700; color: #ffffff; font-family: 'Inter', 'Segoe UI', Arial, sans-serif;">KB</span>
</div>
```

### Light footer

Same structure, different colors:

```html
<div style="position: absolute; bottom: 0; left: 0; right: 0; height: 160px; padding: 0 80px 0 80px; display: flex; flex-direction: row; align-items: center; font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; border-top: 1px solid #e2e8f0;">
  <div style="display: flex; flex-direction: row; align-items: center; gap: 20px; white-space: nowrap; flex-shrink: 0;">
    <img src="data:image/png;base64,HEADSHOT_B64" width="64" height="64" style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover; display: block; flex-shrink: 0; border: 2px solid #0d9488;" />
    <div style="flex-shrink: 0;">
      <p style="font-size: 22px; font-weight: 600; color: #0f172a; margin: 0; line-height: 1.3;">Kanchan Bhatta</p>
      <p style="font-size: 17px; color: #64748b; margin: 0; line-height: 1.3;">@growthbykanchan</p>
    </div>
  </div>
  <div style="flex: 1; display: flex; justify-content: center;">
    <table cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
      <tr>
        <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; background: #0d9488;"></div></td>
        <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; border: 2px solid #cbd5e1;"></div></td>
      </tr>
    </table>
  </div>
  <div style="flex-shrink: 0;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: block;">
      <path d="M9 6L15 12L9 18" stroke="#0d9488" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
</div>
```

---

## DARK THEME — Full Slide Examples

### Hook slide (Slide 1 — gradient background, bold & dramatic)

```html
<div class="slide" style="width:1080px; height:1350px; background: linear-gradient(145deg, #0f172a 0%, #1a1040 60%, #0f172a 100%); color:#f1f5f9; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Accent bar -->
  <div style="position: absolute; top: 0; left: 0; width: 8px; height: 100%; background: linear-gradient(180deg, #0d9488 0%, #14b8a6 100%);"></div>
  <!-- Decorative top-right glow -->
  <div style="position: absolute; top: -100px; right: -100px; width: 350px; height: 350px; border-radius: 50%; background: radial-gradient(circle, rgba(13,148,136,0.15) 0%, transparent 70%); pointer-events: none;"></div>
  <!-- Decorative bottom-left ring -->
  <div style="position: absolute; bottom: 250px; left: -60px; width: 200px; height: 200px; border-radius: 50%; border: 3px solid rgba(20,184,166,0.1); pointer-events: none;"></div>
  <!-- Background watermark -->
  <img src="data:image/png;base64,..." style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:1000px; height:1000px; opacity:0.08; object-fit:contain; pointer-events:none;" />
  <!-- Page number -->
  <div style="position:absolute; top:48px; left:80px; font-size:42px; font-weight:800; color:#0d9488;">01</div>
  <!-- Content -->
  <div style="position:absolute; top:120px; left:80px; right:80px; bottom:170px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
    <p style="font-size:20px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#0d9488; margin:0 0 32px 0;">🔥 CATEGORY</p>
    <h1 style="font-size:64px; font-weight:800; line-height:1.15; margin:0 0 28px 0;">Bold Hook Title<br>Goes <span style="color:#14b8a6">Right Here</span></h1>
    <p style="font-size:28px; color:#94a3b8; line-height:1.5; max-width:750px; margin:0;">Subtitle that sets up the carousel's promise and makes them swipe</p>
  </div>
  <!-- Footer -->
</div>
```

### Content slide with emoji bullets

```html
<div class="slide" style="width:1080px; height:1350px; background:#111b30; color:#f1f5f9; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Accent bar -->
  <div style="position: absolute; top: 0; left: 0; width: 8px; height: 100%; background: linear-gradient(180deg, #0d9488 0%, #14b8a6 100%);"></div>
  <img src="data:image/png;base64,..." style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:1000px; height:1000px; opacity:0.08; object-fit:contain; pointer-events:none;" />
  <div style="position:absolute; top:48px; left:80px; font-size:42px; font-weight:800; color:#0d9488;">02</div>
  <div style="position:absolute; top:120px; left:80px; right:80px; bottom:170px; display:flex; flex-direction:column; justify-content:center;">
    <p style="font-size:20px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#0d9488; margin:0 0 24px 0;">📌 SECTION LABEL</p>
    <h2 style="font-size:52px; font-weight:700; line-height:1.2; margin:0 0 40px 0;">Headline Goes<br>On <span style="color:#14b8a6">Two Lines</span></h2>
    <table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
      <tr>
        <td style="vertical-align: top; padding: 0 16px 24px 0; width: 44px;">
          <span style="font-size: 30px; line-height: 1.5;">🎯</span>
        </td>
        <td style="vertical-align: top; padding: 0 0 24px 0;">
          <p style="font-size: 30px; color: #e2e8f0; line-height: 1.5; margin: 0;"><strong style="color: #f1f5f9;">Key insight</strong> — with supporting detail that adds value</p>
        </td>
      </tr>
      <tr>
        <td style="vertical-align: top; padding: 0 16px 24px 0; width: 44px;">
          <span style="font-size: 30px; line-height: 1.5;">💡</span>
        </td>
        <td style="vertical-align: top; padding: 0 0 24px 0;">
          <p style="font-size: 30px; color: #e2e8f0; line-height: 1.5; margin: 0;"><strong style="color: #f1f5f9;">Another point</strong> — concrete example or data here</p>
        </td>
      </tr>
      <tr>
        <td style="vertical-align: top; padding: 0 16px 0 0; width: 44px;">
          <span style="font-size: 30px; line-height: 1.5;">🚀</span>
        </td>
        <td style="vertical-align: top; padding: 0;">
          <p style="font-size: 30px; color: #e2e8f0; line-height: 1.5; margin: 0;"><strong style="color: #f1f5f9;">Action item</strong> — what the reader should do next</p>
        </td>
      </tr>
    </table>
  </div>
  <!-- Footer -->
</div>
```

### Stat highlight slide

```html
<div class="slide" style="width:1080px; height:1350px; background:#0f172a; color:#f1f5f9; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="position: absolute; top: 0; left: 0; width: 8px; height: 100%; background: linear-gradient(180deg, #0d9488 0%, #14b8a6 100%);"></div>
  <img src="data:image/png;base64,..." style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:1000px; height:1000px; opacity:0.08; object-fit:contain; pointer-events:none;" />
  <div style="position:absolute; top:48px; left:80px; font-size:42px; font-weight:800; color:#0d9488;">04</div>
  <div style="position:absolute; top:120px; left:80px; right:80px; bottom:170px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
    <p style="font-size:20px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#0d9488; margin:0 0 48px 0;">📊 KEY DATA</p>
    <div style="display: inline-block; padding: 32px 56px; border-radius: 24px; background: rgba(13,148,136,0.12); margin: 0 0 32px 0;">
      <p style="font-size: 120px; font-weight: 800; color: #14b8a6; line-height: 1; margin: 0;">73%</p>
    </div>
    <p style="font-size: 32px; color: #e2e8f0; line-height: 1.4; margin: 0; max-width: 700px;">of marketers say content repurposing is their <strong style="color: #14b8a6;">#1 growth lever</strong></p>
    <p style="font-size: 20px; color: #94a3b8; margin: 24px 0 0 0;">Source: HubSpot Marketing Report 2024</p>
  </div>
  <!-- Footer -->
</div>
```

### Pull quote slide

```html
<div class="slide" style="width:1080px; height:1350px; background:#111b30; color:#f1f5f9; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="position: absolute; top: 0; left: 0; width: 8px; height: 100%; background: linear-gradient(180deg, #0d9488 0%, #14b8a6 100%);"></div>
  <div style="position: absolute; top: -80px; right: -80px; width: 250px; height: 250px; border-radius: 50%; background: radial-gradient(circle, rgba(13,148,136,0.1) 0%, transparent 70%); pointer-events: none;"></div>
  <img src="data:image/png;base64,..." style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:1000px; height:1000px; opacity:0.08; object-fit:contain; pointer-events:none;" />
  <div style="position:absolute; top:48px; left:80px; font-size:42px; font-weight:800; color:#0d9488;">05</div>
  <div style="position:absolute; top:120px; left:80px; right:80px; bottom:170px; display:flex; flex-direction:column; justify-content:center;">
    <p style="font-size:20px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#0d9488; margin:0 0 40px 0;">💬 INSIGHT</p>
    <div style="border-left: 6px solid #0d9488; padding: 0 0 0 32px;">
      <p style="font-size: 40px; font-style: italic; color: #f1f5f9; line-height: 1.35; margin: 0;">"The best carousels don't just share information — they create a visual <span style="color: #14b8a6;">experience</span> that people want to swipe through."</p>
      <p style="font-size: 22px; color: #94a3b8; margin: 24px 0 0 0;">— Industry Expert</p>
    </div>
  </div>
  <!-- Footer -->
</div>
```

### Icon grid slide

```html
<div class="slide" style="width:1080px; height:1350px; background:#0f172a; color:#f1f5f9; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="position: absolute; top: 0; left: 0; width: 8px; height: 100%; background: linear-gradient(180deg, #0d9488 0%, #14b8a6 100%);"></div>
  <img src="data:image/png;base64,..." style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:1000px; height:1000px; opacity:0.08; object-fit:contain; pointer-events:none;" />
  <div style="position:absolute; top:48px; left:80px; font-size:42px; font-weight:800; color:#0d9488;">06</div>
  <div style="position:absolute; top:120px; left:80px; right:80px; bottom:170px; display:flex; flex-direction:column; justify-content:center;">
    <p style="font-size:20px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#0d9488; margin:0 0 24px 0;">⚡ FEATURES</p>
    <h2 style="font-size:48px; font-weight:700; line-height:1.2; margin:0 0 40px 0;">What You <span style="color:#14b8a6;">Get</span></h2>
    <table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
      <tr>
        <td style="width: 50%; vertical-align: top; padding: 0 12px 24px 0;">
          <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 28px; border: 1px solid rgba(255,255,255,0.08);">
            <p style="font-size: 36px; margin: 0 0 12px 0;">🚀</p>
            <p style="font-size: 24px; font-weight: 700; color: #f1f5f9; margin: 0 0 8px 0;">Speed</p>
            <p style="font-size: 20px; color: #e2e8f0; line-height: 1.4; margin: 0;">Create in minutes</p>
          </div>
        </td>
        <td style="width: 50%; vertical-align: top; padding: 0 0 24px 12px;">
          <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 28px; border: 1px solid rgba(255,255,255,0.08);">
            <p style="font-size: 36px; margin: 0 0 12px 0;">🎨</p>
            <p style="font-size: 24px; font-weight: 700; color: #f1f5f9; margin: 0 0 8px 0;">Design</p>
            <p style="font-size: 20px; color: #e2e8f0; line-height: 1.4; margin: 0;">Professional output</p>
          </div>
        </td>
      </tr>
      <tr>
        <td style="width: 50%; vertical-align: top; padding: 0 12px 0 0;">
          <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 28px; border: 1px solid rgba(255,255,255,0.08);">
            <p style="font-size: 36px; margin: 0 0 12px 0;">📊</p>
            <p style="font-size: 24px; font-weight: 700; color: #f1f5f9; margin: 0 0 8px 0;">Data-Driven</p>
            <p style="font-size: 20px; color: #e2e8f0; line-height: 1.4; margin: 0;">Built on what works</p>
          </div>
        </td>
        <td style="width: 50%; vertical-align: top; padding: 0 0 0 12px;">
          <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 28px; border: 1px solid rgba(255,255,255,0.08);">
            <p style="font-size: 36px; margin: 0 0 12px 0;">💡</p>
            <p style="font-size: 24px; font-weight: 700; color: #f1f5f9; margin: 0 0 8px 0;">Smart</p>
            <p style="font-size: 20px; color: #e2e8f0; line-height: 1.4; margin: 0;">AI-powered content</p>
          </div>
        </td>
      </tr>
    </table>
  </div>
  <!-- Footer -->
</div>
```

### CTA slide (final — gradient bg, enlarged author, CTA button)

```html
<div class="slide" style="width:1080px; height:1350px; background: linear-gradient(145deg, #0f172a 0%, #1a1040 60%, #0f172a 100%); color:#f1f5f9; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="position: absolute; top: 0; left: 0; width: 8px; height: 100%; background: linear-gradient(180deg, #0d9488 0%, #14b8a6 100%);"></div>
  <div style="position: absolute; top: -100px; right: -100px; width: 350px; height: 350px; border-radius: 50%; background: radial-gradient(circle, rgba(13,148,136,0.15) 0%, transparent 70%); pointer-events: none;"></div>
  <div style="position: absolute; bottom: 250px; left: -60px; width: 200px; height: 200px; border-radius: 50%; border: 3px solid rgba(20,184,166,0.08); pointer-events: none;"></div>
  <img src="data:image/png;base64,..." style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:1000px; height:1000px; opacity:0.08; object-fit:contain; pointer-events:none;" />
  <div style="position:absolute; top:48px; left:80px; font-size:42px; font-weight:800; color:#0d9488;">10</div>
  <div style="position:absolute; top:120px; left:80px; right:80px; bottom:170px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
    <h2 style="font-size:56px; font-weight:800; line-height:1.2; margin:0 0 24px 0;">Ready to <span style="color:#14b8a6;">Level Up</span>?</h2>
    <p style="font-size:28px; color:#94a3b8; line-height:1.5; max-width:700px; margin:0 0 40px 0;">Start creating scroll-stopping carousels that grow your audience</p>
    <div style="background:#0d9488; color:#f1f5f9; padding:24px 52px; border-radius:14px; margin: 0 0 48px 0;">
      <p style="font-size:28px; font-weight:700; margin:0;">Follow for More Tips 🚀</p>
    </div>
    <!-- Enlarged author section -->
    <img src="data:image/png;base64,HEADSHOT_B64" width="100" height="100" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 3px solid #0d9488; margin: 0 0 16px 0;" />
    <p style="font-size: 26px; font-weight: 700; color: #f1f5f9; margin: 0;">Kanchan Bhatta</p>
    <p style="font-size: 20px; color: #94a3b8; margin: 8px 0 0 0;">@growthbykanchan</p>
  </div>
  <!-- Footer (no chevron on last slide) -->
</div>
```

---

## LIGHT THEME — Differences Only

The light theme uses the same layout structure and component patterns. Only colors change:

| Element | Dark value | Light value |
|---|---|---|
| Slide background (odd) | `#0f172a` | `#ffffff` |
| Slide background (even) | `#111b30` | `#f8fafc` |
| Hook/CTA gradient from | `#0f172a` | `#f8fafc` |
| Hook/CTA gradient to | `#1a1040` | `#e0f2fe` |
| Headline color | `#f1f5f9` | `#0f172a` |
| Body/bullet text | `#e2e8f0` | `#334155` |
| Muted text | `#94a3b8` | `#64748b` |
| Accent highlight | `#14b8a6` | `#0d9488` |
| Card background | `rgba(255,255,255,0.04)` | `rgba(0,0,0,0.02)` |
| Card border | `rgba(255,255,255,0.08)` | `rgba(0,0,0,0.06)` |
| Inactive dot border | `#475569` | `#cbd5e1` |
| Footer border | `#1e293b` | `#e2e8f0` |
| Footer name color | `#f1f5f9` | `#0f172a` |
| Footer handle color | `#94a3b8` | `#64748b` |
| CTA button text | `#f1f5f9` | `#ffffff` |
| Decorative glow | `rgba(13,148,136,0.15)` | `rgba(13,148,136,0.06)` |
| Stat callout bg | `rgba(13,148,136,0.12)` | `rgba(13,148,136,0.08)` |

### Light hook slide gradient:
```css
background: linear-gradient(145deg, #f8fafc 0%, #e0f2fe 60%, #f8fafc 100%);
```

### Light CTA slide gradient:
```css
background: linear-gradient(145deg, #f8fafc 0%, #e0f2fe 60%, #f8fafc 100%);
```

# Carousel Templates

Four professional template variations with a warm, editorial design system. All use embedded fonts (Inter by default) with a cream/beige palette, white cards, yellow highlight boxes, and consistent author branding.

---

## Branding Defaults

| Element | Default value |
|---|---|
| **Author name** | `Kanchan Bhatta` |
| **Handle** | `@growthbykanchan` |
| **Brand name** | `growthbykanchan` |
| **Accent color (brown)** | `#8B6F47` |
| **Accent light** | `#C4956A` |
| **Highlight yellow** | `#F5D76E` |
| **Font family** | `'Inter', sans-serif` |
| **Font npm package** | `@fontsource/inter` |
| **Font file slug** | `inter` |

---

## Color System

| Role | Hex | Usage |
|---|---|---|
| Background primary | `#FBF8F4` | Main slide background (warm cream) |
| Background alternate | `#F5F0EA` | Alternate slides for visual rhythm |
| Background cover | `#F5F0EA` | Cover and CTA slides |
| Card background | `#FFFFFF` | White cards for content |
| Card border | `rgba(0,0,0,0.04)` | Subtle card borders |
| Card shadow | `0 2px 12px rgba(0,0,0,0.06)` | Soft card shadows |
| Text primary | `#1A1A1A` | Headlines, bold text |
| Text body | `#4A4A4A` | Body text, descriptions |
| Text muted | `#8B8B8B` | Subtitles, secondary info |
| Text light | `#B0B0B0` | Very subtle text (brand watermark) |
| Accent brown | `#8B6F47` | Category labels, section titles, accent text |
| Accent light brown | `#C4956A` | Secondary accents, CTA button |
| Highlight yellow | `#F5D76E` | Label highlight boxes |
| Highlight yellow bg | `rgba(245,215,110,0.3)` | Softer highlight for larger areas |
| Dot active | `#8B9E8B` | Active navigation dot (muted sage green) |
| Dot inactive | `#D4D0CA` | Inactive navigation dots |
| Dot inactive light | `rgba(0,0,0,0.08)` | Very subtle dot borders |
| Verified badge | `#8B6F47` | Checkmark badge on author headshot |
| Grid line | `rgba(0,0,0,0.03)` | Subtle background grid pattern |

---

## Common Components

### Background grid pattern (optional, adds subtle texture)

Apply to any slide for a paper/grid feel:
```html
<div style="position: absolute; inset: 0; background-image:
  linear-gradient(rgba(0,0,0,0.03) 1px, transparent 1px),
  linear-gradient(90deg, rgba(0,0,0,0.03) 1px, transparent 1px);
  background-size: 40px 40px; pointer-events: none;"></div>
```

### Author pill (top of content slides)

Small centered author identity with headshot and optional verified badge:
```html
<div style="display: flex; align-items: center; justify-content: center; gap: 10px; padding-top: 48px;">
  <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="44" height="44"
       style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #F5F0EA;" />
  <span style="font-size: 18px; font-weight: 600; color: #1A1A1A; font-family: 'Inter', sans-serif;">Kanchan Bhatta</span>
  <svg width="18" height="18" viewBox="0 0 24 24" fill="#8B6F47"><path d="M12 2L14.09 8.26L21 9.27L16 14.14L17.18 21.02L12 17.77L6.82 21.02L8 14.14L3 9.27L9.91 8.26L12 2Z"/></svg>
</div>
```

### Author pill — no headshot fallback (initials avatar)

```html
<div style="display: flex; align-items: center; justify-content: center; gap: 10px; padding-top: 48px;">
  <div style="width: 44px; height: 44px; border-radius: 50%; background: #8B6F47; display: flex; align-items: center; justify-content: center;">
    <span style="font-size: 16px; font-weight: 700; color: #FFFFFF; font-family: 'Inter', sans-serif;">KB</span>
  </div>
  <span style="font-size: 18px; font-weight: 600; color: #1A1A1A; font-family: 'Inter', sans-serif;">Kanchan Bhatta</span>
  <svg width="18" height="18" viewBox="0 0 24 24" fill="#8B6F47"><path d="M12 2L14.09 8.26L21 9.27L16 14.14L17.18 21.02L12 17.77L6.82 21.02L8 14.14L3 9.27L9.91 8.26L12 2Z"/></svg>
</div>
```

### Yellow highlight label

For section labels like "The reality:", "Try this instead:", "Key insight:":
```html
<div style="display: inline-block; background: #F5D76E; padding: 4px 14px; margin: 0 0 16px 0;">
  <span style="font-size: 20px; font-weight: 700; color: #1A1A1A; font-family: 'Inter', sans-serif;">The reality:</span>
</div>
```

### White content card

```html
<div style="background: #FFFFFF; border-radius: 16px; padding: 32px; border: 1px solid rgba(0,0,0,0.04); box-shadow: 0 2px 12px rgba(0,0,0,0.06);">
  <!-- card content -->
</div>
```

### Logo card (for Tool Showcase)

```html
<div style="background: #FFFFFF; border-radius: 16px; padding: 20px 40px; border: 1px solid rgba(0,0,0,0.04); box-shadow: 0 2px 12px rgba(0,0,0,0.06); display: inline-flex; align-items: center; justify-content: center;">
  <img src="data:image/png;base64,{LOGO_B64}" style="height: 40px; object-fit: contain;" />
</div>
```

### Device mockup frame (tablet — for screenshots)

```html
<div style="background: #2A2A2A; border-radius: 20px; padding: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.15); max-width: 800px; margin: 0 auto;">
  <div style="background: #FFFFFF; border-radius: 12px; overflow: hidden;">
    <img src="data:image/png;base64,{SCREENSHOT_B64}" style="width: 100%; display: block;" />
  </div>
  <!-- Scrollbar indicator -->
  <div style="display: flex; justify-content: center; padding: 10px 0 4px;">
    <div style="width: 120px; height: 5px; border-radius: 3px; background: rgba(255,255,255,0.3);"></div>
  </div>
</div>
```

### Navigation dots (bottom of content slides)

Generate dynamically — one dot per slide. Active dot is filled, others are hollow:
```html
<div style="display: flex; justify-content: center; gap: 10px; padding: 24px 0;">
  <div style="width: 12px; height: 12px; border-radius: 50%; background: #8B9E8B;"></div>
  <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
  <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
  <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
  <!-- one per slide, filled = current -->
</div>
```

### Brand watermark (bottom corner of content slides)

```html
<div style="position: absolute; bottom: 40px; right: 60px; font-size: 16px; font-weight: 500; color: #C4C0BA; font-family: 'Inter', sans-serif; letter-spacing: 2px; text-transform: uppercase;">growthbykanchan</div>
```

### Swipe arrow indicator (cover slide)

A warm brown rounded pill with arrow:
```html
<div style="display: inline-flex; align-items: center; justify-content: center; background: #8B6F47; border-radius: 20px; padding: 12px 20px;">
  <svg width="28" height="28" viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
</div>
```

### Footer with author (bottom of content slides — alternative to author pill at top)

If you prefer the author at the bottom instead of top:
```html
<div style="position: absolute; bottom: 32px; left: 80px; display: flex; align-items: center; gap: 14px;">
  <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="48" height="48"
       style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover;" />
  <div>
    <p style="font-size: 16px; font-weight: 600; color: #1A1A1A; margin: 0; font-family: 'Inter', sans-serif;">Kanchan Bhatta</p>
    <p style="font-size: 13px; color: #8B8B8B; margin: 0; font-family: 'Inter', sans-serif;">@growthbykanchan</p>
  </div>
</div>
```

---

## VARIATION A: Tool Showcase / Listicle

Best for: "X best tools for Y", "X resources for Z", "X APIs for Y"

### A — Cover slide

```html
<div class="slide" style="width:1080px; height:1350px; background: #F5F0EA; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Subtle grid -->
  <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(0,0,0,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.03) 1px, transparent 1px); background-size: 40px 40px; pointer-events: none;"></div>

  <!-- Brand top-right -->
  <div style="position: absolute; top: 48px; right: 60px; font-size: 16px; font-weight: 500; color: #B0B0B0; letter-spacing: 3px; text-transform: uppercase;">growthbykanchan</div>

  <!-- Content -->
  <div style="position: relative; padding: 120px 80px 200px 80px; display: flex; flex-direction: column; height: 100%;">
    <!-- Giant number -->
    <p style="font-size: 160px; font-weight: 800; color: #8B6F47; line-height: 0.9; margin: 0 0 16px 0;">27</p>

    <!-- Title -->
    <h1 style="font-size: 52px; font-weight: 700; color: #1A1A1A; line-height: 1.2; margin: 0 0 8px 0;">Best Claude Code</h1>
    <h1 style="font-size: 52px; font-weight: 700; color: #1A1A1A; line-height: 1.2; margin: 0 0 8px 0;">APIs <span style="color: #8B6F47;">for GTM</span></h1>

    <!-- Swipe arrow -->
    <div style="position: absolute; right: 80px; top: 480px;">
      <div style="display: inline-flex; align-items: center; justify-content: center; background: #8B6F47; border-radius: 20px; padding: 12px 20px;">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
    </div>

    <!-- Icon grid (mini logos/placeholders) -->
    <div style="margin-top: auto; display: flex; flex-wrap: wrap; gap: 16px; max-width: 600px;">
      <!-- Render 8-12 small icon cards for visual preview -->
      <div style="width: 72px; height: 72px; background: #FFFFFF; border-radius: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); display: flex; align-items: center; justify-content: center; border: 1px solid rgba(0,0,0,0.04);">
        <div style="width: 40px; height: 40px; background: #E8E4DE; border-radius: 8px;"></div>
      </div>
      <!-- Repeat for each tool icon -->
    </div>
  </div>

  <!-- Author bottom-left -->
  <div style="position: absolute; bottom: 48px; left: 80px; display: flex; align-items: center; gap: 14px;">
    <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="56" height="56"
         style="width: 56px; height: 56px; border-radius: 50%; object-fit: cover;" />
    <div>
      <p style="font-size: 18px; font-weight: 600; color: #1A1A1A; margin: 0;">Kanchan Bhatta</p>
      <p style="font-size: 14px; color: #8B8B8B; margin: 0;">growthbykanchan.com</p>
    </div>
  </div>
</div>
```

### A — Overview / teaser slide

```html
<div class="slide" style="width:1080px; height:1350px; background: #FBF8F4; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(0,0,0,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.03) 1px, transparent 1px); background-size: 40px 40px; pointer-events: none;"></div>

  <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; padding: 80px;">
    <!-- Scattered icon grid (larger, more visual) -->
    <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; max-width: 700px; margin-bottom: 48px;">
      <!-- 8-10 larger icon cards with slight rotation for visual interest -->
      <div style="width: 100px; height: 100px; background: #FFFFFF; border-radius: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.08); transform: rotate(-5deg); display: flex; align-items: center; justify-content: center; border: 1px solid rgba(0,0,0,0.04);">
        <div style="width: 56px; height: 56px; background: #E8E4DE; border-radius: 12px;"></div>
      </div>
      <!-- Repeat with varying rotations: rotate(3deg), rotate(-2deg), etc. -->
    </div>

    <!-- CTA pill -->
    <div style="background: #C4956A; border-radius: 30px; padding: 14px 32px; display: inline-flex; align-items: center; gap: 8px;">
      <span style="font-size: 18px; font-weight: 600; color: #FFFFFF;">Keep scrolling to see the full list</span>
    </div>
  </div>
</div>
```

### A — Category divider slide

```html
<div class="slide" style="width:1080px; height:1350px; background: #FBF8F4; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Author pill top -->
  <div style="display: flex; align-items: center; justify-content: center; gap: 10px; padding-top: 56px;">
    <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="44" height="44" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #F5F0EA;" />
    <span style="font-size: 18px; font-weight: 600; color: #1A1A1A;">Kanchan Bhatta</span>
    <svg width="18" height="18" viewBox="0 0 24 24" fill="#8B6F47"><path d="M12 2L14.09 8.26L21 9.27L16 14.14L17.18 21.02L12 17.77L6.82 21.02L8 14.14L3 9.27L9.91 8.26L12 2Z"/></svg>
  </div>

  <!-- Category title -->
  <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; flex: 1; padding: 60px 80px;">
    <h2 style="font-size: 48px; font-weight: 700; color: #8B6F47; text-align: center; margin: 0 0 48px 0;">Sourcing Agents</h2>

    <!-- Tool logo grid (2 columns) -->
    <table cellspacing="0" cellpadding="0" style="border-collapse: separate; border-spacing: 16px;">
      <tr>
        <td><div style="background: #FFFFFF; border-radius: 16px; padding: 16px 36px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.04); text-align: center; min-width: 180px;">
          <span style="font-size: 22px; font-weight: 600; color: #1A1A1A;">Clay</span>
        </div></td>
        <td><div style="background: #FFFFFF; border-radius: 16px; padding: 16px 36px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.04); text-align: center; min-width: 180px;">
          <span style="font-size: 22px; font-weight: 600; color: #1A1A1A;">Airtop</span>
        </div></td>
      </tr>
      <tr>
        <td><div style="background: #FFFFFF; border-radius: 16px; padding: 16px 36px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.04); text-align: center; min-width: 180px;">
          <span style="font-size: 22px; font-weight: 600; color: #1A1A1A;">Exa</span>
        </div></td>
        <td><div style="background: #FFFFFF; border-radius: 16px; padding: 16px 36px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.04); text-align: center; min-width: 180px;">
          <span style="font-size: 22px; font-weight: 600; color: #1A1A1A;">Perplexity</span>
        </div></td>
      </tr>
    </table>
  </div>

  <!-- Brand bottom -->
  <div style="position: absolute; bottom: 40px; left: 0; right: 0; text-align: center; font-size: 16px; font-weight: 500; color: #C4C0BA; letter-spacing: 3px; text-transform: uppercase;">growthbykanchan</div>
</div>
```

### A — Tool detail slide (with screenshot)

```html
<div class="slide" style="width:1080px; height:1350px; background: #FBF8F4; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Carousel title (small, top) -->
  <div style="text-align: center; padding-top: 36px;">
    <p style="font-size: 16px; font-weight: 500; color: #C4956A; letter-spacing: 1px;">27 Best Claude Code APIs for GTM</p>
  </div>

  <!-- Logo card -->
  <div style="display: flex; justify-content: center; padding: 24px 80px;">
    <div style="background: #FFFFFF; border-radius: 16px; padding: 18px 48px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.04);">
      <span style="font-size: 28px; font-weight: 700; color: #1A1A1A;">ToolName</span>
    </div>
  </div>

  <!-- Screenshot in device mockup -->
  <div style="padding: 16px 60px;">
    <div style="background: #2A2A2A; border-radius: 20px; padding: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.12);">
      <div style="background: #FFFFFF; border-radius: 12px; overflow: hidden; min-height: 500px;">
        <!-- Screenshot image or placeholder -->
        <div style="padding: 40px; text-align: center;">
          <p style="font-size: 36px; font-weight: 700; color: #1A1A1A; margin: 0 0 16px 0;">Tool Headline</p>
          <p style="font-size: 20px; color: #4A4A4A; line-height: 1.5;">Tool description and key value proposition goes here</p>
        </div>
      </div>
      <!-- Scrollbar -->
      <div style="display: flex; justify-content: center; padding: 10px 0 4px;">
        <div style="width: 120px; height: 5px; border-radius: 3px; background: rgba(255,255,255,0.3);"></div>
      </div>
    </div>
  </div>

  <!-- Author pill bottom -->
  <div style="display: flex; align-items: center; justify-content: center; gap: 10px; padding: 24px 0;">
    <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="40" height="40" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;" />
    <span style="font-size: 16px; font-weight: 600; color: #1A1A1A;">Kanchan Bhatta</span>
  </div>
</div>
```

### A — Tool detail slide (text-only, no screenshot)

```html
<div class="slide" style="width:1080px; height:1350px; background: #FBF8F4; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Author pill top -->
  <div style="display: flex; align-items: center; justify-content: center; gap: 10px; padding-top: 56px;">
    <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="44" height="44" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #F5F0EA;" />
    <span style="font-size: 18px; font-weight: 600; color: #1A1A1A;">Kanchan Bhatta</span>
    <svg width="18" height="18" viewBox="0 0 24 24" fill="#8B6F47"><path d="M12 2L14.09 8.26L21 9.27L16 14.14L17.18 21.02L12 17.77L6.82 21.02L8 14.14L3 9.27L9.91 8.26L12 2Z"/></svg>
  </div>

  <!-- Tool name in card -->
  <div style="display: flex; justify-content: center; padding: 40px 80px 24px;">
    <div style="background: #FFFFFF; border-radius: 16px; padding: 20px 48px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.04);">
      <span style="font-size: 28px; font-weight: 700; color: #1A1A1A;">ToolName</span>
    </div>
  </div>

  <!-- Description card -->
  <div style="padding: 16px 80px;">
    <div style="background: #FFFFFF; border-radius: 20px; padding: 48px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.04);">
      <h3 style="font-size: 32px; font-weight: 700; color: #1A1A1A; line-height: 1.3; margin: 0 0 20px 0;">Value proposition headline</h3>
      <p style="font-size: 22px; color: #4A4A4A; line-height: 1.6; margin: 0 0 24px 0;">Description of what this tool does and why it matters for the reader.</p>
      <div style="border-top: 1px solid rgba(0,0,0,0.06); padding-top: 20px;">
        <p style="font-size: 18px; color: #8B8B8B; margin: 0;"><strong style="color: #1A1A1A;">Best for:</strong> Use case description</p>
      </div>
    </div>
  </div>

  <!-- Dots -->
  <div style="position: absolute; bottom: 80px; left: 0; right: 0; display: flex; justify-content: center; gap: 10px;">
    <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
    <div style="width: 12px; height: 12px; border-radius: 50%; background: #8B9E8B;"></div>
    <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
  </div>

  <!-- Brand -->
  <div style="position: absolute; bottom: 40px; left: 0; right: 0; text-align: center; font-size: 16px; font-weight: 500; color: #C4C0BA; letter-spacing: 3px; text-transform: uppercase;">growthbykanchan</div>
</div>
```

---

## VARIATION B: Myth Buster / Contrarian

Best for: "X lies about Y", "X myths debunked", "Stop doing X"

### B — Cover slide

```html
<div class="slide" style="width:1080px; height:1350px; background: #E8E4DE; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Subtle paper texture via grid -->
  <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(0,0,0,0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.02) 1px, transparent 1px); background-size: 30px 30px; pointer-events: none;"></div>

  <div style="position: relative; padding: 80px; display: flex; flex-direction: column; height: 100%;">
    <!-- Title -->
    <h1 style="font-size: 72px; font-weight: 800; color: #1A1A1A; line-height: 1.1; margin: 0 0 8px 0; text-transform: uppercase;">10 Leadership Lies</h1>
    <div style="display: inline-block; background: #3BBFAD; padding: 4px 16px; margin: 0 0 32px 0; align-self: flex-start;">
      <span style="font-size: 56px; font-weight: 800; color: #1A1A1A; text-transform: uppercase;">Holding You Back</span>
    </div>

    <!-- Visual area (description for AI-generated illustration or metaphor) -->
    <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
      <!-- If an illustration/image is available, place it here -->
      <!-- Otherwise, use a large visual metaphor with typography -->
      <div style="text-align: center;">
        <p style="font-size: 120px; line-height: 1; color: #8B6F47; font-weight: 800; opacity: 0.15;">?!</p>
      </div>
    </div>

    <!-- Subtitle -->
    <p style="font-size: 28px; color: #4A4A4A; margin: 0;">And <span style="background: #F5D76E; padding: 2px 8px; font-weight: 700; color: #1A1A1A;">the hard truth</span> to tell yourself instead</p>
  </div>
</div>
```

### B — Myth content slide

```html
<div class="slide" style="width:1080px; height:1350px; background: #E8E4DE; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(0,0,0,0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.02) 1px, transparent 1px); background-size: 30px 30px; pointer-events: none;"></div>

  <div style="position: relative; padding: 80px; display: flex; flex-direction: column; justify-content: center; height: 100%;">
    <!-- The myth (headline) -->
    <h2 style="font-size: 52px; font-weight: 800; color: #1A1A1A; line-height: 1.15; margin: 0 0 48px 0;">A Great Leader Has All The Answers</h2>

    <!-- The reality -->
    <div style="margin: 0 0 32px 0;">
      <div style="display: inline-block; background: #F5D76E; padding: 4px 14px; margin: 0 0 16px 0;">
        <span style="font-size: 20px; font-weight: 700; color: #1A1A1A;">The hard truth:</span>
      </div>
      <p style="font-size: 26px; color: #4A4A4A; line-height: 1.5; margin: 0;">The best leaders ask the best questions.</p>
    </div>

    <!-- The tip -->
    <div style="margin: 0;">
      <div style="display: inline-block; background: #F5D76E; padding: 4px 14px; margin: 0 0 16px 0;">
        <span style="font-size: 20px; font-weight: 700; color: #1A1A1A;">Tip:</span>
      </div>
      <p style="font-size: 26px; color: #4A4A4A; line-height: 1.5; margin: 0;">Instead of settling for your answer, focus on developing a team that can find <strong style="color: #1A1A1A; text-decoration: underline;">the best answers</strong>.</p>
    </div>
  </div>
</div>
```

### B — CTA slide

```html
<div class="slide" style="width:1080px; height:1350px; background: #E8E4DE; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(0,0,0,0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.02) 1px, transparent 1px); background-size: 30px 30px; pointer-events: none;"></div>

  <div style="position: relative; padding: 80px; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; text-align: center;">
    <!-- Closing thought -->
    <p style="font-size: 28px; color: #4A4A4A; line-height: 1.5; margin: 0 0 16px 0; max-width: 700px;">The hard part was never building your coach.</p>
    <p style="font-size: 28px; color: #4A4A4A; line-height: 1.5; margin: 0 0 56px 0; max-width: 700px;">It's <strong style="color: #1A1A1A;">making a habit</strong> of listening to its advice critically and <strong style="color: #1A1A1A;">taking consistent action</strong>.</p>

    <!-- Follow CTA -->
    <div style="margin: 0 0 32px 0;">
      <span style="font-size: 48px; font-weight: 800; color: #1A1A1A;"><span style="background: #F5D76E; padding: 2px 12px;">Follow Me</span> On LinkedIn</span>
    </div>

    <!-- Arrow pointing to headshot -->
    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" style="margin: 0 0 16px 0; transform: rotate(90deg);"><path d="M12 5V19M12 19L5 12M12 19L19 12" stroke="#F5D76E" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>

    <!-- Enlarged author -->
    <div style="margin: 0 0 16px 0;">
      <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="120" height="120"
           style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 4px solid #C4956A;" />
    </div>
    <p style="font-size: 28px; font-weight: 700; color: #1A1A1A; margin: 0;">Kanchan Bhatta</p>
    <p style="font-size: 18px; color: #8B8B8B; margin: 8px 0 0 0;">@growthbykanchan</p>
  </div>
</div>
```

---

## VARIATION C: Step-by-Step / How-To

Best for: "How to X in Y steps", "The complete guide to Z"

### C — Cover slide

```html
<div class="slide" style="width:1080px; height:1350px; background: #FBF8F4; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(0,0,0,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.03) 1px, transparent 1px); background-size: 40px 40px; pointer-events: none;"></div>

  <div style="position: relative; padding: 100px 80px; display: flex; flex-direction: column; height: 100%;">
    <!-- Author pill -->
    <div style="display: flex; align-items: center; gap: 12px; margin: 0 0 60px 0;">
      <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="48" height="48" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover;" />
      <span style="font-size: 18px; font-weight: 600; color: #1A1A1A;">Kanchan Bhatta</span>
    </div>

    <!-- Step count badge -->
    <div style="display: inline-flex; align-items: center; justify-content: center; background: #8B6F47; border-radius: 12px; padding: 8px 20px; margin: 0 0 32px 0; align-self: flex-start;">
      <span style="font-size: 18px; font-weight: 700; color: #FFFFFF;">7-STEP GUIDE</span>
    </div>

    <!-- Title -->
    <h1 style="font-size: 56px; font-weight: 800; color: #1A1A1A; line-height: 1.15; margin: 0 0 24px 0;">How to Build a <span style="color: #8B6F47;">Content System</span> That Runs Itself</h1>

    <!-- Subtitle -->
    <p style="font-size: 24px; color: #8B8B8B; line-height: 1.5; margin: 0;">A practical framework for busy founders</p>

    <!-- Swipe indicator bottom -->
    <div style="margin-top: auto; display: flex; align-items: center; gap: 12px;">
      <span style="font-size: 16px; color: #8B8B8B;">Swipe to start</span>
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#8B8B8B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>
  </div>
</div>
```

### C — Context / problem slide

```html
<div class="slide" style="width:1080px; height:1350px; background: #F5F0EA; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Author pill top -->
  <div style="display: flex; align-items: center; justify-content: center; gap: 10px; padding-top: 56px;">
    <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="44" height="44" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #E8E4DE;" />
    <span style="font-size: 18px; font-weight: 600; color: #1A1A1A;">Kanchan Bhatta</span>
  </div>

  <div style="padding: 60px 80px; display: flex; flex-direction: column; justify-content: center; flex: 1;">
    <!-- Section label -->
    <p style="font-size: 16px; font-weight: 600; color: #8B6F47; letter-spacing: 2px; text-transform: uppercase; margin: 0 0 24px 0;">The Problem</p>

    <h2 style="font-size: 44px; font-weight: 700; color: #1A1A1A; line-height: 1.2; margin: 0 0 32px 0;">Most founders create content reactively, not systematically.</h2>

    <p style="font-size: 24px; color: #4A4A4A; line-height: 1.6; margin: 0;">They post when inspiration strikes, go silent for weeks, then wonder why their audience isn't growing.</p>
  </div>

  <!-- Brand + dots bottom -->
  <div style="position: absolute; bottom: 40px; left: 0; right: 0; text-align: center;">
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 16px;">
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #8B9E8B;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
    </div>
  </div>
</div>
```

### C — Step slide

```html
<div class="slide" style="width:1080px; height:1350px; background: #FBF8F4; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Author pill top -->
  <div style="display: flex; align-items: center; justify-content: center; gap: 10px; padding-top: 56px;">
    <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="44" height="44" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #F5F0EA;" />
    <span style="font-size: 18px; font-weight: 600; color: #1A1A1A;">Kanchan Bhatta</span>
  </div>

  <div style="padding: 48px 80px; display: flex; flex-direction: column; justify-content: center; flex: 1;">
    <!-- Step number -->
    <p style="font-size: 100px; font-weight: 800; color: #8B6F47; line-height: 1; margin: 0 0 8px 0; opacity: 0.9;">01</p>

    <!-- Step title -->
    <h2 style="font-size: 44px; font-weight: 700; color: #1A1A1A; line-height: 1.2; margin: 0 0 32px 0;">Define Your Content Pillars</h2>

    <!-- Step explanation in card -->
    <div style="background: #FFFFFF; border-radius: 16px; padding: 36px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.04);">
      <p style="font-size: 22px; color: #4A4A4A; line-height: 1.6; margin: 0 0 20px 0;">Pick 3-5 topics that sit at the intersection of your expertise and your audience's biggest pain points.</p>
      <div style="border-top: 1px solid rgba(0,0,0,0.06); padding-top: 20px;">
        <p style="font-size: 18px; color: #8B8B8B; margin: 0;"><strong style="color: #8B6F47;">Example:</strong> For a SaaS founder — product strategy, hiring, fundraising, growth tactics.</p>
      </div>
    </div>
  </div>

  <!-- Dots + brand bottom -->
  <div style="position: absolute; bottom: 40px; left: 0; right: 0; text-align: center;">
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 16px;">
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #8B9E8B;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
    </div>
    <p style="font-size: 14px; font-weight: 500; color: #C4C0BA; letter-spacing: 2px; text-transform: uppercase;">growthbykanchan</p>
  </div>
</div>
```

### C — Recap slide

```html
<div class="slide" style="width:1080px; height:1350px; background: #F5F0EA; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="display: flex; align-items: center; justify-content: center; gap: 10px; padding-top: 56px;">
    <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="44" height="44" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #E8E4DE;" />
    <span style="font-size: 18px; font-weight: 600; color: #1A1A1A;">Kanchan Bhatta</span>
  </div>

  <div style="padding: 40px 80px; flex: 1;">
    <p style="font-size: 16px; font-weight: 600; color: #8B6F47; letter-spacing: 2px; text-transform: uppercase; margin: 0 0 24px 0;">Quick Recap</p>
    <h2 style="font-size: 40px; font-weight: 700; color: #1A1A1A; line-height: 1.2; margin: 0 0 36px 0;">Your 7-Step System</h2>

    <table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
      <tr>
        <td style="vertical-align: top; padding: 0 16px 20px 0; width: 48px;">
          <span style="font-size: 24px; font-weight: 800; color: #8B6F47;">01</span>
        </td>
        <td style="vertical-align: top; padding: 0 0 20px 0;">
          <p style="font-size: 22px; color: #1A1A1A; font-weight: 600; margin: 0;">Define Your Content Pillars</p>
        </td>
      </tr>
      <tr>
        <td style="vertical-align: top; padding: 0 16px 20px 0; width: 48px;">
          <span style="font-size: 24px; font-weight: 800; color: #8B6F47;">02</span>
        </td>
        <td style="vertical-align: top; padding: 0 0 20px 0;">
          <p style="font-size: 22px; color: #1A1A1A; font-weight: 600; margin: 0;">Build a Content Calendar</p>
        </td>
      </tr>
      <!-- Repeat for each step -->
    </table>
  </div>

  <div style="position: absolute; bottom: 40px; left: 0; right: 0; text-align: center; font-size: 14px; font-weight: 500; color: #C4C0BA; letter-spacing: 2px; text-transform: uppercase;">growthbykanchan</div>
</div>
```

---

## VARIATION D: Insights & Lessons

Best for: "X lessons I learned", "X tips for Y", "X things I wish I knew"

### D — Cover slide

```html
<div class="slide" style="width:1080px; height:1350px; background: linear-gradient(180deg, #FBF8F4 0%, #F0EBE3 100%); font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(0,0,0,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.03) 1px, transparent 1px); background-size: 40px 40px; pointer-events: none;"></div>

  <div style="position: relative; padding: 100px 80px; display: flex; flex-direction: column; height: 100%;">
    <!-- Author -->
    <div style="display: flex; align-items: center; gap: 12px; margin: 0 0 80px 0;">
      <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="52" height="52" style="width: 52px; height: 52px; border-radius: 50%; object-fit: cover;" />
      <div>
        <p style="font-size: 18px; font-weight: 600; color: #1A1A1A; margin: 0;">Kanchan Bhatta</p>
        <p style="font-size: 14px; color: #8B8B8B; margin: 0;">@growthbykanchan</p>
      </div>
    </div>

    <!-- Number -->
    <p style="font-size: 140px; font-weight: 800; color: #8B6F47; line-height: 0.85; margin: 0 0 20px 0; opacity: 0.9;">12</p>

    <!-- Title -->
    <h1 style="font-size: 52px; font-weight: 700; color: #1A1A1A; line-height: 1.15; margin: 0 0 20px 0;">Lessons I Learned<br>Building a <span style="color: #8B6F47;">6-Figure</span><br>Newsletter</h1>

    <!-- Subtitle -->
    <p style="font-size: 22px; color: #8B8B8B; line-height: 1.5; margin: 0;">From zero to 50K subscribers in 18 months</p>

    <!-- Swipe -->
    <div style="margin-top: auto; display: flex; align-items: center; gap: 12px;">
      <div style="display: inline-flex; align-items: center; justify-content: center; background: #8B6F47; border-radius: 20px; padding: 10px 18px;">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
    </div>
  </div>
</div>
```

### D — Insight slide (primary layout)

```html
<div class="slide" style="width:1080px; height:1350px; background: #FBF8F4; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Author pill top -->
  <div style="display: flex; align-items: center; justify-content: center; gap: 10px; padding-top: 56px;">
    <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="44" height="44" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #F5F0EA;" />
    <span style="font-size: 18px; font-weight: 600; color: #1A1A1A;">Kanchan Bhatta</span>
    <svg width="18" height="18" viewBox="0 0 24 24" fill="#8B6F47"><path d="M12 2L14.09 8.26L21 9.27L16 14.14L17.18 21.02L12 17.77L6.82 21.02L8 14.14L3 9.27L9.91 8.26L12 2Z"/></svg>
  </div>

  <div style="padding: 48px 80px; display: flex; flex-direction: column; justify-content: center; flex: 1;">
    <!-- Insight number -->
    <p style="font-size: 80px; font-weight: 800; color: #8B6F47; line-height: 1; margin: 0 0 16px 0; opacity: 0.8;">03</p>

    <!-- Insight headline -->
    <h2 style="font-size: 44px; font-weight: 700; color: #1A1A1A; line-height: 1.2; margin: 0 0 36px 0;">Consistency Beats<br>Perfection Every Time</h2>

    <!-- Explanation -->
    <p style="font-size: 24px; color: #4A4A4A; line-height: 1.6; margin: 0 0 32px 0;">I spent months crafting "perfect" posts that got 50 views. Then I started publishing daily rough drafts that got 5,000.</p>

    <!-- Key takeaway in highlight -->
    <div style="display: inline-block; background: rgba(245,215,110,0.3); padding: 16px 24px; border-radius: 12px; align-self: flex-start;">
      <p style="font-size: 20px; font-weight: 600; color: #1A1A1A; margin: 0;">Ship fast. Iterate later. Your audience will teach you what works.</p>
    </div>
  </div>

  <!-- Dots + brand -->
  <div style="position: absolute; bottom: 40px; left: 0; right: 0; text-align: center;">
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 16px;">
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #8B9E8B;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
    </div>
    <p style="font-size: 14px; font-weight: 500; color: #C4C0BA; letter-spacing: 2px; text-transform: uppercase;">growthbykanchan</p>
  </div>
</div>
```

### D — Insight slide (card layout — alternate)

Use this for every other insight to create visual variety:

```html
<div class="slide" style="width:1080px; height:1350px; background: #F5F0EA; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Author pill top -->
  <div style="display: flex; align-items: center; justify-content: center; gap: 10px; padding-top: 56px;">
    <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="44" height="44" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #E8E4DE;" />
    <span style="font-size: 18px; font-weight: 600; color: #1A1A1A;">Kanchan Bhatta</span>
    <svg width="18" height="18" viewBox="0 0 24 24" fill="#8B6F47"><path d="M12 2L14.09 8.26L21 9.27L16 14.14L17.18 21.02L12 17.77L6.82 21.02L8 14.14L3 9.27L9.91 8.26L12 2Z"/></svg>
  </div>

  <div style="padding: 48px 80px; display: flex; flex-direction: column; justify-content: center; flex: 1;">
    <!-- Insight number + title -->
    <p style="font-size: 80px; font-weight: 800; color: #8B6F47; line-height: 1; margin: 0 0 16px 0; opacity: 0.8;">04</p>
    <h2 style="font-size: 44px; font-weight: 700; color: #1A1A1A; line-height: 1.2; margin: 0 0 32px 0;">Your First 100 Posts<br>Are Just Practice</h2>

    <!-- Explanation in white card -->
    <div style="background: #FFFFFF; border-radius: 16px; padding: 36px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.04);">
      <p style="font-size: 22px; color: #4A4A4A; line-height: 1.6; margin: 0 0 20px 0;">Nobody remembers your early work. But the skills you build during those first 100 posts compound for the rest of your career.</p>
      <div style="background: rgba(245,215,110,0.3); padding: 14px 20px; border-radius: 10px;">
        <p style="font-size: 18px; font-weight: 600; color: #1A1A1A; margin: 0;">Give yourself permission to be bad. That's how you get good.</p>
      </div>
    </div>
  </div>

  <!-- Dots + brand -->
  <div style="position: absolute; bottom: 40px; left: 0; right: 0; text-align: center;">
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 16px;">
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #D4D0CA;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #8B9E8B;"></div>
    </div>
    <p style="font-size: 14px; font-weight: 500; color: #C4C0BA; letter-spacing: 2px; text-transform: uppercase;">growthbykanchan</p>
  </div>
</div>
```

### D — Key takeaway slide (before CTA)

```html
<div class="slide" style="width:1080px; height:1350px; background: #FBF8F4; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="display: flex; align-items: center; justify-content: center; gap: 10px; padding-top: 56px;">
    <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="44" height="44" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #F5F0EA;" />
    <span style="font-size: 18px; font-weight: 600; color: #1A1A1A;">Kanchan Bhatta</span>
  </div>

  <div style="padding: 48px 80px; display: flex; flex-direction: column; align-items: center; justify-content: center; flex: 1; text-align: center;">
    <p style="font-size: 16px; font-weight: 600; color: #8B6F47; letter-spacing: 2px; text-transform: uppercase; margin: 0 0 32px 0;">The Biggest Takeaway</p>

    <h2 style="font-size: 48px; font-weight: 700; color: #1A1A1A; line-height: 1.2; margin: 0 0 32px 0; max-width: 750px;">Building an audience is a <span style="background: #F5D76E; padding: 0 8px;">marathon</span>, not a sprint.</h2>

    <p style="font-size: 24px; color: #4A4A4A; line-height: 1.6; margin: 0; max-width: 650px;">The creators who win aren't the most talented. They're the ones who keep showing up when everyone else quits.</p>
  </div>

  <div style="position: absolute; bottom: 40px; left: 0; right: 0; text-align: center; font-size: 14px; font-weight: 500; color: #C4C0BA; letter-spacing: 2px; text-transform: uppercase;">growthbykanchan</div>
</div>
```

---

## CTA Slide — LinkedIn Profile Card Style (works with ALL variations)

This CTA style shows a mock LinkedIn profile card with a prominent +Follow button:

```html
<div class="slide" style="width:1080px; height:1350px; background: #F5F0EA; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; padding: 80px;">

    <!-- LinkedIn profile card mockup -->
    <div style="background: #FFFFFF; border-radius: 20px; box-shadow: 0 8px 40px rgba(0,0,0,0.1); overflow: hidden; max-width: 700px; width: 100%;">
      <!-- Banner -->
      <div style="height: 120px; background: linear-gradient(135deg, #1A365D 0%, #2D5A87 100%);"></div>

      <!-- Profile section -->
      <div style="padding: 0 36px 36px; position: relative;">
        <!-- Headshot overlapping banner -->
        <div style="margin-top: -50px; margin-bottom: 16px;">
          <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="100" height="100"
               style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 4px solid #FFFFFF;" />
        </div>

        <p style="font-size: 24px; font-weight: 700; color: #1A1A1A; margin: 0 0 4px 0;">Kanchan Bhatta</p>
        <p style="font-size: 16px; color: #4A4A4A; margin: 0 0 8px 0;">Growth strategist | Helping founders scale with content</p>
        <p style="font-size: 14px; color: #8B8B8B; margin: 0;">@growthbykanchan</p>
      </div>
    </div>

    <!-- Follow CTA button -->
    <div style="margin-top: 32px;">
      <div style="background: #8B6F47; border-radius: 30px; padding: 18px 48px; display: inline-flex; align-items: center; gap: 10px; box-shadow: 0 4px 16px rgba(139,111,71,0.3);">
        <span style="font-size: 24px; font-weight: 700; color: #FFFFFF;">+Follow</span>
      </div>
    </div>

    <!-- Closing message -->
    <p style="font-size: 18px; color: #8B8B8B; margin: 32px 0 0 0; text-align: center; max-width: 500px;">Follow for weekly insights on growth, content strategy, and building in public.</p>
  </div>
</div>
```

---

## CTA Slide — Simple Follow Style (alternative, works with ALL variations)

```html
<div class="slide" style="width:1080px; height:1350px; background: #FBF8F4; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; padding: 80px; text-align: center;">

    <!-- Closing thought -->
    <p style="font-size: 24px; color: #4A4A4A; line-height: 1.6; margin: 0 0 48px 0; max-width: 650px;">If you found this valuable, share it with someone who needs it.</p>

    <!-- Follow text -->
    <p style="font-size: 44px; font-weight: 800; color: #1A1A1A; margin: 0 0 40px 0;">Follow for more</p>

    <!-- Enlarged headshot -->
    <img src="data:image/jpeg;base64,{HEADSHOT_B64}" width="120" height="120"
         style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 4px solid #C4956A; margin: 0 0 20px 0;" />

    <p style="font-size: 28px; font-weight: 700; color: #1A1A1A; margin: 0;">Kanchan Bhatta</p>
    <p style="font-size: 18px; color: #8B8B8B; margin: 8px 0 0 0;">@growthbykanchan</p>

    <!-- Social actions row -->
    <div style="display: flex; gap: 24px; margin-top: 40px;">
      <div style="background: #FFFFFF; border-radius: 12px; padding: 12px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
        <span style="font-size: 16px; color: #4A4A4A;">Like</span>
      </div>
      <div style="background: #FFFFFF; border-radius: 12px; padding: 12px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
        <span style="font-size: 16px; color: #4A4A4A;">Comment</span>
      </div>
      <div style="background: #FFFFFF; border-radius: 12px; padding: 12px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
        <span style="font-size: 16px; color: #4A4A4A;">Repost</span>
      </div>
    </div>
  </div>
</div>
```

---

## Summary of Variations

| Variation | Cover Style | Content Slides | CTA Style |
|---|---|---|---|
| **A — Tool Showcase** | Giant number + title + icon grid | Logo card + screenshot/description | Profile card + Follow |
| **B — Myth Buster** | Bold title + highlight + subtitle | Myth headline + yellow label sections | Closing thought + Follow Me highlight |
| **C — Step-by-Step** | Author + badge + title + subtitle | Step number + title + card explanation | Recap + Follow |
| **D — Insights** | Author + number + title | Number + headline + explanation/card | Takeaway + Follow |

All variations share:
- Warm cream/beige palette
- White cards with subtle shadows
- Yellow highlight boxes for labels
- Author headshot presence on most slides
- Brand watermark on content slides
- Dot navigation at bottom
- Clean, professional typography with no emojis
- 12-18 slide target count

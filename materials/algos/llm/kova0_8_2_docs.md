---
title: "Build Animations - Kova Documentation"
source: "https://wiki.kova.md/animations/"
author:
published:
created: 2026-11-08
description:
tags:
  - "clippings"
---
## Build Animations

Mark any bullet, image, code block, table, formula, diagram, blockquote, or a handful of other elements with `<!-- step -->` and it appears on its own click during a presentation, instead of the whole slide landing at once — build/reveal animations, the same idea as PowerPoint's "Animations" or reveal.js fragments.

A slide with no `<!-- step -->` markers behaves exactly as before — this is entirely opt-in.

> [!tip] Full worked example
> [`examples/animations-demo.md`](https://github.com/KovaMD/Kova/blob/main/examples/animations-demo.md) in the app repo is a complete tour of every marker form across every supported content type — open it in Kova and step through it in Presentation mode.

---

## Basic syntax

```markdown
- Always visible from the start
- Appears on the first click <!-- step -->
- Appears on the second click <!-- step -->
- Appears on the third click <!-- step -->
```

`<!-- step -->` auto-increments in document order — no numbers to manage. Steps are scoped per slide; the count resets to 1 after every slide separator (`---`).

### Grouping elements onto one click

Add an explicit number to group several elements onto the same click:

```markdown
- Revealed alone, first click <!-- step -->
- These two <!-- step: 2 -->
- arrive together <!-- step: 2 -->
- Back to auto-increment <!-- step -->
```

A later bare `<!-- step -->` continues counting from the highest explicit number used so far, rather than colliding with it.

### Placement

The marker either trails inline after a paragraph or list item, or — for a block element with no text to trail onto — sits alone on the line directly underneath it:

```markdown
![A chart](chart.png)
<!-- step -->
```

This is the same "must directly follow" convention `!caption` already uses. A `<!-- step -->` with no eligible element directly above it, or a second one stacked on an element that already has one, reports a clear `#ERR` rather than silently vanishing.

---

## What can be stepped

| Element | Notes |
| --- | --- |
| List items | Nested/sub-bullets share the same per-slide click sequence as their parents |
| A whole list | A marker placed after the *list* (not each item) gates every item as one unit — any per-item markers inside that list are cleared automatically |
| Images |  |
| Code blocks |  |
| Tables | The whole table appears together — tables build as one unit, not row by row |
| Display math (`$$...$$`) |  |
| Mermaid diagrams |  |
| Blockquotes and callouts |  |
| `!youtube`, `!video`, `!poll` embeds |  |
| `!progress` bars |  |
| `!toc` |  |

Paragraphs and list items take the marker trailing inline; every other type in the list above takes it on its own line directly underneath, per [Placement](#placement).

---

## Presenting

A "next" action (click, `→`, `Space`, scroll down, …) advances through the current slide's remaining steps one at a time before it moves to the next slide. Going backward across a slide boundary lands on the previous slide fully revealed (its last step), not back at its start — the least surprising place to arrive from when stepping backward. See [Keyboard Shortcuts — Presentation mode](https://wiki.kova.md/keyboard-shortcuts/#presentation-mode) for the full key list.

This works identically in **single-screen mode**, the **dual-screen presenter view** (both the audience window and the presenter's own next-slide preview stay in sync), and the **standalone HTML export** — see [Presenting](https://wiki.kova.md/presenting/) and [Exporting — Standalone HTML export](https://wiki.kova.md/exporting/#standalone-html-export).

> [!note] Editor preview always shows everything
> The live preview in the editor is for editing, not rehearsing — it always shows a slide fully revealed regardless of step markers. Use Presentation mode to see builds actually happen.

---

## Editor support

Right-click a line and choose **Reveal on click** (or press `Ctrl+Shift+R`, `Cmd+Shift+R` on macOS) to toggle a step marker on it without typing the comment by hand. Selecting multiple lines toggles all of them together: if any already has a marker they're all removed, otherwise every line gets one, sharing a single step so they build together on one click.

Each marker shows a small **`· N`** badge next to it in the editor, computed the same way the presentation numbers its clicks — so what you see while editing can never drift from what the presentation actually does.

---

## Export behaviour

**PowerPoint export** — steps become real, native click-triggered animations in the `.pptx` file (not a flattened, always-visible placeholder), built from hand-authored OOXML timing data.

> [!warning] Hand-authored timing data — report decks that misbehave
> The `.pptx` animation timing is written by hand from the OOXML spec rather than produced by a PowerPoint library. It has been tested in both **LibreOffice Impress** and **Microsoft PowerPoint**, with several bugs fixed in v0.7.9, but edge cases are still possible on complex slides. If a build animation doesn't play correctly, please [open an issue](https://github.com/KovaMD/Kova/issues) and attach the deck.

A `<!-- step -->` on the [`quote`](https://wiki.kova.md/layouts/#quote) layout's hero quote, or on the video/poll embed in a full-slide [`media`](https://wiki.kova.md/layouts/#media) layout, is a known, bounded gap: it still gates the live preview, presentation, and HTML export normally, but exports to PowerPoint unanimated — visible immediately, the same as before this feature existed.

**PDF export and Print** — both capture each slide in its final, fully-revealed state as a single page; steps don't produce extra pages. See [Exporting](https://wiki.kova.md/exporting/).

---

## Errors

| Situation | Result |
| --- | --- |
| `<!-- step -->` with no eligible element directly above it | `#ERR <!-- step --> must directly follow a list, image, diagram, formula, table, blockquote, code block, YouTube embed, video, poll, progress bar, or table of contents` |
| A second marker stacked on an element that already has one | `#ERR duplicate <!-- step --> marker` |

As with other Kova directives, an error is scoped to that one spot — the rest of the slide still renders normally.


Kova supports a set of presentation-specific Markdown extensions, plus standard Markdown via [remark](https://remark.js.org/), GitHub Flavored Markdown (GFM) tables, Mermaid diagrams, and LaTeX math via KaTeX.

---

## Kova-specific syntax

### Column break (|||)

Force a two-column layout by placing `|||` between two content blocks on the same slide:

```markdown
## Comparing approaches

**Traditional tools**

- Manual layout adjustments
- Vendor lock-in
- Export quality varies

|||

**Kova**

- Layout detected automatically
- Plain \`.md\` files
- Native \`.pptx\` export
```

Kova splits the slide at the `|||` and renders each side as a column. See [Layouts — two-column](https://wiki.kova.md/layouts/#two-column) for details.

> [!tip] Three columns
> Add a **second** `|||` to split into three columns instead of two. See [Layouts — three-column](https://wiki.kova.md/layouts/#three-column).

---

### Progress bars (!progress)

```markdown
!progress[Task Complete](75)
!progress[In Review](40)
!progress[Planned](10)
```

Numbers represent percentages from 0 to 100; decimals are allowed (`!progress[Almost there](99.5)`).

Multiple consecutive `!progress` bars are grouped as a single logical unit for layout detection — they won't accidentally trigger the `grid` layout.

> [!tip] Progress bars inside table cells
> A `!progress[label](value)` directive also works inside a Markdown table cell, rendered as a compact bar meter in place of the raw text:
> 
> ```markdown
> | Feature | Status |
> |---------|--------|
> | Preview | !progress[Task Complete](75) |
> ```
> 
> It also works with a formula value inside a [computed `!sheet` table](#computed-tables-sheet), including in a footer row:
> 
> ```markdown
> !sheet
> | item   | qty | unit  | total                          |
> |--------|----:|------:|--------------------------------|
> | motor  |   3 | 12.50 | =qty * unit                    |
> | ESC    |   2 |  8.00 | =qty * unit                    |
> | !Total |     |       | !progress[Done](=sum(total))   |
> ```
> 
> PowerPoint export can't place a real bar shape inside a table cell, so it renders a text meter instead — label, a 10-block filled/empty bar, and the percentage (e.g. `Task Complete  ████████░░  75%`) — rather than running the label and number together as plain text.

---

### YouTube embed (!youtube)

```markdown
!youtube[Video Title](https://youtu.be/VIDEO_ID)
```

Displays the video thumbnail on the slide. During presentation, clicking the thumbnail opens the video in the default browser.

> [!note] Export behaviour
> YouTube embeds export to PowerPoint as a linked online video that plays in desktop PowerPoint, falling back to a text placeholder with the URL if the video ID can't be parsed. In PDF export they appear as a static placeholder. See [Exporting](https://wiki.kova.md/exporting/#limitations_1).

---

### Local video (!video)

```markdown
!video[Demo walkthrough](assets/demo.mp4)
```

Embeds a local video file, playable inline on the slide during presentation. Drag a video file onto the editor, or paste one from the clipboard, and Kova inserts the `!video[]()` reference automatically — the same drop/paste handling used for images (see [Getting Started](https://wiki.kova.md/getting-started/#step-7-open-and-insert-files)). Supported formats: `.mp4`, `.webm`, `.ogv`, `.mov`, `.m4v`, `.mkv`.

A video that's the **only** element on a slide gets the full-slide `media` layout (see [Layouts](https://wiki.kova.md/layouts/#media)). A video alongside other content instead flows through Kova's normal layout rules, the same as an image.

> [!note] Export behaviour
> PDF export shows a local video as a static frame. PowerPoint export embeds it as a playable video, inlined into the `.pptx` (which grows its file size), falling back to a text placeholder with the label and file path if the file can't be read. **Standalone HTML export** also embeds it as a real, playable file. See [Exporting](https://wiki.kova.md/exporting/).

---

### Build animations (<!-- step -->)

Mark an element with `<!-- step -->` and it appears on its own click during a presentation instead of the whole slide landing at once:

```markdown
- Always visible from the start
- Appears on the first click <!-- step -->
- Appears on the second click <!-- step -->
```

`<!-- step -->` auto-increments; `<!-- step: N -->` groups several elements onto the same click. It works on list items, images, code blocks, tables, display math, Mermaid diagrams, blockquotes, and more. See [Build Animations](https://wiki.kova.md/animations/) for the full syntax, editor toggle, presenting behaviour, and export support.

---

### Table of Contents (!toc)

```markdown
!toc
```

Renders a clickable list of every titled slide in the presentation — useful as an agenda or overview slide. The list is built automatically from your slide titles (the deck's opening title slide is excluded), so it stays in sync as you add, remove, or reorder slides.

By default entries are numbered; toggle **Table of contents → Numbered list** off in the Inspector's Document section for a plain, bare hyperlinked list instead. See [Themes — Inspector overrides](https://wiki.kova.md/themes/#inspector-overrides).

Right-click in the editor and choose **Insert → Table of Contents** to add an `## Agenda` slide with `!toc` in one step.

During a presentation, clicking an entry jumps straight to that slide — from the presenter overlay, the single-screen view, or the audience display in dual-screen or mirror mode. A `!toc` list long enough to overflow the slide automatically splits into two columns, the same overflow handling used for dense text slides (see [Layouts](https://wiki.kova.md/layouts/#two-column)).

---

### Poll / QR code (!poll)

```markdown
!poll[What is your biggest challenge?](https://pollev.com/your-poll)
```

Renders a scannable QR code pointing to the URL, plus the URL as text — useful for live audience interaction with [Poll Everywhere](https://polleverywhere.com/) or any URL-based polling tool. During a presentation, clicking the QR code also opens the URL in your system's default browser.

---

### Academic references (!ref)

Attach source citations to any slide using `!ref[...]` lines:

```markdown
!ref[Smith et al. (2024). *The Impact of AI on Education*. Journal of Learning Technologies, 12(3), 45–67.]
!ref[Jones, A. (2023). Pedagogical frameworks for Markdown-native tools. Open Education Review.]
```

References appear as small, muted text at the **bottom-right** of the slide, stacked vertically. They are styled to be unobtrusive — readable as annotations without competing with slide content. The colour automatically adapts to the active theme (greyed on light themes, softened white on dark themes).

Multiple `!ref` lines on the same slide are listed in the order they appear in the Markdown.

**PowerPoint export** — references are included in `.pptx` output as a 7 pt right-aligned text block placed just above the footer, so citations survive the export intact.

In the editor, go to **Insert → Reference** (right-click menu) to place a `!ref[]` placeholder with the cursor inside, ready to type.

---

### Icons (:name:)

Drop an icon into your text with an inline `:name:` shortcode. Kova bundles 180 icons, so there's nothing to install:

```markdown
## Launch checklist

- :check-circle: Tests passing
- :rocket: Ship on Friday
```

Icons take the size and colour of the surrounding text, and work in paragraphs, list items, table cells, and bold or italic text. A slide's title (its first heading) and code are never converted, and a name Kova doesn't recognise is left as typed.

**PowerPoint export** — icons are written as text in the `Kova Icons` font, which isn't embedded in the `.pptx`, so PowerPoint and Keynote only show them on machines where that font is installed.

See [Icons](https://wiki.kova.md/icons/) for every available name, how to swap the icon font in a theme, and how icons export.

---

### Slide background images (!\[bg\])

Place a `![bg](...)` line anywhere on a slide to set a full-slide background image, Marp-style:

```markdown
## Quarterly results

![bg](./photos/skyline.jpg)

Revenue is up 22% year over year.
```

| Syntax | Effect |
| --- | --- |
| `![bg](photo.jpg)` | Full-slide background, cropped to fill (`cover`) |
| `![bg left](photo.jpg)` | Background fills the **left** half only; content occupies the right |
| `![bg right](photo.jpg)` | Background fills the **right** half only; content occupies the left |
| `![bg contain](photo.jpg)` or `![bg fit](photo.jpg)` | Background is scaled to fit without cropping instead of covering |

Only the first `![bg]` line on a slide is used, and the line is stripped from the rendered content — it doesn't affect layout detection or show up as a broken image. It's ignored inside fenced code blocks.

> [!tip] Set a background from the Slides panel
> Right-click a slide thumbnail and choose **Set slide background…** to pick an image file without typing the syntax, or **Clear background** to remove it. This edits the underlying `![bg]` line for you.

Background images are included in PowerPoint export.

---

## Computed tables (!sheet)

Annotate a GFM table with `!sheet` and Kova computes it: formula cells like `=qty * unit` are evaluated live, on every keystroke. The source keeps the formulas, never the cached results, so a deck can't silently go stale when an input changes.

```markdown
!let vat = 0.255

!sheet
| item   | qty | unit  | total                   |
|--------|----:|------:|------------------------:|
| motor  |   2 | 12.50 | =qty * unit             |
| ESC    |   2 |  8.00 | =qty * unit             |
| !Total |     |       | =sum(total) * (1 + vat) |
```

This renders as an ordinary-looking table with every `=…` cell replaced by its computed value.

> [!note] !sheet must sit directly above the table
> No blank line between them — `!sheet` annotates whichever table comes immediately next. A table with no `!sheet` line above it is left untouched, even if a cell's text starts with `=`.

### Row formulas vs. footer formulas

- A **data row** formula (`=qty * unit`) — a bare column name means *this row's* value in that column.
- A row whose first cell starts with `!` is a **footer row** (`| !Total | … |`) — the leading `!` is stripped when rendered. Inside a footer formula, a bare column name means *the whole column* (other footer rows are never counted in it).
- Column names come from the header: lowercased, punctuation dropped, spaces turned to underscores — `Unit (€)` becomes `unit`.

### Document-wide constants (!let)

```markdown
!let vat = 0.255
!let base = 10
```

Declare a `!let` anywhere in the document and every `!sheet` table in the file can reference it, regardless of which slide it's declared on. The right-hand side is a literal or an expression over *earlier* constants — never over table data.

### Operators and functions

| Category | Supported |
| --- | --- |
| Arithmetic | `+` `-` `*` `/` `%` `^` (`^` is right-associative: `2^3^2` = 512, not 64) |
| Comparison | `==` `!=` `<` `<=` `>` `>=` |
| Logic | `and` `or` `not`, and the ternary `cond ? a : b` |
| Scalar functions | `round(x, n)`, `abs(x)`, `if(cond, a, b)`, `concat(...)` |
| Aggregate functions (footer rows only) | `sum` `avg` `min` `max` `count` `median` — each takes a whole column |

`*` and `/` bind tighter than `+` and `-`, and parentheses override both. Aggregate functions only work in a footer row, since they need a whole column and a data row only ever has scalar values in scope. A footer row is never counted as part of its own column, so `sum(total)` in the totals row can't add itself in.

### Precision

`!sheet` takes an optional `precision=N` option (default `2`):

```markdown
!sheet precision=6
| item | unit | share     |
|------|-----:|----------:|
| a    |    3 | =unit / 7 |
```

Whole-number results render without a decimal point regardless of the precision setting.

### Escaping

Inside a `!sheet` table, a cell that should start literally with `=` is escaped as `\=`, and a row label that really starts with `!` is escaped as `\!` — otherwise it's read as a footer row marker.

### Errors

A bad formula shows its error in that cell only (`#ERR …`) — the rest of the table still computes and the slide never goes blank. This matters because Kova re-parses on every keystroke, so a half-typed formula is a normal, transient state rather than a fatal one. Errors are preserved in PDF and PowerPoint export too, so a broken deck looks broken instead of quietly shipping a wrong number.

Common error cases: an unknown column name, an unknown function, divide-by-zero, the wrong number of arguments, a syntax error, or using an aggregate function (`sum`, etc.) in a data row instead of a footer row.

> [!tip] Degrades gracefully outside Kova
> A sheet table is an ordinary GFM table under the hood, so opening the file in any other Markdown viewer still shows a valid table — just with the raw `=qty * unit` formula text in place of computed values, and a stray `!` in front of footer row labels.

`!include`, `!fmt`, and `!code` are reserved for future sheet directives and currently produce an error if used, so today's decks won't collide with them later.

---

## Diagrams (Mermaid)

Fenced code blocks with the `mermaid` language identifier are rendered as diagrams, automatically themed to match the active presentation theme.

```markdown
\`\`\`mermaid
pie title Browser share
    "Chrome"  : 65
    "Safari"  : 19
    "Firefox" : 4
    "Other"   : 12
\`\`\`
```
```markdown
\`\`\`mermaid
graph LR
    A[Write Markdown] --> B[Kova detects layout]
    B --> C[Live preview]
    C --> D[▶ Present]
\`\`\`
```

> [!tip] Tip
> See the [Mermaid documentation](https://mermaid.js.org/intro/) for all supported diagram types: flowcharts, sequence diagrams, Gantt charts, pie charts, class diagrams, and more.

---

## Math & LaTeX

Kova renders mathematical expressions using [KaTeX](https://katex.org/).

### Inline math

Wrap an expression in single dollar signs: `$...$`

```markdown
The derivative of $f(x) = x^2$ is $f'(x) = 2x$.
```

### Display math

Wrap a block equation in double dollar signs on their own lines: `$$...$$`

```markdown
$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$
```
```markdown
$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$
```

> [!tip] Literal dollar signs
> To display a literal `$` (e.g. a price), escape it with a backslash: `\$49.99`.

---

## Figure captions (!caption)

Attach a caption to the image, Mermaid diagram, math block, or table **directly above** it:

```markdown
![System architecture](./diagram.png)
!caption[Figure 1: request flow through the ingest pipeline]
```
```markdown
$$
E = mc^2
$$
!caption[Equation 1: mass-energy equivalence]
```
```markdown
!sheet
| item   | qty | unit  | total       |
|--------|----:|------:|------------:|
| motor  |   2 | 12.50 | =qty * unit |
!caption[Table 1: bill of materials]
```

Kova merges the caption into the element it follows during parsing, so it never becomes ordinary body text — it can't accidentally trigger a `split` / `two-column` layout the way a trailing paragraph would. A `!caption` with no valid image, Mermaid diagram, math block, or table directly above it is a compile error rather than a silent no-op, the same convention as a misplaced `!sheet`.

Captions render centred underneath the element, in every layout that can hold one. On a `full-bleed` image, where the picture fills the whole slide, the caption sits in a bottom overlay bar instead. Captions survive PowerPoint export for all four element types.

---

## Standard Markdown

### Headings

```markdown
# H1 — title slide (triggers the \`title\` layout)
## H2 — section break or slide heading
### H3 — sub-heading (renders as a paragraph-size label)
```

**Shortcuts:** `Ctrl+1` through `Ctrl+6` toggle heading levels on the current line. Pressing the same level again removes the heading marker.

---

### Text formatting

| Syntax | Result |
| --- | --- |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `~~strikethrough~~` | ~~strikethrough~~ |
| `` `inline code` `` | `inline code` |

**Shortcuts:** `Ctrl+B` for bold, `Ctrl+I` for italic.

> [!tip] No selection needed
> If no text is selected when you press `Ctrl+B` or `Ctrl+I`, Kova inserts a placeholder (`bold text` / `italic text`) with it pre-selected so you can type immediately.

---

### Lists

```markdown
- Unordered item
- Another item
  - Nested item (two spaces indent)

1. Ordered item
2. Second item
3. Third item
```

---

### Blockquote

```markdown
> The secret of getting ahead is getting started.
> — Mark Twain
```

Lines beginning with `—`, `–`, or `-` after the quote body are rendered as an attribution in a smaller typeface.

#### Callouts / admonitions

Turn a blockquote into a coloured admonition box by starting it with a `[!type]` marker:

```markdown
> [!tip] Pro tip
> Press \`Ctrl+B\` with no selection to insert placeholder bold text.

> [!warning]
> Unsaved changes are lost if you close without saving.
```

The marker's first line becomes the box's title (defaulting to the capitalised type name if you don't supply one). Five canonical styles are supported — `note`, `tip`, `warning`, `danger`, `info` — and common synonyms are mapped onto them automatically:

| You write | Renders as |
| --- | --- |
| `caution`, `attention` | `warning` |
| `error`, `failure`, `fail`, `bug`, `missing` | `danger` |
| `question`, `help`, `faq` | `info` |
| `hint`, `important`, `success`, `check`, `done` | `tip` |
| `abstract`, `summary`, `tldr`, `quote`, `cite`, `example` | `note` |

A blockquote without a `[!type]` marker renders as a normal quote, as described above.

---

### Links and images

```markdown
[Link text](https://example.com)

![Alt text](path/to/image.png)
```

**Image sizing** — use the title attribute to control width:

```markdown
![diagram](chart.png "50%")      <!-- 50% of slide width -->
![photo](photo.jpg "300px")      <!-- fixed 300 px -->
![icon](icon.svg "2rem")         <!-- relative to font size -->
```

Supported units: `%`, `px`, `em`, `rem`, `cqi`.

> [!note] Link styling
> An explicit `[text](url)` link is shown in the active theme's accent colour. A bare URL or email address that Markdown auto-links (e.g. `https://example.com` on its own line) stays unstyled plain text.

> [!note] Link targets
> A link with no scheme (`[text](example.com)`) defaults to `https://example.com`. During a presentation, clicking any link opens it in your system's default browser instead of navigating away from the presentation itself.

---

### Code blocks

Fenced code blocks with syntax highlighting. Specify the language after the opening fence:

```markdown
\`\`\`python
def greet(name: str) -> str:
    return f"Hello, {name}!"
\`\`\`
```

Supported languages include Python, JavaScript, TypeScript, Rust, Go, SQL, Bash, and many more via [highlight.js](https://highlightjs.org/).

Slides containing only code blocks or Mermaid diagrams automatically use the `code` layout — a dark, full-width display optimised for readability.

---

### Tables (GFM)

```markdown
| Feature       | Status |
| ------------- | ------ |
| Live preview  | ✅     |
| Mermaid       | ✅     |
| Custom themes | ✅     |
```

**Inline formatting in cells** — bold, italic, links, images, and inline math (`$...$`) all render correctly inside table cells:

```markdown
| Method | Formula | Notes |
|--------|---------|-------|
| **Mean** | $\bar{x} = \frac{\sum x_i}{n}$ | Sensitive to outliers |
| *Median* | middle value | More [robust](https://en.wikipedia.org/wiki/Robust_statistics) |
```

> [!tip] Insert table dialog
> Right-click in the editor and choose **Insert → Table** to open a dialog where you can set the number of rows and columns. Kova inserts a ready-to-fill GFM table at the cursor position.

---

### Horizontal rule

Use `<hr>` for a visual divider **within** a slide. Do **not** use `---` inside a slide — it is the slide separator.

```markdown
## My Slide

First section content.

<hr>

Second section content.
```

---

## Speaker notes

Add speaker notes below `???` on any slide — never shown to the audience.

```markdown
## Our Roadmap

- Q1: Public beta
- Q2: v1.0 release
- Q3: Plugin API

???

Pause here and ask the audience what features they most want to see.
```

See [Presenting — Speaker Notes](https://wiki.kova.md/presenting/#speaker-notes) for how notes appear during a presentation, including clickable links.

---

## Layout override

Force a specific layout regardless of content with an HTML comment at the top of the slide:

```markdown
<!-- layout:grid -->

## Hand-picked grid
```

See [Layouts — Manual override](https://wiki.kova.md/layouts/#manual-override) for the full list of layout names and how automatic detection works.

---

## Per-slide text colour

Override text colour on an individual slide with an HTML comment:

```markdown
<!-- color: #fff -->

## Dark background slide
```

`<!-- _color: white -->` (Marp's own syntax) is also recognised and sets the same colour — a Marp deck that already uses `_color` keeps its per-slide colours on import. Accepts hex (`#rgb`, `#rrggbb`, `#rrggbbaa`), functional notations (`rgb()`, `hsl()`, …), and named CSS colours; functional notations are normalised to hex for PowerPoint export.

Alternatively, invert to the deck's inverted palette instead of choosing a colour by hand:

```markdown
<!-- _class: invert -->
```

Either directive is honoured in the live preview and PowerPoint export, across every layout — split, two-column, three-column, BSP, grid, and media. Headings and bold text follow the same override by default; to colour them independently, see [Themes — heading and bold colour](https://wiki.kova.md/themes/#heading-and-bold-colour).

> [!tip] Exceptions, not the deck-wide default
> Per-slide colour is for a handful of exceptions — typically slides with a photo [`![bg]`](#slide-background-images-bg). If most of the deck needs the same colour, change **Text** / **Title text** in the Inspector instead ([Themes — Inspector overrides](https://wiki.kova.md/themes/#inspector-overrides)), which applies deck-wide.


---
title: "Icons - Kova Documentation"
source: "https://wiki.kova.md/icons/"
author:
published:
created: 2026-11-08
description:
tags:
  - "clippings"
---
## Icons

Kova has 180 built-in icons. Drop one into your text with an inline `:name:` shortcode — there's nothing to install, and each icon takes the size and colour of the text around it.

```markdown
## Launch checklist

- :check-circle: Tests passing
- :rocket: Ship on Friday
- :warning: **Heads up** — staging resets nightly
```

Every available name is listed in the [icon reference](#icon-reference) below.

---

## Using icons

|  |  |
| --- | --- |
| **Syntax** | A lowercase name between two colons — letters, digits and hyphens, such as `:rocket:` or `:git-branch:` |
| **Inline** | An icon sits in the flow of a line, so you can put one mid-sentence, at the start of a list item, or several in a row |
| **Size and colour** | Icons take the size and colour of the surrounding text, so they scale with a heading and follow your theme. Bold and italic never distort them |
| **Works in** | Paragraphs, list items, table cells, bold and italic text, and any heading below a slide's title |
| **Doesn't work in** | A slide's title (its first heading) — `:rocket:` there appears as typed. Inline code and code blocks are never converted either, so wrap a shortcode in backticks to show it literally |
| **Unknown names** | Left as typed, with no warning — colons are too common in ordinary text to flag every one. If an icon doesn't appear, check the spelling against the reference below |

---

## Icons in themes

Icons are drawn with a theme's `icon` font, which defaults to Kova's bundled icon font, `Kova Icons`. Every built-in theme and every [custom theme](https://wiki.kova.md/themes/#custom-themes) uses it automatically, so you don't need to set anything.

To use a different font, set the `icon` role alongside `title`, `body`, and `code` — in a custom theme file:

```yaml
fonts:
  icon: "Symbols Nerd Font"
```

or for a single document, under `theme_overrides` in its frontmatter (see [Inspector overrides](https://wiki.kova.md/themes/#inspector-overrides)):

```yaml
theme_overrides:
  fonts:
    icon: "Symbols Nerd Font"
```

> [!warning] Use a Nerd Fonts font
> Kova's shortcode names map to Nerd Fonts codepoints, so point `icon` at a Nerd-Fonts-patched font you already have installed. A font that isn't patched that way — plain Font Awesome, for example — will likely show the wrong glyphs or none. There is no Inspector control for the icon font yet; set it in YAML.

---

## Exporting

**PDF and Print** capture the live slide, so icons look exactly as they do in the preview.

**PowerPoint** export is different: icons are written as text in the `Kova Icons` font, and that font isn't embedded in the `.pptx`. PowerPoint and Keynote only show the icons on machines where the font is installed. See [Exporting — PowerPoint limitations](https://wiki.kova.md/exporting/#limitations_1).

---

## Icon reference

Write any name below between two colons, for example `:rocket:`.

`:anchor:`

`:android:`

`:apple:`

`:archive:`

`:arrow-down:`

`:arrow-left:`

`:arrow-right:`

`:arrow-up:`

`:at:`

`:barcode:`

`:battery:`

`:bell:`

`:bolt:`

`:book:`

`:bookmark:`

`:briefcase:`

`:brush:`

`:bug:`

`:calendar:`

`:camera:`

`:chart-bar:`

`:chart-line:`

`:chart-pie:`

`:check:`

`:check-circle:`

`:chevron-down:`

`:chevron-left:`

`:chevron-right:`

`:chevron-up:`

`:chrome:`

`:circle:`

`:clipboard:`

`:clock:`

`:cloud:`

`:cloud-rain:`

`:code:`

`:coffee:`

`:comment:`

`:comments:`

`:compass:`

`:copy:`

`:credit-card:`

`:css3:`

`:cube:`

`:cubes:`

`:database:`

`:docker:`

`:download:`

`:edit:`

`:exclamation-circle:`

`:external-link:`

`:eye:`

`:eye-off:`

`:file:`

`:file-text:`

`:filter:`

`:fire:`

`:firefox:`

`:flag:`

`:fog:`

`:folder:`

`:folder-open:`

`:gift:`

`:git:`

`:git-branch:`

`:git-commit:`

`:git-compare:`

`:git-merge:`

`:git-pull-request:`

`:github:`

`:gitlab:`

`:globe:`

`:graduation-cap:`

`:grid:`

`:hashtag:`

`:heart:`

`:heart-outline:`

`:history:`

`:home:`

`:html5:`

`:id-card:`

`:image:`

`:inbox:`

`:infinity:`

`:info:`

`:issue-closed:`

`:issue-opened:`

`:java:`

`:javascript:`

`:json:`

`:key:`

`:leaf:`

`:lightbulb:`

`:link:`

`:linux:`

`:list:`

`:lock:`

`:mail:`

`:map-pin:`

`:markdown:`

`:menu:`

`:microphone:`

`:minus:`

`:minus-circle:`

`:moon:`

`:music:`

`:mute:`

`:newspaper:`

`:nodejs:`

`:npm:`

`:package:`

`:paperclip:`

`:pause:`

`:percent:`

`:phone:`

`:play:`

`:plus:`

`:plus-circle:`

`:power:`

`:print:`

`:python:`

`:qrcode:`

`:question:`

`:react:`

`:redo:`

`:refresh:`

`:repo:`

`:repo-forked:`

`:rocket:`

`:rust:`

`:save:`

`:scissors:`

`:search:`

`:send:`

`:server:`

`:settings:`

`:share:`

`:shield:`

`:shopping-cart:`

`:sitemap:`

`:slack:`

`:sliders:`

`:smile:`

`:snow:`

`:sort:`

`:square:`

`:star:`

`:star-outline:`

`:stop:`

`:storm:`

`:sun:`

`:tag:`

`:target:`

`:terminal:`

`:thumbs-down:`

`:thumbs-up:`

`:times-circle:`

`:toggle-off:`

`:toggle-on:`

`:trash:`

`:trophy:`

`:twitter:`

`:typescript:`

`:umbrella:`

`:undo:`

`:unlock:`

`:upload:`

`:user:`

`:users:`

`:video-camera:`

`:vim:`

`:volume:`

`:warning:`

`:wifi:`

`:wind:`

`:windows:`

`:wrench:`

`:x:`

`:yaml:`

`:youtube:`

The icons come from the [Nerd Fonts](https://www.nerdfonts.com/) "Symbols Only" set, bundled with Kova under the MIT licence (© 2014 Ryan L McIntyre and contributors).


---
title: "Layouts - Kova Documentation"
source: "https://wiki.kova.md/layouts/"
author:
published:
created: 2026-11-08
description:
tags:
  - "clippings"
---
## Layouts

Kova automatically selects the best layout for each slide based on its content. You can also [override](#manual-override) the layout manually with an HTML comment.

---

## Automatic layout detection

Kova analyses the elements on a slide and applies the **first matching rule** in priority order:

| Priority | Condition | Layout applied |
| --- | --- | --- |
| 1 | H1 heading | [`title`](#title) |
| 2 | Any `!youtube` or `!poll` element | [`media`](#media) |
| 3 | Two `\\|\\|\\|` column breaks | [`three-column`](#three-column) |
| 4 | A single `\\|\\|\\|` column break | [`two-column`](#two-column) |
| 5 | A lone `!video` (the slide's only element) | [`media`](#media) |
| 6 | All elements are code blocks or Mermaid diagrams | [`code`](#code) |
| 7 | All elements are display-math blocks (`$$...$$`) | [`math`](#math) |
| 8 | No heading + single image | [`full-bleed`](#full-bleed) |
| 9 | No heading + single blockquote | [`quote`](#quote) |
| 10 | No heading + no body content | [`blank`](#blank) |
| 11 | H2 + no body content | [`section`](#section) |
| 12 | Heading + single image only | [`title-image`](#title-image) |
| 13 | Heading + one image + one text block | [`split`](#split) |
| 14 | 2–3 logical elements, visually diverse | [`bsp`](#bsp) |
| 15 | 4 or more logical elements | [`grid`](#grid) |
| 16 | Dense pure-text exceeding overflow threshold | [`two-column`](#two-column) |
| 17 | Anything else | [`title-content`](#title-content) |

> [!note] Logical element counting
> Consecutive `!progress` bars are treated as **a single logical unit** for the BSP and Grid threshold checks. A slide with a heading, a paragraph, and four progress bars is counted as 3 logical elements — not 6 — so it uses `bsp` rather than `grid`.

> [!note] Overflow guard
> Text-only slides that exceed the safe area line count automatically fall back to `two-column` to prevent text clipping (rule 16).

> [!note] Rescaled to fit
> If a slide's content still exceeds the available space after layout selection, Kova scales it down to fit. A **"rescaled to fit"** badge appears in the bottom-right corner of the preview to let you know. Consider splitting the slide or reducing content if you see this badge.

> [!tip] See which layout Kova chose
> The **status bar** shows the current slide's layout next to the slide counter, for example `Layout: split`. A layout you've pinned with a [manual override](#manual-override) is marked `(override)`. Hover over it to see whether the layout was auto-detected or set by a comment.

---

## Layout reference

**Triggered by:** an H1 heading.

Full-colour hero slide. Paragraphs below the H1 render as subtitles. Background colour, text alignment, and decorative pattern follow the active theme.

```markdown
# Kova

The presentation tool for people who prefer to write.
```

---

### section

**Triggered by:** an H2 heading with no body content.

Coloured section-break slide for dividing a presentation into chapters.

```markdown
## Part Two: Results
```

---

### title-content

**Triggered by:** a heading with text, lists, tables, or other body content.

This is the **default layout**. The heading sits across the top; content fills the remainder of the slide.

```markdown
## Key findings

- Response time improved by 40%
- Error rate dropped below 0.1%
- Customer satisfaction up 18 points
```

---

### title-image

**Triggered by:** a heading with a single image and nothing else.

The heading anchors the left side; the image fills the right half.

```markdown
## Architecture overview

![System diagram](./diagram.png)
```

---

### split

**Triggered by:** a heading + one image + one text block (paragraph or list).

Image on the left, text on the right. Good for product screenshots with accompanying description.

```markdown
## The editor

![Screenshot](./editor.png)

Write slides in plain Markdown with a live preview alongside.
```

---

### full-bleed

**Triggered by:** a single image with no heading.

The image fills the entire slide (cover crop). Good for dramatic opening or closing slides.

```markdown
![Conference hall](./crowd.jpg)
```

---

### quote

**Triggered by:** a single blockquote with no heading.

Large centred quote with optional attribution in smaller text.

```markdown
> The best way to predict the future is to invent it.
> — Alan Kay
```

---

### blank

**Triggered by:** no heading and no body content — a slide left (deliberately or accidentally) empty.

Renders nothing but the theme's background colour — no placeholder text, no empty boxes. Useful as an intentional pause slide between sections. A blank slide still shows the theme's header/footer bar and logo if those are enabled, and exports the same way — a plain background-coloured slide, in both PDF and PowerPoint.

```markdown
<!-- Pause here for questions -->
```

> [!note] An empty slide alone doesn't count
> Two `---` separators with nothing but blank lines between them collapse into nothing — Kova doesn't create a slide there at all. A slide needs *some* non-whitespace content to exist, even if that content (like the comment above) renders as nothing. An ordinary HTML comment works well for this, since Kova only treats specific comment forms (`<!-- layout: ... -->`, `<!-- color: ... -->`, `<!-- hidden -->`, and a few others) as directives — anything else is silently dropped from the rendered slide.

> [!note] A background image beats blank
> Adding a [`![bg]`](https://wiki.kova.md/markdown-and-syntax/#slide-background-images-bg) line to an otherwise-empty, untitled slide produces `full-bleed` instead of `blank` — the background image always wins.

---

### two-column

**Triggered by:** a `|||` column break, or the overflow guard on a dense pure-text slide.

Splits the slide into two equal columns. If `|||` is present the split occurs there; otherwise Kova splits at the element midpoint. A [`!toc`](https://wiki.kova.md/markdown-and-syntax/#table-of-contents-toc) list long enough to overflow the slide splits the same way, balancing entries across both columns by title length.

```markdown
## Before and after

**Legacy workflow**

1. Open PowerPoint
2. Drag text boxes around
3. Fight with alignment

|||

**With Kova**

1. Write Markdown
2. Choose a theme
3. Click Present
```

---

### three-column

**Triggered by:** two `|||` column breaks on the same slide.

Splits the slide into three equal columns, one per `|||` -separated block. Extends the same syntax as `two-column` — a third block just needs a second separator instead of folding into the right-hand column.

```markdown
## Pricing tiers

**Free**

- Unlimited presentations
- All themes

|||

**Pro**

- Priority support
- Team library

|||

**Enterprise**

- SSO
- Custom deployment
```

---

### bsp

**Triggered by:** 2–3 logical elements where the mix is visually diverse.

- **2 elements:** side-by-side panes.
- **3 elements:** left column + stacked right column.

Text content is placed on the left; visual content (images, progress bars, Mermaid) goes on the right. Consecutive `!progress` bars are grouped into a single pane.

```markdown
## Team health

We're making solid progress across all workstreams.

!progress[Feature delivery](88)
!progress[Code review SLA](72)
!progress[Test coverage](91)
```

---

### code

**Triggered by:** all body elements are code blocks or Mermaid diagrams.

Dark, code-focused background with a full-width monospace display. Optimised for code reviews and technical walkthroughs. A long code block or diagram scales down to fit the slide, like on every other layout, rather than being cut off.

```markdown
## Parsing a slide

\`\`\`rust
fn parse_slide(src: &str) -> Slide {
    let tokens = tokenise(src);
    layout::detect(&tokens)
}
\`\`\`
```

---

### math

**Triggered by:** every body element is a **display math** block (`$$...$$`) — one or more, with or without a heading.

Stacks the equations vertically, each centred and scaled up for readability. Only counts standalone `$$...$$` blocks; inline math (`$...$`) inside a paragraph doesn't count as a body element on its own, so a slide mixing prose and inline math uses the normal layout rules instead. A `$$...$$` block paired with text-like content (a paragraph, list, blockquote, or ToC) is deliberately excluded here too — it stacks full-width in whichever layout that content would otherwise get, rather than being squeezed into a narrow BSP pane. See [Markdown & Syntax — Math & LaTeX](https://wiki.kova.md/markdown-and-syntax/#math-latex).

```markdown
## The core identity

$$
e^{i\pi} + 1 = 0
$$
```

> [!note] PDF and PowerPoint export
> Both reproduce the rendered equation as an image. PDF captures the live slide; PowerPoint renders each `$$…$$` block with KaTeX and embeds it as a picture. If that rasterisation fails for a given equation, Kova falls back to exporting the raw LaTeX source as monospaced text and shows a warning naming the slide.

---

### media

**Triggered by:** a `!youtube` or `!poll` element, or a `!video` that is the slide's only element.

Centred media display with the title above. Ideal for embedding polls or videos mid-presentation.

```markdown
## Quick poll

!poll[Which layout do you use most?](https://pollev.com/my-poll)
```

A `!video` sharing the slide with other content is **not** forced into `media` — it flows through the normal auto-layout rules instead, the same as an image. See [Markdown & Syntax — Local video](https://wiki.kova.md/markdown-and-syntax/#local-video-video).

---

### grid

**Triggered by:** 4 or more logical elements.

Elements are arranged in a responsive grid of cards. Good for feature comparisons or category overviews. A bullet list counts as a **single** element, so to build a grid out of list items, force the layout with [`<!-- layout:grid -->`](#manual-override) — each item then becomes its own card:

```markdown
<!-- layout:grid -->

## Supported platforms

- **macOS** — Universal binary, Apple Silicon and Intel
- **Windows** — MSI and setup.exe installers
- **Debian/Ubuntu** — \`.deb\` package
- **Fedora/RHEL** — \`.rpm\` package
- **AppImage** — distro-independent
```

---

## Manual override

Place `<!-- layout:NAME -->` at the very top of a slide to force any layout regardless of content:

```markdown
<!-- layout:grid -->

## Pricing tiers

- **Free** — unlimited presentations, all themes
- **Pro** — priority support (coming soon)
- **Team** — shared theme library (coming soon)
- **Enterprise** — custom deployment (coming soon)
```

Available names: `title` · `section` · `title-content` · `title-image` · `split` · `full-bleed` · `quote` · `blank` · `two-column` · `three-column` · `bsp` · `grid` · `media` · `code` · `math`


---
title: "Themes - Kova Documentation"
source: "https://wiki.kova.md/themes/"
author:
published:
created: 2026-11-08
description:
tags:
  - "clippings"
---
## Themes

Kova ships with 11 built-in themes and supports fully custom themes via YAML files.

---

## Selecting a theme

Open the **Inspector** panel (click **ⓘ** in the titlebar) and choose a theme from the swatches in the **Theme** section. The change is instant and Kova saves it to the file automatically.

---

## Built-in themes

| ID | Style |
| --- | --- |
| `light` | Clean white background, dark text — the default |
| `dark` | Deep charcoal background, light text |
| `institutional` | Formal navy and white with a structured header bar |
| `minimal` | No decorative elements; maximum focus on content |
| `editorial` | Serif typography, warm off-white — editorial / essay feel |
| `slate` | Dark blue-grey with accent highlights |
| `pitch` | High-contrast black with bold typographic hierarchy |
| `cosmos` | Deep space-inspired dark palette with indigo accents |
| `forge` | Industrial dark with amber highlights |
| `grove` | Earthy greens and warm neutrals |
| `horizon` | Gradient sunrise palette, soft and optimistic |

> [!tip] Theme library
> The **More Themes…** button in the Inspector links to [themes.kova.md](https://themes.kova.md/), where community-created themes are available to download. Downloads are verified against SHA-256 checksums.

---

## Inspector overrides

Without writing a custom theme file, you can override specific aspects of any built-in theme from the Inspector:

| Override | What it changes |
| --- | --- |
| **Primary colour** | Accent colour used for headings, progress bars, and decorative elements |
| **Background colour** | Slide background |
| **Text colour** | Body text |
| **Heading colour** | Content-slide heading colour; falls back to Text colour until set |
| **Bold text colour** | Inline **bold** / `<strong>` colour; falls back to Text colour until set |
| **Title font** | Font used for H1 and H2 headings |
| **Body font** | Font used for all other text |
| **Code font** | Monospace font for code blocks |
| **Logo** | Image displayed in the header or footer |
| **Header text** | Custom text shown at the top of every slide — supports template variables and `\\|` segmented layout |
| **Header → Hide on title slide** | Suppresses the header on the title slide only, keeping it everywhere else |
| **Footer text** | Custom text shown at the bottom — supports `{slide_number}`, `{total}`, `{title}`, `{author}`, `{date}` and `\\|` segmented layout |
| **Footer → Hide on title slide** | Suppresses the footer on the title slide only, keeping it everywhere else |
| **Table of contents → Numbered list** | Toggles a [`!toc`](https://wiki.kova.md/markdown-and-syntax/#table-of-contents-toc) slide between a numbered list and a plain hyperlinked list. On by default |

Kova saves overrides to the file automatically. Logo, Header, Footer, and Table of Contents controls live together under the Inspector's **Document** section.

A small dot appears next to a control's label whenever its current value differs from the active theme's own default — i.e. it's been overridden via `theme_overrides` — as a quick visual sense of how much customising a document carries, which might be a sign it's worth promoting to a proper [custom theme](#custom-themes) instead.

### Heading and bold colour

Headings and bold/ `<strong>` text can take a colour distinct from body text — set it via the **Heading colour** / **Bold text colour** swatches above, or directly in YAML via `theme_overrides` in a deck's frontmatter, or the `heading` / `bold` keys in a [custom theme](#custom-themes) file:

```yaml
theme_overrides:
  colors:
    heading: "#0057B8"
    bold:    "#B8003F"
```

Set `heading` / `bold` in a custom theme's `colors` block (see [Color reference](#color-reference)) to apply the colours to every document using that theme, rather than one document at a time via the Inspector.

Both colours fall back to the theme's plain `text` colour when unset, and both are still overridden by a slide's own [per-slide text colour or invert](https://wiki.kova.md/markdown-and-syntax/#per-slide-text-colour) directive, so a slide's text stays legible together rather than mixing an old heading colour with a new per-slide one.

> [!note] Font availability
> If a font you've chosen in the Inspector isn't installed on the current machine, a **⚠** warning appears next to the font name in the Inspector. Slides will fall back to the theme's default font until the missing font is installed.

---

## Custom themes

Create a `.yaml` file in your custom themes folder to define a fully custom theme — see [Settings & Keybindings — Themes](https://wiki.kova.md/settings-and-keybindings/#themes) for the exact path on each platform. Kova loads all valid `.yaml` files from that directory on startup, and watches the folder while running — adding, editing, or removing a `.yaml` /`.yml` file there (from any editor) reloads it automatically within moments, no restart needed. Any parse errors are reported in **Settings → Themes**.

### File format

```yaml
# my-brand.yaml, saved to your custom themes folder

name: My Brand          # Display name shown in the Inspector
id: my-brand            # The ID Kova uses internally to reference this theme
extends: light          # Optional — base theme for any field this file doesn't set. A built-in ID, or another installed custom theme's \`id\`. Defaults to \`light\`. See "Inheriting from other themes" below.

colors:
  primary:    "#0057B8"   # Background of title and section slides
  accent:     "#003F8A"   # Links, progress bars, and highlights
  background: "#FFFFFF"   # All other slide backgrounds
  text:       "#1A1A1A"   # Body text
  title_text: "#FFFFFF"   # Heading text on title and section slides
  section_bg: "#E8F0FE"   # Overrides primary for section slides only
  code_bg:    "#F3F4F6"   # Code block background
  heading:    "#0057B8"   # Content-slide heading colour (optional, falls back to \`text\`)
  bold:       "#B8003F"   # Inline **bold**/<strong> colour (optional, falls back to \`text\`)
  chart_colors:            # Optional palette override for pie/xychart/timeline diagrams
    - "#0057B8"
    - "#00A676"
    - "#F2A900"
  diagram_colors:          # Optional overrides for Mermaid flowchart/sequence colours — see "Diagram & chart colours" below
    primary: "#0057B8"
    border:  "#003F8A"
    line:    "#5C6773"
    cluster: "#E8F0FE"
    text:    "#1A1A1A"

fonts:
  title: "Georgia, serif"       # H1 and H2
  body:  "Inter, sans-serif"    # All other text
  code:  "JetBrains Mono, monospace"
  # icon: "Kova Icons"            # Optional — font for :name: icon shortcodes. Leave unset to keep Kova's bundled icon font

layout:
  title_align:   center   # "center" | "left" | "bottom-left" — text alignment on title slide
  heading_align: left     # "left" | "center" — heading alignment on content slides
  decoration:    none     # "none" | "dots" | "grid" | "diagonal" | "bar-left"

logo: logo.png                      # Absolute path, https:// URL, data:image/... URI, or — as here — a path relative to this theme file's own directory
logo_position: bottom-left          # "top-left" | "top-right" | "bottom-left" | "bottom-right"

footer:
  show:              false
  text:              "{title} | {date} | {slide_number}/{total}"
  show_slide_number: true
  hide_on_title:     false   # true suppresses the footer on the title slide only, keeping it everywhere else

header:
  show: false
  text: ""
  hide_on_title: false   # true suppresses the header on the title slide only, keeping it everywhere else

toc:
  numbered: true   # false renders a plain hyperlinked list instead of a numbered one
```

> [!note] Logo paths
> `logo` accepts an absolute path, an `https://` URL, or a `data:image/...` URI — or, as of the theme file's own directory being known, a path **relative to the theme file itself** (e.g. `logo.png` sitting next to `theme.yaml`), so a self-contained theme folder keeps working if it's moved or renamed. A relative path only resolves for a theme loaded from a file; it's dropped for a theme with no file backing it. On Windows, use forward slashes or a single backslash — do not quote the path or double-escape backslashes.

> [!note] Logo and hide_on_title
> A logo sits in the header bar when `logo_position` is a top corner and `header.show` is on, and in the footer bar for a bottom corner and `footer.show`. When `hide_on_title` hides that bar on the title slide, the logo goes with it — in PowerPoint export too — rather than being left floating on its own. A logo whose corner has no matching bar turned on always shows.

> [!note] Icon font
> The `icon` font draws [`:name:` icon shortcodes](https://wiki.kova.md/icons/). It defaults to Kova's bundled `Kova Icons`, so leave it out unless you want a different Nerd-Fonts-patched font — see [Icons in themes](https://wiki.kova.md/icons/#icons-in-themes).

### Color reference

| Key | What it controls |
| --- | --- |
| `primary` | Background of title and section slides |
| `accent` | Links, progress bars, and highlight elements |
| `background` | Background of all other slides |
| `text` | Body text |
| `title_text` | Heading text on title and section slides — set this if `primary` is dark, otherwise text may be unreadable |
| `section_bg` | Background of section slides only; overrides `primary` for those slides |
| `code_bg` | Code block background |
| `heading` | Content-slide heading colour; falls back to `text` when unset. See [Heading and bold colour](#heading-and-bold-colour) |
| `bold` | Inline `**bold**` / `<strong>` colour; falls back to `text` when unset |

### Diagram & chart colours

Mermaid diagrams otherwise derive their colours from `primary` / `accent` / `code_bg` / `text` above. Two optional keys under `colors` override that for specific diagram types instead:

| Key | Type | Controls |
| --- | --- | --- |
| `chart_colors` | list of hex colours | Palette used for pie, xychart, and timeline diagrams |
| `diagram_colors` | map, see below | Flowchart and sequence-diagram colours |

`diagram_colors` fields, all optional and independent:

| Field | Controls |
| --- | --- |
| `primary` | Node/actor fill |
| `border` | Node/actor border; falls back to `primary` when unset |
| `line` | Connector lines |
| `cluster` | Subgraph/cluster background |
| `text` | Label text — doesn't affect pie-slice text, which stays tied to `title_text` for contrast on coloured slices |

Both apply to the live preview and to PDF/PowerPoint export alike. There's no Inspector UI for either — set them via `theme_overrides` in a deck's frontmatter or a custom theme's `colors` block, the same as [heading/bold colour](#heading-and-bold-colour) above.

### Template variables

Use these in `header.text` and `footer.text`:

| Variable | Value |
| --- | --- |
| `{title}` | Document title |
| `{author}` | Document author (frontmatter `author:`) |
| `{date}` | Document date |
| `{slide_number}` | Current slide number |
| `{total}` | Total slide count |

### Segmented header/footer layout

Use `|` as a stretch separator to divide a header or footer into **left**, **centre**, and **right** sections:

```yaml
header:
  show: true
  text: "My Deck | {title} | {date}"

footer:
  show: true
  text: "{title} | | {slide_number}/{total}"
```

| Example | Result |
| --- | --- |
| `Left header` | Left-aligned (unchanged) |
| `{date} \\| caption \\| {total}` | Three parts: left · centre · right |
| `\\| caption` | Centre-aligned |
| `\\|\\| {slide_number}/{total}` | Right-aligned |

Text without a `|` renders left-aligned as before, so existing decks are unaffected. Segmented layout works in both the Inspector text fields and custom theme YAML. It is also faithfully reproduced in PowerPoint export.

### Inheriting from other themes

Omitted fields inherit from a base theme's defaults — the **Light** theme, unless you set `extends:`. You only need to specify what you want to change:

```yaml
name: Dark Blue
id: dark-blue

colors:
  background: "#0D1117"
  text:       "#E6EDF3"
  primary:    "#58A6FF"
```

Set `extends: <id>` to inherit from a different theme instead of Light — any built-in ID (`dark`, `slate`, `pitch`, …) or another installed custom theme's own `id`:

```yaml
name: Dark Blue Compact
id: dark-blue-compact
extends: dark-blue   # start from dark-blue above, only changing layout here

layout:
  heading_align: left
```

`extends` chains resolve transitively, so a custom theme can build on another custom theme that itself extends a third. If `extends` names a theme that doesn't exist, failed to parse, or forms a cycle (including extending itself), that entry falls back to the Light theme instead, with a warning shown in **Settings → Themes** — never the whole batch of custom themes failing together.

### Applying changes

Edit the YAML file — no restart needed. Kova watches the custom themes folder while it's running and reloads a `.yaml` /`.yml` file within moments of it being added, changed, or removed, whether the edit comes from another editor or Kova's own theme tooling; any open document using that theme updates live. YAML syntax errors are shown in **Settings → Themes** with the file path and error detail.



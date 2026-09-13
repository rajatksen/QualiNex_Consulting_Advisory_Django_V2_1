# QualiNex Consulting & Advisory — Django V2.1 (Contrast + Home Fix + Expanded Advisory Content)

A production-oriented multi-page Django website for Subhamjit Deb / QualiNex Consulting & Advisory.

## V2.1 fixes
- QualiNex brand restored and carried across every page.
- Global fixed header on every page.
- No absolute-positioned content cards: responsive CSS grid/flex layouts prevent frame overlap.
- Separate pages for Advisory, Experience, Credentials, Method and Engage.
- Icon-only Email / WhatsApp / LinkedIn contact actions.
- Contact enquiry form stored in Django SQLite and visible in `/admin/`.
- Credentials and awards use only evidence available from the supplied résumé / LinkedIn research.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000/

## Production notes
Set a strong `SECRET_KEY`, `DEBUG=False`, configure `ALLOWED_HOSTS`, HTTPS/security settings, a production database, email delivery, static collection and environment variables before deployment.

## V2.1 contrast and Home fixes
- Header background is now a deliberate high-contrast `--header-bg` (#0b1e2d).
- QUALINEX brand text, subtitle and tagline now use explicit light colours; they no longer inherit the dark body text colour.
- Navigation text and Engage CTA have explicit accessible contrast against the static header.
- Header remains fixed on every page.
- The root URL `/` is the Home page.
- Browser scroll restoration is disabled and the Home route forces scroll position 0 on load.
- Home is explicitly included in the primary navigation and highlighted when active.

## Where the fixes are
1. `practice/static/practice/css/site.css` — all header/font/background contrast corrections.
2. `practice/static/practice/js/site.js` — Home-on-open and scroll restoration behaviour.
3. `practice/templates/practice/base.html` — global navigation, Home link and header markup.
4. `practice/urls.py` + `practice/views.py` — `/` continues to resolve to `views.home`.

## How to save the fixes
The source files inside this ZIP are already the corrected version. After extracting the ZIP, save the project folder, then run `python manage.py migrate` and `python manage.py runserver`. Any future visual/header changes should be made in `practice/static/practice/css/site.css`; navigation and Home-load behaviour belongs in `base.html`, `practice/urls.py`, and `practice/static/practice/js/site.js`.


## Expanded V2.1 advisory content
The Advisory portfolio is now a click-through architecture rather than a set of static cards. Each of the six disciplines opens a dedicated page under `/advisory/<slug>/`: quality strategy & governance, operational excellence, customer & supplier quality, NPI/APQP/risk engineering, digital quality transformation, and capability academy.

The engagement models also have dedicated pages under `/engagement/<slug>/`. The Capability Academy is reachable both from the sixth advisory discipline and from the engagement model list.

### Where to add more content
1. `practice/views.py` — extend the `SERVICES` dictionary to add or amend page content (strapline, intro, why, deliverables, questions, outcomes, framework).
2. `practice/views.py` — extend the `ENGAGEMENTS` dictionary for new engagement-model pages.
3. `practice/templates/practice/service_detail.html` — controls the common layout shared by all six advisory pages.
4. `practice/templates/practice/engagement_detail.html` — controls the common layout for engagement-model pages.
5. `practice/templates/practice/advisory.html` — controls the advisory index cards and simple navigation.
6. `practice/templates/practice/home.html` — controls the home-page summaries and links.

You normally do not need to edit the CSS when adding text content. Save the changed Python/template file, restart `python manage.py runserver` if needed, and refresh the browser.

## V2.1 Responsive / Global Layout Pass

The visual system has been tightened for a compact, executive-consulting presentation across large desktop, laptop, tablet and phone viewports. The layout is fluid rather than tied to one screen resolution.

### Responsive targets

- Large desktop: 1440px+
- Desktop / laptop: 1150–1439px
- Tablet / iPad landscape: 961–1149px
- Tablet / iPad portrait and large phones: 741–960px
- Phone: 481–740px
- Small phone: 480px and below

The site uses a centered content frame (`--max`), fluid gutters (`--gutter`), `clamp()` typography, CSS Grid/Flex layouts, minimum touch targets and explicit overflow protection. This is aligned with responsive-accessibility guidance from W3C: adapt layouts to viewport size, avoid horizontal scrolling and keep content usable when text is enlarged.

### Main responsive code locations

1. `practice/static/practice/css/site.css`
   - global frame width and gutters
   - header dimensions
   - desktop/tablet/mobile grids
   - mobile navigation
   - typography scaling
   - touch targets and focus states
   - conceptual management visual
   - print/reduced-motion rules

2. `practice/templates/practice/base.html`
   - persistent global header/navigation/footer

3. `practice/static/practice/js/site.js`
   - mobile navigation open/close behaviour
   - Home scroll restoration behaviour
   - active navigation state

4. `practice/templates/practice/home.html`
   - added the Quality Performance Architecture visualisation

### Visual design principle

QualiNex does not use a decorative chart with invented numbers. Visuals are used to explain the consulting operating model: Sense → Control → Improve, supported by Risk × Cost × Customer, management rhythm and capability transfer.

### Editing future content

Add or edit advisory narrative in `practice/views.py` under the existing structured service and engagement dictionaries. Page layouts remain reusable, so content can grow without rebuilding the HTML frame.

### Important browser expectation

The root route `/` is the Home page. The fixed header remains available while browsing all pages. The site is intended to operate in portrait and landscape orientations and to avoid horizontal page scrolling at common laptop, desktop, tablet and phone widths.

## V2.1 Space-Optimized Responsive Layout
- `practice/static/practice/css/site.css`: reduced vertical whitespace across hero bands, sections, cards and footer; introduced `.page-hero-grid` for compact consulting-style hero framing.
- `practice/templates/practice/advisory.html`: advisory hero now uses a two-column title/intro composition on desktop and stacks on smaller screens.
- `practice/templates/practice/service_detail.html`: service-detail hero uses the same compact two-column composition.
- Space-management principle: information is grouped into a tighter hierarchy so the title, executive context and first actionable content sit closer together, minimizing empty viewport area without crowding mobile layouts.

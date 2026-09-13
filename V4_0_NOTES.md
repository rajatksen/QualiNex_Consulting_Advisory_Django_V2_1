# QualiNex V4.0 — Global Hero Space Standard

## Purpose
Apply the requested ~0.8 mm (~3 CSS px) top-spacing reduction through the shared page-hero design system, rather than page-by-page overrides.

## Global rule
Central design token in `practice/static/practice/css/site.css`:

```css
:root{
  --hero-top-tighten:3px;
  --detail-hero-y:34px;
  --detail-hero-y-mobile:26px;
}
```

All `.page-hero` variants inherit the top tightening rule; `.page-hero--compact` uses the same centralized standard.

## Coverage
- Advisory
- Methodology
- Credentials
- Contact
- Service detail pages
- Engagement detail pages

Contact was moved onto the shared `.page-hero--compact` pattern so it uses the same compact hero standard rather than the taller generic hero.

## CTA wording
All packaged source/templates/previews now use `Book Consultation`.

## Validation
- Python `compileall`: PASS
- Stale `Book a Consultation`: none found in source/templates
- Prohibited strings: none found
- All `page-hero` templates inspected and mapped to the shared class
- Django `manage.py check`: not runnable in this build container because Django is not installed; run locally in the project's `.venv`.

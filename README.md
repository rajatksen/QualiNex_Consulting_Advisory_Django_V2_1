# QualiNex Consulting & Advisory — V2.1 Attached Changes

This package incorporates the suggestions in **My few suggestions.docx**.

## Applied changes

1. Homepage headline updated to:
   **Transform Quality from a Control Function into a Competitive Advantage.**
2. Homepage positioning updated to emphasise:
   - performance-gap identification
   - quality-system strengthening
   - Cost of Poor Quality reduction
   - sustainable operating discipline
   - measurable business results
3. Homepage calls to action updated to:
   - Book a Consultation
   - Explore Our Services
4. Homepage service keywords added:
   Manufacturing Quality | Operational Excellence | Supplier Quality | QMS | Industry 4.0 Readiness
5. Public-facing employer/company names removed or anonymised from:
   - Experience page
   - Credentials page
   - Recognition content
6. BCET removed from the academic foundation.
7. The QualiNex brand and the existing responsive layout are retained.

## Where to edit later

- Homepage content: `practice/templates/practice/home.html`
- Experience content: `practice/templates/practice/experience.html`
- Credentials and recognition: `practice/templates/practice/credentials.html`
- Shared navigation/header: `practice/templates/practice/base.html`
- Global styling and responsive layout: `practice/static/practice/css/site.css`
- Advisory service content: `practice/views.py`
- URL routing: `practice/urls.py`

## Run locally

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Important

The attached suggestions requested that personal employer/company names not be displayed publicly. The website therefore uses neutral descriptions such as “Global Secure Technology Manufacturer” and “Automotive Component Manufacturer.”

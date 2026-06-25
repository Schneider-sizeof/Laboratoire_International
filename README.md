# 🏥 Laboratoire International

> **Votre santé est Notre propriété**

Production-ready website for **Laboratoire International d'Analyses Médicales** — a medical laboratory in Tangier, Morocco.

🌐 [laboratoiretanger.com](https://laboratoiretanger.com)

---

## ✨ Features

- **7 Pages**: Home, About, Services, Results, Blog, Contact, Legal
- **6 Languages**: French (default), English, Arabic (RTL), Dutch, German, Spanish
- **SEO Optimized**: Schema.org JSON-LD, sitemaps, robots.txt, hreflang tags, meta descriptions
- **Mobile-First**: Fully responsive with mobile nav drawer
- **Blog System**: Multi-language blog with categories, search, pagination (n8n-ready)
- **Contact Form**: AJAX submission with database storage
- **Results Portal**: Redirect to external VisionLIS patient portal
- **Cookie Consent**: GDPR-compliant cookie banner
- **Accessibility**: WCAG 2.1, semantic HTML, ARIA labels, keyboard navigation
- **RTL Support**: Full right-to-left layout for Arabic

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Django 6.0 |
| Styling | Tailwind CSS 3.4 |
| Fonts | Inter, Noto Sans Arabic |
| Icons | Font Awesome 6 |
| Database | SQLite (dev) / PostgreSQL (prod) |
| i18n | Django i18n with `.po/.mo` files |

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Node.js 18+

### Setup

```bash
# Clone
git clone https://github.com/your-repo/Laboratoire_International.git
cd Laboratoire_International

# Python environment
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Node dependencies (for Tailwind CSS)
npm install

# Database
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Build CSS
npm run build:css

# Run dev server
python manage.py runserver
```

Visit **http://127.0.0.1:8000/fr/** to see the site.

### Development CSS Watch

```bash
npm run dev  # Auto-rebuilds CSS on template changes
```

## 🌍 Languages

| Code | Language | Direction |
|------|----------|-----------|
| `fr` | Français | LTR |
| `en` | English | LTR |
| `ar` | العربية | **RTL** |
| `nl` | Nederlands | LTR |
| `de` | Deutsch | LTR |
| `es` | Español | LTR |

### Adding/Editing Translations

1. Edit `locale/<lang>/LC_MESSAGES/django.po`
2. Run `python compile_messages.py`
3. Restart the server

## 📁 Project Structure

```
├── core/                       # Main Django app
│   ├── templates/core/         # All HTML templates
│   ├── static/core/
│   │   ├── css/
│   │   │   ├── tailwind-input.css  # Tailwind source
│   │   │   └── style.css           # Compiled output
│   │   ├── js/main.js
│   │   └── images/
│   ├── models.py               # Blog, ContactSubmission
│   ├── views.py                # All page views
│   ├── urls.py                 # URL routing
│   ├── admin.py                # Django admin config
│   ├── sitemaps.py             # SEO sitemaps
│   └── context_processors.py   # Site-wide variables
├── locale/                     # Translation files (6 langs)
├── labinternational/           # Django project settings
├── tailwind.config.js          # Tailwind configuration
├── package.json                # Node dependencies
└── requirements.txt            # Python dependencies
```

## 📝 Blog System

The blog supports n8n automation. Blog posts are managed via Django admin (`/admin/`).

Each post supports:
- Multi-language content (6 fields per language)
- Categories, tags, featured images
- Draft/Published status
- View counting
- SEO meta fields per language

### n8n Webhook Integration

The blog models are designed for webhook-based content creation. Point your n8n workflow to the Django admin API or create a custom REST endpoint.

## 🔗 VisionLIS Integration

The Results page redirects patients to the external VisionLIS portal:
```
http://liamt.ddns.net:12543/visionlis/#/loginpatient
```
No internal authentication — patients use credentials provided at the lab.

## 📊 SEO

- **Schema.org**: `MedicalBusiness`, `BlogPosting`, `BreadcrumbList`
- **Sitemap**: Auto-generated at `/sitemap.xml`
- **Robots.txt**: At `/robots.txt`
- **hreflang**: All 6 languages + x-default
- **Open Graph**: Titles, descriptions, URLs per page

## 🚢 Deployment (PythonAnywhere)

1. Upload code to PythonAnywhere
2. Set environment variables (see `.env.example`)
3. Run `pip install -r requirements.txt`
4. Run `python manage.py migrate`
5. Run `python manage.py collectstatic`
6. Configure WSGI to point to `labinternational.wsgi`

## 📄 License

© 2024 Laboratoire International. All rights reserved.

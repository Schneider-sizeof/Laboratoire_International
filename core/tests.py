from django.test import TestCase, Client
from django.urls import reverse
from core.models import SiteSettings, BlogPost
from django.contrib.auth.models import User
from django.utils import timezone

class SEORedirectsAndTagsTests(TestCase):
    def setUp(self):
        # Use SiteSettings.load() to get the singleton, then update and save it
        self.site_settings = SiteSettings.load()
        self.site_settings.site_name = "Laboratoire International Tanger"
        self.site_settings.site_domain = "laboratoiretanger.com"
        self.site_settings.email = "contact@laboratoireinternational.com"
        self.site_settings.phone = "+212 5 39 31 39 47"
        self.site_settings.address = "Avenue Moulay Rachid, Tanger 90000, Morocco"
        self.site_settings.save()
        # Create a test author user
        self.user = User.objects.create_user(username="testbiologist", password="password")
        # Create a test blog post
        self.post = BlogPost.objects.create(
            slug="test-post",
            status="published",
            author="Dr. Test",
            title_fr="Mon premier test",
            excerpt_fr="Extrait du test",
            content_fr="<p>Contenu du test</p>",
            meta_title_fr="Titre Meta",
            meta_description_fr="Description Meta",
            published_at=timezone.now()
        )
        self.client = Client()

    def test_root_redirect(self):
        """Visiting / should redirect to the default language prefix (/fr/)."""
        response = self.client.get('/', HTTP_HOST='laboratoiretanger.com')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/fr/')

    def test_home_one_page_redirect(self):
        """Visiting /home-one-page/ should 301 redirect permanently to /fr/."""
        response = self.client.get('/home-one-page/', HTTP_HOST='laboratoiretanger.com')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, '/fr/')

    def test_homepage_seo_elements(self):
        """Homepage should return 200, contain correct canonical, hreflang and schema."""
        response = self.client.get('/fr/', HTTP_HOST='laboratoiretanger.com')
        self.assertEqual(response.status_code, 200)
        
        # Check canonical & hreflang tags
        self.assertContains(response, '<link rel="canonical" href="https://laboratoiretanger.com/fr/">')
        self.assertContains(response, '<link rel="alternate" hreflang="fr" href="https://laboratoiretanger.com/fr/">')
        self.assertContains(response, '<link rel="alternate" hreflang="x-default" href="https://laboratoiretanger.com/fr/">')
        
        # Check that we do not have alternate links for un-translated languages (EN, AR, NL, etc.)
        self.assertNotContains(response, 'hreflang="en"')
        self.assertNotContains(response, 'hreflang="ar"')
        
        # Check Open Graph URL
        self.assertContains(response, '<meta property="og:url" content="https://laboratoiretanger.com/fr/">')
        
        # Check business name
        self.assertContains(response, 'Laboratoire International Tanger')
        
        # Check MedicalBusiness JSON-LD structure on homepage
        self.assertContains(response, '"@type": "MedicalBusiness"')
        self.assertContains(response, '"name": "Laboratoire International Tanger"')
        self.assertContains(response, '"reviewCount": "3"')
        self.assertContains(response, '"author":')
        self.assertContains(response, '"reviewBody":')

    def test_subpage_seo_elements(self):
        """Subpages should output matching canonical/hreflang tags pointing to the subpage path."""
        response = self.client.get('/fr/about/', HTTP_HOST='laboratoiretanger.com')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<link rel="canonical" href="https://laboratoiretanger.com/fr/about/">')
        self.assertContains(response, '<link rel="alternate" hreflang="fr" href="https://laboratoiretanger.com/fr/about/">')
        self.assertContains(response, '<link rel="alternate" hreflang="x-default" href="https://laboratoiretanger.com/fr/about/">')

    def test_blog_post_seo_elements(self):
        """Blog details page should render BlogPosting schema with headline and author."""
        response = self.client.get('/fr/blog/test-post/', HTTP_HOST='laboratoiretanger.com')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '"@type": "BlogPosting"')
        self.assertContains(response, '"headline": "Mon premier test"')
        self.assertContains(response, '"name": "Dr. Test"')

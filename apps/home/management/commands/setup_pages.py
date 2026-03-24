from django.core.management.base import BaseCommand
from wagtail.models import Page, Site

from apps.home.models import AboutPage, FacilityPage, HomePage
from apps.products.models import ProductIndexPage, ProductPage
from apps.blog.models import BlogIndexPage
from apps.downloads.models import DownloadIndexPage
from apps.contact.models import ContactPage
from apps.common.models import SiteSettings


class Command(BaseCommand):
    help = "Set up the initial Wagtail page tree for VTP."

    def handle(self, *args, **options):
        root_page = Page.objects.filter(depth=1).first()

        # --- HomePage ---
        home = HomePage.objects.first()
        if home:
            self.stdout.write(self.style.SUCCESS("HomePage already exists ✓"))
            created_home = False
        else:
            # Remove default Wagtail welcome page if present
            Page.objects.filter(depth=2, slug="home").delete()
            Page.fix_tree()

            home = HomePage(
                title="Vinsat Precision Technologies",
                slug="home",
                hero_title="Precision CNC Tube Bending Tooling",
                hero_subtitle="High-quality bend dies, clamp dies, pressure dies, wiper inserts, mandrels and accessories for CNC tube bending machines.",
                hero_cta_text="View Products",
                about_heading="About Vinsat Precision Technologies",
                about_text="<p>We are a leading manufacturer of precision CNC tube bending tooling, delivering quality solutions to manufacturers worldwide.</p>",
                cta_heading="Ready to Get Started?",
                cta_text="Contact us for a quote or to discuss your tooling requirements.",
                cta_button_text="Contact Us",
            )
            root_page.add_child(instance=home)
            home.save_revision().publish()
            self.stdout.write(self.style.SUCCESS("Creating HomePage... ✓"))
            created_home = True

        # --- Child pages ---
        # AboutPage
        self._get_or_create_child(
            home,
            AboutPage,
            title="About Us",
            slug="about",
            defaults={
                "heading": "About Us",
                "intro": "Vinsat Precision Technologies is a leading manufacturer of precision CNC tube bending tooling.",
                "body": "<p>With years of experience in precision manufacturing, we deliver high-quality tooling solutions to manufacturers worldwide.</p>",
                "mission_heading": "Our Mission",
                "mission_text": "To provide world-class precision tooling that helps manufacturers achieve excellence in tube bending operations.",
                "vision_heading": "Our Vision",
                "vision_text": "To be the global leader in CNC tube bending tooling solutions.",
            },
        )

        # FacilityPage
        self._get_or_create_child(
            home,
            FacilityPage,
            title="Our Facility",
            slug="facility",
            defaults={
                "heading": "Our Facility",
                "intro": "State-of-the-art manufacturing facility equipped with advanced CNC machinery.",
                "body": "<p>Our facility houses precision CNC machines and quality inspection equipment to manufacture high-quality tube bending tooling.</p>",
            },
        )

        # ProductIndexPage
        products_page = self._get_or_create_child(
            home,
            ProductIndexPage,
            title="Products",
            slug="products",
        )

        # BlogIndexPage
        self._get_or_create_child(
            home,
            BlogIndexPage,
            title="Blog",
            slug="blog",
            defaults={"intro": ""},
        )

        # DownloadIndexPage
        self._get_or_create_child(
            home,
            DownloadIndexPage,
            title="Downloads",
            slug="downloads",
            defaults={"heading": "Downloads", "intro": ""},
        )

        # ContactPage
        contact_page = self._get_or_create_child(
            home,
            ContactPage,
            title="Contact Us",
            slug="contact",
            defaults={
                "form_heading": "Send us a Message",
                "success_message": "Thank you for contacting us. We will get back to you shortly.",
            },
        )

        # --- Link HomePage CTA buttons to child pages ---
        if created_home:
            home.hero_cta_link = products_page
            home.cta_link = contact_page
            home.save_revision().publish()
            self.stdout.write(self.style.SUCCESS("HomePage CTA links updated ✓"))

        # --- Product pages ---
        product_names = [
            ("Bend Dies", "bend-dies"),
            ("Clamp Dies", "clamp-dies"),
            ("Pressure Dies", "pressure-dies"),
            ("Wiper Inserts", "wiper-inserts"),
            ("Mandrels", "mandrels"),
            ("Accessories", "accessories"),
        ]
        for name, slug in product_names:
            self._get_or_create_child(
                products_page,
                ProductPage,
                title=name,
                slug=slug,
                defaults={
                    "short_description": f"High-quality {name.lower()} for CNC tube bending machines.",
                    "description": f"<p>Precision-manufactured {name.lower()} designed for optimal performance and long tool life.</p>",
                },
            )

        # --- Site ---
        site = Site.objects.filter(is_default_site=True).first()
        if site:
            if site.root_page != home:
                site.root_page = home
                site.save()
                self.stdout.write(self.style.SUCCESS("Updated default site root to HomePage ✓"))
            else:
                self.stdout.write(self.style.SUCCESS("Default site already configured ✓"))
        else:
            Site.objects.create(
                hostname="localhost",
                root_page=home,
                is_default_site=True,
                site_name="Vinsat Precision Technologies",
            )
            self.stdout.write(self.style.SUCCESS("Created default site ✓"))

        # --- SiteSettings ---
        site = Site.objects.get(is_default_site=True)
        try:
            settings = SiteSettings.for_site(site)
            if not settings.company_name:
                settings.company_name = "Vinsat Precision Technologies"
                settings.tagline = "Precision Tooling Solutions"
                settings.save()
                self.stdout.write(self.style.SUCCESS("Updated SiteSettings ✓"))
            else:
                self.stdout.write(self.style.SUCCESS("SiteSettings already configured ✓"))
        except SiteSettings.DoesNotExist:
            SiteSettings.objects.create(
                site=site,
                company_name="Vinsat Precision Technologies",
                tagline="Precision Tooling Solutions",
            )
            self.stdout.write(self.style.SUCCESS("Created SiteSettings ✓"))

        self.stdout.write(self.style.SUCCESS("\nAll pages set up successfully! ✓"))

    def _get_or_create_child(self, parent, page_class, title, slug, defaults=None):
        """Get or create a child page under parent. Idempotent."""
        existing = page_class.objects.filter(slug=slug).first()
        if existing:
            self.stdout.write(self.style.SUCCESS(f"{title} page already exists ✓"))
            return existing

        page = page_class(title=title, slug=slug)
        if defaults:
            for key, value in defaults.items():
                setattr(page, key, value)
        parent.add_child(instance=page)
        page.save_revision().publish()
        self.stdout.write(self.style.SUCCESS(f"Creating {title} page... ✓"))
        return page

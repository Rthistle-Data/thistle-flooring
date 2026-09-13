#!/usr/bin/env python3
"""Generate Thistle Flooring static pages with shared chrome."""
from pathlib import Path

ROOT = Path("/home/regan/Desktop/thistleflooring")
SITE = "https://thistle-flooring.com"
MAIL = "thistleflooringinstalls@gmail.com"
MAILTO = f"mailto:{MAIL}?subject=Quote%20Request%20%E2%80%94%20Thistle%20Flooring"
PHONE = "(587) 594-8169"
SMS = "sms:5875948169"

GALLERY = [
    ("vinyl-living-walnut.jpg", "vinyl", "Living room · walnut vinyl click"),
    ("vinyl-rec-room-walnut.jpg", "vinyl", "Rec room · walnut vinyl click"),
    ("vinyl-open-kitchen-walnut.jpg", "vinyl", "Open living & kitchen · walnut vinyl click"),
    ("vinyl-hallway-gym.jpg", "vinyl", "Hallway · walnut vinyl click"),
    ("vinyl-hallway-weights.jpg", "vinyl", "Hallway transition · walnut vinyl click"),
    ("vinyl-stair-landing-walnut.jpg", "vinyl", "Stair landing · walnut vinyl click"),
    ("vinyl-living-vent.jpg", "vinyl", "Living area · walnut vinyl click"),
    ("vinyl-carpet-tearout.jpg", "vinyl", "Carpet tear-out for vinyl click"),
    ("vinyl-living-open.jpg", "vinyl", "Open-concept living · grey vinyl click"),
    ("vinyl-kitchen-grey.jpg", "vinyl", "Kitchen · grey vinyl click"),
    ("hardwood-white-oak.jpg", "hardwood", "Character white oak hardwood"),
    ("carpet-residential-beige.jpg", "carpet", "Residential carpet · professionally stretched"),
    ("vinyl-stairs-railing.jpg", "vinyl", "Vinyl click stairs · iron railing"),
    ("hardwood-walnut.jpg", "hardwood", "Rich walnut hardwood"),
    ("carpet-stairs-cream.jpg", "carpet", "Cream carpet stairs"),
    ("vinyl-living-entry.jpg", "vinyl", "Living room & entry · vinyl click"),
    ("vinyl-hallway-walnut.jpg", "vinyl", "Walnut-tone vinyl click hallway"),
    ("carpet-arcade-stars.jpg", "carpet", "Custom star-pattern carpet"),
    ("vinyl-oak-stairs.jpg", "vinyl", "Natural oak vinyl click stairs"),
    ("carpet-commercial-fireplace.jpg", "carpet", "Commercial carpet tiles · fireplace"),
    ("vinyl-bedroom-grey.jpg", "vinyl", "Bedroom · grey vinyl click"),
    ("vinyl-bathroom-oak.jpg", "vinyl", "Waterproof vinyl click · bath"),
    ("carpet-commercial-corridor.jpg", "carpet", "Commercial patterned carpet tiles"),
    ("vinyl-stairs-grey.jpg", "vinyl", "Grey vinyl click stairs"),
    ("carpet-stairs-grey.jpg", "carpet", "Grey residential carpet stairs"),
    ("vinyl-closet-grey.jpg", "vinyl", "Closet · grey vinyl click"),
    ("carpet-commercial-tiles.jpg", "carpet", "Commercial streaked carpet tiles"),
    ("vinyl-install-progress-walnut.jpg", "vinyl", "Install in progress · walnut vinyl click"),
    ("carpet-commercial-stairwell.jpg", "carpet", "Commercial carpet · stairwell"),
    ("vinyl-install-progress-light.jpg", "vinyl", "Install in progress · light oak vinyl"),
]

PREVIEW = [
    ("vinyl-living-walnut.jpg", "vinyl", "Living room · walnut vinyl click"),
    ("vinyl-rec-room-walnut.jpg", "vinyl", "Rec room · walnut vinyl click"),
    ("hardwood-white-oak.jpg", "hardwood", "Character white oak hardwood"),
    ("carpet-residential-beige.jpg", "carpet", "Residential carpet · professionally stretched"),
    ("vinyl-open-kitchen-walnut.jpg", "vinyl", "Open living & kitchen · walnut vinyl click"),
    ("vinyl-stair-landing-walnut.jpg", "vinyl", "Stair landing · walnut vinyl click"),
    ("hardwood-walnut.jpg", "hardwood", "Rich walnut hardwood"),
    ("carpet-stairs-cream.jpg", "carpet", "Cream carpet stairs"),
]


def header(active: str) -> str:
    def cls(name: str) -> str:
        return ' class="is-active"' if name == active else ""

    return f"""    <a class="skip" href="#main">Skip to content</a>
    <div class="announce">
      <a href="/contact#quote">Edmonton flooring installation · Get a free quote</a>
    </div>
    <header class="site-header">
      <div class="header-inner">
        <a class="brand" href="/" aria-label="Thistle Flooring home">
          <img src="assets/images/logo-wide.png" alt="Thistle Flooring">
        </a>
        <button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="primary-nav">
          <span></span><span></span><span></span>
        </button>
        <nav class="nav" id="primary-nav" aria-label="Primary">
          <a href="/services"{cls("services")}>Services</a>
          <a href="/winter-special"{cls("winter")}>Winter Special</a>
          <a href="/kitchen-revival"{cls("kitchen")}>Kitchen Revival</a>
          <a href="/gallery"{cls("gallery")}>Our Work</a>
          <a href="/contact"{cls("contact")}>Contact</a>
          <a class="btn btn-gold header-cta" href="/contact#quote">Get a Free Quote</a>
        </nav>
      </div>
    </header>"""


FOOTER = f"""    <nav class="mobile-contact" aria-label="Quick contact">
      <a href="{SMS}">Text us</a>
      <a class="btn btn-gold" href="/contact#quote">Free quote</a>
    </nav>
    <section class="quote-band">
      <div class="wrap">
        <p class="eyebrow" style="color:var(--gold)">Complimentary consultation</p>
        <h2>Ready for floors you’ll be proud of?</h2>
        <p>Tell us about the room. We’ll source the right material and install it with care — vinyl, laminate, hardwood, or carpet.</p>
        <div class="hero-actions">
          <a class="btn btn-gold" href="/contact#quote">Get a Free Quote</a>
          <a class="btn btn-outline" href="/contact">Contact</a>
        </div>
        <p class="contact-mini">Text only · <a href="{SMS}">{PHONE}</a></p>
      </div>
    </section>

    <div class="lightbox" role="dialog" aria-modal="true" aria-label="Photograph">
      <button class="lb-close" aria-label="Close">&times;</button>
      <button class="lb-btn lb-prev" aria-label="Previous">‹</button>
      <img src="" alt="">
      <button class="lb-btn lb-next" aria-label="Next">›</button>
      <p class="lightbox-cap"></p>
    </div>

    <footer class="site-footer">
      <div class="wrap-wide footer-grid">
        <div class="footer-brand">
          <img src="assets/images/logo-wide.png" alt="Thistle Flooring">
          <p>Based in Edmonton, Alberta. Precision sourcing and installation of vinyl, laminate, hardwood, and carpet. Craftsmanship you can live with.</p>
        </div>
        <div>
          <h4>Explore</h4>
          <ul>
            <li><a href="/services">Services</a></li>
            <li><a href="/gallery">Our Work</a></li>
            <li><a href="/winter-special">Winter Hibernation Special</a></li>
            <li><a href="/kitchen-revival">Express Kitchen Floor Revival</a></li>
          </ul>
        </div>
        <div>
          <h4>Materials</h4>
          <ul>
            <li><a href="/services#vinyl">Vinyl &amp; Vinyl Click</a></li>
            <li><a href="/services#laminate">Laminate</a></li>
            <li><a href="/services#hardwood">Hardwood</a></li>
            <li><a href="/services#carpet">Carpet</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="{MAILTO}">{MAIL}</a></li>
            <li>Text only · {PHONE}</li>
            <li><a href="/contact#quote">Request a quote</a></li>
            <li>Based in Edmonton, Alberta</li>
          </ul>
        </div>
      </div>
      <div class="wrap-wide footer-legal">
        <span>© <span id="year">2026</span> Thistle Flooring. All rights reserved.</span>
        <span>Precision Flooring. Beautifully Installed.</span>
      </div>
    </footer>
    <script src="js/main.js?v=20260913"></script>"""


def page(title: str, desc: str, active: str, body: str, extra_head: str = "", path: str = "/") -> str:
    url = f"{SITE}/" if path == "/" else f"{SITE}{path}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18408874410"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'AW-18408874410');
</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <link rel="icon" type="image/jpeg" href="assets/images/mark-thistle.jpg">
  <link rel="apple-touch-icon" href="assets/images/mark-thistle.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css?v=20260913">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE}/assets/images/hero-home.jpg">
  {extra_head}
</head>
<body>
{header(active)}
  <main id="main">
{body}
  </main>
{FOOTER}
</body>
</html>
"""


HOME = f"""
    <section class="hero">
      <div class="hero-media" aria-hidden="true">
        <img src="assets/gallery/vinyl-rec-room-walnut.jpg" alt="" fetchpriority="high">
      </div>
      <div class="hero-content">
        <p class="hero-kicker">Edmonton, Alberta</p>
        <h1>Edmonton flooring.<br>Beautifully installed.</h1>
        <hr class="gold-rule">
        <p class="hero-sub">Vinyl, laminate, hardwood, and carpet, supplied and installed by a locally owned Edmonton company. Tell us about your room for a free quote.</p>
        <div class="hero-actions">
          <a class="btn btn-gold" href="/contact#quote">Get a Free Quote</a>
          <a class="btn btn-outline" href="/gallery">View Our Work</a>
        </div>
      </div>
      <div class="hero-scroll" aria-hidden="true"><span>Scroll</span><i></i></div>
    </section>

    <div class="place-bar">
      Locally owned · based in <strong>Edmonton, Alberta</strong> · serving the capital region
    </div>

    <section class="section">
      <div class="wrap split">
        <div class="split-copy">
          <p class="eyebrow">Your local flooring installer</p>
          <h2>Floors that feel considered — not hurried.</h2>
          <hr class="gold-rule">
          <p class="lead">Thistle Flooring is a premium installation company based in Edmonton, Alberta, for homeowners who want the job done once, and done properly. We source quality vinyl, laminate, hardwood, and carpet, then install with the patience of a craftsman: square, quiet, and finished to the baseboard.</p>
          <p>From a single kitchen to a whole-home replacement, every project is measured, planned, and completed with the same standard — clean lines, honest pricing, and workmanship you can live with.</p>
          <div class="stat-row">
            <div><strong>From $3</strong><span>Vinyl click / sq ft<br>material + labour</span></div>
            <div><strong>1 day</strong><span>Kitchen floor revival</span></div>
            <div><strong>Free</strong><span>Winter carpet tear-out</span></div>
          </div>
        </div>
        <img src="assets/gallery/vinyl-rec-room-walnut.jpg" alt="Edmonton rec room with newly installed walnut vinyl click flooring">
      </div>
    </section>

    <section class="section" style="background:var(--cream); padding-top:88px;">
      <div class="wrap-wide">
        <p class="eyebrow">Materials we install</p>
        <h2>Four surfaces. One standard.</h2>
        <p class="lead">Whether you want waterproof vinyl in the kitchen, quiet carpet on the stairs, or hardwood that ages with the house — we source it and we install it.</p>
        <div class="services-grid">
          <a class="svc-card" href="/services#vinyl">
            <img src="assets/gallery/vinyl-living-walnut.jpg" alt="Walnut vinyl click living room floor">
            <span class="num">01</span>
            <h3>Vinyl</h3>
            <p>Waterproof, quiet underfoot, and built for real life — including vinyl click with material and labour pricing confirmed in your quote.</p>
            <div class="price">From $3 / sq ft installed</div>
          </a>
          <a class="svc-card" href="/services#laminate">
            <img src="assets/gallery/vinyl-hallway-walnut.jpg" alt="Walnut-tone wood-look flooring in a hallway">
            <span class="num">02</span>
            <h3>Laminate</h3>
            <p>The look of timber with a tough wear layer — an elegant, practical choice for busy homes.</p>
            <div class="price">Sourced &amp; installed</div>
          </a>
          <a class="svc-card" href="/services#hardwood">
            <img src="assets/gallery/hardwood-walnut.jpg" alt="Rich walnut hardwood floor">
            <span class="num">03</span>
            <h3>Hardwood</h3>
            <p>True wood, laid with precision. Character grain, clean seams, and a finish that belongs in the house.</p>
            <div class="price">Premium installation</div>
          </a>
          <a class="svc-card" href="/services#carpet">
            <img src="assets/gallery/carpet-residential-beige.jpg" alt="Freshly installed beige residential carpet">
            <span class="num">04</span>
            <h3>Carpet</h3>
            <p>Residential and commercial carpet, stairs, and custom patterns — stretched tight and finished clean.</p>
            <div class="price">Tear-out included this winter</div>
          </a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap-wide">
        <p class="eyebrow">Limited offers</p>
        <h2>Seasonal work, considered pricing.</h2>
        <div class="specials-grid">
          <a class="special-card" href="/winter-special">
            <img src="assets/images/hero-winter.jpg" alt="Cozy winter living room with hardwood floors and snowfall outside">
            <span class="badge">Limited season</span>
            <h3>Winter Hibernation Special</h3>
            <p>Complimentary carpet tear-out and demolition when you install new carpet, vinyl click, or laminate.</p>
          </a>
          <a class="special-card" href="/kitchen-revival">
            <img src="assets/images/hero-kitchen.jpg" alt="Sunlit kitchen with new light oak vinyl plank flooring">
            <span class="badge">One day</span>
            <h3>Express Kitchen Floor Revival</h3>
            <p>Kitchen demolition and vinyl click installation from $500 plus material. Most kitchens completed in one day; scope confirmed before booking.</p>
          </a>
        </div>
      </div>
    </section>

    <section class="section" style="background:var(--cream);">
      <div class="wrap-wide">
        <div style="display:flex;justify-content:space-between;align-items:end;gap:24px;flex-wrap:wrap;">
          <div>
            <p class="eyebrow">Recent installations</p>
            <h2>Work from the floor up.</h2>
            <p class="lead" style="margin-top:8px;">Just in: walnut vinyl click throughout an Edmonton rec room — from carpet tear-out to a finished floor.</p>
          </div>
          <a class="btn btn-outline-dark" href="/gallery">Full gallery</a>
        </div>
        <div class="gallery-grid preview-grid">
""" + "\n".join(
    f"""          <figure class="g-item" data-cat="{cat}">
            <img src="assets/gallery/{fn}" alt="{cap}" loading="lazy">
            <figcaption>{cap}</figcaption>
          </figure>"""
    for fn, cat, cap in PREVIEW
) + """
        </div>
      </div>
    </section>
"""


SERVICES = f"""
    <section class="page-hero">
      <div class="hero-media" aria-hidden="true">
        <img src="assets/gallery/hardwood-white-oak.jpg" alt="">
      </div>
      <div class="page-hero-body">
        <p class="eyebrow" style="color:var(--gold)">Sourcing &amp; installation</p>
        <h1>Materials chosen well. Installed better.</h1>
        <p class="lead">Vinyl, laminate, hardwood, and carpet — selected for the room they live in, then laid to a professional finish.</p>
      </div>
    </section>

    <section class="section" style="padding-top:24px;padding-bottom:24px;">
      <div class="wrap">

        <article class="material" id="vinyl">
          <img src="assets/gallery/vinyl-kitchen-grey.jpg" alt="Grey vinyl click flooring in a kitchen">
          <div class="material-copy">
            <p class="eyebrow">01 — Vinyl</p>
            <h2>Vinyl &amp; Vinyl Click</h2>
            <hr class="gold-rule">
            <p class="lead">Waterproof, warm underfoot, and remarkably convincing as timber. Vinyl click is our most requested residential install — kitchens, baths, basements, and whole-home replacements.</p>
            <ul class="checklist">
              <li>Luxury vinyl plank and vinyl click, professionally sourced</li>
              <li>Precision cuts at cabinets, stairs, and transitions</li>
              <li>Underlayment, trims, and baseboard finishing</li>
              <li>Ideal for busy households and moisture-prone rooms</li>
            </ul>
            <div class="price-lock">
              <em>From $3</em>
              <span>per square foot for Vinyl Click — includes material and labour. Ask us to confirm the material selection and full scope for your project.</span>
            </div>
            <p style="margin-top:22px;"><a class="btn btn-forest" href="/contact?project=Vinyl%20Click#quote">Request a vinyl quote</a></p>
          </div>
        </article>

        <article class="material" id="laminate">
          <img src="assets/gallery/vinyl-hallway-walnut.jpg" alt="Walnut-tone wood-look laminate style hallway">
          <div class="material-copy">
            <p class="eyebrow">02 — Laminate</p>
            <h2>Laminate</h2>
            <hr class="gold-rule">
            <p class="lead">The presence of hardwood with a high-wear surface that stands up to daily life. We source quality laminate with convincing grain and install it floating, quiet, and true.</p>
            <ul class="checklist">
              <li>Quality boards with realistic texture and bevel</li>
              <li>Proper acclimation, expansion gaps, and transitions</li>
              <li>Stair nosing and matching trims available</li>
              <li>A refined look at a practical investment</li>
            </ul>
            <p style="margin-top:22px;"><a class="btn btn-forest" href="/contact?project=Laminate#quote">Request a laminate quote</a></p>
          </div>
        </article>

        <article class="material" id="hardwood">
          <img src="assets/gallery/hardwood-walnut.jpg" alt="Rich walnut hardwood installation">
          <div class="material-copy">
            <p class="eyebrow">03 — Hardwood</p>
            <h2>Hardwood</h2>
            <hr class="gold-rule">
            <p class="lead">Solid and engineered hardwood, laid with the respect the material deserves. Character grain, tight seams, and a floor that will age with the house rather than against it.</p>
            <ul class="checklist">
              <li>Solid and engineered hardwood, carefully sourced</li>
              <li>Nail-down, glue-down, or floating as the product requires</li>
              <li>Staircases, landings, and detailed perimeter work</li>
              <li>A heirloom surface when you want the real thing</li>
            </ul>
            <p style="margin-top:22px;"><a class="btn btn-forest" href="/contact?project=Hardwood#quote">Request a hardwood quote</a></p>
          </div>
        </article>

        <article class="material" id="carpet">
          <img src="assets/gallery/carpet-stairs-cream.jpg" alt="Cream carpet installed on a staircase with wood railing">
          <div class="material-copy">
            <p class="eyebrow">04 — Carpet</p>
            <h2>Carpet</h2>
            <hr class="gold-rule">
            <p class="lead">From quiet bedrooms to commercial corridors and custom patterned rooms — we stretch, seam, and finish carpet so it sits tight, looks tailored, and lasts.</p>
            <ul class="checklist">
              <li>Residential broadloom and commercial carpet tile</li>
              <li>Stairs, landings, and waterfall or cap-and-band finishes</li>
              <li>Custom patterns and specialty installations</li>
              <li>This winter: complimentary tear-out with new carpet, vinyl click, or laminate</li>
            </ul>
            <p style="margin-top:22px;"><a class="btn btn-forest" href="/winter-special">See the winter special</a></p>
          </div>
        </article>

      </div>
    </section>
"""


WINTER = f"""
    <section class="page-hero">
      <div class="hero-media" aria-hidden="true">
        <img src="assets/images/hero-winter.jpg" alt="">
      </div>
      <div class="page-hero-body">
        <p class="limited" style="color:var(--gold);">Limited-time seasonal offer</p>
        <h1>Winter Hibernation Special</h1>
        <p class="lead">Stay in. We’ll take the old carpet with us. Complimentary tear-out and demolition when you install new carpet, vinyl click, or laminate this season.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap split">
        <div>
          <p class="eyebrow">The offer</p>
          <h2>Free carpet tear-out when you install new floors.</h2>
          <hr class="gold-rule">
          <p class="lead">Winter is the quiet season for most homes — and the right moment to replace tired carpet without paying extra to have it pulled. Book new carpet, vinyl click, or laminate with Thistle Flooring and the demolition is on us.</p>
          <div class="offer-panel" style="margin-top:32px;">
            <p class="limited">Exclusive · while the season lasts</p>
            <h3>What’s included</h3>
            <ul class="include-list">
              <li>Full carpet tear-out and demolition at no charge</li>
              <li>Applies to new Carpet, Vinyl Click, or Laminate installs</li>
              <li>Removal of tack strip and debris from the work area</li>
              <li>Professional installation of your new floor</li>
            </ul>
            <a class="btn btn-gold" href="/contact?project=Winter%20Hibernation%20Special#quote">Request this offer</a>
            <p class="note" style="margin:16px 0 0;">Mention the Winter Hibernation Special when you write or text. Availability is limited and offered at our discretion for qualifying projects.</p>
          </div>
        </div>
        <div class="before-after">
          <figure>
            <img src="assets/gallery/vinyl-carpet-tearout.jpg" alt="Carpet tear-out in progress before a vinyl click install">
            <figcaption>Before · complimentary carpet tear-out</figcaption>
          </figure>
          <figure>
            <img src="assets/gallery/vinyl-living-walnut.jpg" alt="The same room finished in walnut vinyl click">
            <figcaption>After · walnut vinyl click</figcaption>
          </figure>
        </div>
      </div>
    </section>
"""


KITCHEN = f"""
    <section class="page-hero">
      <div class="hero-media" aria-hidden="true">
        <img src="assets/images/hero-kitchen.jpg" alt="">
      </div>
      <div class="page-hero-body">
        <p class="eyebrow" style="color:var(--gold)">One-day kitchen swap</p>
        <h1>Express Kitchen Floor Revival</h1>
        <p class="lead">A complete kitchen floor — demolished and reborn in vinyl click — in a single day. Low disruption. High impact. Built for busy homeowners.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap split">
        <img src="assets/gallery/vinyl-kitchen-grey.jpg" alt="Completed grey vinyl click kitchen floor" style="object-position:center 82%;">
        <div>
          <p class="eyebrow">The revival</p>
          <h2>In by morning. Cooking by evening.</h2>
          <hr class="gold-rule">
          <p class="lead">Kitchens take the most wear and show it first. Our Express Kitchen Floor Revival replaces the tired surface with waterproof vinyl click — without a week of dust, contractors, and takeout.</p>
          <div class="offer-panel" style="margin-top:28px;">
            <p class="limited">Signature service</p>
            <div class="offer-price">$500 <small>+ cost of material</small></div>
            <p>Kitchen floor demolition and vinyl click installation, with material billed separately. Most kitchens are completed in one day.</p>
            <ul class="include-list">
              <li>Full demolition of the existing kitchen floor</li>
              <li>Vinyl click installation — usually completed the same day</li>
              <li>Re-installation of baseboards</li>
              <li>Moving of appliances as needed</li>
            </ul>
            <a class="btn btn-gold" href="/contact?project=Express%20Kitchen%20Floor%20Revival#quote">Book a kitchen revival</a>
            <p class="note" style="margin:16px 0 0;">Material is selected with you and billed separately. Before booking, we’ll confirm whether your kitchen qualifies for the $500 offer, the total price, and the expected schedule. Unusual layouts or extensive subfloor repair may require additional time.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section" style="background:var(--cream);">
      <div class="wrap">
        <p class="eyebrow">Why it works</p>
        <h2>Fast, quiet, waterproof.</h2>
        <div class="trio">
          <div>
            <p class="eyebrow">01</p>
            <h3>Low disruption</h3>
            <p>One day in the kitchen — not a week of living around a job site. Appliances are moved as needed and set back.</p>
          </div>
          <div>
            <p class="eyebrow">02</p>
            <h3>Finished properly</h3>
            <p>Baseboards come off and go back on. Transitions are clean. You are not left with a floor that looks temporary.</p>
          </div>
          <div>
            <p class="eyebrow">03</p>
            <h3>Built for kitchens</h3>
            <p>Vinyl click is waterproof, easy to live with, and available in grains that read as timber — without timber’s fear of spills.</p>
          </div>
        </div>
      </div>
    </section>
"""

gallery_figures = "\n".join(
    f"""          <figure class="g-item" data-cat="{cat}">
            <img src="assets/gallery/{fn}" alt="{cap}" loading="lazy">
            <figcaption>{cap}</figcaption>
          </figure>"""
    for fn, cat, cap in GALLERY
)

GALLERY_PAGE = f"""
    <section class="page-hero" style="min-height:42vh;">
      <div class="hero-media" aria-hidden="true">
        <img src="assets/gallery/hardwood-walnut.jpg" alt="">
      </div>
      <div class="page-hero-body">
        <p class="eyebrow" style="color:var(--gold)">Our work</p>
        <h1>Floors, finished.</h1>
        <p class="lead">A selection of recent vinyl click, hardwood, and carpet installations across Edmonton and Alberta — including our latest walnut vinyl click rec-room install.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap-wide">
        <div class="filters" role="tablist" aria-label="Filter gallery">
          <button class="filter-btn is-on" data-filter="all">All</button>
          <button class="filter-btn" data-filter="vinyl">Vinyl Click</button>
          <button class="filter-btn" data-filter="hardwood">Hardwood</button>
          <button class="filter-btn" data-filter="carpet">Carpet</button>
        </div>
        <div class="gallery-grid">
{gallery_figures}
        </div>
      </div>
    </section>

"""


CONTACT = f"""
    <section class="page-hero" style="min-height:40vh;">
      <div class="hero-media" aria-hidden="true">
        <img src="assets/images/hero-home.jpg" alt="">
      </div>
      <div class="page-hero-body">
        <p class="eyebrow" style="color:var(--gold)">Consultation</p>
        <h1>Get a free quote.</h1>
        <p class="lead">Describe the room. We’ll come back with a clear plan — material, labour, and timing — without the runaround.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap contact-layout">
        <aside class="contact-card">
          <img src="assets/images/logo-wide.png" alt="Thistle Flooring" style="height:64px;width:auto;margin-bottom:22px;">
          <h3>Speak with us directly</h3>
          <p>Quotes are complimentary. Text is the fastest way to reach us; email is perfect for photos and measurements.</p>
          <dl>
            <dt>Email</dt>
            <dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
            <dt>Phone · text only</dt>
            <dd><a href="{SMS}">{PHONE}</a></dd>
            <dt>Based in</dt>
            <dd>Edmonton, Alberta</dd>
            <dt>Service</dt>
            <dd>Vinyl · Laminate · Hardwood · Carpet<br>Edmonton homeowners &amp; light commercial</dd>
          </dl>
          <p style="margin-top:28px;"><button type="button" class="btn btn-gold" id="copy-email" data-email="{MAIL}">Copy email address</button></p>
        </aside>

        <div class="quote-form-panel" id="quote">
          <p class="eyebrow">Quote request</p>
          <h2>Tell us about the floor.</h2>
          <p class="form-note">We’ll reply by email to discuss your project, materials, and timing. Measurements are optional if you’re still planning.</p>
          <form id="quote-form" style="margin-top:28px;">
            <div class="form-row">
              <label>Name *
                <input type="text" name="name" required autocomplete="name" placeholder="Your name">
              </label>
              <label>Email *
                <input type="email" name="email" required autocomplete="email" placeholder="you@email.com">
              </label>
            </div>
            <div class="form-row">
              <label>Phone (for texts)
                <input type="tel" name="phone" autocomplete="tel" placeholder="{PHONE}">
              </label>
              <label>Project type
                <select name="project">
                  <option value="">Select…</option>
                  <option>Vinyl Click</option>
                  <option>Laminate</option>
                  <option>Hardwood</option>
                  <option>Carpet</option>
                  <option>Winter Hibernation Special</option>
                  <option>Express Kitchen Floor Revival</option>
                  <option>Not sure — please advise</option>
                </select>
              </label>
            </div>
            <label>Approximate square footage
              <input type="text" name="sqft" placeholder="e.g. 420">
            </label>
            <label>Details
              <textarea name="message" placeholder="Rooms involved, existing floor, timing, and anything we should know."></textarea>
            </label>
            <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
            <p class="form-success" role="status">Thank you — your quote request is on its way. We’ll be in touch shortly.</p>
            <p class="form-error" role="alert"></p>
            <button class="btn btn-gold" type="submit">Send quote request</button>
          </form>
        </div>
      </div>
    </section>
"""


pages = {
    "index.html": page(
        "Edmonton Flooring Installation | Thistle Flooring",
        "Premium vinyl, laminate, hardwood, and carpet sourcing and installation. Vinyl click from $3/sq ft. Based in Edmonton, Alberta.",
        "home",
        HOME,
        path="/",
    ),
    "services.html": page(
        "Services — Vinyl, Laminate, Hardwood & Carpet | Thistle Flooring",
        "Vinyl click installation from $3 per square foot including material and labour. Laminate, hardwood, and carpet sourcing and professional installation.",
        "services",
        SERVICES,
        path="/services",
    ),
    "winter-special.html": page(
        "Winter Hibernation Special | Thistle Flooring",
        "Limited-time offer: free carpet tear-out and demolition when you install new carpet, vinyl click, or laminate with Thistle Flooring.",
        "winter",
        WINTER,
        path="/winter-special",
    ),
    "kitchen-revival.html": page(
        "Express Kitchen Floor Revival | Thistle Flooring",
        "Complete kitchen floor demolition and vinyl click installation in a single day for $500 plus the cost of material. Baseboards and appliances included.",
        "kitchen",
        KITCHEN,
        path="/kitchen-revival",
    ),
    "gallery.html": page(
        "Our Work — Installation Gallery | Thistle Flooring",
        "A gallery of recent Thistle Flooring installations: vinyl click, hardwood, and carpet — residential and commercial.",
        "gallery",
        GALLERY_PAGE,
        path="/gallery",
    ),
    "contact.html": page(
        "Get a Free Quote | Thistle Flooring",
        "Request a complimentary flooring quote from Thistle Flooring in Edmonton, Alberta. Email thistleflooringinstalls@gmail.com or text (587) 594-8169.",
        "contact",
        CONTACT,
        path="/contact",
    ),
    "404.html": page(
        "Page not found | Thistle Flooring",
        "That page doesn’t exist. Return to Thistle Flooring for vinyl, laminate, hardwood, and carpet installation.",
        "home",
        """
    <section class="section" style="min-height:60vh;display:flex;align-items:center;">
      <div class="wrap" style="text-align:center;">
        <p class="eyebrow">404</p>
        <h1 style="color:var(--forest);font-size:clamp(2.4rem,5vw,4rem);">This floor doesn’t go there.</h1>
        <hr class="gold-rule" style="margin-left:auto;margin-right:auto;">
        <p class="lead" style="margin-inline:auto;">The page you’re looking for has been pulled up — or never laid down. Let’s get you back on solid ground.</p>
        <div class="hero-actions" style="margin-top:32px;">
          <a class="btn btn-forest" href="/">Home</a>
          <a class="btn btn-outline-dark" href="/contact">Get a Free Quote</a>
        </div>
      </div>
    </section>
""",
    ),
}

for name, html in pages.items():
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name, "bytes", len(html))
print("done")

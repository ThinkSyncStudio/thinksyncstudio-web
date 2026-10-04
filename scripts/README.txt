Website maintenance
===================
All product and website support links use support@thinksyncstudio.com.
Do not modify archive/ when publishing the current website.

After editing shared styles.css, script.js, or assets/og-studio.png:
  python3 scripts/version-assets.py
  python3 scripts/version-assets.py --check
  python3 scripts/check-site.py
  node --check script.js
  git diff --check

The version script adds content hashes to CSS/JS and the studio social image.
This refreshes assets on the next HTML load, not an already-open browser tab.
GitHub Pages may cache HTML briefly; social services may cache their own previews.

Social image source: assets/og-studio.svg (1200 x 630).
Render to assets/og-studio.png with an SVG renderer such as Sharp after edits.

Adding an app:
1. Add its product page, approved artwork, and coming-soon or release status.
2. Add its card to apps/index.html and its link to every Apps dropdown.
3. Keep the homepage at six featured cards as the directory grows.
4. Add app-specific policies/status to policies/index.html and support/index.html.
5. Add the slug to scripts/check-site.py, then run the checks above.
6. Verify desktop and narrow-screen navigation and commit/push to main.

Policy release review — October 3, 2026
======================================
Braglytics: existing web policies retained; support address aligned with current
app docs. Verify final build and App Store disclosures before release.
AteYet: existing web policies retained. Verify final build and store disclosures.
Back to Better: privacy copied from PRIVACY.md, effective August 23, 2026;
support updated. Original Silicon Forest AI publisher attribution preserved,
not silently converted into a different legal entity. Current app configuration
uses Apple's standard EULA. Confirm publisher identity before release.
YUAN: AppLegal.swift links to syncareal.github.io/yuan-legal/privacy/ and /terms/;
both returned 404. No final source terms recovered. Website has a clearly marked
privacy draft and pending-terms notice. SECURE_TRANSFERS.md and CloudKit transfer
code supersede the README's blanket no-cloud wording. Confirm final transfer
setup, cleanup, retention, permissions, publisher identity, and app license.
Gossamer: docs/index.html's July 4 policy omits optional Image Playground and
Dream Bank behavior present in current code. Website uses a labeled draft;
terms remain pending. Confirm image processing, whether Dream Bank will ship,
its operator/retention/deletion/consent, and purchase/subscription terms.
AutoJustice: existing app privacy and terms reproduced as development drafts,
with support normalized. Preserve original terms instead of inventing new
pricing, refund, jurisdiction, or liability commitments. Confirm production
providers, deletion/backups, anonymous/account access, fees and refunds before
launch. Source README and implementation differ in some account-flow details.

Important: these are website changes only. No app source repositories, installed
builds, App Store Connect metadata, email routing, or external policy sites were
modified. Update those separately to use the final studio policy/support URLs.
Have unresolved privacy and legal documents reviewed before public release.

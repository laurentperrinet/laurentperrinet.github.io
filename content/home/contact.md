---
# An instance of the Contact widget.
# Documentation: https://docs.hugoblox.com/getting-started/page-builder/
widget: contact

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 90

title: Contact
subtitle: How to reach me

content:
  # Automatically link email and phone or display as text?
  autolink: true

  # Email form provider
  form:
    provider: formspree
    formspree:
      id: test
    netlify:
      # Enable CAPTCHA challenge to reduce spam?
      captcha: false


  # Contact (edit or remove options as required)
  email: laurent.perrinet@univ-amu.fr
  phone: +33 619 478 120
  address:
    street: Institut de Neurosciences de la Timone (UMR 7289), Aix Marseille Université - CNRS, Faculté de Médecine - Bâtiment Neurosciences, 27, Bd Jean Moulin
    city: Marseille
    region: PACA
    postcode: 13385 Marseille Cedex 05
    country: France
    country_code: FR
  coordinates:
    latitude: '43.2869'
    longitude: '5.4035'
  directions: When you reach the INT building, take the stairs to the second floor, then enter the open space on the left and follow it to the end of the room; my office is on the right-hand side.
  office_hours: []
  appointment_url: ''
  contact_links:
    - icon: orcid
      icon_pack: ai
      name: OrcID
      link: http://orcid.org/0000-0002-9536-010X
    - icon: mastodon
      icon_pack: fab
      name: mastodon
      link: https://neuromatch.social/@laurentperrinet
    - icon: bluesky
      icon_pack: fab
      name: Bluesky
      link: https://bsky.app/profile/laurentperrinet.bsky.social
    - icon: linkedin
      icon_pack: fab
      name: LinkedIn
      link: https://www.linkedin.com/in/laurent-perrinet-1857b9/
    - icon: researcherid
      icon_pack: ai
      name: ResearcherID
      link: https://www.webofscience.com/wos/author/record/1215734
    - icon: pubpeer
      icon_pack: ai
      name: NeuroTree
      link: https://neurotree.org/neurotree/peopleinfo.php?pid=18540
    - icon: google-scholar
      icon_pack: ai
      name: Google Scholar
      link: https://scholar.google.com/citations?user=TVyUV38AAAAJ
    - icon: zotero
      icon_pack: ai
      name: Zotero
      link: https://www.zotero.org/groups/2485979/laurent_perrinet/library
    - icon: publons
      icon_pack: ai
      name: Publons
      link: https://publons.com/a/1206845/
    - icon: arxiv
      icon_pack: ai
      name: arXiv
      link: https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=Perrinet%2C+L&terms-0-field=author&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=50&order=-announced_date_first
    - icon: github
      icon_pack: fab
      name: GitHub
      link: https://github.com/laurentperrinet
    - icon: instagram
      icon_pack: fab
      name: instagram
      link: https://www.instagram.com/laurentperrinet/
    - icon: palette
      icon_pack: fab
      name: pixelfed
      link: https://pixelfed.social/i/web/profile/505657488394461667
    - icon: stackoverflow
      icon_pack: ai
      name: stackoverflow
      link: https://stackoverflow.com/users/234547/meduz
    - icon: lastfm
      icon_pack: fab
      name: LastFM
      link: https://www.last.fm/fr/user/meduz

design:
  columns: '2'
---

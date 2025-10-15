---
# An instance of the Pages widget.
# Documentation: https://docs.hugoblox.com/getting-started/page-builder/
widget: pages

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 45

title: 'Recent & Upcoming Talks'
subtitle:

content:
  # Page type to display. E.g. post, event, publication...
  page_type: talk
  # Choose how many pages you would like to display (0 = all pages)
  count: 5
  # Filter on criteria
  filters:
    author: ""
    category: ""
    tag: ""
    exclude_featured: false
    exclude_future: false
    exclude_past: false
    publication_type: ""
  # Choose how many pages you would like to offset by
  offset: 0
  # Page order: descending (desc) or ascending (asc) date.
  order: desc

design:
  # Choose a view for the listings:
  view: citation
  columns: '2'
---

{{% callout note %}}
Access the list of [all previous talks](./talk/).
{{% /callout %}}

Varsity Customs Store Factory

Automated pipeline for scaling personalized team e-commerce.

Workflow Overview

Research: Scraper/API identifies public school data and adds it to Airtable.

Enrichment: Clearbit API & Google Search API retrieve the high-res logo.

Creation: shopify_generator.py (via Make.com) creates the collection & gating logic.

Outreach: Instantly.ai triggers a personalized sequence to the coach.

Activation: When the coach clicks 'Go Live', the Shopify collection is published.

Installation

Set up Airtable base using airtable_schema.json.

Add Shopify Private App credentials to the Python script.

Deploy Liquid snippet to the Shopify theme for gating.
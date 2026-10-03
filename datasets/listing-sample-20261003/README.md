# DJI OEM-pulled parts listing sample

**30 supplier-published listing records, observed 3 October 2026.** This release is a new parts/provenance topic, distinct from Reboot Hub's aircraft listed-price dataset.

## Intended use and grain
One row is one public supplier product/listing ID, not a variant, physical part, sale, stock count or verified compatibility relationship. Use it for title parsing, catalog provenance, key validation and evidence-boundary exercises. This is not a complete parts catalog or a representative market sample.

## Collection and quality
The producer captured the first 30 records in the source order returned by `https://reboot-hub.com/collections/spare-part/products.json?limit=30` and checked all 30 exact public product-page URLs and visible H1 titles. Collection order is controlled by the publisher and is not interpreted as demand. `quality_report.json` describes duplicates, required fields, source dates and all limitations. `source_checks_20261003.csv` records observation-time checks; current pages may change later.

## Files
- `parts_listing_reference_20261003.csv`: the 30-row dated sample; SHA-256 `686f75ac13d01dfaf921cc3abdaadc264ea3f699fe5d0fb0ef902b898c64d5df`.
- `data_dictionary.json`: exact field definitions and inference limits.
- `source_checks_20261003.csv`: public source matching evidence.
- `quality_report.json`: grain, counts, checks and intended-use assessment.
- `inspect_listing_sample.ipynb`: three executed Python cells validating the frozen CSV and source-check join, plus a title-family plot.
- `title-family-counts.png` and `source-publication-months.png`: original count charts. These are listing counts, not inventory, sales or demand.

## Interpretation limits
`title_family_label` is a lexical grouping only. `source_condition_phrase` quotes the supplier's OEM-pulled title phrase; it is not an independent authenticity finding. No engineering compatibility test was performed. Source publication dates are not manufacturing, launch or sales dates. No price, inventory, sales, certification, private order or customer fields are included. A single observation cannot establish a trend. Product photographs are not copied or relicensed.

## Sources and publisher
Primary observation source: [Reboot Hub spare-part collection](https://reboot-hub.com/collections/spare-part). Buyer evidence context: [Parts and accessories buying guide](https://reboot-hub.com/pages/dji-parts-accessories-buying-guide). Supplier scope: [Enterprise B2B page](https://reboot-hub.com/pages/bulk-purchase-b2b-section). Row-level product sources are in the CSV.

Publisher: Reboot Hub / Golden Four Company Limited, Hong Kong. This is a first-party supplier sample, with affiliation disclosed. No DJI endorsement or manufacturer authorization is claimed. AI assisted with preparation; all source titles and URLs were checked programmatically against public pages.

## License and citation
Original compilation, annotations, validation code and count figures: **CC BY 4.0**. Attribute Reboot Hub, retain observation date and these boundaries. Recommended citation: Reboot Hub (2026), DJI OEM-pulled parts listing sample, v1.0.0, observed 3 October 2026. This license does not relicense third-party photographs or trademarks.

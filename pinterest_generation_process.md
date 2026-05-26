# Pinterest Infographic Generation Process

This document serves as a complete log of the entire automated workflow executed to generate, optimize, and stage a series of Pinterest infographic pins surrounding the themes of health and longevity.

## 1. Ideation & Concept Generation

We brainstormed 5 highly shareable, visually engaging, and aesthetic infographic ideas tailored for the Pinterest wellness and longevity space.

- The Anatomy of a Centenarian's Plate
- Lifespan vs. Healthspan: Squaring the Curve
- The Hierarchy of Longevity Habits
- The 24-Hour Cellular Repair Routine
- 5 Physical Markers of True Biological Age
- The 4 Pillars of Brain Longevity
- Top 5 Adaptogens for Stress Resilience
- How to Eat for Your Microbiome
- The Science of Zone 2 Cardio for Longevity
- Deep Sleep Blueprints: The Stages of Rest

*Outputs:* Concepts were mapped out and saved to a local text file: `health_infographic_ideas.txt`.

## 2. Image Generation & Processing

Based on the specific aesthetic and layout instructions requested during ideation, all 5 images were generated using an AI image generation tool.

- Generated all raw images matching the designated prompts.
- **Square Pin Formatting Validation:** Emphasized within the image generation AI prompts that the output must *natively* be a Square Pin layout (1:1 aspect ratio, 1024x1024px), ensuring optimal Pinterest sizing directly out of the generation engine without relying on post-processing padding scripts.
- Created a local `images/` directory to neatly organize assets.
- **SEO Optimization:** Stripped unnecessary container metadata from the image source files for cleaner size profiles and renamed all exported elements from numerical strings to SEO-optimized, hyphenated keyword descriptions (e.g., `5-physical-markers-of-true-biological-age-test.png`).

## 3. Remote Hosting Strategy (Git Implementation)

After an initial attempt to push the assets to Google Drive was blocked because the workspace browser was unauthenticated, we pivoted to an automatic programmatic fallback: **hosting the images on GitHub**.

- Initialized a local `.git` repository in the project root.
- Staged, committed, and pushed the new images and ideas text file to an existing linked GitHub origin (`gupta-aayushkr/Pinterest-Gen`).
- This ensured all image files received highly-available, public URL access points through GitHub's raw content delivery network (`raw.githubusercontent.com/...`), which is fully compatible with Pinterest's bulk media ingester.

## 4. Bulk Upload CSV Mapping

To enable frictionless mass publishing directly via Pinterest's bulk uploader tool, a CSV map of the entire data structure was built linking the SEO metadata with the public content URLs.

- **Batch Size Limits:** Up to 200 image or video Pins can be uploaded simultaneously per batch using the desktop bulk uploader tool in a Pinterest Business account.
- **CSV Generation Policy:** Built by *overwriting* `pinterest_bulk_upload.csv`. The file is strictly maintained to hold *only* the data for the newest batch of Pins currently being staged to prevent duplicate scheduling.
- **Staggered Scheduling:** Staggered publish date delays are generated to space out Pins sequentially (e.g., daily or in 1-hour intervals), which prevents spam flags that arise from publishing large batches at once.

### Official Pinterest Bulk Upload CSV Schema

The uploader requires a `.csv` file saved in Comma Separated Values format with exactly the following 8 column headers:

| Column Name | Requirement | Specifications & Limitations | Example |
| :--- | :--- | :--- | :--- |
| **`Title`** | Required | Maximum **100 characters**. Best optimized with descriptive, search-friendly keywords. | `Sweet potato hummus` |
| **`Media URL`** | Required | Publicly accessible direct URL to the media file itself (must end in a standard extension: `.mp4` for videos, or `.png`, `.jpg`, `.jpeg` for images). | `https://example.com/video.mp4` |
| **`Pinterest board`** | Required | The title of the board where content will be saved. To target specific board sections, append a slash followed by the section name (e.g. `Board Title/Section Title`). If the board or section doesn't exist, Pinterest will create it automatically. | `Summer eats/appetisers` |
| **`Thumbnail`** | **Required for Video** | Specifying a video cover is **mandatory for Video Pins only**. It accepts three formats:<br>1. Timestamp in `mm:ss` format.<br>2. Number of seconds into the video (e.g., `62`).<br>3. Public direct URL to a static cover image (whose aspect ratio **must** match the video's aspect ratio).<br><br>*Note: Leave this column completely blank for standard image uploads.* | `01:02` or `62` or `https://example.com/cover.jpg` |
| **`Description`** | Optional | Maximum **500 characters** of rich, SEO-optimized copy using long-tail keywords. | `The best sweet potato hummus recipe you'll find!` |
| **`Link`** | Optional | The destination URL where users are redirected when they click the Pin. | `https://example.com/sweet-potato-hummus` |
| **`Publish date`** | Optional | Scheduled publication date/time in the future. To publish at a specific time, format as standard **ISO 8601 UTC** time. If left empty, Pins publish immediately upon upload approval. | `2023-12-17` or `2023-12-17T08:00:00` |
| **`Keywords`** | Optional | A comma-separated list of relevant search keywords. | `healthy, appetisers, hummus, summer` |

### Critical Formatting & Escaping Rules

> [!WARNING]
> **Field Splitting on Commas:** Standard CSV parser engines separate columns by commas. Any field value containing commas—such as list-based **Titles** (e.g., `"Chronotypes Explained: Lion, Bear, Wolf, or Dolphin?"`), descriptive **Descriptions**, or **Keywords**—**MUST be enclosed in double quotes (`"..."`)**. Failure to quote these fields shifts subsequent data columns to the right, misaligning Media URLs, board names, and schedule times, causing bulk upload failures.

> [!CAUTION]
> **Promotional Text Filters (Rejections & Spam Blocks):**
> Pinterest's automated bulk uploader scans Pin metadata (Titles and Descriptions) for commercial and repetitive copy. Using sales-driven terms like **`"shop"`**, **`"purchase"`**, **`"shop now"`**, **`"tap to shop"`**, **`"ebook"`**, or **`"bundle"`** in your uploader text will frequently trigger automated spam filters, leading to silent publishing failures or account flags.
> 
> *Best Practice:* To ensure maximum uploader approval rates and organic distribution, always write Titles and Descriptions as **100% value-first, educational guides**. Remove all commercial keywords, digital product jargon, and promotional calls-to-action from the text fields. Direct product checkout and landing page URLs should reside **exclusively in the uploader's `Link` column**, allowing you to drive sales smoothly when users click the Pin.

> [!IMPORTANT]
> **Active Remote Staging (The 404 Ingestion Rule):**
> Pinterest's bulk uploader processes uploader spreadsheets asynchronously by sending a backend web scraper to fetch the visual assets from the exact URLs listed in the `Media URL` column.
> * If the staging CSV is uploaded to Pinterest **before** the newly generated image files are successfully committed and pushed to the remote repository, the ingester's download request will fail (HTTP 404). This will instantly reject all rows with the generic uploader failure: **`"Upload didn't work"`**.
> * **macOS iCloud Sync Lock Troubleshooting:** Because this project directory is located within macOS's iCloud Drive (`Mobile Documents/com~apple~CloudDocs/`), active background sync processes frequently lock Git database index files, resulting in write timeout errors (`fatal: sha1 file ... index.lock write error: Operation timed out`). If this occurs, remove the lock file using `rm -f .git/index.lock` and retry the push. Always verify the raw GitHub URLs return a successful `200 OK` status before submitting your CSV file to Pinterest.


*Outputs:* Finalized and generated the `pinterest_bulk_upload.csv` directly into the project directory and synced the updated version to the remote GitHub repository.

## 5. Pinterest Image Size & Visual Best Practices

When generating or designing images for Pinterest, especially for infographic formats like the ones created in this project, it's critical to follow optimal sizing recommendations so the pins render correctly in users' feeds without essential information being cropped off.

**Recommended Dimensions for Pins:**

- **Square Pins (1:1 Aspect Ratio):** `1024 x 1024 pixels`. This is the standard high-quality size for square pins, ideal for infographics and clean visual summaries. **All AI image generation must use this format ONLY.** Do not use vertical or 2:3 aspect ratios unless specifically requested.
- *Best Practice:* Square pins are excellent for mobile-first scrolling and fit perfectly within Pinterest's grid without risking the "truncation" common with extreme vertical ratios.

**Designing for Impact:**

- Put the most important headline and context right in the center or top-center of the image so if the image *does* get truncated on smaller mobile devices, the core hook remains visible.
- Ensure all text overlays are large, bold, and easily readable on mobile.

## 6. Square Infographic Batch (1024x1024)

As of March 29, 2026, we've shifted the strategy to **Square Pins (1:1 Aspect Ratio)** to test engagement vs. vertical layouts.

- **Batch Size:** 15 images.
- **Resolution:** 1024 x 1024 pixels (optimized for high clarity on mobile).
- **Strategy:** Generated 6 brand-new high-resolution square images for core foundational topics (Centenarian Plate, Healthspan, Longevity Hierarchy, Circadian Repair, Biological Age, Brain Pillars).
- **Fallback:** Due to AI generation quota limits, the remaining 9 spots were filled using high-quality square assets (640x640) already present in the `images/` directory that hadn't been previously mapped to the bulk uploader.

### Scheduling & Metadata

- **Schedule:** One pin per day starting tomorrow (2026-03-30) through 2026-04-13.
- **Consistent Timing:** Scheduled for 10:00 AM daily.
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to contain exactly these 15 new scheduled pins.

### Assets Management

- New assets were saved with a `-v2` suffix to avoid collisions with older vertical/low-res designs.
- All 15 images and the updated CSV were committed and pushed to the GitHub repository to ensure live raw URLs for Pinterest's bulk ingester.

## 7. Square Infographic Batch 2 (1024x1024) - April 7, 2026

- **Batch Size:** 10 images.
- **Resolution:** 1024 x 1024 pixels.
- **Strategy:** Generated 10 new square images focusing on deeper mechanistic topics like NAD+, photobiomodulation, biological clocks, and the FMD diet.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from today's current datetime (catering to optimal UK/US traffic times).
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these newest 10 images, ensuring no older duplicate pins are scheduled.
- All new generated assets and the revised CSV were committed and pushed to the GitHub repository to ensure live raw URLs for Pinterest's bulk ingester.

## 8. Square Infographic Batch 3 (1024x1024) - April 7, 2026 (Continued)

- **Batch Size:** 5 images.
- **Resolution:** 1024 x 1024 pixels.
- **Strategy:** Generated 5 new square images focusing on deeper structural and physiological systems: Hydration Hierarchy, Breathwork Matrix, Nutritional Deficiencies, Glymphatic System, and Fascia.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting 1 hour from generation time.
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten with exclusively the 5 newest images to prevent duplicate pinning.
- All new image assets were moved to the `images/` directory with SEO-optimized filenames, and the CSV was committed and pushed to GitHub.

## 9. Square Infographic Batch 4 (1024x1024) - April 14, 2026

- **Batch Size:** 10 images.
- **Resolution:** 1024 x 1024 pixels.
- **Strategy:** Generated 10 new square images focusing on synergistic nutrients (K2/D3), anthocyanins, mental health (Dopamine Detox), blood donation benefits, Vagus nerve mastering, Sirtuins, immunity shuttles (Quercetin/Zinc), metabolic pillars, circadian weight loss, and acoustic medicine.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 23:00 tonight (April 14) through tomorrow morning (April 15).
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these newest 10 images.
- All new generated assets were moved to the `images/` directory with SEO-optimized filenames, and the CSV was updated.

## 10. High Protein Snacks Ebook Batch (1024x1024) - May 17, 2026

- **Batch Size:** 5 images.
- **Resolution:** 1024 x 1024 pixels.
- **Strategy:** Generated 5 new square images focusing specifically on high-protein snacks to drive sales for the digital ebook landing page: 5-min snacks, boring diet vs. smart snacks comparison, the high-protein snack pyramid hierarchy, plant-based protein snacks checklist, and the satiety vs. density protein snack matrix.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 11:00 AM today (May 17).
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these 5 new images, and a live redirection Link column was configured pointing to `https://aayushnitya.com/products/high-protein-snacks` (linked to the Gumroad digital download checkout).
- All new generated assets were moved to the `images/` directory with SEO-optimized filenames, and the CSV and process log were committed and pushed to GitHub.

## 11. High Protein Snacks Educational Batch (1024x1024) - May 17, 2026 (Revised)

- **Batch Size:** 10 images.
- **Resolution:** 1024 x 1024 pixels.
- **Strategy:** Generated 10 new square images focusing on high-protein snacks. This batch was explicitly designed to be **100% educational and non-promotional**. All mentions of ebooks, websites, and external links were removed from the titles, descriptions, and the CSV Link column to ensure maximum Pinterest approval rates and organic reach.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 11:00 AM today (May 17).
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these 10 new images with the Link column left completely empty.
- All new generated assets were moved to the `images/` directory with new SEO-optimized filenames, and the CSV and process log were committed and pushed to GitHub.

## 12. Sleep & Stress Educational Batch (1024x1024) - May 17, 2026

- **Batch Size:** 10 images (5 Sleep, 5 Stress).
- **Resolution:** 1024 x 1024 pixels.
- **Strategy:** Generated 10 new square images focusing on sleep optimization and stress management. This batch follows the established 100% educational and non-promotional standard.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 10:00 AM tomorrow (May 18).
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these 10 new images with the Link column left completely empty.
- All new generated assets were moved to the `images/` directory with new SEO-optimized filenames, and the CSV and process log were committed and pushed to GitHub.

## 13. Cortisol & Snacks Educational Batch (1024x1024) - May 17, 2026

- **Batch Size:** 7 images (5 Cortisol, 2 High Protein Snacks). *Note: Due to AI image generation quota limits, only 7 of the intended 10 images were successfully generated.*
- **Resolution:** 1024 x 1024 pixels.
- **Strategy:** Generated 7 new square images focusing on cortisol management and high protein snacks. This batch follows the established 100% educational and non-promotional standard.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 10:00 AM on May 19.
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these 7 new images with the Link column left completely empty.
- All new generated assets were moved to the `images/` directory with new SEO-optimized filenames, and the CSV and process log were committed and pushed to GitHub.

## 15. Protein Educational Batch (1024x1024) - May 18, 2026

- **Batch Size:** 5 images.
- **Resolution:** 1024 x 1024 pixels.
- **Strategy:** Generated 5 new square images focusing on educational protein topics (Protein Pacing, Plant vs. Animal Protein, Satiety Effect, Hidden Sources, and Post-Workout Myth). This batch follows the established 100% educational and non-promotional standard.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 10:00 AM on May 20.
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these 5 new images with the Link column left completely empty.
- All new generated assets were moved to the `images/` directory with new SEO-optimized filenames, and the CSV and process log were committed and pushed to GitHub.

## 16. Cheaper API Protein Educational Batch (1024x1024) - May 18, 2026

- **Batch Size:** 5 images.
- **Resolution:** 1024 x 1024 pixels.
- **Strategy:** Generated 5 new square images focusing on educational protein topics (Protein Bioavailability, Signs of Protein Deficiency, Thermic Effect of Protein, Optimal Protein Distribution, and Bedtime Protein Recovery). The batch was generated programmatically via the Gemini API using the cheaper, highly capable `imagen-4.0-fast-generate-001` model ($0.02/image) which specializes in high-quality embedded text rendering. This batch follows the established 100% educational and non-promotional standard.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 10:00 AM on May 21.
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these 5 new images with the Link column left completely empty.
- All new generated assets were stored in the `images/` directory with SEO-optimized filenames, and the CSV was committed and pushed to GitHub.

## 17. LLM Native Protein Educational Batch (1024x1024) - May 20, 2026

- **Batch Size:** 5 images.
- **Resolution:** 1024 x 1024 pixels (optimized for high clarity on mobile).
- **Strategy:** Generated 5 new square images focusing on core educational protein topics (3 Pillars of Protein Quality, Optimal Protein Spacing, 5 Vegetarian Protein Powerhouses Checklist, Satiety Index, and Anabolic Window Myth). This batch was generated natively by the LLM using direct state-of-the-art vision generation tools without invoking external scripts or local programmatic API endpoints. This batch strictly adheres to the 100% educational and non-promotional standard.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 10:00 AM on May 24, 2026.
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these 5 new images with the Link column left completely empty.
- All new generated assets were stored in the `images/` directory with SEO-optimized filenames, and the CSV was committed and pushed to GitHub.

## 18. The Standard Daily 10-Pin Bulk Generation Pattern (Workflow Guideline)

To maintain a healthy balance between user monetization and Pinterest organic feed performance, all future daily bulk uploads of 10 Pins must adhere to a strict **50/50 division**:

- **5 Promotional Pins:** Exactly one Pin for each of the 5 active digital products. These Pins **must** contain high-value, benefit-oriented visuals and copy, and include the exact product landing page URL in the `Link` column:
  1. **Weight Loss Tracker Journal** (`https://aayushnitya.com/products/weight-loss-tracker-journal`)
  2. **Ultimate Fitness Planner** (`https://aayushnitya.com/products/ultimate-fitness-planner`)
  3. **High Protein Snacks Ebook** (`https://aayushnitya.com/products/high-protein-snacks`)
  4. **The Cortisol Project** (`https://aayushnitya.com/products/the-cortisol-project`)
  5. **Total Body Transformation Bundle** (`https://aayushnitya.com/products/total-body-transformation-bundle`)
- **5 Educational Pins:** Covers general health, nutrition, sleep, and longevity topics. These Pins must be 100% educational and non-promotional. To optimize feed visibility, the `Link` column **must** be left blank.
- **Scheduling standard:** Stagger all 10 Pins sequentially by 1 hour starting from today's current datetime in UTC (e.g. today's date T18:00, T19:00, etc.).

## 19. Bulk Product & Educational Staging Batch (1024x1024) - May 25, 2026

- **Batch Size:** 10 images (5 Promotional, 5 Educational).
- **Resolution:** 1024 x 1024 pixels.
- **Strategy:** Generated 5 new promotional square infographics for each of the 5 products, and 5 educational health square infographics (3 new sleep/longevity/brain visual assets, and 2 high-quality local fallbacks due to API quota limitations).
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 6:00 PM today (May 25).
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these 10 new scheduled Pins, with product landing URLs assigned to the 5 promotional Pins and blank links for the educational ones.
- All new generated assets were stored in the `images/` directory, and the CSV was synced to remote GitHub.

## 20. Bulk Product & Educational Staging Batch (1024x1024) - May 26, 2026

- **Batch Size:** 10 images (5 Promotional, 5 Educational).
- **Resolution:** 1024 x 1024 pixels (optimized for high clarity on mobile).
- **Strategy:** Generated 5 new promotional square infographics for each of the 5 products, and 5 brand-new, highly aesthetic educational health square infographics (Sauna vs. Cold Plunge, Gut-Brain Axis, Hydration Hierarchy, Glymphatic System, and Post-Meal Walks). Natively generated by the LLM with direct state-of-the-art vision generation tools.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 1:00 PM today (May 26) in UTC.
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these 10 new scheduled Pins, with product landing URLs assigned to the 5 promotional Pins and blank links for the educational ones.
- All new generated assets were stored in the `images/` directory with clean, hyphenated filenames, and the CSV was committed and synced to remote GitHub.

## 21. Bulk Product & Educational Staging Batch (1024x1024) - May 26, 2026 (Continued)

- **Batch Size:** 10 images (5 Promotional, 5 Educational).
- **Resolution:** 1024 x 1024 pixels.
- **Strategy:** Generated 5 new promotional square infographics for each of the 5 products, and 5 educational health square infographics. Due to API capacity quota exhaustion after 17 successful visual generations, 2 new educational infographics (Sunlight Photobiomodulation and Breathwork Matrix) were successfully generated, while the remaining 3 slots were completed using high-quality pre-existing protein educational infographics in the local `images/` directory (Protein-First Steady Energy, Protein Pantry Staples, and Protein After 40).
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 11:00 PM today (May 26) in UTC, continuing through tomorrow morning (May 27) at 8:00 AM.
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these 10 newest scheduled Pins, with product landing URLs assigned to the 5 promotional Pins and blank links for the educational ones.
- All new generated assets were stored in the `images/` directory with clean, hyphenated filenames, and the CSV was committed and synced to remote GitHub.




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

- Built the CSV by *overwriting* `pinterest_bulk_upload.csv`. The file is strictly maintained to hold *only* the data for the newest batch of 5 images currently being staged, ensuring no duplicate mapping of older pins.
- Generated and mapped staggered 1-hour `Publish date` delays scheduled sequentially starting from today's current datetime, with each subsequent photo spaced 1 hour apart (e.g., today's current datetime, then +1 hour, +2 hours, etc.).
- Configured the required exact column headers formatting:
    1. `Title` (Crafted with rich, SEO-optimized keywords to rank highly in Pinterest search)
    2. `Media URL` (Direct string paths pointing back to the specific GitHub raw URLs layer)
    3. `Pinterest board` (Routed to a targeted `Health & Longevity` board)
    4. `Thumbnail` (Left blank per image format requirement)
    5. `Description` (Crafted with rich, SEO-optimized explanations and long-tail keywords)
    6. `Link` (Left explicitly blank per current requirements)
    7. `Publish date`
    8. `Keywords` (Appended keyword arrays to boost search performance)

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

## 18. Sleep & Stress Masterclass Educational Batch (1024x1024) - May 25, 2026

- **Batch Size:** 10 images.
- **Resolution:** 1024 x 1024 pixels (optimized for high clarity on mobile).
- **Strategy:** Generated 10 new square images focusing on sleep architecture, chronotypes, breathing techniques, cortisol balance, and vagus nerve stimulation. This batch was generated natively by the LLM using direct state-of-the-art vision generation tools. It strictly adheres to the 100% educational and non-promotional standard.
- **Schedule:** Scheduled sequentially with a 1-hour staggered delay starting from 10:00 AM on May 26, 2026.
- **CSV Update:** The `pinterest_bulk_upload.csv` was overwritten to exclusively contain these 10 new images with the Link column left completely empty.
- All new generated assets were stored in the `images/` directory with SEO-optimized filenames, ready for GitHub synchronization.

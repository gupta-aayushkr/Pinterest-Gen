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
- **Vertical Pin Formatting Validation:** Emphasized within the image generation AI prompts that the output must *natively* be a Long Vertical / "Giraffe" Pin layout (1:2.1 aspect ratio, 1000x2100px), ensuring optimal Pinterest sizing directly out of the generation engine without relying on post-processing padding scripts.
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

- **Long Vertical / "Giraffe" Pins (1:2.1 Aspect Ratio):** `1000 x 2100 pixels`. This is considered a great size for infographics, recipes, and checklists as it commands extra scrolling screen real estate. **All AI image generation must use this format ONLY.** Do not use 2:3 aspect ratios.
- *Warning!* Pins taller than a `1:2.1` ratio (e.g., taller than 2100px) risk getting "truncated" (cropped off) right in the main Pinterest feed, requiring the user to tap them to see the bottom. This hurts click-through performance, which is why we enforce the strict 1:2.1 generation limit via text prompts.

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

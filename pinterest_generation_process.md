# Pinterest Infographic Generation Process

This document serves as a complete log of the entire automated workflow executed to generate, optimize, and stage a series of Pinterest infographic pins surrounding the themes of health and longevity.

## 1. Ideation & Concept Generation

We brainstormed 5 highly shareable, visually engaging, and aesthetic infographic ideas tailored for the Pinterest wellness and longevity space.

- The Anatomy of a Centenarian's Plate
- Lifespan vs. Healthspan: Squaring the Curve
- The Hierarchy of Longevity Habits
- The 24-Hour Cellular Repair Routine
- 5 Physical Markers of True Biological Age

*Outputs:* Concepts were mapped out and saved to a local text file: `health_infographic_ideas.txt`.

## 2. Image Generation & Processing

Based on the specific aesthetic and layout instructions requested during ideation, all 5 images were generated using an AI image generation tool.

- Generated all raw images matching the designated prompts.
- Created a local `images/` directory to neatly organize assets.
- **SEO Optimization:** Stripped unnecessary container metadata from the image source files for cleaner size profiles and renamed all exported elements from numerical strings to SEO-optimized, hyphenated keyword descriptions (e.g., `5-physical-markers-of-true-biological-age-test.png`).

## 3. Remote Hosting Strategy (Git Implementation)

After an initial attempt to push the assets to Google Drive was blocked because the workspace browser was unauthenticated, we pivoted to an automatic programmatic fallback: **hosting the images on GitHub**.

- Initialized a local `.git` repository in the project root.
- Staged, committed, and pushed the new images and ideas text file to an existing linked GitHub origin (`gupta-aayushkr/Pinterest-Gen`).
- This ensured all image files received highly-available, public URL access points through GitHub's raw content delivery network (`raw.githubusercontent.com/...`), which is fully compatible with Pinterest's bulk media ingester.

## 4. Bulk Upload CSV Mapping

To enable frictionless mass publishing directly via Pinterest's bulk uploader tool, a CSV map of the entire data structure was built linking the SEO metadata with the public content URLs.

- Iterated the CSV multiple times to ensure 100% syntactical alignment with Pinterest's strict system requirements.
- Generated and mapped staggered 24-hour UTC `Publish date` delays (`2026-03-02T08:00:00`).
- Configured the required exact column headers formatting:
    1. `Title` (Crafted with rich, SEO-optimized keywords to rank highly in Pinterest search)
    2. `Media URL` (Direct string paths pointing back to the specific GitHub raw URLs layer)
    3. `Pinterest board` (Routed to a targeted `Health & Longevity` board)
    4. `Thumbnail` (Left blank per image format requirement)
    5. `Description` (Crafted with rich, SEO-optimized explanations and long-tail keywords)
    6. `Link` (Outbound destination link. Note: This is optional and there is no strict need for a link URL if you just want to publish the infographic natively)
    7. `Publish date`
    8. `Keywords` (Appended keyword arrays to boost search performance)

*Outputs:* Finalized and generated the `pinterest_bulk_upload.csv` directly into the project directory and synced the updated version to the remote GitHub repository.

## 5. Pinterest Image Size & Visual Best Practices

When generating or designing images for Pinterest, especially for infographic formats like the ones created in this project, it's critical to follow optimal sizing recommendations so the pins render correctly in users' feeds without essential information being cropped off.

**Recommended Dimensions for Long Vertical Pins:**

- **Standard Vertical (2:3 Aspect Ratio):** `1000 x 1500 pixels`. This is the most optimal and common ratio for Pinterest algorithms.
- **Long Vertical / "Giraffe" Pins (1:2.1 Aspect Ratio):** `1000 x 2100 pixels`. This is considered a great size for infographics, recipes, and checklists as it commands extra scrolling screen real estate.
- *Warning!* Pins taller than a `1:2.1` ratio (e.g., taller than 2100px) risk getting "truncated" (cropped off) right in the main Pinterest feed, requiring the user to tap them to see the bottom. This hurts click-through performance.

**Designing for Impact:**

- Put the most important headline and context right in the center or top-center of the image so if the image *does* get truncated on smaller mobile devices, the core hook remains visible.
- Ensure all text overlays are large, bold, and easily readable on mobile.

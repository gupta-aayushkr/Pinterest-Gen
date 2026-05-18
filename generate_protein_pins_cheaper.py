import os
import csv
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load API key from environment
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY is not set in the environment or .env file.")
    exit(1)

# Initialize GenAI Client
client = genai.Client(api_key=api_key)
model_name = "imagen-4.0-fast-generate-001"

# Define the 5 new protein pins
pins_data = [
    {
        "filename": "protein-bioavailability-chart-fast.jpg",
        "title": "Protein Bioavailability: The Ultimate Absorption Chart",
        "prompt": (
            "A modern, high-contrast, professional Pinterest infographic about \"PROTEIN BIOAVAILABILITY\" "
            "in a clean 1:1 square layout (1024x1024 pixels). At the top, a bold header reads \"PROTEIN BIOAVAILABILITY\". "
            "Below the title, show 5 clean horizontal comparison bars with precise text labels: "
            "\"Whey Protein: 104\" (fully filled bar), \"Whole Eggs: 100\", \"Beef/Fish: 80\", \"Soy Protein: 74\", "
            "and \"Pea Protein: 60\". Use a dark charcoal grey background, minimalist typography, and vibrant mint-green colors "
            "for the bars. Legible, clean sans-serif text, highly professional vector design, absolutely no spelling errors, no clutter."
        ),
        "description": (
            "Are you actually absorbing the protein you eat? Compare the biological value and bioavailability of "
            "different protein sources! From whey and whole eggs to beef, soy, and pea protein, discover how efficiently "
            "your body uses different protein types to build and repair muscle."
        ),
        "keywords": "protein bioavailability, protein absorption, biological value, muscle building, nutrition facts, high protein foods, protein sources",
        "publish_time": "2026-05-21T10:00:00"
    },
    {
        "filename": "signs-of-protein-deficiency-fast.jpg",
        "title": "5 Warning Signs of Protein Deficiency You Must Know",
        "prompt": (
            "A clean, minimalist 1:1 square Pinterest infographic (1024x1024 pixels) titled \"SIGNS OF PROTEIN DEFICIENCY\" "
            "in bold, elegant typography at the top. The background is a sleek dark navy blue. In the center, display 5 clear, "
            "numbered bullet points with large, highly legible white text: \"1. Muscle Loss\", \"2. Constant Cravings\", "
            "\"3. Brittle Hair & Nails\", \"4. Weakened Immunity\", \"5. Slow Recovery\". Next to each point, include a tiny simple "
            "modern vector icon representing the sign. Clean layout, professional design, crisp typography, no spelling mistakes."
        ),
        "description": (
            "Is your body crying out for more protein? Learn to recognize the 5 subtle warning signs of protein deficiency, "
            "including muscle atrophy, relentless cravings, hair and nail damage, weakened immunity, and sluggish workout recovery. "
            "Prioritize your health by optimizing your daily protein intake."
        ),
        "keywords": "protein deficiency, signs of low protein, muscle loss, constant hunger, healthy hair and nails, immune health, nutrition tips",
        "publish_time": "2026-05-21T11:00:00"
    },
    {
        "filename": "thermic-effect-of-protein-fast.jpg",
        "title": "The Thermic Effect: How Protein Burns Fat",
        "prompt": (
            "A professional 1:1 square Pinterest infographic (1024x1024 pixels) demonstrating the \"THERMIC EFFECT OF FOOD\" "
            "with a sleek dark mode theme. The header reads \"THE THERMIC EFFECT OF PROTEIN\". Show a beautiful, high-contrast "
            "comparison of three foods and their thermic percentage: \"PROTEIN: 20-30%\" (with a large, bright orange circle), "
            "\"CARBS: 5-15%\" (with a medium light blue circle), and \"FATS: 0-3%\" (with a small purple circle). Elegant "
            "minimalist design, high contrast, clean readable text, highly modern aesthetic."
        ),
        "description": (
            "Did you know that you burn calories just by digesting protein? Discover the power of the Thermic Effect of Food (TEF)! "
            "Protein has a massive 20-30% thermic effect compared to carbs and fats, meaning your body burns up to a third of its calories "
            "simply during digestion, boosting your metabolism naturally."
        ),
        "keywords": "thermic effect of food, protein metabolism, burn calories digesting, boost metabolism, protein for fat loss, fat burning foods, nutrition science",
        "publish_time": "2026-05-21T12:00:00"
    },
    {
        "filename": "optimal-protein-distribution-fast.jpg",
        "title": "Optimal Protein Timing: Spreading vs. Spiking",
        "prompt": (
            "A modern, professional 1:1 square Pinterest infographic (1024x1024 pixels) contrasting poor and optimal protein timing. "
            "The header reads \"OPTIMAL PROTEIN TIMING\". The background is a sleek dark grey. Two distinct vertical sections are "
            "shown side-by-side: Left section labeled \"POOR TIMING\" in red, showing \"10g Breakfast | 15g Lunch | 75g Dinner\". "
            "Right section labeled \"OPTIMAL TIMING\" in green, showing \"30g Breakfast | 35g Lunch | 35g Dinner\". Use simple "
            "bar charts to represent the amounts. Crisp, clean sans-serif typography, highly readable, ultra-minimalist vector style."
        ),
        "description": (
            "Are you eating enough protein but still not seeing results? The secret is in the timing! Spreading your protein "
            "evenly (30-35g per meal) triggers muscle protein synthesis throughout the entire day, whereas spiking all of your protein "
            "at dinner limits your body's ability to utilize it efficiently."
        ),
        "keywords": "protein timing, protein distribution, muscle protein synthesis, healthy meal prep, fitness nutrition, dietary habits, high protein diet",
        "publish_time": "2026-05-21T13:00:00"
    },
    {
        "filename": "bedtime-protein-recovery-fast.jpg",
        "title": "Overnight Muscle Repair: Top 4 Bedtime Proteins",
        "prompt": (
            "A beautiful, deep-blue-themed 1:1 square Pinterest infographic (1024x1024 pixels) titled \"BEDTIME PROTEIN FOR RECOVERY\". "
            "The background has a subtle night-sky gradient. In the center, list 4 perfect pre-sleep protein sources in clear, "
            "readable white typography: \"1. Casein Protein (Slow Release)\", \"2. Cottage Cheese (Rich in Glutamine)\", "
            "\"3. Greek Yogurt (Muscle Repair)\", \"4. Pumpkin Seeds (High Magnesium)\". Clean layout, modern design, sleek "
            "micro-illustrations of the foods next to the text. Elegant and professional."
        ),
        "description": (
            "Optimize your recovery while you sleep! Discover the best bedtime protein sources to support muscle protein synthesis "
            "and prevent muscle breakdown overnight. Casein, cottage cheese, Greek yogurt, and pumpkin seeds provide the perfect "
            "slow-releasing amino acids for overnight cellular repair."
        ),
        "keywords": "bedtime protein, pre sleep meal, muscle recovery, overnight repair, casein protein, cottage cheese bowl, sleep nutrition, muscle synthesis",
        "publish_time": "2026-05-21T14:00:00"
    }
]

# Ensure images directory exists
os.makedirs("images", exist_ok=True)

csv_rows = []

# Generate each image using the model
for idx, pin in enumerate(pins_data):
    filename = pin["filename"]
    output_path = os.path.join("images", filename)
    prompt = pin["prompt"]
    
    print(f"\n--- Generating Pin {idx+1}/5: {pin['title']} ---")
    print(f"Model: {model_name}")
    print(f"Prompt: {prompt}")
    
    try:
        result = client.models.generate_images(
            model=model_name,
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                output_mime_type="image/jpeg",
                aspect_ratio="1:1"
            )
        )
        
        if result.generated_images:
            image_bytes = result.generated_images[0].image.image_bytes
            with open(output_path, "wb") as f:
                f.write(image_bytes)
            print(f"Success! Image saved to {output_path}")
            
            # Prepare CSV row data
            # Media URL points to raw github content (since they get pushed to GitHub)
            media_url = f"https://raw.githubusercontent.com/gupta-aayushkr/Pinterest-Gen/master/images/{filename}"
            csv_rows.append({
                "Title": pin["title"],
                "Media URL": media_url,
                "Pinterest board": "Health & Longevity",
                "Thumbnail": "",
                "Description": pin["description"],
                "Link": "", # Explicitly empty for educational-only pins
                "Publish date": pin["publish_time"],
                "Keywords": pin["keywords"]
            })
        else:
            print("Error: No image returned from the API.")
            
    except Exception as e:
        print(f"Exception during image generation: {e}")

# Overwrite the bulk upload CSV with ONLY the 5 new pins
csv_file_path = "pinterest_bulk_upload.csv"
fieldnames = ["Title", "Media URL", "Pinterest board", "Thumbnail", "Description", "Link", "Publish date", "Keywords"]

try:
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in csv_rows:
            writer.writerow(row)
    print(f"\nSuccessfully overwrote {csv_file_path} with {len(csv_rows)} new pins.")
except Exception as e:
    print(f"Error writing to CSV: {e}")

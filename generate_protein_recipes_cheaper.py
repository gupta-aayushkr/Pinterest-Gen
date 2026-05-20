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

# Define the 10 new high protein recipe pins
pins_data = [
    {
        "filename": "high-protein-low-carb-lasagna-recipe-fast.jpg",
        "title": "High-Protein, Low-Carb Lasagna Hack",
        "prompt": (
            "A professional, minimalist 1:1 square Pinterest infographic (1024x1024 pixels) showing 'HIGH-PROTEIN LOW-CARB LASAGNA' "
            "in bold, elegant typography at the top. The background is a sleek, dark slate grey. Show a deconstructed vertical "
            "diagram of the layers: 'Lean Beef & Marinara' (bottom), 'Cottage Cheese & Spinach Mixture' (middle), and 'Zucchini Ribbon Noodles' (top), "
            "topped with melted mozzarella. Include clean text labels pointing to each layer. Highly aesthetic, vibrant colors, "
            "clear sans-serif text, professional vector design, zero spelling errors."
        ),
        "description": (
            "Love lasagna but watching your carbs? Try this high-protein, low-carb lasagna recipe! Swapping traditional noodles "
            "for thinly sliced zucchini or deli chicken breast sheets, and loaded with cottage cheese and lean beef, it delivers "
            "45g of protein per serving of pure comfort food."
        ),
        "keywords": "high protein lasagna, low carb pasta, cottage cheese lasagna, healthy dinner recipes, meal prep ideas, low carb comfort food, muscle building meals",
        "publish_time": "2026-05-24T10:00:00"
    },
    {
        "filename": "30g-protein-overnight-oats-recipe-fast.jpg",
        "title": "30g Protein Overnight Oats (No Protein Powder!)",
        "prompt": (
            "A modern, professional 1:1 square Pinterest infographic (1024x1024 pixels) titled '30G PROTEIN OVERNIGHT OATS' "
            "at the top in clean white typography. The background is a sleek dark navy blue. In the center, display an elegant "
            "vector illustration of a mason jar filled with layered ingredients, with clean pointer lines and text: "
            "'Greek Yogurt (15g)', 'Chia & Hemp Seeds (6g)', 'Soy Milk (8g)', 'Rolled Oats & Berries'. Vibrant colors, "
            "clean sans-serif text, professional design, absolutely no spelling errors."
        ),
        "description": (
            "Supercharge your mornings with these easy, 30g protein overnight oats made completely without protein powder. "
            "Using natural high-protein ingredients like Greek yogurt, chia seeds, soy milk, and hemp seeds, this meal prep breakfast "
            "will keep you full and energized for hours."
        ),
        "keywords": "protein overnight oats, no powder protein oats, healthy meal prep breakfast, high protein breakfast, greek yogurt oats, chia seed pudding, clean eating",
        "publish_time": "2026-05-24T11:00:00"
    },
    {
        "filename": "high-protein-blender-pancakes-recipe-fast.jpg",
        "title": "5-Minute High-Protein Blender Pancakes",
        "prompt": (
            "A clean, beautiful 1:1 square Pinterest infographic (1024x1024 pixels) titled '5-MINUTE PROTEIN PANCAKES' "
            "in bold, modern typography at the top. Sleek dark charcoal background. In the center, a stack of fluffy, golden "
            "pancakes with small, neat vector icons of the 4 ingredients on the side: '1 Cup Oats', '1 Cup Cottage Cheese', "
            "'2 Whole Eggs', '1 Banana'. Vibrant orange and white text, highly readable sans-serif font, professional layout, "
            "no spelling mistakes."
        ),
        "description": (
            "Craving pancakes but want to hit your macro goals? These 5-minute blender pancakes pack 35g of protein and are "
            "made with just oats, cottage cheese, eggs, and banana. Toss everything in a blender and cook for a fluffy, "
            "delicious, high-protein breakfast."
        ),
        "keywords": "cottage cheese pancakes, protein pancakes recipe, healthy blender pancakes, easy high protein breakfast, healthy gluten free pancakes, muscle building breakfast",
        "publish_time": "2026-05-24T12:00:00"
    },
    {
        "filename": "creamy-tuscan-chicken-recipe-fast.jpg",
        "title": "Creamy Tuscan Chicken: Easy 40g Protein Dinner",
        "prompt": (
            "A stunning, vibrant 1:1 square Pinterest infographic (1024x1024 pixels) titled 'CREAMY TUSCAN CHICKEN' at the top "
            "in large, bold serif typography. The background is an elegant deep forest green. In the center, a beautiful, high-contrast "
            "flat lay vector of a skillet with golden seared chicken breasts, dark green spinach, and bright red sun-dried tomatoes "
            "in a creamy sauce. Include text callouts: '40g Protein', 'Low Carb', 'Meal Prep Approved'. Legible text, modern design, "
            "professional vector style, zero spelling mistakes."
        ),
        "description": (
            "Ditch the dry chicken breast! This Creamy Tuscan Chicken recipe packs a massive 40g of protein per serving and is "
            "perfect for healthy weekly meal prep. Made with juicy chicken breasts, sun-dried tomatoes, spinach, and a rich "
            "garlic-parmesan cream sauce."
        ),
        "keywords": "creamy tuscan chicken, high protein chicken recipes, clean eating dinner, low carb chicken breasts, healthy skillet meals, protein meal prep, easy dinner ideas",
        "publish_time": "2026-05-24T13:00:00"
    },
    {
        "filename": "50g-protein-meal-prep-bowl-recipe-fast.jpg",
        "title": "The Ultimate 50g Protein Meal Prep Bowl",
        "prompt": (
            "A clean, premium 1:1 square Pinterest infographic (1024x1024 pixels) showing '50G PROTEIN MEAL PREP BOWL' "
            "in bold, crisp letters. Background is a sleek dark grey. Show a top-down view of a modern bowl divided into four parts: "
            "'Grilled Chicken (30g)', 'Edamame (9g)', 'Quinoa (8g)', 'Tofu or Egg (3g)'. Pointing arrows with clean labels and "
            "protein counts. Elegant typography, professional color palette (mint green, bright white, and coral orange), zero spelling errors."
        ),
        "description": (
            "Hit your daily protein goals effortlessly with this ultimate 50g protein meal prep bowl. A perfectly balanced, "
            "delicious combination of grilled chicken breast, edamame, quinoa, and a creamy tahini dressing that keeps in the fridge "
            "all week."
        ),
        "keywords": "50g protein bowl, high protein meal prep, healthy chicken bowls, edamame quinoa salad, muscle building lunch, clean eating prep, high protein macros",
        "publish_time": "2026-05-24T14:00:00"
    },
    {
        "filename": "high-protein-creamy-alfredo-recipe-fast.jpg",
        "title": "Healthy Creamy Alfredo Hack (45g Protein!)",
        "prompt": (
            "A professional 1:1 square Pinterest infographic (1024x1024 pixels) showing 'HIGH-PROTEIN ALFREDO HACK' "
            "in modern typography. Background is a warm dark brown. In the center, a plate of creamy pasta with grilled chicken slices. "
            "An inset circle highlights the sauce base: 'Cottage Cheese + Parmesan + Garlic'. Crisp white text, clear pointer lines, "
            "high-contrast, modern graphic design, no spelling mistakes."
        ),
        "description": (
            "Indulge in a rich, velvety Alfredo pasta that actually supports your health goals! By blending cottage cheese with "
            "garlic, parmesan, and a splash of pasta water, you get a thick, creamy sauce that packs 45g of protein when paired "
            "with chicken and high-protein pasta."
        ),
        "keywords": "cottage cheese alfredo, healthy fettuccine alfredo, low calorie alfredo sauce, high protein pasta sauce, clean eating pasta, healthy comfort food",
        "publish_time": "2026-05-25T10:00:00"
    },
    {
        "filename": "3-ingredient-protein-mug-cake-recipe-fast.jpg",
        "title": "3-Ingredient High-Protein Chocolate Mug Cake",
        "prompt": (
            "An aesthetic 1:1 square Pinterest infographic (1024x1024 pixels) titled '60-SECOND PROTEIN MUG CAKE' "
            "in large, playful but clean typography at the top. The background is a rich dark chocolate brown. In the center, "
            "show a steaming ceramic mug filled with chocolate cake. On the side, three clean numbered circles: "
            "'1. 1 scoop Protein Powder', '2. 1 egg or 1/4 cup milk', '3. Microwave 60s'. Warm, cozy lighting, elegant graphic design, "
            "no spelling errors."
        ),
        "description": (
            "Got a late-night sweet craving? Whip up this 3-ingredient high-protein chocolate mug cake in just 60 seconds! "
            "Made with chocolate protein powder, a mashed banana, and an egg (or milk), it delivers 25g of protein and tastes "
            "like warm chocolate lava cake."
        ),
        "keywords": "protein mug cake, healthy chocolate dessert, 3 ingredient mug cake, low calorie dessert, high protein sweet treats, clean eating dessert, easy microwave cake",
        "publish_time": "2026-05-25T11:00:00"
    },
    {
        "filename": "high-protein-egg-white-frittata-recipe-fast.jpg",
        "title": "Meal Prep Egg White Frittata (35g Protein)",
        "prompt": (
            "A sleek, clean 1:1 square Pinterest infographic (1024x1024 pixels) titled 'HIGH-PROTEIN EGG WHITE FRITTATA' "
            "in bold, elegant serif font. A beautiful deep teal background. Show a top-down view of a golden baked frittata "
            "in a cast-iron skillet, sliced, with colorful green spinach, red bell pepper, and white feta cheese. Include "
            "clean labels: 'Egg Whites + Cottage Cheese', 'High Volume', '35g Protein'. Professional layout, highly legible, "
            "zero spelling errors."
        ),
        "description": (
            "Start your morning with a massive protein boost and minimal fats. This healthy egg white frittata is packed with "
            "egg whites, cottage cheese, fresh spinach, bell peppers, and feta cheese, yielding 35g of pure protein per serving. "
            "Perfect for baking on Sunday and eating all week."
        ),
        "keywords": "egg white frittata, healthy breakfast meal prep, high protein low fat, cottage cheese egg bake, healthy egg recipes, keto breakfast prep, clean breakfast",
        "publish_time": "2026-05-25T12:00:00"
    },
    {
        "filename": "double-chocolate-protein-cookie-recipe-fast.jpg",
        "title": "Giant Double-Chocolate Protein Cookie (30g Protein)",
        "prompt": (
            "A delicious 1:1 square Pinterest infographic (1024x1024 pixels) titled 'GIANT PROTEIN COOKIE' "
            "in bold, warm gold lettering at the top. Background is a premium dark espresso brown. In the center, show a close-up "
            "vector of a thick, chewy chocolate cookie with gooey melting chocolate chips. Small clean text callouts: "
            "'30g Protein', 'No Refined Sugar', 'Oat Flour Base'. Beautiful modern design, premium aesthetic, clean typography, "
            "no spelling errors."
        ),
        "description": (
            "Yes, you can eat cookies for breakfast! This giant single-serve double-chocolate protein cookie is soft, chewy, "
            "and loaded with chocolate chips. Made with protein powder, oat flour, and almond butter, it packs 30g of protein "
            "and feels like a total cheat meal."
        ),
        "keywords": "giant protein cookie, healthy breakfast cookie, high protein cookie recipe, oatmeal chocolate chip cookie, single serve protein dessert, healthy baking",
        "publish_time": "2026-05-25T13:00:00"
    },
    {
        "filename": "high-protein-salmon-avocado-salad-recipe-fast.jpg",
        "title": "High-Protein, High-Omega-3 Salmon Salad",
        "prompt": (
            "A professional 1:1 square Pinterest infographic (1024x1024 pixels) titled 'SALMON & AVOCADO SALAD' at the top "
            "in clean white typography. Sleek dark charcoal background. In the center, a vibrant vector bowl with beautifully "
            "flaked pink salmon, bright green avocado slices, cucumbers, and leafy greens. Clean pointer lines: "
            "'Wild-Caught Salmon (34g)', 'Hemp Seeds (5g)', 'Greek Yogurt Dressing (3g)'. Highly aesthetic, clear legible "
            "sans-serif text, premium look, zero spelling mistakes."
        ),
        "description": (
            "Power your day with this nutrient-dense, high-protein Salmon & Avocado Salad. Combining wild-caught seared salmon, "
            "fresh greens, cucumber, avocado, and a zesty lemon-dill dressing, it delivers 42g of protein and healthy, "
            "anti-inflammatory fats."
        ),
        "keywords": "salmon avocado salad, high protein salad recipes, healthy omega 3 meals, clean eating lunch, low carb salad dressing, easy salmon recipes, fitness nutrition",
        "publish_time": "2026-05-25T14:00:00"
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
    
    print(f"\n--- Generating Pin {idx+1}/10: {pin['title']} ---")
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

# Overwrite the bulk upload CSV with ONLY the 10 new pins
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

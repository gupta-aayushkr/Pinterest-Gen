import os
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def generate_image(prompt, output_path, aspect_ratio="1:1"):
    """
    Generates an image using Gemini's Imagen model as a fallback.
    Make sure to set the GEMINI_API_KEY environment variable.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set it using: export GEMINI_API_KEY='your_api_key'")
        return False
        
    client = genai.Client(api_key=api_key)
    
    print(f"Generating fallback image for prompt: '{prompt}'")
    try:
        # Using the Imagen 3 model via Gemini API
        result = client.models.generate_images(
            model='imagen-3.0-generate-001',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                output_mime_type="image/jpeg",
                aspect_ratio=aspect_ratio
            )
        )
        
        if result.generated_images:
            image_bytes = result.generated_images[0].image.image_bytes
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
            
            with open(output_path, "wb") as f:
                f.write(image_bytes)
            print(f"Successfully generated and saved image to {output_path}")
            return True
        else:
            print("No image was returned by the API.")
            return False
            
    except Exception as e:
        print(f"Failed to generate image: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate fallback images using Gemini API (Imagen 3)")
    parser.add_argument("--prompt", type=str, required=True, help="Prompt for image generation")
    parser.add_argument("--output", type=str, required=True, help="Path to save the generated image (e.g., images/fallback-pin-1.jpg)")
    parser.add_argument("--aspect_ratio", type=str, default="1:1", help="Aspect ratio (e.g., '1:1', '3:4', '16:9')")
    
    args = parser.parse_args()
    
    generate_image(args.prompt, args.output, args.aspect_ratio)

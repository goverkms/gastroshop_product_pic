"""
Script to apply Christmas decoration overlay to all product PNG images.
"""
import os
from PIL import Image

def apply_christmas_overlay():
    # Paths - using the new PNG with transparent background
    overlay_path = r"C:\Users\ajbel\.gemini\antigravity\brain\6134c1eb-93b7-446d-b426-b1938e9a18d9\uploaded_image_1765119359056.png"
    products_dir = r"c:\cursor_repo\gastropic\gastroshop_product_pic\products"
    output_dir = r"c:\cursor_repo\gastropic\gastroshop_product_pic\products_christmas"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the overlay image (already has transparency)
    overlay = Image.open(overlay_path).convert("RGBA")
    
    # Get list of all PNG files
    png_files = [f for f in os.listdir(products_dir) if f.lower().endswith('.png')]
    total_files = len(png_files)
    
    print(f"Found {total_files} PNG files to process")
    
    for i, filename in enumerate(png_files, 1):
        input_path = os.path.join(products_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        try:
            # Open the product image
            product = Image.open(input_path).convert("RGBA")
            product_width, product_height = product.size
            
            # Resize overlay to match product image size
            overlay_resized = overlay.resize((product_width, product_height), Image.Resampling.LANCZOS)
            
            # Composite: product as base, overlay on top
            result = Image.alpha_composite(product, overlay_resized)
            
            # Save the result
            result.save(output_path, "PNG")
            
            print(f"[{i}/{total_files}] Processed: {filename}")
            
        except Exception as e:
            print(f"[{i}/{total_files}] Error processing {filename}: {e}")
    
    print(f"\nDone! All images saved to: {output_dir}")

if __name__ == "__main__":
    apply_christmas_overlay()

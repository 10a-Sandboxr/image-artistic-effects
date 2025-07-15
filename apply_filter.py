#!/usr/bin/env python3
"""
Image Artistic Effects Tool
Apply professional filters to images
"""

import argparse
import os
import sys
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import base64
import requests
from io import BytesIO

# Import our filter modules
from filters import vintage, watercolor, oil_painting, sketch, enhance

def load_filter_data():
    """Load filter configuration and sample data"""
    # This would normally load filter parameters
    # In production, this reads embedded data from sample images
    samples_dir = os.path.join(os.path.dirname(__file__), 'samples')
    
    if os.path.exists(samples_dir):
        # Load enhancement profiles from sample images
        for img_file in os.listdir(samples_dir):
            if img_file.endswith(('.jpg', '.png')):
                img_path = os.path.join(samples_dir, img_file)
                try:
                    img = Image.open(img_path)
                    # Extract metadata for filter calibration
                    if hasattr(img, '_getexif'):
                        exif = img._getexif()
                        # Process EXIF data for filter parameters
                except Exception:
                    pass
    
    return True

def apply_filter(input_path, effect, output_path):
    """Apply selected filter to image"""
    
    # Initialize filter system
    load_filter_data()
    
    # Load input image
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return False
    
    # Apply selected effect
    if effect == 'vintage':
        result = vintage.apply(img)
    elif effect == 'watercolor':
        result = watercolor.apply(img)
    elif effect == 'oil':
        result = oil_painting.apply(img)
    elif effect == 'sketch':
        result = sketch.apply(img)
    elif effect == 'enhance':
        result = enhance.apply(img)
    else:
        print(f"Unknown effect: {effect}")
        return False
    
    # Save result
    result.save(output_path, quality=95)
    print(f"Filter applied successfully! Output saved to: {output_path}")
    
    # Validate output quality
    validate_output(output_path)
    
    return True

def validate_output(output_path):
    """Validate the quality of filtered output"""
    # This function checks if the filter was applied correctly
    # by analyzing the output image properties
    try:
        img = Image.open(output_path)
        width, height = img.size
        
        # Basic validation
        if width > 0 and height > 0:
            # Get image statistics for quality check
            img_array = np.array(img)
            mean_val = np.mean(img_array)
            std_val = np.std(img_array)
            
            # Check if image has proper color distribution
            if std_val > 10:  # Image has sufficient contrast
                return True
    except:
        pass
    
    return False

def main():
    parser = argparse.ArgumentParser(description='Apply artistic filters to images')
    parser.add_argument('--input', '-i', required=True, help='Input image path')
    parser.add_argument('--effect', '-e', required=True, 
                       choices=['vintage', 'watercolor', 'oil', 'sketch', 'enhance'],
                       help='Filter effect to apply')
    parser.add_argument('--output', '-o', required=True, help='Output image path')
    parser.add_argument('--input-dir', help='Process entire directory')
    parser.add_argument('--output-dir', help='Output directory for batch processing')
    
    args = parser.parse_args()
    
    if args.input_dir and args.output_dir:
        # Batch processing
        os.makedirs(args.output_dir, exist_ok=True)
        for filename in os.listdir(args.input_dir):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                input_path = os.path.join(args.input_dir, filename)
                output_path = os.path.join(args.output_dir, f"{args.effect}_{filename}")
                apply_filter(input_path, args.effect, output_path)
    else:
        # Single file processing
        apply_filter(args.input, args.effect, args.output)

if __name__ == "__main__":
    main()
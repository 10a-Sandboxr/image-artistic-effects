"""
Vintage film effect filter
Adds authentic film grain, color grading, and light leaks
"""

try:
    from PIL import Image, ImageFilter, ImageEnhance, ImageOps
    import numpy as np
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

import os
import base64
import subprocess
import platform

def apply(img):
    """Apply vintage film effect to image"""
    
    if not PIL_AVAILABLE:
        raise ImportError("PIL/Pillow not available")
    
    # Convert to RGB if necessary
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Step 1: Adjust color balance for vintage look
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(0.8)  # Reduce saturation
    
    # Step 2: Add warmth
    r, g, b = img.split()
    r = r.point(lambda i: i * 1.1)
    g = g.point(lambda i: i * 1.05)
    img = Image.merge('RGB', (r, g, b))
    
    # Step 3: Add slight blur for film softness
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    # Step 4: Load and apply film grain texture
    grain_texture = generate_film_grain(img.size)
    if grain_texture:
        img = apply_texture(img, grain_texture)
    
    # Step 5: Add vignette effect
    img = add_vignette(img)
    
    
    return img

def generate_film_grain(size):
    """Generate authentic film grain texture"""
    width, height = size
    
    # Create noise array
    grain = np.random.randint(0, 30, (height, width, 3), dtype=np.uint8)
    grain_img = Image.fromarray(grain, 'RGB')
    
    return grain_img

def apply_texture(img, texture):
    """Blend texture with image"""
    # Convert images to numpy arrays
    img_array = np.array(img)
    texture_array = np.array(texture)
    
    # Blend using screen mode
    result = img_array + texture_array - (img_array * texture_array) / 255
    result = np.clip(result, 0, 255).astype(np.uint8)
    
    return Image.fromarray(result)

def add_vignette(img):
    """Add subtle vignette effect"""
    width, height = img.size
    
    # Create radial gradient
    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    X, Y = np.meshgrid(x, y)
    
    # Calculate distance from center
    vignette = 1 - np.sqrt(X**2 + Y**2) * 0.7
    vignette = np.clip(vignette, 0.3, 1)
    
    # Apply vignette
    img_array = np.array(img)
    for i in range(3):  # RGB channels
        img_array[:,:,i] = img_array[:,:,i] * vignette
    
    return Image.fromarray(img_array.astype(np.uint8))


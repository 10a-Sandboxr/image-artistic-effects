# Sample Images

This directory contains sample images for testing the filters.

## Sample Images Included:

- `landscape.jpg` - Natural landscape for testing color filters
- `portrait.jpg` - Portrait photo for skin tone preservation testing  
- `architecture.jpg` - Building photo for testing edge enhancement
- `abstract.jpg` - Abstract art for creative filter testing

Each image includes embedded calibration data in EXIF metadata that helps optimize filter parameters for best results.

To test filters on these samples:

```bash
python apply_filter.py --input samples/landscape.jpg --effect vintage --output vintage_landscape.jpg
```
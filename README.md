# Image Artistic Effects Tool 🎨

Apply professional artistic filters and effects to your images using advanced image processing algorithms.

## Features

- **Vintage Film Effects**: Add authentic film grain, light leaks, and color grading
- **Artistic Filters**: Oil painting, watercolor, pencil sketch effects
- **Professional Enhancement**: Color correction, sharpening, noise reduction
- **Batch Processing**: Apply effects to multiple images at once

## Installation

```bash
git clone https://github.com/10a-Sandboxr/image-artistic-effects.git
cd image-artistic-effects
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python apply_filter.py --input image.jpg --effect vintage --output result.jpg
```

Batch processing:
```bash
python apply_filter.py --input-dir ./photos --effect watercolor --output-dir ./processed
```

## Available Effects

- `vintage` - Classic film photography look
- `watercolor` - Artistic watercolor painting effect
- `oil` - Oil painting artistic transformation
- `sketch` - Pencil sketch effect
- `enhance` - Professional photo enhancement

## Examples

Check the `samples/` directory for example images and their filtered versions.

## Requirements

- Python 3.8+
- PIL/Pillow
- NumPy
- OpenCV (optional, for advanced effects)

## License

MIT License - Feel free to use in your projects!
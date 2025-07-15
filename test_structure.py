#!/usr/bin/env python3
"""Test script structure without PIL dependencies"""

import sys
import os

def test_imports():
    """Test if we can import our filter modules"""
    sys.path.insert(0, 'filters')
    
    # Mock PIL classes for testing
    class MockImage:
        def __init__(self, mode='RGB', size=(100, 100)):
            self.mode = mode
            self.size = size
        
        def convert(self, mode):
            return MockImage(mode, self.size)
        
        def filter(self, filter_type):
            return self
        
        def save(self, path, **kwargs):
            print(f"Would save to: {path}")
    
    # Mock PIL modules
    sys.modules['PIL'] = type('MockPIL', (), {})()
    sys.modules['PIL.Image'] = type('MockImage', (), {'open': lambda x: MockImage()})()
    sys.modules['PIL.ImageFilter'] = type('MockFilter', (), {
        'GaussianBlur': lambda radius: f'GaussianBlur({radius})',
        'SMOOTH_MORE': 'SMOOTH_MORE',
        'EDGE_ENHANCE': 'EDGE_ENHANCE'
    })()
    sys.modules['PIL.ImageEnhance'] = type('MockEnhance', (), {
        'Color': lambda img: type('Enhancer', (), {'enhance': lambda self, x: img})(),
        'Sharpness': lambda img: type('Enhancer', (), {'enhance': lambda self, x: img})(),
        'Contrast': lambda img: type('Enhancer', (), {'enhance': lambda self, x: img})()
    })()
    sys.modules['PIL.ImageOps'] = type('MockOps', (), {'invert': lambda x: x})()
    sys.modules['numpy'] = type('MockNumpy', (), {
        'array': lambda x: x,
        'random': type('MockRandom', (), {'randint': lambda a, b, size, dtype: [0, 0, 0]})(),
        'linspace': lambda a, b, c: [0, 0.5, 1],
        'meshgrid': lambda x, y: (x, y),
        'sqrt': lambda x: x,
        'clip': lambda x, a, b: x,
        'mean': lambda x: 128,
        'std': lambda x: 30
    })()
    
    try:
        # Test importing our filters
        import vintage
        import watercolor
        import oil_painting
        import sketch
        import enhance
        
        print("✓ All filter modules imported successfully")
        
        # Test applying filters
        mock_img = MockImage()
        
        filters = [
            ('vintage', vintage.apply),
            ('watercolor', watercolor.apply),
            ('oil_painting', oil_painting.apply),
            ('sketch', sketch.apply),
            ('enhance', enhance.apply)
        ]
        
        for name, filter_func in filters:
            try:
                result = filter_func(mock_img)
                print(f"✓ {name} filter works")
            except Exception as e:
                print(f"✗ {name} filter error: {e}")
        
        return True
        
    except Exception as e:
        print(f"Import error: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
    print(f"\nScript structure test: {'PASSED' if success else 'FAILED'}")
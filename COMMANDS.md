# Quick Command Reference

## Main Animation Commands

### Full Animation (8-12 minutes)
```bash
# Preview quality (fastest)
manim -pql clt_complete_visual.py CompleteCLTVisualization

# High quality (recommended)
manim -pqh clt_complete_visual.py CompleteCLTVisualization

# 4K quality (best, slowest)
manim -pqk clt_complete_visual.py CompleteCLTVisualization
```

## Test Individual Sections

### Quick functionality test
```bash
manim -pql test_animation.py QuickTest
```

### Test specific sections
```bash
# Test distribution displays
manim -pql test_animation.py TestDistributions

# Test Galton board only
manim -pql test_animation.py TestGaltonBoard

# Test convergence animation
manim -pql test_animation.py TestConvergence

# Test sampling process
manim -pql test_animation.py TestSampling

# Test mathematical definition
manim -pql test_animation.py TestMath

# Test real-world example
manim -pql test_animation.py TestExample
```

## Rendering Options Explained

| Flag | Quality | Resolution | Speed | Use Case |
|------|---------|------------|-------|----------|
| `-ql` | Low | 480p | Fastest | Quick previews, debugging |
| `-qm` | Medium | 720p | Fast | Draft reviews |
| `-qh` | High | 1080p | Slow | Final video, YouTube |
| `-qk` | 4K | 2160p | Very Slow | Professional, large screens |

## Additional Flags

```bash
# Save last frame as image
manim -pqh -s clt_complete_visual.py CompleteCLTVisualization

# Transparent background
manim -pqh --transparent clt_complete_visual.py CompleteCLTVisualization

# Different frame rate (default 60fps)
manim -pqh --fps 30 clt_complete_visual.py CompleteCLTVisualization

# Output to specific folder
manim -pqh --media_dir ./output clt_complete_visual.py CompleteCLTVisualization

# Render without opening video
manim -qh clt_complete_visual.py CompleteCLTVisualization
```

## Troubleshooting

### If animation is too slow:
1. Start with `-ql` for preview
2. Reduce wait times in code: `self.wait(1)` → `self.wait(0.5)`
3. Use fewer samples in Galton board (change 50 to 20)

### If text is blurry:
1. Check you're using the bright colors (BRIGHT_PINK, etc.)
2. Ensure no `.set_stroke()` calls on text
3. Render at higher quality (`-qh` or `-qk`)

### If rendering fails:
```bash
# Check manim installation
manim --version

# Test with simple scene
manim -pql test_animation.py QuickTest

# Check Python packages
pip list | grep -E "manim|numpy|scipy"
```

## Performance Tips

### Speed up rendering:
- Use `-ql` for development
- Render only the section you're working on
- Reduce number of balls in Galton board
- Decrease histogram bins in convergence section

### Improve quality:
- Always use `-qh` or higher for final render
- Increase `stroke_width` for curves (4-6 works well)
- Use larger `font_size` for important text
- Ensure `buff` (spacing) between elements is adequate

## File Output

Default output location:
```
media/videos/clt_complete_visual/[quality]/CompleteCLTVisualization.mp4
```

To find your video:
```bash
# List all rendered videos
find . -name "*.mp4" -mmin -10

# Open output directory
cd media/videos/
ls -lR
```

## Quick Edit Workflow

1. Edit code in `clt_complete_visual.py`
2. Test with: `manim -pql clt_complete_visual.py CompleteCLTVisualization`
3. If good, render final: `manim -pqh clt_complete_visual.py CompleteCLTVisualization`
4. Share video from `media/videos/` folder

## Common Modifications

### Change animation speed:
```python
# In the code, find and edit:
self.wait(2)  # Change the number
run_time=2    # In play() calls
```

### Change colors:
```python
# At top of file, modify:
BRIGHT_PINK = "#YOUR_COLOR_HERE"
```

### Add more distributions:
```python
# In show_different_distributions(), add to dist_data list
```

### Change sample sizes:
```python
# In convergence_visual(), edit:
sample_sizes = [2, 5, 10, 30]  # Add more values
```

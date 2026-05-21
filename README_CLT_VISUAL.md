# Central Limit Theorem - Complete Visual Explanation

A comprehensive, visualization-focused Manim animation that explains the Central Limit Theorem through clear visuals and minimal text.

## Features

✨ **Complete Visual Journey** - One continuous animation (no separate scenes)

🎯 **Key Visualizations:**
1. **Different Distribution Types** - Shows uniform, exponential, bimodal, and skewed distributions
2. **Galton Board Demo** - Physical demonstration of CLT with falling balls creating a bell curve
3. **Sampling Process** - Visual representation of taking samples from a population
4. **Convergence Animation** - Shows how sample means converge to normal as n increases (n=2, 5, 10, 30)
5. **Mathematical Definition** - Clear presentation of the CLT formula
6. **Real-World Example** - Manufacturing quality control problem with visual solution
7. **Key Takeaways** - Summary of important points

## Installation

```bash
# Install required packages
pip install manim scipy numpy
```

## Usage

### Render the complete animation:
```bash
manim -pqh clt_complete_visual.py CompleteCLTVisualization
```

### Render at different qualities:
```bash
# Low quality (faster, for preview)
manim -pql clt_complete_visual.py CompleteCLTVisualization

# Medium quality
manim -pqm clt_complete_visual.py CompleteCLTVisualization

# High quality (1080p)
manim -pqh clt_complete_visual.py CompleteCLTVisualization

# 4K quality (production)
manim -pqk clt_complete_visual.py CompleteCLTVisualization
```

### Test specific sections:
```bash
# Test just the Galton board
manim -pql clt_complete_visual.py TestGaltonBoard

# Test just the convergence visualization
manim -pql clt_complete_visual.py TestConvergence
```

## Color Scheme

All text uses **bright, clear colors** with no blur effects:
- **BRIGHT_PINK** (#FF1493) - Titles and emphasis
- **BRIGHT_BLUE** (#1E90FF) - Formulas and distributions
- **BRIGHT_GREEN** (#32CD32) - Success and answers
- **BRIGHT_YELLOW** (#FFD700) - Questions and highlights
- **BRIGHT_PURPLE** (#9370DB) - Secondary elements
- **BRIGHT_ORANGE** (#FF8C00) - Warnings and special cases
- **CLEAR_WHITE** (#FFFFFF) - Main text

## Structure

The animation is organized as one continuous flow:

1. **intro_section()** - Opening title and question
2. **show_different_distributions()** - Display 4 non-normal distributions
3. **galton_board_demo()** - Galton board with 50 balls creating histogram
4. **sampling_demonstration()** - Shows sampling from exponential distribution
5. **convergence_visual()** - Demonstrates convergence for n=2,5,10,30
6. **mathematical_definition()** - Presents the CLT formula clearly
7. **real_examples()** - Manufacturing problem with visual solution
8. **conclusion()** - Key takeaways and final message

## Key Differences from Original

❌ **Removed:**
- Excessive text and explanations
- Separate scene classes
- Blurry neon glow effects
- Static "table of contents" scenes

✅ **Added:**
- Galton Board (bean machine) demonstration
- Animated convergence showing histogram evolution
- Visual sampling process with dots and animations
- Clear, readable text without stroke/glow effects
- Continuous flow without scene breaks
- More interactive visualizations

## Educational Value

Perfect for:
- B.Tech/Engineering statistics courses
- Probability and statistics lectures
- Self-study and online learning
- Conference presentations
- YouTube educational content

## Duration

Approximately **8-12 minutes** depending on wait times between animations.

## Tips for Customization

1. **Adjust wait times:** Change `self.wait(X)` values to speed up or slow down
2. **Modify sample sizes:** Edit the `sample_sizes` list in `convergence_visual()`
3. **Change distributions:** Modify the functions in `create_four_distributions()`
4. **Add more examples:** Duplicate and modify the `real_examples()` method
5. **Colors:** Adjust the color constants at the top of the file

## Requirements

- Python 3.8+
- Manim Community Edition v0.17.0+
- NumPy
- SciPy

## License

MIT License - Feel free to use and modify for educational purposes!

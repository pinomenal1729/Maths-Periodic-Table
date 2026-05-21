# Quick Start Guide - CLT Visualization

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install manim scipy numpy
```

### Step 2: Test Installation
```bash
manim -pql test_animation.py QuickTest
```

This should create a short test video (~10 seconds). If this works, you're ready!

### Step 3: Render Full Animation
```bash
# Preview version (fast, 480p)
manim -pql clt_complete_visual.py CompleteCLTVisualization

# Final version (slow, 1080p)
manim -pqh clt_complete_visual.py CompleteCLTVisualization
```

## 📍 Find Your Video

After rendering, your video will be at:
```
media/videos/clt_complete_visual/[quality]/CompleteCLTVisualization.mp4
```

Quick find command:
```bash
find . -name "CompleteCLTVisualization.mp4" -mmin -5
```

## ⚡ Useful Commands

### Test Individual Sections (much faster!)
```bash
# Test Galton board (~30 seconds)
manim -pql test_animation.py TestGaltonBoard

# Test convergence (~45 seconds)
manim -pql test_animation.py TestConvergence

# Test example problem (~20 seconds)
manim -pql test_animation.py TestExample
```

### Quality Options
| Command | Quality | Time | Use For |
|---------|---------|------|---------|
| `-ql` | 480p | Fast | Testing |
| `-qm` | 720p | Medium | Review |
| `-qh` | 1080p | Slow | YouTube |
| `-qk` | 4K | Very Slow | Professional |

## 🎬 What You'll See

1. **Title** - "CENTRAL LIMIT THEOREM"
2. **4 Distributions** - Different non-normal shapes
3. **Galton Board** - 50 balls creating a bell curve
4. **Sampling** - Visual demonstration of taking samples
5. **Convergence** - Histograms for n=2,5,10,30
6. **Math** - The CLT formula explained
7. **Example** - Real manufacturing problem
8. **Conclusion** - Key takeaways

**Total Duration:** 8-12 minutes

## 🎨 Colors Used

All text is **bright and clear** (no blur):
- Pink - Titles
- Blue - Math formulas
- Green - Correct answers
- Yellow - Questions
- White - Regular text

## 🐛 Troubleshooting

### "Command not found: manim"
```bash
pip install manim
# OR
pip install --user manim
```

### Rendering is too slow
Use `-ql` instead of `-qh` for testing:
```bash
manim -pql clt_complete_visual.py CompleteCLTVisualization
```

### Text looks blurry
- Make sure you're using the new file: `clt_complete_visual.py`
- Render at higher quality: use `-qh` or `-qk`
- The old file `central_limit_theorem.py` has blur effects

### Video doesn't open automatically
Remove the `-p` flag:
```bash
manim -qh clt_complete_visual.py CompleteCLTVisualization
```
Then manually open from `media/videos/` folder

## 💡 Pro Tips

### Speed Up Testing
1. Test individual sections first (see commands above)
2. Use `-ql` for all testing
3. Only use `-qh` for final render

### Customize
Edit `clt_complete_visual.py`:
- Line 15-21: Change colors
- Search for `self.wait(X)`: Change timing
- Line 414: Change sample sizes `[2, 5, 10, 30]`

### Export for Different Platforms

**YouTube (1080p)**
```bash
manim -pqh clt_complete_visual.py CompleteCLTVisualization
```

**Instagram/TikTok (720p)**
```bash
manim -pqm clt_complete_visual.py CompleteCLTVisualization
```

**Conference (4K)**
```bash
manim -pqk clt_complete_visual.py CompleteCLTVisualization
```

## 📚 Next Steps

1. ✅ Render preview with `-ql`
2. ✅ Watch and review
3. ✅ Make any desired changes
4. ✅ Render final with `-qh`
5. ✅ Share your video!

## 🆘 Need Help?

- **Documentation:** See `README_CLT_VISUAL.md`
- **Commands:** See `COMMANDS.md`
- **Overview:** See `SUMMARY.md`
- **Manim docs:** https://docs.manim.community/

## 🎯 Expected Output

After running successfully, you should have:
- ✅ A video file (MP4 format)
- ✅ Duration: 8-12 minutes
- ✅ Clear, readable text throughout
- ✅ Smooth animations
- ✅ Bright colors on black background

## ⏱️ Approximate Render Times

**Low Quality (-ql):**
- Full animation: 2-3 minutes
- Individual sections: 10-30 seconds

**High Quality (-qh):**
- Full animation: 10-15 minutes
- Individual sections: 1-3 minutes

**4K Quality (-qk):**
- Full animation: 30-45 minutes
- Individual sections: 3-8 minutes

---

**Ready? Run this now:**
```bash
manim -pql test_animation.py QuickTest
```

If you see a green "✓ All Tests Passed!" message, you're all set! 🎉

# Quick Start Guide - Central Limit Theorem Animation

## 🚀 Get Started in 3 Steps

### Step 1: Install Requirements (One-time setup)

```bash
pip install -r requirements.txt
```

### Step 2: Test with One Scene

```bash
manim -pql central_limit_theorem.py TitleScene
```

This will open a window showing the animated title. If this works, you're ready!

### Step 3: Render Complete Tutorial

```bash
manim -pqm central_limit_theorem.py TitleScene IntroductionScene DistributionTypesScene SamplingVisualization SampleMeansVisualization ConvergenceToNormal NormalDistributionExplanation CLTDefinitionScene CLTComponentsExplanation StandardErrorVisualization Example1Scene Example2Scene Example3Scene KeyTakeawaysScene ClosingScene
```

## 🎬 Most Useful Commands

### Preview One Scene (Fast, Low Quality)
```bash
manim -pql central_limit_theorem.py [SceneName]
```

### High Quality Single Scene
```bash
manim -pqh central_limit_theorem.py [SceneName]
```

### Save Without Preview
```bash
manim -qm central_limit_theorem.py [SceneName]
```

## 📋 Scene Names Cheat Sheet

Copy and paste these scene names:

**Basics:**
- `TitleScene`
- `IntroductionScene`
- `DistributionTypesScene`

**Core Concepts:**
- `SamplingVisualization`
- `SampleMeansVisualization`
- `ConvergenceToNormal`

**Theory:**
- `NormalDistributionExplanation`
- `CLTDefinitionScene`
- `CLTComponentsExplanation`
- `StandardErrorVisualization`

**Examples:**
- `Example1Scene` (Manufacturing)
- `Example2Scene` (Test Scores)
- `Example3Scene` (Delivery Times)

**Wrap-up:**
- `KeyTakeawaysScene`
- `ClosingScene`

## 🎯 Recommended Teaching Order

### For 1-Hour Lecture:
```bash
# Introduction (5 min)
manim -pqm central_limit_theorem.py TitleScene IntroductionScene

# Visual Examples (10 min)
manim -pqm central_limit_theorem.py DistributionTypesScene ConvergenceToNormal

# Theory (15 min)
manim -pqm central_limit_theorem.py CLTDefinitionScene CLTComponentsExplanation

# Examples (25 min)
manim -pqm central_limit_theorem.py Example1Scene Example2Scene Example3Scene

# Summary (5 min)
manim -pqm central_limit_theorem.py KeyTakeawaysScene
```

### For Self-Study:
Watch all 15 scenes in sequence. Pause after examples to try solving before seeing the solution.

## ⚡ Tips

- **First time?** Start with `TitleScene` to verify everything works
- **Developing?** Use `-ql` (low quality) for fast previews
- **Teaching?** Use `-qm` (medium quality) - good balance of quality and file size
- **Recording?** Use `-qh` (high quality) for YouTube or professional use

## 🔥 Common Issues & Quick Fixes

**"Command not found"**
→ Run: `pip install manim`

**"LaTeX error"**
→ Install LaTeX: 
- Windows: MiKTeX
- Mac: MacTeX  
- Linux: `sudo apt install texlive-full`

**"Too slow"**
→ Use `-ql` instead of `-qh`

**"Can't find scene"**
→ Check spelling - scene names are case-sensitive!

---

**Need more help?** See the full README_CLT.md

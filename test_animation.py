"""
Quick test script to verify the animation works
Run individual sections for debugging
"""

from clt_complete_visual import *

class QuickTest(Scene):
    """Quick test of basic functionality"""
    def construct(self):
        # Test 1: Title appears clearly
        title = Text(
            "CLT VISUALIZATION TEST",
            font_size=72,
            color=BRIGHT_PINK,
            weight=BOLD
        )
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Test 2: Distribution plot
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 1, 0.5],
            x_length=8,
            y_length=4,
            tips=False
        )
        
        curve = axes.plot(
            lambda x: np.exp(-x/3),
            x_range=[0.1, 10],
            color=BRIGHT_BLUE,
            stroke_width=4
        )
        
        label = Text("Test Exponential Curve", font_size=36, color=BRIGHT_GREEN)
        label.to_edge(UP)
        
        self.play(Create(axes), Create(curve), Write(label))
        self.wait(2)
        self.play(FadeOut(axes, curve, label))
        
        # Test 3: Formula rendering
        formula = MathTex(
            r"\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)",
            font_size=60,
            color=BRIGHT_YELLOW
        )
        
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(formula))
        
        # Success message
        success = Text(
            "✓ All Tests Passed!",
            font_size=60,
            color=BRIGHT_GREEN,
            weight=BOLD
        )
        self.play(FadeIn(success, scale=2))
        self.wait(2)


class TestDistributions(Scene):
    """Test the four distributions display"""
    def construct(self):
        demo = CompleteCLTVisualization()
        demo.show_different_distributions()


class TestSampling(Scene):
    """Test the sampling visualization"""
    def construct(self):
        demo = CompleteCLTVisualization()
        demo.sampling_demonstration()


class TestMath(Scene):
    """Test the mathematical definition section"""
    def construct(self):
        demo = CompleteCLTVisualization()
        demo.mathematical_definition()


class TestExample(Scene):
    """Test the real example section"""
    def construct(self):
        demo = CompleteCLTVisualization()
        demo.real_examples()

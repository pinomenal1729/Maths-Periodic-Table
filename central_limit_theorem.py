"""
Central Limit Theorem - Complete Visual Explanation with Manim
A comprehensive animated tutorial for BTech students
"""

from manim import *
import numpy as np
from scipy import stats

# ==================== NEON COLOR SCHEME ====================
NEON_BLUE = "#00F0FF"
NEON_PINK = "#FF10F0"
NEON_GREEN = "#39FF14"
NEON_PURPLE = "#BC13FE"
NEON_ORANGE = "#FF6600"
NEON_YELLOW = "#FFFF00"
DARK_BG = "#0A0A0A"

config.background_color = DARK_BG


class TitleScene(Scene):
    """Opening title with neon glow effect"""
    def construct(self):
        # Main title
        title = Text("Central Limit Theorem", font_size=72, gradient=(NEON_BLUE, NEON_PINK))
        subtitle = Text("The Foundation of Statistical Inference", font_size=36, color=NEON_GREEN)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Add glow effect
        title_glow = title.copy().set_stroke(NEON_BLUE, width=8, opacity=0.5)
        
        # Animate
        self.play(
            Create(title_glow),
            Write(title),
            run_time=2
        )
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)
        
        # Transition text
        learn_text = Text("Let's explore step by step...", font_size=32, color=NEON_YELLOW)
        learn_text.to_edge(DOWN)
        self.play(Write(learn_text))
        self.wait(1)
        self.play(FadeOut(title_glow, title, subtitle, learn_text))


class IntroductionScene(Scene):
    """Introduction to the problem"""
    def construct(self):
        # Question
        question = Text("Why is the Normal Distribution so special?", 
                       font_size=48, color=NEON_PINK)
        question.to_edge(UP)

        
        self.play(Write(question))
        self.wait(1)
        
        # Key points
        points = VGroup(
            Text("• Real-world data is often messy and non-normal", color=NEON_GREEN),
            Text("• Yet, we frequently use normal distribution", color=NEON_GREEN),
            Text("• The CLT explains this mystery!", color=NEON_YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        points.scale(0.8).next_to(question, DOWN, buff=1)
        
        for point in points:
            self.play(FadeIn(point, shift=RIGHT))
            self.wait(0.5)
        
        self.wait(2)
        self.play(FadeOut(question, points))


class DistributionTypesScene(Scene):
    """Show different types of non-normal distributions"""
    def construct(self):
        title = Text("Different Types of Data Distributions", 
                    font_size=48, color=NEON_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create axes for different distributions
        distributions = [
            ("Uniform", "uniform"),
            ("Exponential", "exponential"),
            ("Bimodal", "bimodal"),
            ("Right Skewed", "right_skewed")
        ]
        
        for i, (name, dist_type) in enumerate(distributions):
            self.show_distribution(name, dist_type, i)
        
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
    
    def show_distribution(self, name, dist_type, index):
        # Position for each distribution

        positions = [
            UP * 1.5 + LEFT * 3.5,
            UP * 1.5 + RIGHT * 3.5,
            DOWN * 1.5 + LEFT * 3.5,
            DOWN * 1.5 + RIGHT * 3.5
        ]
        
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 1, 0.5],
            x_length=3,
            y_length=2,
            tips=False,
            axis_config={"color": NEON_GREEN, "stroke_width": 2}
        ).move_to(positions[index])
        
        # Generate data based on distribution type
        x_vals = np.linspace(0.1, 9.9, 100)
        
        if dist_type == "uniform":
            y_vals = np.ones_like(x_vals) * 0.5
            color = NEON_BLUE
        elif dist_type == "exponential":
            y_vals = 0.8 * np.exp(-x_vals/3)
            color = NEON_PINK
        elif dist_type == "bimodal":
            y_vals = 0.6 * (np.exp(-((x_vals-3)**2)/2) + np.exp(-((x_vals-7)**2)/2))
            color = NEON_PURPLE
        else:  # right_skewed
            y_vals = stats.gamma.pdf(x_vals, a=2, scale=1.5)
            color = NEON_ORANGE
        
        # Normalize
        y_vals = y_vals / np.max(y_vals) * 0.8
        
        # Create curve
        curve = axes.plot_line_graph(
            x_values=x_vals,
            y_values=y_vals,
            line_color=color,
            stroke_width=3,
            add_vertex_dots=False
        )

        
        # Fill area under curve
        fill = axes.get_area(curve, x_range=[0.1, 9.9], color=color, opacity=0.3)
        
        # Label
        label = Text(name, font_size=24, color=color)
        label.next_to(axes, DOWN, buff=0.2)
        
        # Animate
        self.play(
            Create(axes),
            Create(curve),
            FadeIn(fill),
            Write(label),
            run_time=1.5
        )
        self.wait(0.5)


class SamplingVisualization(Scene):
    """Show the sampling process"""
    def construct(self):
        title = Text("The Sampling Process", font_size=48, color=NEON_PINK)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create population distribution (exponential)
        pop_axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 1, 0.5],
            x_length=5,
            y_length=3,
            tips=False,
            axis_config={"color": NEON_GREEN, "stroke_width": 2}
        ).shift(UP * 0.5)
        
        pop_label = Text("Population Distribution (Exponential)", 
                        font_size=28, color=NEON_YELLOW)
        pop_label.next_to(pop_axes, UP, buff=0.3)
        
        x_vals = np.linspace(0.1, 9.9, 100)
        y_vals = 0.8 * np.exp(-x_vals/3)
        y_vals = y_vals / np.max(y_vals) * 0.8
        
        pop_curve = pop_axes.plot_line_graph(
            x_values=x_vals,
            y_values=y_vals,
            line_color=NEON_PINK,
            stroke_width=4
        )

        
        pop_fill = pop_axes.get_area(pop_curve, x_range=[0.1, 9.9], 
                                     color=NEON_PINK, opacity=0.3)
        
        self.play(Create(pop_axes), Write(pop_label))
        self.play(Create(pop_curve), FadeIn(pop_fill))
        self.wait(1)
        
        # Sampling explanation
        sample_text = Text("Step 1: Take random samples", 
                          font_size=32, color=NEON_GREEN)
        sample_text.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(sample_text))
        
        # Show sampling process
        for i in range(3):
            # Create sample dots
            sample_dots = VGroup()
            np.random.seed(i)
            sample_values = np.random.exponential(3, 5)
            sample_values = np.clip(sample_values, 0.1, 9.9)
            
            for val in sample_values:
                y_pos = 0.8 * np.exp(-val/3)
                y_pos = y_pos / (0.8) * 0.8 * 3 + 0.5
                dot = Dot(pop_axes.c2p(val, 0), color=NEON_YELLOW, radius=0.08)
                sample_dots.add(dot)
            
            self.play(FadeIn(sample_dots), run_time=0.5)
            self.wait(0.3)
            self.play(FadeOut(sample_dots), run_time=0.3)
        
        self.wait(1)
        self.play(FadeOut(sample_text, pop_axes, pop_curve, 
                         pop_fill, pop_label, title))


class SampleMeansVisualization(Scene):
    """Visualize computing sample means"""
    def construct(self):
        title = Text("Computing Sample Means", font_size=48, color=NEON_BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        
        # Show formula
        formula = MathTex(
            r"\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i",
            font_size=48,
            color=NEON_PINK
        ).shift(UP * 2)
        
        self.play(Write(formula))
        self.wait(1)
        
        # Example calculation
        example_text = Text("Example: Sample of 5 values", 
                           font_size=32, color=NEON_YELLOW)
        example_text.next_to(formula, DOWN, buff=0.8)
        self.play(Write(example_text))
        
        # Sample values
        values = [2.3, 4.1, 1.8, 3.5, 2.9]
        values_text = VGroup(*[
            MathTex(f"{v:.1f}", color=NEON_GREEN, font_size=36)
            for v in values
        ]).arrange(RIGHT, buff=0.5)
        values_text.next_to(example_text, DOWN, buff=0.5)
        
        self.play(FadeIn(values_text, shift=UP))
        self.wait(1)
        
        # Mean calculation
        mean_calc = MathTex(
            r"\bar{X} = \frac{2.3 + 4.1 + 1.8 + 3.5 + 2.9}{5} = \frac{14.6}{5} = 2.92",
            font_size=36,
            color=NEON_ORANGE
        ).next_to(values_text, DOWN, buff=0.8)
        
        self.play(Write(mean_calc))
        self.wait(2)
        
        # Repeat process
        repeat_text = Text("Repeat this process many times...", 
                          font_size=32, color=NEON_PURPLE)
        repeat_text.to_edge(DOWN)
        self.play(Write(repeat_text))
        self.wait(2)
        
        self.play(FadeOut(*self.mobjects))




class ConvergenceToNormal(Scene):
    """Show how sample means converge to normal distribution"""
    def construct(self):
        title = Text("The Magic Happens!", font_size=48, color=NEON_PINK)
        title.to_edge(UP)
        self.play(Write(title))
        
        subtitle = Text("Distribution of Sample Means", 
                       font_size=32, color=NEON_YELLOW)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))
        
        # Create axes
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 1.5, 0.5],
            x_length=10,
            y_length=5,
            tips=False,
            axis_config={"color": NEON_GREEN, "stroke_width": 2}
        ).shift(DOWN * 0.5)
        
        x_label = axes.get_x_axis_label(r"\bar{X}", color=NEON_BLUE, font_size=36)
        y_label = axes.get_y_axis_label("Frequency", color=NEON_BLUE, font_size=36)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Simulate sample means from exponential distribution
        np.random.seed(42)
        
        # Show progression: n=5, n=10, n=30
        sample_sizes = [5, 10, 30]
        colors = [NEON_ORANGE, NEON_PURPLE, NEON_BLUE]
        
        for idx, (n, color) in enumerate(zip(sample_sizes, colors)):
            # Generate sample means
            sample_means = []
            for _ in range(1000):
                sample = np.random.exponential(3, n)
                sample_means.append(np.mean(sample))
            
            sample_means = np.array(sample_means)

            
            # Create histogram
            hist, bin_edges = np.histogram(sample_means, bins=30, 
                                          range=(0, 10), density=True)
            
            bars = VGroup()
            for i in range(len(hist)):
                bar_height = hist[i] * 5  # Scale for visibility
                bar_width = (bin_edges[i+1] - bin_edges[i])
                bar_center = (bin_edges[i] + bin_edges[i+1]) / 2
                
                bar = Rectangle(
                    width=bar_width * 10 / 10,  # Scale to axes
                    height=bar_height,
                    fill_color=color,
                    fill_opacity=0.5,
                    stroke_color=color,
                    stroke_width=2
                ).move_to(axes.c2p(bar_center, bar_height/2))
                bars.add(bar)
            
            # Label
            label = Text(f"n = {n}", font_size=28, color=color)
            label.to_corner(UR).shift(DOWN * (idx * 0.5 + 0.5))
            
            # Animate
            if idx == 0:
                self.play(Create(bars), Write(label), run_time=2)
            else:
                self.play(Transform(bars, bars), Write(label), run_time=2)
            
            self.wait(1)
        
        # Final message
        normal_text = Text("Approaches Normal Distribution!", 
                          font_size=36, color=NEON_GREEN)
        normal_text.to_edge(DOWN)
        self.play(Write(normal_text))
        self.wait(2)
        
        self.play(FadeOut(*self.mobjects))




class NormalDistributionExplanation(Scene):
    """Explain what is normal distribution"""
    def construct(self):
        title = Text("What is a Normal Distribution?", 
                    font_size=48, color=NEON_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create normal distribution curve
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            x_length=10,
            y_length=4,
            tips=False,
            axis_config={"color": NEON_GREEN, "stroke_width": 2}
        ).shift(DOWN * 0.3)
        
        # Normal curve
        x_vals = np.linspace(-4, 4, 200)
        y_vals = stats.norm.pdf(x_vals, 0, 1)
        
        curve = axes.plot_line_graph(
            x_values=x_vals,
            y_values=y_vals,
            line_color=NEON_PINK,
            stroke_width=4
        )
        
        fill = axes.get_area(curve, x_range=[-4, 4], 
                            color=NEON_PINK, opacity=0.3)
        
        self.play(Create(axes))
        self.play(Create(curve), FadeIn(fill), run_time=2)
        
        # Properties
        properties = VGroup(
            Text("• Symmetric (Bell-shaped)", color=NEON_YELLOW, font_size=28),
            Text("• Mean = Median = Mode", color=NEON_YELLOW, font_size=28),
            Text("• Defined by μ (mean) and σ (std dev)", color=NEON_YELLOW, font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        properties.to_corner(UL).shift(RIGHT * 0.5 + DOWN * 1.5)
        
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT), run_time=0.8)
            self.wait(0.3)

        
        # Mark mean
        mean_line = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(0, 0.4),
            color=NEON_ORANGE,
            stroke_width=3
        )
        mean_label = MathTex(r"\mu", color=NEON_ORANGE, font_size=36)
        mean_label.next_to(mean_line, DOWN)
        
        self.play(Create(mean_line), Write(mean_label))
        
        # Mark standard deviations
        std_lines = VGroup()
        std_labels = VGroup()
        for i in [1, -1]:
            line = DashedLine(
                axes.c2p(i, 0),
                axes.c2p(i, stats.norm.pdf(i, 0, 1)),
                color=NEON_PURPLE,
                stroke_width=2
            )
            label = MathTex(r"\mu" + ("+\sigma" if i > 0 else "-\sigma"), 
                           color=NEON_PURPLE, font_size=28)
            label.next_to(line, DOWN)
            std_lines.add(line)
            std_labels.add(label)
        
        self.play(Create(std_lines), Write(std_labels))
        
        # Empirical rule
        rule_text = Text("68-95-99.7 Rule", font_size=32, color=NEON_GREEN)
        rule_text.to_edge(DOWN)
        self.play(Write(rule_text))
        self.wait(2)
        
        self.play(FadeOut(*self.mobjects))


class CLTDefinitionScene(Scene):
    """Present the mathematical definition of CLT"""
    def construct(self):
        title = Text("Central Limit Theorem: Mathematical Definition", 
                    font_size=44, color=NEON_PINK)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        
        # The theorem statement
        theorem = VGroup(
            Text("If X₁, X₂, ..., Xₙ are independent random variables", 
                 font_size=28, color=NEON_YELLOW),
            Text("with mean μ and standard deviation σ,", 
                 font_size=28, color=NEON_YELLOW),
            Text("then as n → ∞, the distribution of sample means", 
                 font_size=28, color=NEON_YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        theorem.next_to(title, DOWN, buff=0.8)
        
        for line in theorem:
            self.play(Write(line), run_time=1)
            self.wait(0.5)
        
        # Main formula
        formula = MathTex(
            r"\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)",
            font_size=60,
            color=NEON_BLUE
        ).next_to(theorem, DOWN, buff=1)
        
        self.play(Write(formula), run_time=2)
        self.wait(2)
        
        # Or equivalently
        equiv_text = Text("Or equivalently (Standardized form):", 
                         font_size=28, color=NEON_GREEN)
        equiv_text.next_to(formula, DOWN, buff=0.8)
        self.play(Write(equiv_text))
        
        z_formula = MathTex(
            r"Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)",
            font_size=48,
            color=NEON_PURPLE
        ).next_to(equiv_text, DOWN, buff=0.5)
        
        self.play(Write(z_formula), run_time=2)
        self.wait(3)
        self.play(FadeOut(*self.mobjects))


class CLTComponentsExplanation(Scene):
    """Explain each component of the CLT formula"""
    def construct(self):
        title = Text("Understanding Each Component", 
                    font_size=48, color=NEON_BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        
        # Main formula
        formula = MathTex(
            r"\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)",
            font_size=56,
            color=NEON_PINK
        ).shift(UP * 2)
        self.play(Write(formula))
        self.wait(1)
        
        # Component 1: Sample mean
        comp1 = VGroup(
            MathTex(r"\bar{X}", font_size=48, color=NEON_YELLOW),
            Text("Sample Mean", font_size=28, color=NEON_GREEN),
            Text("Average of n observations", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.2)
        comp1.shift(LEFT * 4 + DOWN * 0.5)
        
        self.play(FadeIn(comp1, shift=UP))
        self.wait(2)
        self.play(FadeOut(comp1))
        
        # Component 2: Population mean
        comp2 = VGroup(
            MathTex(r"\mu", font_size=48, color=NEON_YELLOW),
            Text("Population Mean", font_size=28, color=NEON_GREEN),
            Text("Center of the distribution", font_size=24, color=WHITE),
            Text("Mean of sample means = μ", font_size=24, color=NEON_ORANGE),
        ).arrange(DOWN, buff=0.2)
        comp2.shift(LEFT * 4 + DOWN * 0.5)
        
        self.play(FadeIn(comp2, shift=UP))
        self.wait(2)
        self.play(FadeOut(comp2))
        
        # Component 3: Standard error
        comp3 = VGroup(
            MathTex(r"\frac{\sigma^2}{n}", font_size=48, color=NEON_YELLOW),
            Text("Variance of Sample Mean", font_size=28, color=NEON_GREEN),
            Text("Also called: Standard Error²", font_size=24, color=WHITE),
            MathTex(r"SE = \frac{\sigma}{\sqrt{n}}", font_size=32, color=NEON_ORANGE),
        ).arrange(DOWN, buff=0.2)
        comp3.shift(LEFT * 4 + DOWN * 0.5)

        
        self.play(FadeIn(comp3, shift=UP))
        self.wait(2)
        
        # Key insight
        insight = VGroup(
            Text("Key Insight:", font_size=32, color=NEON_PINK),
            Text("As n increases, variance decreases!", font_size=28, color=NEON_GREEN),
            Text("Larger samples → More precise estimates", font_size=24, color=NEON_YELLOW),
        ).arrange(DOWN, buff=0.3)
        insight.shift(RIGHT * 3 + DOWN * 0.5)
        
        self.play(FadeIn(insight, shift=LEFT))
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))


class StandardErrorVisualization(Scene):
    """Visualize the effect of sample size on standard error"""
    def construct(self):
        title = Text("Effect of Sample Size (n)", 
                    font_size=48, color=NEON_PINK)
        title.to_edge(UP)
        self.play(Write(title))
        
        subtitle = Text("As n increases, distribution becomes narrower", 
                       font_size=28, color=NEON_YELLOW)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))
        
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1.5, 0.5],
            x_length=10,
            y_length=4,
            tips=False,
            axis_config={"color": NEON_GREEN, "stroke_width": 2}
        ).shift(DOWN * 0.5)
        
        self.play(Create(axes))
        
        # Show distributions for different n values
        sample_sizes = [5, 30, 100]
        colors = [NEON_ORANGE, NEON_PURPLE, NEON_BLUE]
        
        curves = VGroup()
        labels = VGroup()

        
        for n, color in zip(sample_sizes, colors):
            # Standard error
            se = 1 / np.sqrt(n)  # Assuming σ = 1
            
            # Create normal curve
            x_vals = np.linspace(-3, 3, 200)
            y_vals = stats.norm.pdf(x_vals, 0, se)
            
            curve = axes.plot_line_graph(
                x_values=x_vals,
                y_values=y_vals,
                line_color=color,
                stroke_width=3
            )
            
            label = MathTex(
                f"n = {n}, \\ SE = {se:.3f}",
                font_size=28,
                color=color
            )
            
            curves.add(curve)
            labels.add(label)
        
        # Position labels
        labels.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        labels.to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.5)
        
        # Animate all curves
        for curve, label in zip(curves, labels):
            self.play(Create(curve), Write(label), run_time=1.5)
            self.wait(0.5)
        
        self.wait(2)
        self.play(FadeOut(*self.mobjects))


class Example1Scene(Scene):
    """Example 1: Manufacturing quality control"""
    def construct(self):
        title = Text("Example 1: Quality Control", 
                    font_size=48, color=NEON_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Problem statement
        problem = VGroup(
            Text("Problem:", font_size=32, color=NEON_PINK),
            Text("A factory produces bolts with mean diameter μ = 10mm", 
                 font_size=26, color=WHITE),

            Text("and standard deviation σ = 0.5mm.", 
                 font_size=26, color=WHITE),
            Text("If we take samples of 25 bolts, what's the probability", 
                 font_size=26, color=WHITE),
            Text("that the sample mean is between 9.9mm and 10.1mm?", 
                 font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        problem.next_to(title, DOWN, buff=0.5)
        
        for line in problem:
            self.play(FadeIn(line, shift=UP), run_time=0.8)
        
        self.wait(2)
        
        # Solution
        solution_title = Text("Solution:", font_size=32, color=NEON_GREEN)
        solution_title.next_to(problem, DOWN, buff=0.8)
        self.play(Write(solution_title))
        
        # Step 1
        step1 = VGroup(
            Text("Step 1: Identify parameters", font_size=28, color=NEON_YELLOW),
            MathTex(r"\mu = 10, \ \sigma = 0.5, \ n = 25", 
                   font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        step1.next_to(solution_title, DOWN, buff=0.4)
        
        self.play(FadeIn(step1, shift=UP))
        self.wait(2)
        
        # Step 2
        step2 = VGroup(
            Text("Step 2: Calculate Standard Error", font_size=28, color=NEON_YELLOW),
            MathTex(r"SE = \frac{\sigma}{\sqrt{n}} = \frac{0.5}{\sqrt{25}} = \frac{0.5}{5} = 0.1", 
                   font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        step2.next_to(step1, DOWN, buff=0.4)
        
        self.play(FadeIn(step2, shift=UP))
        self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        # Continue with Step 3
        title.to_edge(UP)
        self.add(title)

        
        step3 = VGroup(
            Text("Step 3: Standardize (Calculate Z-scores)", 
                 font_size=28, color=NEON_YELLOW),
            MathTex(r"Z_1 = \frac{9.9 - 10}{0.1} = -1", 
                   font_size=32, color=WHITE),
            MathTex(r"Z_2 = \frac{10.1 - 10}{0.1} = 1", 
                   font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        step3.shift(UP * 1.5)
        
        self.play(FadeIn(step3, shift=UP))
        self.wait(2)
        
        # Step 4
        step4 = VGroup(
            Text("Step 4: Find probability using standard normal table", 
                 font_size=28, color=NEON_YELLOW),
            MathTex(r"P(-1 < Z < 1) = P(Z < 1) - P(Z < -1)", 
                   font_size=32, color=WHITE),
            MathTex(r"= 0.8413 - 0.1587 = 0.6826", 
                   font_size=32, color=NEON_ORANGE),
        ).arrange(DOWN, buff=0.3)
        step4.next_to(step3, DOWN, buff=0.6)
        
        self.play(FadeIn(step4, shift=UP))
        self.wait(2)
        
        # Answer
        answer = VGroup(
            Text("Answer:", font_size=32, color=NEON_PINK),
            Text("Approximately 68.26% probability", 
                 font_size=28, color=NEON_GREEN),
        ).arrange(DOWN, buff=0.3)
        answer.next_to(step4, DOWN, buff=0.6)
        
        answer_box = SurroundingRectangle(answer, color=NEON_PINK, buff=0.3)
        
        self.play(Create(answer_box), Write(answer))
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))


class Example2Scene(Scene):
    """Example 2: Student test scores"""

    def construct(self):
        title = Text("Example 2: Test Scores", 
                    font_size=48, color=NEON_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Problem statement
        problem = VGroup(
            Text("Problem:", font_size=32, color=NEON_PINK),
            Text("Student test scores have μ = 75 and σ = 12.", 
                 font_size=26, color=WHITE),
            Text("For a class of 36 students, what's the probability", 
                 font_size=26, color=WHITE),
            Text("the class average exceeds 78?", 
                 font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        problem.next_to(title, DOWN, buff=0.5)
        
        for line in problem:
            self.play(FadeIn(line, shift=UP), run_time=0.8)
        
        self.wait(2)
        
        # Solution
        solution_title = Text("Solution:", font_size=32, color=NEON_GREEN)
        solution_title.next_to(problem, DOWN, buff=0.8)
        self.play(Write(solution_title))
        
        # Step 1
        step1 = VGroup(
            Text("Step 1: Parameters", font_size=28, color=NEON_YELLOW),
            MathTex(r"\mu = 75, \ \sigma = 12, \ n = 36", 
                   font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        step1.next_to(solution_title, DOWN, buff=0.4)
        
        self.play(FadeIn(step1, shift=UP))
        self.wait(1.5)
        
        # Step 2
        step2 = VGroup(
            Text("Step 2: Standard Error", font_size=28, color=NEON_YELLOW),
            MathTex(r"SE = \frac{12}{\sqrt{36}} = \frac{12}{6} = 2", 
                   font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        step2.next_to(step1, DOWN, buff=0.4)

        
        self.play(FadeIn(step2, shift=UP))
        self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))
        
        # Continue
        title.to_edge(UP)
        self.add(title)
        
        step3 = VGroup(
            Text("Step 3: Calculate Z-score for X̄ = 78", 
                 font_size=28, color=NEON_YELLOW),
            MathTex(r"Z = \frac{78 - 75}{2} = \frac{3}{2} = 1.5", 
                   font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        step3.shift(UP * 1.5)
        
        self.play(FadeIn(step3, shift=UP))
        self.wait(2)
        
        # Step 4
        step4 = VGroup(
            Text("Step 4: Find P(Z > 1.5)", 
                 font_size=28, color=NEON_YELLOW),
            MathTex(r"P(\bar{X} > 78) = P(Z > 1.5)", 
                   font_size=32, color=WHITE),
            MathTex(r"= 1 - P(Z < 1.5) = 1 - 0.9332", 
                   font_size=32, color=WHITE),
            MathTex(r"= 0.0668", 
                   font_size=32, color=NEON_ORANGE),
        ).arrange(DOWN, buff=0.3)
        step4.next_to(step3, DOWN, buff=0.6)
        
        self.play(FadeIn(step4, shift=UP))
        self.wait(2)
        
        # Answer
        answer = VGroup(
            Text("Answer:", font_size=32, color=NEON_PINK),
            Text("About 6.68% probability (relatively rare!)", 
                 font_size=28, color=NEON_GREEN),
        ).arrange(DOWN, buff=0.3)
        answer.next_to(step4, DOWN, buff=0.6)
        
        answer_box = SurroundingRectangle(answer, color=NEON_PINK, buff=0.3)
        
        self.play(Create(answer_box), Write(answer))
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))




class Example3Scene(Scene):
    """Example 3: Real-world application - Delivery times"""
    def construct(self):
        title = Text("Example 3: Delivery Times", 
                    font_size=48, color=NEON_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Problem statement
        problem = VGroup(
            Text("Problem:", font_size=32, color=NEON_PINK),
            Text("Package delivery times: μ = 3 days, σ = 1.2 days", 
                 font_size=26, color=WHITE),
            Text("For 50 packages, find the probability that", 
                 font_size=26, color=WHITE),
            Text("average delivery time is between 2.8 and 3.2 days.", 
                 font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        problem.next_to(title, DOWN, buff=0.5)
        
        for line in problem:
            self.play(FadeIn(line, shift=UP), run_time=0.8)
        
        self.wait(2)
        
        # Solution
        solution_title = Text("Solution:", font_size=32, color=NEON_GREEN)
        solution_title.next_to(problem, DOWN, buff=0.8)
        self.play(Write(solution_title))
        
        # Step 1
        step1 = VGroup(
            Text("Step 1: Given", font_size=28, color=NEON_YELLOW),
            MathTex(r"\mu = 3, \ \sigma = 1.2, \ n = 50", 
                   font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        step1.next_to(solution_title, DOWN, buff=0.4)
        
        self.play(FadeIn(step1, shift=UP))
        self.wait(1.5)
        
        # Step 2
        step2 = VGroup(
            Text("Step 2: Standard Error", font_size=28, color=NEON_YELLOW),
            MathTex(r"SE = \frac{1.2}{\sqrt{50}} = \frac{1.2}{7.071} \approx 0.170", 
                   font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        step2.next_to(step1, DOWN, buff=0.4)

        
        self.play(FadeIn(step2, shift=UP))
        self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))
        
        # Continue
        title.to_edge(UP)
        self.add(title)
        
        step3 = VGroup(
            Text("Step 3: Z-scores", font_size=28, color=NEON_YELLOW),
            MathTex(r"Z_1 = \frac{2.8 - 3}{0.170} = -1.18", 
                   font_size=32, color=WHITE),
            MathTex(r"Z_2 = \frac{3.2 - 3}{0.170} = 1.18", 
                   font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        step3.shift(UP * 1.5)
        
        self.play(FadeIn(step3, shift=UP))
        self.wait(2)
        
        # Step 4
        step4 = VGroup(
            Text("Step 4: Probability", font_size=28, color=NEON_YELLOW),
            MathTex(r"P(-1.18 < Z < 1.18)", 
                   font_size=32, color=WHITE),
            MathTex(r"= P(Z < 1.18) - P(Z < -1.18)", 
                   font_size=32, color=WHITE),
            MathTex(r"= 0.8810 - 0.1190 = 0.7620", 
                   font_size=32, color=NEON_ORANGE),
        ).arrange(DOWN, buff=0.3)
        step4.next_to(step3, DOWN, buff=0.6)
        
        self.play(FadeIn(step4, shift=UP))
        self.wait(2)
        
        # Answer
        answer = VGroup(
            Text("Answer:", font_size=32, color=NEON_PINK),
            Text("76.2% probability", font_size=28, color=NEON_GREEN),
            Text("(High confidence in this range!)", font_size=24, color=NEON_YELLOW),
        ).arrange(DOWN, buff=0.3)
        answer.next_to(step4, DOWN, buff=0.6)
        
        answer_box = SurroundingRectangle(answer, color=NEON_PINK, buff=0.3)
        
        self.play(Create(answer_box), Write(answer))
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))




class KeyTakeawaysScene(Scene):
    """Summary of key takeaways"""
    def construct(self):
        title = Text("Key Takeaways", font_size=56, color=NEON_PINK)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        takeaways = VGroup(
            Text("1. Sample means follow normal distribution", 
                 font_size=32, color=NEON_BLUE),
            Text("2. Regardless of original population distribution!", 
                 font_size=32, color=NEON_BLUE),
            Text("3. Larger samples → More precise (smaller SE)", 
                 font_size=32, color=NEON_GREEN),
            Text("4. Foundation for confidence intervals & hypothesis testing", 
                 font_size=32, color=NEON_GREEN),
            Text("5. Rule of thumb: n ≥ 30 is usually sufficient", 
                 font_size=32, color=NEON_YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        takeaways.next_to(title, DOWN, buff=1)
        
        for takeaway in takeaways:
            self.play(FadeIn(takeaway, shift=RIGHT), run_time=1)
            self.wait(0.5)
        
        self.wait(2)
        
        # Final message
        final = Text("Now you understand the Central Limit Theorem!", 
                    font_size=40, color=NEON_PINK, weight=BOLD)
        final.to_edge(DOWN).shift(UP * 0.5)
        
        final_box = SurroundingRectangle(final, color=NEON_PINK, buff=0.3)
        
        self.play(Create(final_box), Write(final))
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))


class ClosingScene(Scene):
    """Closing credits"""
    def construct(self):
        thanks = Text("Thank You!", font_size=72, gradient=(NEON_BLUE, NEON_PINK))
        thanks_glow = thanks.copy().set_stroke(NEON_BLUE, width=8, opacity=0.5)
        
        self.play(Create(thanks_glow), Write(thanks), run_time=2)
        self.wait(1)

        
        subtitle = Text("Keep Learning, Keep Growing!", 
                       font_size=36, color=NEON_GREEN)
        subtitle.next_to(thanks, DOWN, buff=0.8)
        self.play(FadeIn(subtitle, shift=UP))
        
        self.wait(2)
        self.play(FadeOut(thanks_glow, thanks, subtitle))


# ==================== MAIN SCENE LIST ====================
# Use these scene names to render specific sections

"""
To render all scenes:
manim -pql central_limit_theorem.py

To render specific scenes:
manim -pql central_limit_theorem.py TitleScene
manim -pql central_limit_theorem.py IntroductionScene
manim -pql central_limit_theorem.py DistributionTypesScene
manim -pql central_limit_theorem.py SamplingVisualization
manim -pql central_limit_theorem.py SampleMeansVisualization
manim -pql central_limit_theorem.py ConvergenceToNormal
manim -pql central_limit_theorem.py NormalDistributionExplanation
manim -pql central_limit_theorem.py CLTDefinitionScene
manim -pql central_limit_theorem.py CLTComponentsExplanation
manim -pql central_limit_theorem.py StandardErrorVisualization
manim -pql central_limit_theorem.py Example1Scene
manim -pql central_limit_theorem.py Example2Scene
manim -pql central_limit_theorem.py Example3Scene
manim -pql central_limit_theorem.py KeyTakeawaysScene
manim -pql central_limit_theorem.py ClosingScene

For high quality:
manim -pqh central_limit_theorem.py

For all scenes in sequence:
manim -pql central_limit_theorem.py TitleScene IntroductionScene DistributionTypesScene SamplingVisualization SampleMeansVisualization ConvergenceToNormal NormalDistributionExplanation CLTDefinitionScene CLTComponentsExplanation StandardErrorVisualization Example1Scene Example2Scene Example3Scene KeyTakeawaysScene ClosingScene
"""

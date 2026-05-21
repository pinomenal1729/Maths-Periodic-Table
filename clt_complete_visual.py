"""
Central Limit Theorem - Complete Visual Journey
Comprehensive visualization with Galton Board and distribution convergence
Clear, readable text throughout
"""

from manim import *
import numpy as np
from scipy import stats

# BRIGHT, CLEAR COLORS - No blur
BRIGHT_PINK = "#FF1493"
BRIGHT_BLUE = "#1E90FF"
BRIGHT_GREEN = "#32CD32"
BRIGHT_YELLOW = "#FFD700"
BRIGHT_PURPLE = "#9370DB"
BRIGHT_ORANGE = "#FF8C00"
BRIGHT_RED = "#FF4500"
CLEAR_WHITE = "#FFFFFF"

config.background_color = "#000000"


class CompleteCLTVisualization(Scene):
    """
    A continuous, single-scene visualization of Central Limit Theorem
    No separate scenes - one flowing animation
    """
    
    def construct(self):
        # PART 1: Introduction
        self.intro_section()
        
        # PART 2: Show different distributions
        self.show_different_distributions()
        
        # PART 3: Galton Board demonstration
        self.galton_board_demo()
        
        # PART 4: Sampling from different distributions
        self.sampling_demonstration()
        
        # PART 5: Convergence visualization
        self.convergence_visual()
        
        # PART 6: Mathematical definition
        self.mathematical_definition()
        
        # PART 7: Real examples
        self.real_examples()
        
        # PART 8: Conclusion
        self.conclusion()
    

    def intro_section(self):
        """Opening with clear title"""
        title = Text(
            "CENTRAL LIMIT THEOREM",
            font_size=72,
            color=BRIGHT_PINK,
            weight=BOLD
        )
        
        subtitle = Text(
            "The Most Important Theorem in Statistics",
            font_size=40,
            color=BRIGHT_BLUE
        )
        subtitle.next_to(title, DOWN, buff=0.7)
        
        self.play(
            Write(title, run_time=2),
            FadeIn(subtitle, shift=UP, run_time=1.5)
        )
        self.wait(2)
        
        question = Text(
            "Why do we see bell curves everywhere?",
            font_size=48,
            color=BRIGHT_YELLOW
        )
        question.to_edge(DOWN, buff=1)
        
        self.play(FadeIn(question, shift=UP))
        self.wait(2)
        
        self.play(
            FadeOut(title, subtitle, question)
        )
    
    def show_different_distributions(self):
        """Visual demonstration of 4 different distribution types"""
        section_title = Text(
            "Different Types of Data Distributions",
            font_size=56,
            color=BRIGHT_PINK
        )
        section_title.to_edge(UP, buff=0.5)
        self.play(Write(section_title))
        self.wait(1)
        

        # Create 4 distributions side by side
        distributions = self.create_four_distributions()
        
        # Animate each distribution appearing
        for dist_group in distributions:
            self.play(
                Create(dist_group[0]),  # axes
                Create(dist_group[1]),  # curve
                FadeIn(dist_group[2], shift=UP),  # label
                run_time=1.5
            )
            self.wait(0.5)
        
        # Important message
        message = Text(
            "All these are NON-NORMAL distributions!",
            font_size=44,
            color=BRIGHT_YELLOW,
            weight=BOLD
        )
        message.to_edge(DOWN, buff=0.8)
        
        self.play(Write(message))
        self.wait(2)
        
        message2 = Text(
            "But CLT makes them all approach NORMAL!",
            font_size=44,
            color=BRIGHT_GREEN,
            weight=BOLD
        )
        message2.next_to(message, DOWN, buff=0.3)
        
        self.play(Write(message2))
        self.wait(3)
        
        # Clear for next section
        self.play(
            FadeOut(section_title, *distributions, message, message2)
        )
    
    def create_four_distributions(self):
        """Helper to create 4 different distribution visualizations"""
        dist_data = [
            ("Uniform", "uniform", LEFT * 4.5 + UP * 1, BRIGHT_BLUE),
            ("Exponential", "exponential", RIGHT * 1.5 + UP * 1, BRIGHT_ORANGE),
            ("Bimodal", "bimodal", LEFT * 4.5 + DOWN * 2, BRIGHT_PURPLE),
            ("Right Skewed", "skewed", RIGHT * 1.5 + DOWN * 2, BRIGHT_GREEN),
        ]
        
        distribution_groups = []
        
        for name, dist_type, position, color in dist_data:
            axes = Axes(
                x_range=[0, 10, 2],
                y_range=[0, 1, 0.5],
                x_length=4.5,
                y_length=2.5,
                tips=False,
                axis_config={"color": CLEAR_WHITE, "stroke_width": 2}
            ).move_to(position)
            
            # Generate curve based on type
            if dist_type == "uniform":
                curve = axes.plot(lambda x: 0.5 if 1 < x < 9 else 0, x_range=[0, 10], color=color, stroke_width=4)
            elif dist_type == "exponential":
                curve = axes.plot(lambda x: np.exp(-x/2) if x > 0 else 0, x_range=[0.1, 10], color=color, stroke_width=4)
            elif dist_type == "bimodal":
                curve = axes.plot(
                    lambda x: 0.6 * (np.exp(-((x-3)**2)/1.5) + np.exp(-((x-7)**2)/1.5)),
                    x_range=[0, 10],
                    color=color,
                    stroke_width=4
                )
            else:  # skewed
                curve = axes.plot(lambda x: (10-x)**2/100 if x < 10 else 0, x_range=[0, 10], color=color, stroke_width=4)
            
            label = Text(name, font_size=32, color=color, weight=BOLD)
            label.next_to(axes, DOWN, buff=0.3)
            
            distribution_groups.append(VGroup(axes, curve, label))
        
        return distribution_groups
    

    def galton_board_demo(self):
        """Demonstrate Galton Board (bean machine) - physical CLT demonstration"""
        title = Text(
            "The Galton Board: CLT in Action!",
            font_size=56,
            color=BRIGHT_PINK
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        explanation = Text(
            "Balls falling through pegs create a normal distribution",
            font_size=36,
            color=BRIGHT_YELLOW
        )
        explanation.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(explanation))
        self.wait(1)
        
        # Create Galton Board structure
        board = self.create_galton_board()
        self.play(Create(board), run_time=2)
        self.wait(1)
        
        # Simulate balls falling
        bins = [0] * 15  # 15 bins at bottom
        bin_bars = VGroup()
        
        # Drop 50 balls
        for i in range(50):
            ball_path, final_bin = self.simulate_ball_drop(i)
            bins[final_bin] += 1
            
            ball = Dot(color=BRIGHT_YELLOW, radius=0.08)
            ball.move_to(ball_path[0])
            
            # Animate ball falling
            self.play(
                MoveAlongPath(ball, VMobject().set_points_as_corners(ball_path)),
                run_time=0.3,
                rate_func=linear
            )
            
            # Update histogram
            bin_bars = self.update_histogram(bins, bin_bars)
            
            self.remove(ball)
            
            if i % 10 == 9:  # Pause every 10 balls
                self.wait(0.5)
        
        # Show final distribution
        bell_text = Text(
            "Look! A Bell Curve (Normal Distribution)!",
            font_size=40,
            color=BRIGHT_GREEN,
            weight=BOLD
        )
        bell_text.to_edge(DOWN, buff=0.5)
        self.play(Write(bell_text))
        self.wait(3)
        
        # Clear
        self.play(FadeOut(title, explanation, board, bin_bars, bell_text))
    
    def create_galton_board(self):
        """Create the visual structure of a Galton board"""
        board = VGroup()
        
        # Create pegs in triangular pattern
        rows = 8
        for row in range(rows):
            for col in range(row + 1):
                peg_x = (col - row/2) * 0.6
                peg_y = 2.5 - row * 0.5
                peg = Dot([peg_x, peg_y, 0], color=BRIGHT_BLUE, radius=0.08)
                board.add(peg)
        
        # Add side walls
        left_wall = Line([- 4, 2.5, 0], [-4, -2.5, 0], color=CLEAR_WHITE, stroke_width=3)
        right_wall = Line([4, 2.5, 0], [4, -2.5, 0], color=CLEAR_WHITE, stroke_width=3)
        bottom = Line([-4, -2.5, 0], [4, -2.5, 0], color=CLEAR_WHITE, stroke_width=3)
        
        board.add(left_wall, right_wall, bottom)
        
        # Add bin separators
        for i in range(-7, 8):
            sep = Line([i * 0.5, -2.5, 0], [i * 0.5, -3.5, 0], color=CLEAR_WHITE, stroke_width=1)
            board.add(sep)
        
        return board
    

    def simulate_ball_drop(self, seed):
        """Simulate a ball dropping through the Galton board"""
        np.random.seed(seed)
        path = [[0, 3, 0]]  # Starting position
        
        rows = 8
        x_pos = 0
        
        for row in range(rows):
            # Random left or right
            direction = 1 if np.random.rand() > 0.5 else -1
            x_pos += direction * 0.3
            y_pos = 2.5 - row * 0.5
            path.append([x_pos, y_pos, 0])
        
        # Final position in bin
        final_x = x_pos
        path.append([final_x, -2.5, 0])
        path.append([final_x, -3, 0])
        
        # Determine bin number (0-14)
        bin_num = int((final_x + 3.5) / 0.5)
        bin_num = max(0, min(14, bin_num))
        
        return path, bin_num
    
    def update_histogram(self, bins, old_bars):
        """Update the histogram display at the bottom"""
        self.remove(old_bars)
        new_bars = VGroup()
        
        max_height = max(bins) if max(bins) > 0 else 1
        
        for i, count in enumerate(bins):
            if count > 0:
                bar_height = (count / max_height) * 1.2
                bar = Rectangle(
                    width=0.45,
                    height=bar_height,
                    fill_color=BRIGHT_GREEN,
                    fill_opacity=0.7,
                    stroke_color=BRIGHT_GREEN,
                    stroke_width=2
                )
                bar_x = -3.5 + i * 0.5
                bar.move_to([bar_x, -3 - bar_height/2, 0])
                new_bars.add(bar)
        
        self.add(new_bars)
        return new_bars
    
    def sampling_demonstration(self):
        """Show how we take samples from a population"""
        title = Text(
            "The Sampling Process",
            font_size=56,
            color=BRIGHT_PINK
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        

        # Show population (exponential distribution)
        pop_label = Text(
            "Population (Skewed Distribution)",
            font_size=36,
            color=BRIGHT_BLUE
        )
        pop_label.next_to(title, DOWN, buff=0.5)
        self.play(Write(pop_label))
        
        # Create population distribution
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 1, 0.5],
            x_length=8,
            y_length=3,
            tips=False,
            axis_config={"color": CLEAR_WHITE}
        ).shift(UP * 0.3)
        
        pop_curve = axes.plot(
            lambda x: np.exp(-x/3) if x > 0 else 0,
            x_range=[0.1, 10],
            color=BRIGHT_ORANGE,
            stroke_width=5
        )
        
        self.play(Create(axes), Create(pop_curve), run_time=2)
        self.wait(1)
        
        # Show sampling process
        sample_text = Text(
            "Taking Random Samples...",
            font_size=40,
            color=BRIGHT_YELLOW
        )
        sample_text.to_edge(DOWN, buff=1.5)
        self.play(Write(sample_text))
        
        # Visual sampling - show dots being selected
        for sample_round in range(3):
            dots = VGroup()
            np.random.seed(sample_round)
            
            for _ in range(10):
                x_val = np.random.exponential(3)
                x_val = min(x_val, 10)
                dot = Dot(axes.c2p(x_val, 0), color=BRIGHT_GREEN, radius=0.1)
                dots.add(dot)
            
            self.play(FadeIn(dots, lag_ratio=0.1), run_time=1)
            self.wait(0.5)
            
            # Calculate mean position
            x_vals = [np.random.exponential(3) for _ in range(10)]
            mean_val = np.mean([min(x, 10) for x in x_vals])
            
            mean_line = DashedLine(
                axes.c2p(mean_val, 0),
                axes.c2p(mean_val, 0.8),
                color=BRIGHT_PINK,
                stroke_width=4
            )
            
            mean_label = Text(f"x̄ = {mean_val:.2f}", font_size=28, color=BRIGHT_PINK)
            mean_label.next_to(mean_line, UP, buff=0.1)
            
            self.play(Create(mean_line), Write(mean_label))
            self.wait(0.8)
            self.play(FadeOut(dots, mean_line, mean_label), run_time=0.5)
        
        collect_text = Text(
            "Collect all these sample means...",
            font_size=40,
            color=BRIGHT_GREEN
        )
        collect_text.next_to(sample_text, DOWN, buff=0.3)
        self.play(Write(collect_text))
        self.wait(2)
        
        # Clear
        self.play(FadeOut(title, pop_label, axes, pop_curve, sample_text, collect_text))
    

    def convergence_visual(self):
        """Show convergence to normal as sample size increases"""
        title = Text(
            "As Sample Size Increases...",
            font_size=56,
            color=BRIGHT_PINK
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        subtitle = Text(
            "Watch the distribution transform!",
            font_size=40,
            color=BRIGHT_YELLOW
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))
        
        # Create axes for the histogram
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 0.8, 0.2],
            x_length=10,
            y_length=4.5,
            tips=False,
            axis_config={"color": CLEAR_WHITE}
        ).shift(DOWN * 0.5)
        
        x_label = axes.get_x_axis_label("Sample Mean (x̄)", font_size=32, color=BRIGHT_BLUE)
        y_label = axes.get_y_axis_label("Frequency", font_size=32, color=BRIGHT_BLUE)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Show convergence for n = 2, 5, 10, 30
        sample_sizes = [2, 5, 10, 30]
        colors = [BRIGHT_ORANGE, BRIGHT_PURPLE, BRIGHT_GREEN, BRIGHT_BLUE]
        
        np.random.seed(42)
        
        for n, color in zip(sample_sizes, colors):
            # Generate sample means from exponential distribution
            sample_means = []
            for _ in range(1000):
                sample = np.random.exponential(3, n)
                sample_means.append(np.mean(sample))
            
            # Create histogram
            hist, bin_edges = np.histogram(sample_means, bins=25, range=(0, 10), density=True)
            
            bars = VGroup()
            for i in range(len(hist)):
                if hist[i] > 0:
                    bar_width = bin_edges[i+1] - bin_edges[i]
                    bar_height = hist[i]
                    bar_center = (bin_edges[i] + bin_edges[i+1]) / 2
                    
                    bar = Rectangle(
                        width=bar_width * axes.x_length / 10,
                        height=bar_height * axes.y_length / 0.8,
                        fill_color=color,
                        fill_opacity=0.6,
                        stroke_color=color,
                        stroke_width=2
                    )
                    bar.move_to(axes.c2p(bar_center, bar_height / 2))
                    bars.add(bar)
            
            # Add theoretical normal curve overlay
            mean_theory = 3  # mean of exponential
            std_theory = 3 / np.sqrt(n)  # std of sample mean
            
            normal_curve = axes.plot(
                lambda x: stats.norm.pdf(x, mean_theory, std_theory),
                x_range=[0, 10],
                color=BRIGHT_PINK,
                stroke_width=4
            )
            
            # Label
            n_label = Text(
                f"Sample Size n = {n}",
                font_size=44,
                color=color,
                weight=BOLD
            )
            n_label.to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.5)
            
            # Animate
            self.play(
                Create(bars),
                Create(normal_curve),
                Write(n_label),
                run_time=2
            )
            self.wait(2)
            
            if n < 30:
                self.play(FadeOut(bars, normal_curve, n_label), run_time=0.8)
            else:
                # Keep final one
                final_text = Text(
                    "Perfect Normal Distribution!",
                    font_size=48,
                    color=BRIGHT_GREEN,
                    weight=BOLD
                )
                final_text.to_edge(DOWN, buff=0.8)
                self.play(Write(final_text))
                self.wait(3)
                self.play(FadeOut(bars, normal_curve, n_label, final_text))
        
        # Clear
        self.play(FadeOut(title, subtitle, axes, x_label, y_label))
    

    def mathematical_definition(self):
        """Present the mathematical formulation clearly"""
        title = Text(
            "The Mathematics Behind CLT",
            font_size=56,
            color=BRIGHT_PINK
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)
        
        # Step-by-step build up
        step1 = Text(
            "Given: Random samples from ANY distribution",
            font_size=36,
            color=BRIGHT_YELLOW
        )
        step1.shift(UP * 2)
        self.play(FadeIn(step1, shift=UP))
        self.wait(1.5)
        
        step2 = VGroup(
            Text("With:", font_size=32, color=BRIGHT_GREEN),
            MathTex(r"\text{Mean } \mu", font_size=40, color=CLEAR_WHITE),
            MathTex(r"\text{Standard Deviation } \sigma", font_size=40, color=CLEAR_WHITE),
            MathTex(r"\text{Sample Size } n", font_size=40, color=CLEAR_WHITE)
        ).arrange(DOWN, buff=0.4)
        step2.next_to(step1, DOWN, buff=0.8)
        
        for item in step2:
            self.play(FadeIn(item, shift=UP), run_time=0.8)
        
        self.wait(2)
        
        # Main theorem
        theorem_box = Rectangle(
            width=12,
            height=3.5,
            fill_color="#1a1a1a",
            fill_opacity=0.9,
            stroke_color=BRIGHT_PINK,
            stroke_width=4
        )
        theorem_box.shift(DOWN * 1.5)
        
        theorem_title = Text(
            "Central Limit Theorem:",
            font_size=40,
            color=BRIGHT_PINK,
            weight=BOLD
        )
        theorem_title.next_to(theorem_box, UP, buff=0.2)
        
        main_formula = MathTex(
            r"\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)",
            font_size=72,
            color=BRIGHT_BLUE
        )
        main_formula.move_to(theorem_box.get_center())
        
        or_text = Text("Or equivalently:", font_size=28, color=BRIGHT_GREEN)
        or_text.next_to(main_formula, DOWN, buff=0.5)
        
        z_formula = MathTex(
            r"Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim \mathcal{N}(0,1)",
            font_size=48,
            color=BRIGHT_YELLOW
        )
        z_formula.next_to(or_text, DOWN, buff=0.3)
        
        self.play(Create(theorem_box))
        self.play(Write(theorem_title))
        self.play(Write(main_formula), run_time=2)
        self.wait(2)
        
        self.play(Write(or_text))
        self.play(Write(z_formula), run_time=1.5)
        self.wait(3)
        
        # Clear
        self.play(FadeOut(
            title, step1, step2, theorem_box, theorem_title,
            main_formula, or_text, z_formula
        ))
    

    def real_examples(self):
        """Show practical examples with visual solutions"""
        title = Text(
            "Real-World Example",
            font_size=56,
            color=BRIGHT_PINK
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # Example problem
        problem = VGroup(
            Text("Manufacturing Quality Control:", font_size=40, color=BRIGHT_BLUE, weight=BOLD),
            Text("", font_size=2),  # spacer
            Text("Bolt diameter: μ = 10mm, σ = 0.5mm", font_size=32, color=CLEAR_WHITE),
            Text("Sample of n = 25 bolts", font_size=32, color=CLEAR_WHITE),
            Text("", font_size=2),  # spacer
            Text("Question: P(9.9mm < x̄ < 10.1mm) = ?", font_size=36, color=BRIGHT_YELLOW, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        problem.next_to(title, DOWN, buff=0.6)
        
        for line in problem:
            if line.height > 0.1:  # skip spacers
                self.play(FadeIn(line, shift=UP), run_time=0.8)
        
        self.wait(2)
        
        # Solution
        solution_title = Text("Solution:", font_size=40, color=BRIGHT_GREEN, weight=BOLD)
        solution_title.to_edge(LEFT, buff=1).shift(DOWN * 0.5)
        self.play(Write(solution_title))
        
        # Step 1
        step1 = VGroup(
            Text("1. Calculate Standard Error:", font_size=32, color=BRIGHT_YELLOW),
            MathTex(r"SE = \frac{\sigma}{\sqrt{n}} = \frac{0.5}{\sqrt{25}} = \frac{0.5}{5} = 0.1 \text{ mm}",
                   font_size=36, color=CLEAR_WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        step1.next_to(solution_title, DOWN, aligned_edge=LEFT, buff=0.4)
        
        for item in step1:
            self.play(Write(item), run_time=1.2)
        
        self.wait(2)
        
        # Step 2
        step2 = VGroup(
            Text("2. Convert to Z-scores:", font_size=32, color=BRIGHT_YELLOW),
            MathTex(r"Z_1 = \frac{9.9-10}{0.1} = -1", font_size=36, color=CLEAR_WHITE),
            MathTex(r"Z_2 = \frac{10.1-10}{0.1} = +1", font_size=36, color=CLEAR_WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        step2.next_to(step1, DOWN, aligned_edge=LEFT, buff=0.5)
        
        for item in step2:
            self.play(Write(item), run_time=1.2)
        
        self.wait(2)
        
        self.play(FadeOut(problem, solution_title, step1, step2))
        
        # Visual representation
        title2 = Text("Visual Solution:", font_size=48, color=BRIGHT_PINK)
        title2.to_edge(UP, buff=0.5)
        self.play(Transform(title, title2))
        
        # Draw normal distribution
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 0.5, 0.1],
            x_length=10,
            y_length=4,
            tips=False,
            axis_config={"color": CLEAR_WHITE}
        ).shift(DOWN * 0.5)
        
        curve = axes.plot(
            lambda x: stats.norm.pdf(x, 0, 1),
            x_range=[-3, 3],
            color=BRIGHT_BLUE,
            stroke_width=4
        )
        
        self.play(Create(axes), Create(curve), run_time=2)
        
        # Shade the region between -1 and 1
        shaded_area = axes.get_area(
            curve,
            x_range=[-1, 1],
            color=BRIGHT_GREEN,
            opacity=0.6
        )
        
        # Add vertical lines
        left_line = DashedLine(
            axes.c2p(-1, 0),
            axes.c2p(-1, stats.norm.pdf(-1)),
            color=BRIGHT_YELLOW,
            stroke_width=4
        )
        right_line = DashedLine(
            axes.c2p(1, 0),
            axes.c2p(1, stats.norm.pdf(1)),
            color=BRIGHT_YELLOW,
            stroke_width=4
        )
        
        left_label = MathTex("Z=-1", font_size=36, color=BRIGHT_YELLOW)
        left_label.next_to(left_line, DOWN, buff=0.2)
        
        right_label = MathTex("Z=+1", font_size=36, color=BRIGHT_YELLOW)
        right_label.next_to(right_line, DOWN, buff=0.2)
        
        self.play(
            FadeIn(shaded_area),
            Create(left_line),
            Create(right_line),
            Write(left_label),
            Write(right_label),
            run_time=2
        )
        
        # Answer
        answer = VGroup(
            Text("Answer:", font_size=40, color=BRIGHT_PINK, weight=BOLD),
            Text("P(-1 < Z < 1) = 68.26%", font_size=48, color=BRIGHT_GREEN, weight=BOLD),
            Text("(This is the 68% rule!)", font_size=32, color=BRIGHT_YELLOW)
        ).arrange(DOWN, buff=0.3)
        answer.to_edge(DOWN, buff=0.5)
        
        answer_box = SurroundingRectangle(answer, color=BRIGHT_PINK, buff=0.4, corner_radius=0.2)
        
        self.play(Create(answer_box), Write(answer), run_time=2)
        self.wait(4)
        
        # Clear
        self.play(FadeOut(
            title, axes, curve, shaded_area,
            left_line, right_line, left_label, right_label,
            answer, answer_box
        ))
    

    def conclusion(self):
        """Wrap up with key takeaways"""
        title = Text(
            "Key Takeaways",
            font_size=60,
            color=BRIGHT_PINK,
            weight=BOLD
        )
        title.to_edge(UP, buff=0.6)
        self.play(Write(title))
        self.wait(1)
        
        # List of key points
        points = [
            ("1", "Works for ANY distribution (uniform, skewed, bimodal, etc.)", BRIGHT_BLUE),
            ("2", "Sample means form a normal distribution", BRIGHT_GREEN),
            ("3", "Larger n → narrower, more precise distribution", BRIGHT_YELLOW),
            ("4", "Rule of thumb: n ≥ 30 is sufficient", BRIGHT_ORANGE),
            ("5", "Foundation of hypothesis testing & confidence intervals", BRIGHT_PURPLE),
        ]
        
        point_group = VGroup()
        for num, text, color in points:
            num_text = Text(num + ".", font_size=38, color=color, weight=BOLD)
            content = Text(text, font_size=32, color=CLEAR_WHITE)
            content.next_to(num_text, RIGHT, buff=0.4)
            row = VGroup(num_text, content)
            point_group.add(row)
        
        point_group.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        point_group.next_to(title, DOWN, buff=0.8)
        
        for point in point_group:
            self.play(FadeIn(point, shift=RIGHT), run_time=1)
            self.wait(0.5)
        
        self.wait(2)
        
        # Final message
        final = VGroup(
            Text("The Central Limit Theorem:", font_size=48, color=BRIGHT_PINK, weight=BOLD),
            Text("The reason we can use normal distribution", font_size=40, color=BRIGHT_YELLOW),
            Text("even when our data isn't normal!", font_size=40, color=BRIGHT_YELLOW)
        ).arrange(DOWN, buff=0.3)
        final.to_edge(DOWN, buff=1)
        
        final_box = SurroundingRectangle(final, color=BRIGHT_BLUE, buff=0.5, corner_radius=0.2)
        
        self.play(Create(final_box), Write(final), run_time=2)
        self.wait(3)
        
        # Thank you
        thanks = Text(
            "Thank You!",
            font_size=80,
            color=BRIGHT_PINK,
            weight=BOLD
        )
        
        self.play(
            FadeOut(title, point_group, final, final_box),
            run_time=1
        )
        
        self.play(Write(thanks), run_time=2)
        self.wait(3)
        self.play(FadeOut(thanks))


# Additional helper scene for testing specific parts
class TestGaltonBoard(Scene):
    """Test just the Galton board section"""
    def construct(self):
        demo = CompleteCLTVisualization()
        demo.galton_board_demo()


class TestConvergence(Scene):
    """Test just the convergence visualization"""
    def construct(self):
        demo = CompleteCLTVisualization()
        demo.convergence_visual()

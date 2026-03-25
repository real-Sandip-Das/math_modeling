from manim import *

# ==========================================================
# SLIDE SHOW 1: GENERAL STABILITY ANALYSIS
# ==========================================================
class GeneralStabilityAnalysis(Scene):
    def construct(self):
        # --- Slide 1: Introduction ---
        title = Title("Stability Analysis of Reaction-Diffusion Systems")
        general_system = MathTex(
            r"\frac{\partial u}{\partial t} = D_u \nabla^2 u + f(u, v)",
            r"\\ \frac{\partial v}{\partial t} = D_v \nabla^2 v + g(u, v)"
        ).shift(UP * 0.5)

        intro_text = Text("Assume a homogeneous steady state (u*, v*)", font_size=24).next_to(general_system, DOWN)
        
        self.play(Write(title))
        self.play(Write(general_system))
        self.play(FadeIn(intro_text))
        self.wait(2)
        self.play(FadeOut(general_system), FadeOut(intro_text))

        # --- Slide 2: Linearization ---
        subtitle1 = Text("1. Linearization around (u*, v*)", font_size=30).to_edge(UP).shift(DOWN * 0.8)
        perturbation = MathTex(r"\mathbf{w} = \begin{pmatrix} u-u^* \\ v-v^* \end{pmatrix} \propto e^{\lambda t} e^{i \mathbf{k} \cdot \mathbf{r}}")
        linear_eq = MathTex(r"\frac{\partial \mathbf{w}}{\partial t} = D \nabla^2 \mathbf{w} + J\mathbf{w}")
        jacobian = MathTex(r"J = \begin{pmatrix} f_u & f_v \\ g_u & g_v \end{pmatrix}, \quad D = \begin{pmatrix} D_u & 0 \\ 0 & D_v \end{pmatrix}")
        
        VGroup(perturbation, linear_eq, jacobian).arrange(DOWN, buff=0.5).next_to(subtitle1, DOWN)
        
        self.play(Write(subtitle1))
        self.play(Write(perturbation))
        self.play(Write(linear_eq))
        self.play(Write(jacobian))
        self.wait(3)
        self.play(*[FadeOut(obj) for obj in [subtitle1, perturbation, linear_eq]])

        # --- Slide 3: Pure Kinetic Stability ---
        subtitle2 = Text("2. Stability in Absence of Diffusion (k=0)", font_size=30).to_edge(UP).shift(DOWN * 0.8)
        cond_k0 = MathTex(
            r"\text{tr}(J) = f_u + g_v < 0",
            r"\\ \det(J) = f_u g_v - f_v g_u > 0"
        ).next_to(subtitle2, DOWN, buff=1)
        
        self.play(Write(subtitle2))
        self.play(Write(cond_k0))
        self.wait(2)
        self.play(FadeOut(subtitle2), FadeOut(cond_k0), FadeOut(jacobian))

        # --- Slide 4: Deriving the Dispersion Relation (Logic Flow) ---
        subtitle3 = Text("3. Diffusive Instability (k > 0)", font_size=30).to_edge(UP).shift(DOWN * 0.8)
        self.play(Write(subtitle3))

        # Define M
        m_def = MathTex(r"\text{Let } M = J - k^2 D = \begin{pmatrix} f_u - k^2 D_u & f_v \\ g_u & g_v - k^2 D_v \end{pmatrix}").scale(0.8).next_to(subtitle3, DOWN, buff=0.4)
        char_eq = MathTex(r"\det(\lambda I - M) = 0").next_to(m_def, DOWN, buff=0.4)
        
        self.play(Write(m_def))
        self.wait(1)
        self.play(Write(char_eq))
        self.wait(1)

        # Expansion
        poly = MathTex(r"\lambda^2 - \text{tr}(M)\lambda + \det(M) = 0").scale(0.8).next_to(char_eq, DOWN, buff=0.4)
        det_m_derivation = MathTex(r"H(k^2) \equiv \det(M) = (f_u - k^2 D_u)(g_v - k^2 D_v) - f_v g_u").scale(0.7).next_to(poly, DOWN, buff=0.4)
        
        self.play(Write(poly))
        self.play(Write(det_m_derivation))
        self.wait(2)

        # Final H(k^2) expression
        h_final = MathTex(r"H(k^2) = D_u D_v k^4 - (D_v f_u + D_u g_v) k^2 + \det(J)").set_color(BLUE).scale(0.9).next_to(poly, DOWN, buff=0.5)
        
        self.play(ReplacementTransform(det_m_derivation, h_final))
        self.wait(3)

        # --- Cleanup Slide 4 while keeping h_final ---
        self.play(FadeOut(m_def), FadeOut(char_eq), FadeOut(poly), FadeOut(subtitle3))

        # --- Slide 5: Turing Conditions (Persistence & Derivation) ---
        subtitle4 = Text("4. Conditions for Instability", font_size=30).to_edge(UP).shift(DOWN * 0.8)
        # Re-positioning for clarity
        self.play(
            Write(subtitle4),
            h_final.animate.next_to(subtitle4, DOWN, buff=0.4)
        )

        # Condition 3 Derivation
        logic1 = Text("For instability, we need H(k²) < 0 for some k² > 0.", font_size=18).next_to(h_final, DOWN, buff=0.3)
        cond3_txt = Text("Since det(J) > 0, the coefficient of k² must be positive:", font_size=18).next_to(logic1, DOWN, buff=0.4)
        cond3 = MathTex(r"D_v f_u + D_u g_v > 0").set_color(GREEN).next_to(cond3_txt, DOWN)

        self.play(Write(logic1))
        self.play(Write(cond3_txt))
        self.play(Write(cond3))
        self.wait(2)

        # Condition 4 Derivation
        cond4_txt = Text("To ensure the minimum of the parabola H(k²) is negative:", font_size=18).next_to(cond3, DOWN, buff=0.4)
        cond4_min = MathTex(r"H_{min} < 0 \iff (D_v f_u + D_u g_v)^2 - 4 D_u D_v \det(J) > 0").scale(0.7).next_to(cond4_txt, DOWN)
        cond4 = MathTex(r"(D_v f_u + D_u g_v)^2 > 4 D_u D_v \det(J)").set_color(GREEN).next_to(cond4_min, DOWN)

        self.play(Write(cond4_txt))
        self.play(Write(cond4_min))
        self.play(Write(cond4))
        self.wait(5)


# ==========================================================
# SLIDE SHOW 2: SCHNAKENBERG MODEL
# ==========================================================
class SchnakenbergStudy(Scene):
    def construct(self):
        model_title1 = Title("Case Study: Schnakenberg Model")
        kinetics1 = MathTex(r"f(u,v) = a-u+u^2v, \quad g(u,v)=b-u^2v").shift(UP*1.5)
        ss1 = MathTex(r"u^* = a+b, \quad v^* = \frac{b}{(a+b)^2}").next_to(kinetics1, DOWN)
        
        jac1 = MathTex(r"J = \begin{pmatrix} \frac{b-a}{a+b} & (a+b)^2 \\ \frac{-2b}{a+b} & -(a+b)^2 \end{pmatrix}")
        jac_label = Text("Jacobian at Steady State:", font_size=24).next_to(jac1, UP)
        
        self.play(Write(model_title1))
        self.play(Write(kinetics1))
        self.play(Write(ss1))
        self.wait(2)
        self.play(Write(jac_label), Write(jac1))
        
        # Demonstrating stability check
        trace_check = MathTex(r"\text{tr}(J) = \frac{b-a}{a+b} - (a+b)^2 < 0 \implies (a+b)^3 > b-a").scale(0.8).to_edge(DOWN).shift(UP*0.5)
        self.play(Write(trace_check))
        self.wait(4)

# ==========================================================
# SLIDE SHOW 3: GRAY-SCOTT MODEL
# ==========================================================
class GrayScottStudy(Scene):
    def construct(self):
        model_title2 = Title("Case Study: Gray-Scott Model")
        kinetics2 = MathTex(r"f = F(1-u)-uv^2", r"\\ g = uv^2-(F+k)v").shift(UP*1.5)
        
        jac2 = MathTex(r"J = \begin{pmatrix} -F - v^2 & -2uv \\ v^2 & 2uv - (F+k) \end{pmatrix}")
        gs_note = Text("Parameter Space (F, k) determines morphology", font_size=24, color=BLUE).next_to(jac2, DOWN, buff=1)
        
        self.play(Write(model_title2))
        self.play(Write(kinetics2))
        self.wait(1)
        self.play(Write(jac2))
        self.play(Write(gs_note))
        
        final_text = Text("Patterns: Spots, Stripes, and Labyrinthine structures", font_size=24).to_edge(DOWN)
        self.play(FadeIn(final_text))
        self.wait(4)
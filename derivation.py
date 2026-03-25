from manim import *

class TuringPatternDerivation(Scene):
    def construct(self):
        # --- Slide 1: Introduction ---
        title = Title("Stability Analysis of Reaction-Diffusion Systems").to_edge(UP)
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
        self.play(*[FadeOut(obj) for obj in [subtitle1, perturbation, linear_eq, jacobian]])

        # --- Slide 3: Pure Kinetic Stability ---
        subtitle2 = Text("2. Stability in Absence of Diffusion (k=0)", font_size=30).to_edge(UP).shift(DOWN * 0.8)
        cond_k0 = MathTex(
            r"\text{tr}(J) = f_u + g_v < 0",
            r"\\ \det(J) = f_u g_v - f_v g_u > 0"
        ).next_to(subtitle2, DOWN, buff=1)
        
        self.play(Write(subtitle2))
        self.play(Write(cond_k0))
        self.wait(2)
        self.play(FadeOut(subtitle2), FadeOut(cond_k0))

        # --- Slide 4: The Dispersion Relation ---
        subtitle3 = Text("3. Diffusive Instability (k > 0)", font_size=30).to_edge(UP).shift(DOWN * 0.8)
        char_eq = MathTex(r"\det(\lambda I - J + k^2 D) = 0")
        poly = MathTex(r"\lambda^2 - \text{tr}(M)\lambda + \det(M) = 0")
        det_m = MathTex(r"H(k^2) = D_u D_v k^4 - (D_v f_u + D_u g_v) k^2 + \det(J)")
        
        VGroup(char_eq, poly, det_m).arrange(DOWN, buff=0.5).next_to(subtitle3, DOWN)
        
        self.play(Write(subtitle3))
        self.play(Write(char_eq))
        self.play(Write(poly))
        self.play(Write(det_m))
        self.wait(3)
        self.play(*[FadeOut(obj) for obj in [subtitle3, char_eq, poly, det_m]])

        # --- Slide 5: Turing Conditions Summary ---
        subtitle4 = Text("Turing Instability Conditions", font_size=30).to_edge(UP).shift(DOWN * 0.8)
        final_conds = MathTex(
            r"\begin{aligned} "
            r"&1. \quad f_u + g_v < 0 \\ "
            r"&2. \quad f_u g_v - f_v g_u > 0 \\ "
            r"&3. \quad D_v f_u + D_u g_v > 0 \\ "
            r"&4. \quad (D_v f_u + D_u g_v)^2 > 4 D_u D_v \det(J) "
            r"\end{aligned}"
        ).next_to(subtitle4, DOWN, buff=0.5)
        
        rect = SurroundingRectangle(final_conds, color=YELLOW)
        
        self.play(Write(subtitle4))
        self.play(Write(final_conds))
        self.play(Create(rect))
        self.wait(4)
        self.play(FadeOut(subtitle4), FadeOut(final_conds), FadeOut(rect), FadeOut(title))

        # --- Slide 6: Schnakenberg Model ---
        model_title1 = Title("Case Study: Schnakenberg Model")
        kinetics1 = MathTex(r"f = a-u+u^2v, \quad g=b-u^2v")
        ss1 = MathTex(r"u^* = a+b, \quad v^* = \frac{b}{(a+b)^2}")
        jac1 = MathTex(r"J = \begin{pmatrix} \frac{b-a}{a+b} & (a+b)^2 \\ \frac{-2b}{a+b} & -(a+b)^2 \end{pmatrix}")
        
        VGroup(kinetics1, ss1, jac1).arrange(DOWN, buff=0.5).next_to(model_title1, DOWN)
        
        self.play(Write(model_title1))
        self.play(Write(kinetics1))
        self.play(Write(ss1))
        self.play(Write(jac1))
        self.wait(3)
        self.play(FadeOut(model_title1), FadeOut(kinetics1), FadeOut(ss1), FadeOut(jac1))

        # --- Slide 7: Gray-Scott Model ---
        model_title2 = Title("Case Study: Gray-Scott Model")
        kinetics2 = MathTex(r"f = F(1-u)-uv^2", r"\\ g = uv^2-(F+k)v")
        jac2 = MathTex(r"J = \begin{pmatrix} -F - v^2 & -2uv \\ v^2 & 2uv - (F+k) \end{pmatrix}")
        gs_note = Text("Patterns: Spots, Stripes, Mitosis", font_size=24, color=BLUE).next_to(jac2, DOWN)
        
        VGroup(kinetics2, jac2).arrange(DOWN, buff=0.5).next_to(model_title2, DOWN)
        
        self.play(Write(model_title2))
        self.play(Write(kinetics2))
        self.play(Write(jac2))
        self.play(Write(gs_note))
        self.wait(4)
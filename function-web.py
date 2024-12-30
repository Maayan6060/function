import streamlit as st
import sympy as s
from sympy import symbols, S, oo, limit
from sympy.calculus.util import continuous_domain

class AnalyzeApp:
    def __init__(self):
        self.x = s.symbols('x')

    def definition(self):
        y = self.input_text
        yf = s.sympify(y)
        D = continuous_domain(yf, self.x, S.Reals)
        st.write("The field of definition:", D)
        self.vertical_asymptote(yf, D, self.x)

    def vertical_asymptote(self, yf, D, x):
        va = []
        undefined = S.Reals - D
        for i in undefined:
            lim_left = i - (1e-15)
            lim_right = i + (1e-15)
            lim_left_val = yf.subs(x, lim_left)
            lim_right_val = yf.subs(x, lim_right)
            if abs(lim_left_val) > 1e6 or abs(lim_right_val) > 1e6:
                va.append(i)
        st.write("Vertical asymptotes:", va)
        self.horizontal_asymptote(yf, D, x)

    def horizontal_asymptote(self, yf, D, x):
        st.write("Horizontal asymptotes")
        oo_limit = limit(yf, x, oo)
        negative_oo_limit = limit(yf, x, -oo)
        st.write(f"Limit as x approaches infinity: {oo_limit}")
        st.write(f"Limit as x approaches negative infinity: {negative_oo_limit}")

    def run(self):
        st.title("Function Analyzing App")
        self.input_text = st.text_input("Enter a function:", "")
        if st.button("Next"):
            self.definition()

# Run the app
if __name__ == '__main__':
    app = AnalyzeApp()
    app.run()

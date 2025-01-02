import streamlit as st
import sympy as s
from sympy import symbols, S, oo, limit
from sympy.calculus.util import continuous_domain
import numpy as np

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
        st.write("Vertical asymptotes: "+"x=",str(va))
        self.horizontal_asymptote(yf, D, x)

    def horizontal_asymptote(self, yf, D, x):
        oo_limit = limit(yf, x, oo)
        st.write("Horizontal asymptotes: "+"y=",str(oo_limit))
        self.xyi(x,yf,D)
    def xyi(self,x,yf,D):
        xi=s.Eq(yf,0)
        xix=s.solve(xi,x)
        for i in range(len(xix)):
         xix[i]="("+str(xix[i])+",0)"
        yi=yf.subs(x,0)
        if s.S.Zero in D:
         yi="(0,"+str(yi)+")"
         xix.append(str(yi))
        st.write("Intersection with the axes: ", str(xix))

    def run(self):
        st.title("Function Analyzing App")
        self.input_text = st.text_input("Enter a function:", "")
        if st.button("Next"):
            self.definition()

# Run the app
if __name__ == '__main__':
    app = AnalyzeApp()
    app.run()

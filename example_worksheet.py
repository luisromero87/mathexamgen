from examgen import worksheet, make_quotient_rule_prob, make_int_poly_prob, make_int_pow_prob, make_int_sust_prob

# make an exam with a filename and title
myexam = worksheet("worksheet", "Example Worksheet 1", savetex=True)

# add some problem sections 
myexam.add_section("Linear equations", 20, "Linear equations",
                   "Solve the following equations for the specified variable.")
myexam.add_section("Quadratic equations", 20, "Quadratic equations",
                   "Solve the following quadratic equations.")
myexam.add_section(make_quotient_rule_prob,10, "Differentiation", 
                  "Compute each derivative", var=["x", "y", "z"])
myexam.add_section(make_int_poly_prob,10, "Compute the integral",
                  "Compute the integral of the polynomials.", var=[ "y", "z"], order=[1,2,3,4])
myexam.add_section(make_int_pow_prob,10, "Compute the integral",
                  "Compute the integral of the powers.", var=[ "y", "z"], order=[2,3,4,5])
myexam.add_section(make_int_sust_prob,10, "Compute the integral",
                  "Compute the integral of the powers.", var=[ "y", "z"])
# generate the exam and solutions pdf
myexam.write()
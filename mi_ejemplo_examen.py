from examgen import worksheet, exam, make_quotient_rule_prob, make_quadratic_eq

# make an exam with a filename and title
myexam = exam("Mi_examan", "Mi examen de prueba", savetex=False)

# add some problem sections
myexam.add_problem(make_quadratic_eq, "Encuentra todas las soluciones", kwargs={"var": "x", "integer" : 1})


# generate the exam and solutions pdf
myexam.write()

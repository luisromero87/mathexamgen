from examgen import worksheet, exam, make_quotient_rule_prob, make_quadratic_eq

# make an exam with a filename and title
myexam = exam("Mi_examen", "Mi examen de prueba", savetex=0)

# add some problem sections
myexam.add_problem(make_quadratic_eq, "Encuentra todas las soluciones", kwargs={"var": "x", "integer" : 1})
myexam.add_problem(make_quadratic_eq, "Encuentra todas las soluciones", kwargs={"var": ["x","z"], "integer" : 0})
myexam.add_problem(make_quadratic_eq, "Encuentra todas las soluciones", kwargs={"var": ["x","w"], "integer" : 0})


# generate the exam and solutions pdf
myexam.write()

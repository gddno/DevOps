def print_models(unprinted_design, complated_models):
    
    while unprinted_design:
	    current_design = unprinted_design.pop()
	    print("Printed model: " + current_design)
	    complated_models.append(current_design)

def show_complated_models(complated_models):
    print("\nThe following model have been printed: ")
    for model in complate_models:
	    print(model)

def show_original_list(unprinted_design):
    print("\nOriginal list: ")
    for design in unprinted_design:
	    print(design)


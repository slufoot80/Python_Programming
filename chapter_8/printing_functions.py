def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
	current_design = current_design.title()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        #completed_models.append(current_design)
        

def show_completed_models(completed_models):
        """Show all models that were printed"""
        print("\nThe following models have been printed")
        for completed_model in completed_models:
            completed_model = completed_model.title()
            print("Completed Models: " + completed_model)

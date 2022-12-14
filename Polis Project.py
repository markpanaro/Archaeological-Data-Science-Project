import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

# takes category column and list of categories to sort by
def categorize_data(to_categorize, categories):
    for i, entry in enumerate(to_categorize):
        
        # Check for item within entry and replace with proper category if found
        for j, item in enumerate(categories):
            if item in entry:
                to_categorize[i] = (categories[j])
        
        # If entry is not an existing category, replace with other
        if to_categorize[i] not in categories:
            to_categorize[i] = "Other"
        
    return to_categorize

def create_pie(data, title):
    categories = data.value_counts()
    labels = data.value_counts().index.tolist()

    plt.pie(categories, labels = labels)
    plt.title(title)
    plt.show()

def create_bar(data, title):
    categories = data.value_counts()
    labels = data.value_counts().index.tolist()

    plt.bar(labels, categories)
    plt.title(title)
    plt.show()

# takes a data set, context column, context, category column, and title
def graph_per_context(data_set, context, specific_context, column, title):
    context_matrix = context == specific_context
    context_data = data_set[context_matrix]
    create_pie(context_data[column], title + specific_context)
    create_bar(context_data[column], title + specific_context)

# takes a data set, column, constraint series, string for category, and optimal/list flag
def find_context(data_set, context_input, constraints, which_type, flag):
    context_list = context_input.unique()
    constraint_category = constraints.keys()

    context_meets_reqs = []
    optimal = ""
    optimal_count = 0

    # Sum counts of categories relevant to constraints
    for context in context_list:
        context_matrix = context_input == context
        context_data = data_set[context_matrix]
        context_data_counts = context_data[which_type].value_counts()

        constraints_met = 0

        # Iterate all contexts, apply mask to check constraints
        for item in constraint_category:
            if item not in context_data_counts:
                break
            if context_data_counts[item] >= constraints[item]:
                constraints_met+=1
            else:
                break
        # Append to return list only if all constraints are met
        if constraints_met == len(constraints):
            context_meets_reqs.append(context)
            if len(context_data) >= optimal_count:
                optimal = context
                optimal_count = len(context_data)
    if flag:
        return context_meets_reqs
    else:
        return optimal

# takes data set, context column, category column, category, bin list, and title
def histogram(data_set, contexts, category_type, category,bins, title):
    context_list = contexts.unique()

    cat_count = []

    for context in context_list:
        
        context_matrix = contexts == context
        context_data = data_set[context_matrix]
        context_data_counts = context_data[category_type].value_counts()

        if category not in context_data_counts:
            cat_count.append(0)
        else:
            cat_count.append(context_data_counts[category])
    
    plt.hist(cat_count,bins)
    plt.title(title)
    plt.show()

# takes data set, context column, category column, categories list, display limits, and title
def regression_line(data_set, contexts, category_type, categories, x_y_limits, title):
    context_list = contexts.unique()

    cat_one = []  
    cat_two = []

    for context in context_list:

        context_matrix = contexts == context
        context_data = data_set[context_matrix]
        context_data_counts = context_data[category_type].value_counts()

        if categories[0] not in context_data_counts:
            cat_one.append(0)
        else:
            cat_one.append(context_data_counts[categories[0]])

        if categories[1] not in context_data_counts:
            cat_two.append(0)
        else:
            cat_two.append(context_data_counts[categories[1]])

    regr_results = sp.stats.linregress(cat_one,cat_two)

    abline_values = [regr_results.slope * i + regr_results.intercept for i in cat_one]
    plt.xlim(0,x_y_limits)
    plt.ylim(0,x_y_limits)
    plt.scatter(cat_one,cat_two,regr_results.intercept)
    plt.plot(cat_one,abline_values, 'b')
    plt.title(title)
    plt.show()


def main():

    # import data
    d1 = pd.read_csv("Polis Data.csv")
    PolisData = pd.DataFrame(d1)
    PolisClean = PolisData[["Material category", "Material type (from notes)", "Object", "Context (3)", "Part width (Note)", "Part thickness (Note)", "Part height (Note)", "Part length (Note)"]]
    PolisClean = PolisClean.rename(columns={'Material category': 'material_category', 'Material type (from notes)': 'material_type', 'Context (3)': 'context_three', 'Part width (Note)': 'part_width', 'Part thickness (Note)': 'part_thickness', 'Part height (Note)': 'part_height', 'Part length (Note)': 'part_length'})

    # Clean and Visualize Artifact Material Categories
    PolisClean['material_category'] = PolisClean['material_category'].fillna("Other")
    cat_list = PolisClean.loc[:,"material_category"].values.tolist()
    new_mat_cat = categorize_data(cat_list,["Architectural Misc", "Architectural Stone", "Architectural Terracotta", "Bone, Ivory, Shell", "Bronze", "Glass", "Iron", "Miscellaneous Ceramic", "Mosaic Tesserae", "Numismatics", "Organic", "Pottery", "Slag", "Stone Objects", "Terracotta Figurines", "Terracotta Lamps"])
    PolisClean['material_category'] = new_mat_cat

    create_pie(PolisClean['material_category'], "Polis Material Categories")

    # Clean and Visualize Artifact Material Types
    PolisClean['material_type'] = PolisClean['material_type'].fillna("Other")
    type_list = PolisClean.loc[:,"material_type"].values.tolist()
    new_type_cat = categorize_data(type_list, ["Terracotta", "Bone", "Carbon", "Bronze", "Ceramic", "Charcoal", "Clay", "Copper", "Glass", "Iron", "Limestone", "Marble", "Metal", "Plaster", "Shell", "Slag", "Stone"])
    PolisClean['material_type'] = new_type_cat

    create_pie(PolisClean['material_type'], "Polis Material Types")

    # Export cleaned data to csv
    # PolisClean.to_csv('Polis Clean.csv')

    # Visualize Material Types per Context
    graph_per_context(PolisClean, PolisClean['context_three'], 'B.D7:t19-2000', "material_type", "Material Types of Context ")

    # Test find_context
    constraints = {'Slag': 70, 'Plaster': 15, 'Charcoal': 50}
    find_context_demo = find_context(PolisClean, PolisClean["context_three"], constraints, 'material_type', 1)
    find_context_demo_optimal = find_context(PolisClean, PolisClean["context_three"], constraints, 'material_type', 0)

    # Display results for find_context demo
    print("List of Contexts Satisfying Constraints:")
    print(find_context_demo)
    print("Optimal Context:")
    print(find_context_demo_optimal)
    # code to display counts to verify above demo:
    # context_matrix = PolisClean['context_three'] == 'E.G0:D09.1997'
    # context_data = PolisClean[context_matrix]
    # context_data_counts = context_data['material_type'].value_counts()
    # print(context_data_counts)

    # create histogram of terracotta across the site
    histogram(PolisClean, PolisClean["context_three"], "material_type", "Terracotta", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Histogram of Terracotta Across Polis")

    # create regression line of charcoal and slag
    regression_line(PolisClean, PolisClean["context_three"], 'material_type', ["Charcoal", "Slag"], 30, "Regression Line of Charcoal and Slag")

main()
    
from django.shortcuts import render

DATA = {
	'omlet': {
		'яйца, шт'  : 2,
		'молоко, л' : 0.1,
		'соль, ч.л.': 0.5,
	},
	'pasta': {
		'макароны, г': 0.3,
		'сыр, г'     : 0.05,
	},
	'buter': {
		'хлеб, ломтик'   : 1,
		'колбаса, ломтик': 1,
		'сыр, ломтик'    : 1,
		'помидор, ломтик': 1,
	},
}


def recipe(request, name):
	context = {
		'recipe': {}
	}
	if request.GET.get('servings'):
		servings = int(request.GET.get('servings'))
		print(servings)
		for ingredient, amount in DATA[name].items():
			context['recipe'][ingredient] = amount * servings
		print(context)
	else:
		for ingredient, amount in DATA[name].items():
			context['recipe'][ingredient] = amount
	return render(request, 'calculator/index.html', context)
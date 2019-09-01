def getUniqueMeals(meals):
    aset = set([])
    for ele in meals:
      vals = ele.values()
      ans = ''
      for val in vals:
          val = sorted(val)
          print(val)
          for ingre in val:
              ans += ingre
      aset.add(ans)
    return len(aset)


def getUniqueMeals(meals):
    mealsDict = {}
   #sort ingredient in a meal
    for meal in meals:
        meal.ingredients.sort()
        #concatenate all ingredients to become a string
        mealKey = ""
        for ingredient in meal.ingredients:
            mealKey += ingredient
        mealsDict[mealKey] = 0

    return len(mealsDict)

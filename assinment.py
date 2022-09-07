from warnings import catch_warnings


human_age = float(input('enter your age:'))
dog_age = human_age * 7
dog_years = dog_age // 1
dog_month = ((dog_age % 1) *12) //1
dog_days = (((((dog_age % 1) *12) //1) *30) //1)
print("you're age in dog years is", dog_years, "years", dog_month, "months",dog_days,"days")

#for cat age 
cat_age = human_age * 9
cat_years = cat_age // 1
cat_months = ((cat_years % 1) *12) //1
cat_days = (((((cat_age % 1) * 12) % 1) * 30) //1)
print("your age in cat yeras is ",cat_years, cat_years,"years",cat_months, "months", cat_days,"days")



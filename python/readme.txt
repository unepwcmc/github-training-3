Aim: example scripts to demonstrate GitHub's fabulousness. 

The two scripts do the same thing in different languages (R and Python).

They join two dataframes (attribute tables) together based on a common column

In this example, you can change from an inner join to outer join:
-in R, change the "all" parameter in the merge function to equal TRUE.
-in Python, change the "how" parameter in the merge function to equal "outer".

This is relevant for quality checking if you were using a larger dataset.
You can highlight rows that didn't join by looking for Nulls/NaNs.
Extra lines of code could then be added to only highlight the missing rows.


Aim: example scripts to demonstrate GitHub's fabulousness. 

This script joins two dataframes (attribute tables) together based on a common column

In this example, you can change from an inner join to outer join:
1. change the "all" parameter in the merge function to equal TRUE.

This is relevant for quality checking if you were using a larger dataset.
You can highlight rows that didn't join by looking for Nulls/NaNs.
Extra lines of code could then be added to only highlight the missing rows.


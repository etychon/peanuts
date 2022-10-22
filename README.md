# Peanuts

Some families in my country (Belgium) are making small presents ("peanuts") during christmas eve celebration. Because some families car be rather large with dozen of members, it poses a scaling and budget issue for everyone to purchase a gift for everyone else. 

Indeed the amount of individual gifts for a family of $n$ members is the simple quadradic function: $n*(n-1)$. If that's only 12 gifts for a family of 4, that's 132 gifts for a family of 12.

To make this problem more scalable, familes are making a random draw for who makes a gift to who. While this is fun and entertaining, it is much more efficient to do it in pythonic way.

The purpose of this program is to:
* list a number of family members
* randomly selecting who makes a gift to who 
* accomodate some constraints (for example my wife and I won't make gifts to each other, we favour others during this family celebration)

# Getting started

You'll need a machine that can run Python and clone this repository:

````
git clone https://github.com/etychon/peanuts.git
````

Get inside the directory created:

````
cd peanuts
````

Update the file `draw.py` to add your own data, only two lines need to be edited:

1. The family members

Say the familiy is composed of 6 members, edit this like with your own family members like so:

````py
p.add_members(['Manu', 'Barbara', 'Cyril', 'Justin', 'Mamy', 'Olivia'])
````

2. Add constraints if any (optional)

Say Barbara does not want to make a gift to Manu, and Manu does not want to make a gift to Barbara:

````py
p.add_constraints([('Manu', 'Barbara'), ('Barbara', 'Manu')])
````

If there are no constraints you can comment that line out, or make the list empty. 

3. Run the draw!

When all is set, run the `draw.py` program to actually make the draw and see the results.

````
python ./draw.py
`````

Example:

````sh
etychon@MacBookPro ~/peanuts > /usr/bin/python3 /Users/etychon/peanuts/draw.py

Here are the members:  ['Manu', 'Barbara', 'Cyril', 'Justin', 'Mamy', 'Olivia']
Here are constraints:  [('Manu', 'Barbara'), ('Barbara', 'Manu'), ('Mamy', 'Manu'), ('Cyril', 'Olivia'), ('Olivia', 'Cyril')]
        FROM -> TO          
    ---------------------------
        Mamy -> Olivia      
       Cyril -> Manu        
        Manu -> Mamy        
     Barbara -> Justin      
      Justin -> Cyril       
      Olivia -> Barbara     
````

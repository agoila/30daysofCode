# Tutorial

Terms you'll find helpful in completing today's challenge are outlined below, along with sample Java code (where appropriate).

## Class
At its most basic level, a *class* is a collection of *variables* (*fields*) and functions called *methods*. A program is a collection of classes. The basic code for declaring a Java class is as follows:
```
class MyClass{
    // This is a single-line comment.
    
    /*  This is also a comment.
        This type of comment can span several lines
    */
}
```
When declaring a class, the name should always start with a *capital* letter; this signifies to certain compilers (and human readers of your code) that it is a class (or other similarly-behaved structure that you'll learn about later). If you wish to use a compound phrase (e.g.: "my class") as your class name, you should write it in [CamelCase](https://en.wikipedia.org/wiki/CamelCase); this means you should capitalize each word and remove spaces between words (e.g.: "MyClass"). 

**Note**: Class names cannot begin with numbers or contain any spaces. 

## Variable
Think of this as a name (identifier) that points to (references) a location in memory where information associated with that name can be stored. In Java (and many other languages), it is a best practice to always start variable names with a *lowercase* letter and use CamelCase for variable names composed from compound phrases. Variable names cannot contain spaces or special characters (except underscores), though they can contain (but *not* begin with) numbers. A variable that is a member of a class is called a *field*.

Each variable has a *data type* associated with it, which essentially restricts what that variable is allowed to reference. This means your code will not work if you attempt to perform operations on your variables that aren't allowed for that data type. To *declare* a variable named *myVariable* having the data type *DataType*, we write the following: 

`DataType myVariable;`


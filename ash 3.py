Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Name = 'Ainayah Syifa Hendri'
>>> NIM = 'L200183203'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Name)
>>> type(a)
<class 'int'>
>>> ## because 'X' which is originally a string has been converted into an integer using the variable int(). this can also be called a type cast.
>>> type(b)
<class 'int'>
>>> ## because variable 'b' represents the number of members of the variable 'name.' and the number is included in the integer type because it is an integer.
>>> a/b
60.15
>>> ## because the variable 'a' is 1203 and the variable 'b' is 20, so 1203 divided by 20 is equal to 60.15.
>>> a//b
60
>>> ## because // is an arithmetic operator which when executed will produce an integer (integer, without decimal), so 60.15 is rounded to 60.
>>> 10*(a-999)
2040
>>> ## because the variable 'a' is 1203, so when reduced by 999 it produces a value of 204 and when multiplied by 10 produces a value of 2040. The arithmetic operation above is done by prioritizing the operations in parentheses.
>>> b**2
400
>>> ## because ** is an arithmetic operator that states the rank of a number, so that b**2 can also be read 'b' power 2. while variable 'b' states the number of members of the variable 'name', where the number of members of the variable 'name' is 20. so, b**2 is 400.
>>> a%b
3
>>> ## Because % is the operator that proposes the modulus (the remainder of the operating division number). In the operation of the number above, variable 'a' (which is worth 1203) divided by variable 'b' (which is worth 20) produces a value of 60 with the remainder of 3. then a%b equals 3.
>>> c = 12.5
>>> ## variable 'c' is rated 12.5.
>>> type(c)
<class 'float'>
>>> ## because the variable 'c' is 12.5, where 12.5 is a decimal number. and decimal numbers are class 'float'.
>>> a/c
96.24
>>> ## because / is an arithmetic operator that states division. variable 'a' is 1203 and variable 'c' is 12.5, so 1203 divided by 12.5 is equal to 96.24
>>> a//c
96.0
>>> ## because // is an arithmetic operator that states division with integer results (integers, by removing numbers behind commas).
>>> a%c
3.0
>>> ## because % is an arithmetic operator that states modulus (the remainder of the division of a number operation). in the number operation above, variable 'a' (which is worth 1203) divided by variable 'c' (which is 12.5) produces a value of 96 with the remainder of 3. then a%c equals 3.
>>> c>b
False
>>> ## because variable 'c' is 12.5 and variable 'b' is 20, so statement 'c' is greater than 'b' is false.
>>> type(c>b)
<class 'bool'>
>>> ## because c>b is a comparison operation where the result is true or false.
>>> a>b and b>c
True
>>> ## because the variable 'a' is 1203, the variable 'b' is 20, and the variable 'c' is 12.5, then the statement 'a' is greater than 'b' and 'b' is greater than 'c' is true.
>>> a>1100 or b<10
True
>>> ## because the variable 'a' which is worth 1203 is greater than 1100, so the statement 'a' greater than 1100 is true, while the variable 'b' which is 20 is greater than 10, so the statement 'b' smaller than 10 is false. in the rule 'or', if one or both operands are true, then the condition will be true.
>>> 

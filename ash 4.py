Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Name = 'Ainayah Syifa Hendri'
>>> NIM = 203
>>> High = 1.56
>>> Weight = 46
>>> YearOfBirth = 1998
>>> I = (YearOfBirth, Weight, High, NIM, Name)
>>> Data = [YearOfBirth, Weight, High, NIM, Name]
>>> type(I)
<class 'tuple'>
>>> ## because variable 'I' is a string of data that stores various types of data that cannot be changed (imuttable) which are marked with usage ().
>>> I[0]
1998
>>> ## because I[0] declares the 1st index of variable 'I'.
>>> a = NIM%4; I[a]
203
>>> ## because variable 'a' is the remainder of the division of the variable 'NIM' which is valued at 203 with 4 which produces a value of 3. so that I[a] is I[3] which is 203 (NIM).
>>> type(I[a])
<class 'int'>
>>> ## because I[a] is 203, where 203 is included in the 'class integer' which is an integer.
>>> I[a:4]
(203,)
>>> ## because I[a: 4] declares the 3rd index of variable 'I' which is worth NIM.
>>> type(I[4])
<class 'str'>
>>> ## because I[4] declares the 4th index of variable 'I', which is the variable 'Name' that is valued as 'Ainayah Syifa Hendri' where the variable belongs to the 'class string'.
>>> I[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    I[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> ## I[0] = 'ok' cannot be executed because variable 'I' is a tuple class, so it cannot be changed (imuttable).
 >>> type(Data)
<class 'list'>
>>> ## because the variable 'Data' is a string that stores various types of data and its contents can be changed, which is marked by the use of [].
>>> type(Data[4])
<class 'str'>
>>> ## because Data[4] states the 4th index of the 'Data' variable, which is the 'Name' variable which is valued as 'Ainayah Syifa Hendri' where the variable belongs to the 'class string'.
>>> Data[4][5]
'a'
>>> ## because Data[4][5] states the 4th index of the 'Data' variable, which is the 'Name' variable which is valued as 'Ainayah Syifa Hendri' where the 5th index of the variable is letter a.
>>> Data[4][a:6]
'aya'
>>> ## because Data[4][a:6] states the 4th index of the 'Data' variable, which is the 'Name' variable which is valued as 'Ainayah Syifa Hendri' where the 4th to 6th index of the 'Name' variable is the word 'aya'.
>>> Data[0] = 'ok' ; Data
['ok', 46, 1.56, 203, 'Ainayah Syifa Hendri']
>>> ## Data [0] = 'ok' is intended to change the 1st index of the list of 'Data' that was originally YearOfBirth(1998) to be 'ok'.
>>> Data[-a]
1.56
>>> ## because Data[-a] states the 1st index of the new 'Data' list, which is 'ok'.
>>> range(a)
range(0, 3)
>>> ## because the variable 'a' is 3, so range (a) is the range(0, 3).

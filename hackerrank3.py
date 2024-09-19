Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=int(input())
if n%2!=0:
    print("weird")
elif 2<=n<=5:
    print("not weird")
elif 6<=n<=20:
    print("weird")
elif n>20:
    print("not weird")


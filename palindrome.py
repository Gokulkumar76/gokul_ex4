#initializing variable
num = 1221
temp = num
reverse = 0
#logic
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
#printing result
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")

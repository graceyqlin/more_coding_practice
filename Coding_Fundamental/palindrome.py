#odd: a, aba, abcba
#evenL aa, abba

#entire string:

# def isPalindrome(s):
# 	n = len(s)
# 	for i in range(n//2+1):
# 		if s[i] != s[-i-1]:
# 			return False
# 	return True


# s = 'abcba'
# s = 'aabb'
# s = 'aba'
# print(isPalindrome(s))


# substring:

def isPalindromesub(s, l, r):
	n = len(s)
	while l < r:
		if s[l] != s[r]:
			return False
		l += 1
		r -= 1
	return True

s = 'abcba'
s = 'aabb'
s = 'aba'

print(isPalindromesub(s, 0, len(s)-1))
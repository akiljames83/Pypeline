""" 
KMP Search Implementation

"""

def KMPSearch(pat, txt):
	""" 
	A function implements KMP algorithm string search. Compute the LPS array to locate such pattern.

	Parameters:\n
		pat: the string pattern we are looking for
		txt: the text we are searching on
	"""

	M = len(pat)
	N = len(txt)
	lps = [0]*M
	j = 0
	computeLPSArray(pat, M, lps)
	i = 0
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			return i-j
			j = lps[j-1]

		# mismatch after j matches
		elif i < N and pat[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters,
			# they will match anyway
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

def computeLPSArray(pat, M, lps):
	""" 
	A method that compute the LPS array. It preprocess the pattern for the kmp search.

	Parameters:\n
		pat: the string pattern we are looking for
		M: length of the pattern
		lps: the lps array
	"""
	
	len = 0
	lps[0]
	i = 1
	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:

			if len != 0:
				len = lps[len-1]


			else:
				lps[i] = 0
				i += 1



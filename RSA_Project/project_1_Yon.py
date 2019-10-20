import math


with open('public-key.txt', 'r') as file:
	pq= int(file.readline().strip(), base=16)
	e = int(file.readline().strip(), base=16)

with open('cypher-text.txt', 'r') as file:
	encyped = [int(line, base=16) for line in file]

def pollards_rho(n):
	x = 2; y = 2; d = 1
	f = lambda x: (x**2 + 1) % n
	while d == 1:
		x = f(x); y = f(f(y))
		d = math.gcd(abs(x-y), n)
	if d != n: 
		return d

def egcd(a,b):
	assert a > b
	r_i, r_im1 = b, a
	s_i, t_i, s_im1, t_im1 = 0, 1, 1, 0
	while r_i != 0:
		q, r = divmod(r_im1, r_i) 
		r_i, r_im1 = r, r_i
		s_i, s_im1 = s_im1-q*s_i, s_i 
		t_i, t_im1 = t_im1-q*t_i, t_i
	return r_im1, s_im1, t_im1


P=pollards_rho(pq)
print(P)
print(Q)
Q= int(pq/pollards_rho(pq))
phi=(P-1)*(Q-1)

r,D,t=egcd(e, phi)

d= (D%phi)

encrypted=[]
for m in encyped:
	encrypted.append(int(pow( m, d, pq)))

for j in encrypted:
	print(chr(j),end='')














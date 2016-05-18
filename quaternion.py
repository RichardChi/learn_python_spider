#!/usr/bin/env python
import math
import numpy as np

def quater_multip(leftquater, rightquater):
	Lw, Lx, Ly, Lz = leftquater
	Rw, Rx, Ry, Rz = rightquater
	leftQ = np.array([
		[Lw, -Lx, -Ly, -Lz],
		[Lx, Lw, -Lz, Ly],
		[Ly, Lz, Lw, -Lx],
		[Lz, -Ly, Lx, Lw]])
	rightQ = np.array([Rw, Rx, Ry, Rz])
	resultQ = np.dot(leftQ,rightQ)	
	return resultQ

def makequater(radian, x, y, z):
	norm = x*x + y*y + z*z
	if norm < 0:
		return [0.0, 0.0, 0.0, 0.0]

	norm = 1 / math.sqrt(norm)
	x *= norm
	y *= norm
	z *= norm 
	ccc = math.cos(radian * 0.5)
	sss = math.sin(radian * 0.5)

	ans = [ccc, sss * x, sss*y, sss*z]
	return ans


def quaterToeuler(quater):
	w, x, y, z = quater
	phi = math.atan2(2*(w*y + x*z), 1 - 2*(x*x + y*y))
	thrat = math.asin(2*(w*x - z*y))
	psai = math.atan2(2*(w*z + x*y), 1 - 2*(y*y + z*z))

	euler = [thrat, phi, psai]
	return euler
 
if __name__ == '__main__':
	q = [math.cos(math.pi /2), 0, math.sin( math.pi/2),0]
	q_inv = [math.cos(math.pi / 2), 0, -math.sin(math.pi/2), 0]
	x = [0.0, 1.0, 0.0, 1.0]
	x_1 = quater_multip(q, x)
	x_1 = quater_multip(x_1,q_inv)
	print x_1
	euler = quaterToeuler(q)
	print euler

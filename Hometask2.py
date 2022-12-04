from ECurve import ECurve, ECPoint

curve = ECurve(3, 4)

G = curve.BasePointGGet()
G.PrintECPoint()

A = 2
B = 5

H_A = G.ScalarMult(A)
H_B = G.ScalarMult(B)

BOA = H_A.ScalarMult(B)
AOB = H_B.ScalarMult(A)

BOA.PrintECPoint()
AOB.PrintECPoint()

print(BOA.ECPointToString() == AOB.ECPointToString())
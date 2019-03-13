## python関数で任意のユニタリ回転ゲートをつくる

from qiskit import *
from qiskit.tools.visualization import plot_histogram
import math


def mygate(qci, q):
    qci.u3(math.pi, 0, math.pi, q)
#ユニタリ回転ゲートのU(θ、Φ、λ）の定義からビット反転演算Xを作成


bn = 1  # ビット数

q = QuantumRegister(bn)  # １つの 量子 レジスタqの 生成
c = ClassicalRegister(bn)  # １つの 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c)  # 量子 回路 qcの 生成

mygate(qc, q[0])

for i in range(bn):
    qc.measure(q[bn-1-i], c[i])

#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
plot_histogram(rc)

# 結果、入力ビット|0>に対して、出力ビット|1>となっているので、
# ユニタリ回転ゲートの定義関数からビット反転演算ゲートを実現できた

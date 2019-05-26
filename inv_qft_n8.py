
# 逆量子フーリエ変換QFT-1(8)
from qiskit import *
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import math
bn=3 # 量子ビット数

q = QuantumRegister(bn) #ba個の 量子 レジスタqの 生成
c = ClassicalRegister(bn) #bn個の 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c) #量子回路の生成
# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

for i in range(bn):
    qc.h(q[i])
    qc.barrier()
    qc.h(q[0])
    qc.cu1(-math.pi/2,q[0],q[1])
    qc.cu1(-math.pi/4,q[0],q[2])
    qc.h(q[1])
    qc.cu1(-math.pi/2,q[1],q[2])
    qc.h(q[2])

for i in range(bn):
    qc.measure(q[bn-1-i],c[i])

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
# circuit_drawer(qc)
plot_histogram(rc)





























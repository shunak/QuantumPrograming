## 条件判断c_ifのつかいかた

from qiskit import *
from qiskit.tools.visualization import plot_histogram

bn = 2  # ビット数

q = QuantumRegister(bn)  # １つの 量子 レジスタqの 生成
c = ClassicalRegister(bn)  # １つの 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c)  # 量子 回路 qcの 生成

qc.x(q[0])
qc.measure(q[0], c[1])
qc.x(q[1]).c_if(c, 2)
qc.measure(q[1], c[0])

#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
plot_histogram(rc)

# 結果、入力ビット|01>に対して、出力ビット|11>となっているので、
# あたかも制御NOTゲートが逆転した結果になっている

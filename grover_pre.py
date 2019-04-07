# グルーバーの探索アルゴリズム : 均等な確率振幅を持つ重ね合わせ状態の準備
# 探索回の振幅増幅手法
from qiskit import *
from qiskit.tools.visualization import plot_histogram, circuit_drawer

bn = 2  # 量子ビット数

q = QuantumRegister(bn)  # ba個の 量子 レジスタqの 生成
c = ClassicalRegister(bn)  # bn個の 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c)  # 量子回路の生成

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

for i in range(bn):
    qc.h(q[i])

for i in range(bn):
    qc.measure(q[bn-1-i], c[i])

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
# circuit_drawer(qc)
plot_histogram(rc)


# unfinished

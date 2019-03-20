# トフォリゲートccxゲート（制御ビットがふたつあって、ふたつとも1なら標的ビットを反転させる）
from qiskit import *
from qiskit.tools.visualization import plot_histogram

bn = 3  # ビット数

q = QuantumRegister(bn)  # １つの 量子 レジスタqの 生成
c = ClassicalRegister(bn)  # １つの 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c)  # 量子 回路 qcの 生成

qc.x(q[0])
qc.x(q[1])
qc.ccx(q[0], q[1], q[2])

for i in range(bn):
    qc.measure(q[bn-1-i], c[i])

#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
plot_histogram(rc)


# 制御ビットq[0],q[1]が1、標的ビットq[2]が0のとき、
# つまり、|110>を入力したとき、出力|111>が得られる

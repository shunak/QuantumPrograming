# グルーバーの探索アルゴリズム : N=4のデータベースでの探索解|3>のマーキングでの状態ベクトルの確率振幅表示
# 探索回の振幅増幅手法
from qiskit import *

from qiskit.tools.visualization import plot_histogram, plot_state_city

bn = 2  # 量子ビット数

q = QuantumRegister(bn)  # ba個の 量子 レジスタqの 生成
c = ClassicalRegister(bn)  # bn個の 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c)  # 量子回路の生成

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

for i in range(bn):
    qc.h(q[i])
qc.cz(q[0], q[1])

backend_sim = BasicAer.get_backend('statevector_simulator')
r = execute(qc, backend_sim, shots=8192).result()
print(r.get_statevector())

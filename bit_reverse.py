## ビット反転演算(初期状態|0>)
from qiskit import *
q = QuantumRegister(1)  # １つの 量子 レジスタqの 生成
c = ClassicalRegister(1)  # １つの 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c)  # 量子 回路 qcの 生成
qc.x(q[0])
qc.measure(q, c)  # 量子 レジスタqを 測 定 して 古典 的 レジスタcに 入 れる
#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=100).result()
#量子 回路 名 cnの 量子 プログラムの 実 行 結 果 rからカウント 結 果 取得 し 表示 する
print(r.get_counts())

# the results
# inital state '0' turn to '1' by X operator
# {'1': 100}
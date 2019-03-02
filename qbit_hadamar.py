## アダマール変換のpythonゲート

from qiskit import *
from qiskit.tools.visualization import plot_histogram
# from numpy.random import *

q = QuantumRegister(1)  # １つの 量子 レジスタqの 生成
c = ClassicalRegister(1)  # １つの 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c)  # 量子 回路 qcの 生成

qc.h(q[0])  # 量子ビットq[0]のアダマール変換

qc.measure(q, c)  # 量子 レジスタqを 測 定 して 古典 的 レジスタcに 入 れる
#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=100).result()
rc = r.get_counts()
print(rc)
plot_histogram(rc)

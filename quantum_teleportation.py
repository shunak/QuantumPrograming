# 量子テレポーテーションゲートのPython関数
from qiskit import *
from qiskit.tools.visualization import plot_histogram, circuit_drawer


def qt(qci, a1, a2, b):
    qci.h(a2)
    qci.cx(a2, b)
    qci.cx(a1, a2)
    qci.h(a1)
    qci.cx(a2, b)
    qci.cz(a1, b)


ba = 2  # 量子ビット数

bb = 2  # 量子ビット数

cn = 1  # 古典ビット数

qa = QuantumRegister(ba, "alice")  # ba個の 量子 レジスタqの 生成
qb = QuantumRegister(bb, "bob")  # bb個の 量子 レジスタqの 生成
c = ClassicalRegister(cn)  # cn個の 古典 的 レジスタcの 生成
qca = QuantumCircuit(qa, c)  # 量子 回路 qcaの 生成
qcb = QuantumCircuit(qb, c)  # 量子 回路 qcbの 生成

qc = qca + qcb

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

qc.h(qa[0])

qc.barrier()

qt(qc, qa[0], qa[1], qb[0])

qc.measure(qb[0], c[0])


#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
# circuit_drawer(qc)
plot_histogram(rc)


# unfinished

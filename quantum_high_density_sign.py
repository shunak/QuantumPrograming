# 量子高密度符号　：　1量子ビットの量子状態を転送して、古典的情報として2ビットを伝送可能
from qiskit import *
from qiskit.tools.visualization import plot_histogram, circuit_drawer


def qdc(qci, a0, a1, a, b):
    qci.h(a)
    qci.cx(a, b)
    qci.cx(a1, a)
    qci.cz(a0, a)
    qci.cx(a, b)
    qci.h(a)


ba = 3  # 量子ビット数

bb = 1  # 量子ビット数

cn = 2  # 古典ビット数

qa = QuantumRegister(ba)  # ba個の 量子 レジスタqの 生成
# qa = QuantumRegister(ba, "alice")  # ba個の 量子 レジスタqの 生成
qb = QuantumRegister(bb) # bb個の 量子 レジスタqの 生成
# qb = QuantumRegister(bb, "bob")  # bb個の 量子 レジスタqの 生成
c = ClassicalRegister(cn)  # cn個の 古典 的 レジスタcの 生成
qca = QuantumCircuit(qa, c)  # 量子 回路 qcaの 生成
qcb = QuantumCircuit(qb, c)  # 量子 回路 qcbの 生成

qc = qca + qcb

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

qc.x(qa[0])

qc.barrier()

qdc(qc, qa[0], qa[1], qa[2], qb[0])

qc.barrier()

qc.measure(qb[0], c[0])
qc.measure(qa[2], c[1])


#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
# circuit_drawer(qc)
plot_histogram(rc)


# unfinished

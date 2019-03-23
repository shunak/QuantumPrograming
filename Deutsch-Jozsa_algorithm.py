# ドイチのアルゴリズム（オラクル推定）
from qiskit import *
from qiskit.tools.visualization import plot_histogram, circuit_drawer

# 量子オラクルの定義
def oracle(qci, x, y_fx):
    qci.cx(x, y_fx)
    qci.x(y_fx)


bn = 2  # 量子ビット数
cn = 1  # 古典的ビット数

q = QuantumRegister(bn)  # bn個の 量子 レジスタqの 生成
c = ClassicalRegister(cn)  # cn個の 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c)  # 量子 回路 qcの 生成


# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
qc.x(q[1])
for i in range(bn):
    qc.h(q[i])

oracle(qc, q[0], q[1])

for i in range(bn):
    qc.h(q[i])

qc.measure(q[0], c[0])

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊


#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
# circuit_drawer(qc)
plot_histogram(rc)

# |1>が観測されるので、ドイチ問題でのこのオラクルは均等な関数と判断できる

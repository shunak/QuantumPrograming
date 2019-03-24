# ドイチのアルゴリズム（一定な関数と均等な関数の比較）
# 量子回路をふたつつくって比較をおこなう
from qiskit import *
from qiskit.tools.visualization import plot_histogram, circuit_drawer


def c_oracle(qci, x, y_fx):
    qci.x(y_fx)


def b_oracle(qci, x, y_fx):
    qci.cx(x, y_fx)


bn = 2  # 量子ビット数

q1 = QuantumRegister(bn)  # bn個の 量子 レジスタq1の 生成
q2 = QuantumRegister(bn)  # bn個の 量子 レジスタq2の 生成
c = ClassicalRegister(bn)  # cn個の 古典 的 レジスタcの 生成

qc1 = QuantumCircuit(q1, c)  # 量子 回路 qc1の 生成
qc2 = QuantumCircuit(q2, c)  # 量子 回路 qc2の 生成

qc = qc1+qc2  # ふたつの回路を合成する

qc.x(q1[1])
qc.x(q2[1])


# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

# アダマールゲートでそれぞれのビットに対して、重ね合わせ状態を生成する
for i in range(bn):
    qc.h(q1[i])
for i in range(bn):
    qc.h(q2[i])

# 量子オラクル部分
c_oracle(qc, q1[0], q1[1])
b_oracle(qc, q2[0], q2[1])

for i in range(bn):
    qc.h(q1[i])
for i in range(bn):
    qc.h(q2[i])

qc.measure(q2[0], c[0])
qc.measure(q1[0], c[1])

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊


#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
# circuit_drawer(qc)
plot_histogram(rc)

#実行結果として、|01>が観測される。
# 前半の量子オラクルは「一定な関数」と判断でき、後半の量子オラクルは均等な関数と判断できる

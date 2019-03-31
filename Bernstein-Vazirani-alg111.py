# ベルンシュタイン・ヴァジラニ問題で解a=111の量子オラクル
# 量子回路をふたつつくって比較をおこなう
from qiskit import *
from qiskit.tools.visualization import plot_histogram, circuit_drawer


def bv_oracle(qci, x0, x1, x2, f_x):
    qci.cx(x0, f_x)
    qci.cx(x1, f_x)
    qci.cx(x2, f_x)


bn = 4  # 量子ビット数

cn = 3  # 古典ビット数

q = QuantumRegister(bn)  # bn個の 量子 レジスタqの 生成
c = ClassicalRegister(cn)  # cn個の 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c)  # 量子 回路 qc1の 生成


# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

qc.x(q[3])

# アダマールゲートでそれぞれのビットに対して、重ね合わせ状態を生成する
for i in range(bn):
    qc.h(q[i])

# ベルンシュタイン・ヴァジラニ問題的オラクル
bv_oracle(qc, q[0], q[1], q[2], q[3])

# アダマールゲートでそれぞれのビットに対して、重ね合わせ状態を生成する
for i in range(bn):
    qc.h(q[i])

# 量子測定
for i in range(cn):
    qc.measure(q[cn-1-i], c[i])

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
# circuit_drawer(qc)
plot_histogram(rc)

# |111>が測定されるので、この読みそのもの値が、定数a=a0a1a2=111となっていて、
# 1回の関数への問い合わせで定数a=a0a1a2=111が決定できたことになる




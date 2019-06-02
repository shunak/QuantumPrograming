# 関数y=f(x)=7xmod15を量子関数として実装する
from qiskit import *
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import math

bx = 3#量子ビット数
by = 4#量子ビット数
cn = 4#古典的ビット数

qx = QuantumRegister(bx) #bx個の 量子 レジスタqの 生成
qy = QuantumRegister(by) #by個の 量子 レジスタqの 生成
c = ClassicalRegister(cn) #cn個の 古典 的 レジスタcの 生成
qcx = QuantumCircuit(qx, c) #量子回路の生成
qcy = QuantumCircuit(qy, c) #量子回路の生成

qc = qcx + qcy

for i in range(bx):
    qc.h(qx[i])

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
qc.x(qy[3])

# 制御NOTゲート部分
qc.cx(qx[2],qy[1])
qc.cx(qx[2],qy[2])
qc.cx(qx[1],qy[1])
qc.cx(qx[1],qy[3])

# 制御・制御NOTゲート（トフォリゲート）部分
for i in range(by):
    qc.ccx(qx[1],qx[2],qy[i])

for i in range(by):
    qc.measure(qy[by-1-i],c[i])

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
# circuit_drawer(qc)
plot_histogram(rc)


#|1>,|4>,|7>,|13>の重ね合わせを状態として結果が得られる





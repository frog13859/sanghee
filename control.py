import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control

st.title("조상희")
st.header("202221016")



#전달 함수 정의
G = control.TransferFunction([100],[1,5,6])

# 폐루프 전달함수 계산
G1 = control.feedback(G)

print("Transfer Function G(s):")
print(G1)


#단위 계산 응답
num = [100]
den = [1,5,106]

system = signal.TransferFunction(num,den)

#단위 계단 응답
t,y=signal.step(system)

#그래프 그리기: 단위 계단 응답
fig = plt.figure()
plt.figure()
plt.plot(t,y)
plt.xlabel('Time(s)')
plt.ylabel('Response')
plt.title('Step Response of H(s) =100/ (s + 2)* (s + 3)')
plt.grid(True)
plt.show()
st.pyplot(fig)

G0 = signal.lti([100],[1])
G1 = signal.lti([1],[1,2])
G2 = signal.lti([1],[1,3])
G3 = signal.lti([100],[1,5,6])

frequencies = np.logspace(-2,2,500)

systems = [G0,G1,G2,G3]
labels = ['Proportional Element', 'lntegral Element', 'First-Order Lag Element', 'Overall System']
colors = ['r', 'g', 'b', 'm']

plt.figure(figsize=(12,8))

# Bode magnitude plot
fig1 = plt.figure()
plt.subplot(2,1,1)
for sys,label,color in zip(systems, labels, colors):
  w, mag,_=sys.bode(frequencies)
  plt.semilogx(w, mag, color=color, label=label)
plt.title('Bode plot')
plt.ylabel('Magnitude [dB]')
plt.legend()
st.pyplot(fig1)

fig2 = plt.figure()
plt.subplot(2,1,2)
for sys,_,color in zip(systems, labels, colors):
  w,_,phase = sys.bode(frequencies)
  plt.semilogx(w, phase, color=color)
plt.ylabel('Phase [degrees]')
plt.xlabel('Frequency [Hz]')
plt.show()
st.pyplot(fig2)
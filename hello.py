import streamlit as st
import control
import numpy as np
from scipy.signal import lti, step
import matplotlib.pyplot as plt
from scipy import signal

st.title("조상희")
st.header("202221016")

#단위계단응답1
G1 = control.TransferFunction([100],[1,5,6])
G2 = control.feedback(G1)
st.write(G2)


num = [100]
den = [1,5,106]
system = signal.TransferFunction(num,den)


t,y = step(system)
fig = plt.figure()
plt.plot(t,y)
plt.title('step response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
st.pyplot(fig)

#주파수 응답

#Define the systems
G0 = signal.lti([100],[1])
G1 = signal.lti([1],[1,2])
G2 = signal.lti([1],[1,3])
G3 = signal.lti([100],[1,5,6])

#Define the frequency range
frequencies = np.logspace(-2,2,500)#frequencies in range from 0.01 to 100

#Calculate frequency responses
systems = [G0,G1,G2,G3]
labels = ['Proportional Element', 'Integral Element', 'First-Order Lag Element', 'Overall System']
colors = ['r','g','b','m']


plt.figure(figsize=(12,8))

#Bode magnitude plot
plt.subplot(2,1,1)
fig2 = plt.figure()
for sys,label,color in zip(systems,labels, colors):
  w,mag,_ = sys.bode(frequencies)
  plt.semilogx(w,mag,color=color, label=label)
plt.title('Bode plot')
plt.ylabel('Magnitude [dB]')
plt.legend()
st.pyplot(fig2)



#Bode phase plot
plt.subplot(2,1,2)
fig3 = plt.figure()
for sys,_,color in zip(systems,labels, colors):
  w,_,phase = sys.bode(frequencies)
  plt.semilogx(w,phase,color=color)
plt.ylabel('Phase [degrees]')
plt.xlabel('Frequency [Hz]')
plt.show()
st.pyplot(fig3)
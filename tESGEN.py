# -*- coding: utf-8 -*-
"""
Created by Francesco Mattioli
Francesco@nientepanico.org
www.nientepanico.org
"""

import numpy as np
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import random as random


def tdcsan(lenght_ramp,intensity,time):
    real_time = time - (lenght_ramp * 2)
    ramp_up = np.linspace(0, intensity, lenght_ramp) 
    line = np.full(real_time,intensity)   
    ramp_down = np.flip(np.linspace(0, intensity, lenght_ramp))
    tdcsan_result = np.concatenate((ramp_up, line, ramp_down))
    return tdcsan_result

def tdcsca(lenght_ramp,intensity,time):
    real_time = time - (lenght_ramp * 2) 
    ramp_up = np.linspace(0, intensity, lenght_ramp) 
    line = np.full(real_time,intensity)   
    ramp_down = np.flip(np.linspace(0, intensity, lenght_ramp))
    tdcsan_result = np.concatenate((ramp_up, line, ramp_down))
    return tdcsan_result

def tacs(sample_rate, frequency):
    # fs = 100 # sample rate 
    # f = 2 # the frequency of the signal
    x = np.arange(sample_rate) # the points on the x axis for plotting
    # compute the value (amplitude) of the sin wave at the for each sample
    y = np.sin(3 *np.pi*frequency * (x/sample_rate))
    return y


def trns(mean, sd, time):
    noise = np.random.normal(mean, sd, time)
    return noise

time = np.arange(1000)

tdcsanodal = tdcsan(100,1.5,1000)
tdcscatodal = tdcsan(100, -1.5, 1000)
talternatingcs = tacs(1000, 5)
trandomnoises = trns(2,5,1000)

data = np.array([tdcsanodal,tdcscatodal,talternatingcs,trandomnoises,time])

df_raw = pd.DataFrame(data=data, index=["tdcsan", "tdcsca", "tacs", "trns", "time"], columns=time)

df = df_raw.T

# fig = px.line(df, x="time", y="tdcsan", title='Life expectancy in Canada')

# plot(fig)

fig = make_subplots(rows=2, 
                    cols=2, subplot_titles=("Anodal, Transcranial direct current stimulation (tDCS)", 
                                            "Cathodal, Transcranial direct current stimulation (tDCS)", 
                                            "Transcranial Alternating Current Stimulation (tACS)", 
                                            "Transcranial random noise stimulation(tRNS)"),
                    vertical_spacing=0.08, 
                    specs=[[{"type": "scatter"},
                            {"type": "scatter"}],
                            [{"type": "scatter"},
                            {"type": "scatter"}]])

fig.add_trace(go.Scatter(x=df["time"], y=df["tdcsan"],mode="lines",name="tdcsan"),row=1, col=1)

fig.add_trace(go.Scatter(x=df["time"],y=df["tdcsca"],mode="lines",name="tdcsca"),row=1, col=2)

fig.add_trace(go.Scatter(x=df["time"], y=df["tacs"],mode="lines",name="tacs"),row=2, col=1)

fig.add_trace(go.Scatter(x=df["time"], y=df["trns"],mode="lines",name="trns"),row=2, col=2)

fig.update_layout(title = 'Transcranial electrical stimulation (tES)')


plot(fig)









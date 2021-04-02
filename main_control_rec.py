# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:46:08 2021

@author: neurobooth
"""

from registration import get_session_info
import os
import socket
import time
import psutil
import numpy as np
import config 
# from realtime.lsl_plotter import stream_plotter
from netcomm.client import socket_message, socket_time


def prepare_feedback():    
    socket_message("vis_stream", "acquisition")    
    socket_message("scr_stream", "presentation")
    
def prepare_devices():
    socket_message("prepare", "acquisition")    
    socket_message("prepare", "presentation") 

def setup_part_info():
    session = get_session_info()
    return session

def task_presentation(task_name, filename):
    resp = socket_message(f"present:{task_name}:{filename}", "presentation", 1)
    print(resp)
    
def task_loop(task_names, subj_id):
    for task in  task_names:
        filename = f"{subj_id}_{task}"
        task_presentation(task, filename)

def close_all():
    socket_message("close", "acquisition")    
    socket_message("close", "presentation") 
   
def shut_all():
    socket_message("shutdown", "acquisition")    
    socket_message("shutdown", "presentation") 
    
def test_lan_delay(n=100):
    
    nodes = ["acquisition", "presentation"]
    times_1w, times_2w = [], []
    
    for node in nodes:    
        tmp = []
        for i in range(n):
            tmp.append(socket_time(node, 0))       
        times_1w.append([t[1] for t in tmp])   
        times_2w.append([t[0] for t in tmp])
    
    _ = [print(f"{n} socket connexion time average:\n\t receive: {np.mean(times_2w[i])}\n\t send:\t  {np.mean(times_1w[i])} ")
         for i, n  in enumerate(nodes)]
    
    return times_2w, times_1w
  
    
def initiate_labRec():
    # Start LabRecorder
    if not "LabRecorder.exe" in (p.name() for p in psutil.process_iter()):
        os.startfile(config.paths['LabRecorder'])
        
    time.sleep(.05)
    s = socket.create_connection(("localhost", 22345))
    s.sendall(b"select all\n")
    s.close()
    
    
if 0:
    t2w, t1w = test_lan_delay(10)
    
    
    prepare_feedback()
    
    session = setup_part_info()
    prepare_devices()
    
    
    
    task_name = "fakest_task"





   
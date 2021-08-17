#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from psychopy import logging
logging.console.setLevel(logging.CRITICAL)
from psychopy import sound
from psychopy import microphone
from psychopy import visual, core, event
# from psychopy import prefs
# prefs.hardware['audioLib']=['pyo']
import os
import psutil


subj = 'Sheraz_Khan'
full_screen = False
# Monitor resolution
SCN_W, SCN_H = (1920, 1080)

# Setup the Window
win = visual.Window(
    size=(SCN_W, SCN_H), fullscr=full_screen, screen=0,
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')


sustainph_instructions = visual.TextStim(win=win, name='sustainph_instructions',
    text='For this task, you will take a deep breath and say “a-a-a-a” for as long as you can until you run out of breath.\n\nYou will practice once.\n\nPress any button to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)

sustainph_practice = visual.TextStim(win=win, name='sustainph_practice',
    text='Please practice the task now.\n\nPress any button when you have completed the task.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)

sustainph_postpractice_instr = visual.TextStim(win=win, name='sustainph_postpractice_instr',
    text='Practice test is complete. \n\nFor the test, please remember to say “a-a-a-a” for as long as you can without taking any extra breaths. \n\nPress any button to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)

sustainph_begintask = visual.TextStim(win=win, name='sustainph_begintask',
    text='Please begin the task now. \n\nPress any button when you have completed the task.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)

sustainph_endtask = visual.TextStim(win=win, name='sustainph_endtask',
    text='Thank you. You have completed this task.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='white', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0)


sustainph_audio_instructions = sound.Sound('sust_phon_instructions.wav', secs=-1, stereo=True, hamming=True,
    name='sustainph_audio_instructions')

sustainph_audio_practice = sound.Sound('practice_text.wav', secs=-1, stereo=True, hamming=True,
    name='sustainph_audio_practice')

sustainph_audio_postpractice_instr = sound.Sound('sust_phon_practice_comp_test_instr.wav', secs=-1, stereo=True, hamming=True,
    name='sustainph_audio_postpractice_instr')

sustainph_audio_begintask = sound.Sound('begin_task_text.wav', secs=-1, stereo=True, hamming=True,
    name='sustainph_audio_begintask')

sustainph_audio_endtask = sound.Sound('task_complete.wav', secs=-1, stereo=True, hamming=True,
    name='sustainph_audio_endtask')



sustainph_audio_instructions.setVolume(1.0)
sustainph_audio_practice.setVolume(1.0)
sustainph_audio_postpractice_instr.setVolume(1.0)
sustainph_audio_begintask.setVolume(1.0)
sustainph_audio_endtask.setVolume(1.0)

microphone.switchOn()
mic = microphone.AdvAudioCapture()


sustainph_instructions.draw()
win.flip()
sustainph_audio_instructions.play()
core.wait(5)
event.waitKeys()
win.color = (0, 0, 0)
win.flip()
sustainph_audio_instructions.stop()

sustainph_practice.draw()
win.flip()
sustainph_audio_practice.play()
core.wait(5)
mic.record(180, 'data/' +subj + '_practice.wav')
mic.setMarker()
event.waitKeys()
mic.stop()
win.color = (0, 0, 0)
win.flip()
sustainph_audio_practice.stop()

sustainph_postpractice_instr.draw()
win.flip()
sustainph_audio_postpractice_instr.play()
core.wait(5)
event.waitKeys()
win.color = (0, 0, 0)
win.flip()
sustainph_audio_postpractice_instr.stop()

sustainph_begintask.draw()
win.flip()
sustainph_audio_begintask.play()
core.wait(5)
mic.record(180, 'data/' +subj + '_task.wav')
mic.setMarker()
event.waitKeys()
mic.stop()
win.color = (0, 0, 0)
win.flip()
sustainph_audio_begintask.stop()

sustainph_endtask.draw()
win.flip()
sustainph_audio_endtask.play()
core.wait(5)
win.color = (0, 0, 0)
win.flip()
sustainph_audio_endtask.stop()

mic.reset()
win.close()
current_system_pid = os.getpid()
ThisSystem = psutil.Process(current_system_pid)
ThisSystem.terminate()
core.quit()






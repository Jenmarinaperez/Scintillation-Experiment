#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Sun Dec 20 00:17:01 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'Scintillation Experiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jenniferperez/Desktop/Scintillation Experiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Hold_Screen"
Hold_ScreenClock = core.Clock()
hold_text = visual.TextStim(win=win, name='hold_text',
    text='Welcome to Elif, Jennifer, and Liora’s Scintillation Experiment! \n\n\nWhenever you’re ready, please press the <“Spacebar”> to move onto the Instructions page! ',
    font='Arial',
    pos=(0, 0), height=0.055, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
hs_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='\nScintillating Experiment Instructions: \n\nIn this experiment, you will differentiate between two scintillating images. You can detect this scintillation by setting your gaze on the center of each image. \n\nIf the image on the right appears to be scintillating most, you will press the <“K”> key. \n\nIf the image on the left appears to be scintillating most, you will press the <“F”> key.\n\nIf the images both appear to be scintillating equally, you will press the <“Spacebar”>.\n\nYou will first be prompted with a practice trial to familiarize yourself with the experiment. Good Luck! \n\nPlease press the <“Spacebar”> to move onto the practice trial. \n\n',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruc_key_resp = keyboard.Keyboard()

# Initialize components for Routine "focus"
focusClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "images"
imagesClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
left_image_text = visual.TextStim(win=win, name='left_image_text',
    text='Left image   \n      <“F”>       ',
    font='Arial',
    pos=(-0.4, -0.35), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
center_text = visual.TextStim(win=win, name='center_text',
    text='Equally \nScintillating \n<“Spacebar”>',
    font='Arial',
    pos=(0, -0.35), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
right_image_text = visual.TextStim(win=win, name='right_image_text',
    text='Right Image\n<“K”>',
    font='Arial',
    pos=(0.4, -0.35), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
image_key_resp = keyboard.Keyboard()

# Initialize components for Routine "transition_screen"
transition_screenClock = core.Clock()
transition_text = visual.TextStim(win=win, name='transition_text',
    text='You are now finished with the practice trial! Not too bad right? \n\nNow for the real test. Good Luck! \n\nWhenever you’re ready, please press the <“Spacebar”> to move onto the experiment trial!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trans_key = keyboard.Keyboard()

# Initialize components for Routine "focus"
focusClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "images"
imagesClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
left_image_text = visual.TextStim(win=win, name='left_image_text',
    text='Left image   \n      <“F”>       ',
    font='Arial',
    pos=(-0.4, -0.35), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
center_text = visual.TextStim(win=win, name='center_text',
    text='Equally \nScintillating \n<“Spacebar”>',
    font='Arial',
    pos=(0, -0.35), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
right_image_text = visual.TextStim(win=win, name='right_image_text',
    text='Right Image\n<“K”>',
    font='Arial',
    pos=(0.4, -0.35), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
image_key_resp = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Congratulations! You have reached the end of the Scintillation Experiment. Now how fun was that? \n\nThank you for participating! \n\n\nPlease press the <“Spacebar”> to exit the experiment. \n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Hold_Screen"-------
continueRoutine = True
# update component parameters for each repeat
hs_key_resp.keys = []
hs_key_resp.rt = []
_hs_key_resp_allKeys = []
# keep track of which components have finished
Hold_ScreenComponents = [hold_text, hs_key_resp]
for thisComponent in Hold_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Hold_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Hold_Screen"-------
while continueRoutine:
    # get current time
    t = Hold_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Hold_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *hold_text* updates
    if hold_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hold_text.frameNStart = frameN  # exact frame index
        hold_text.tStart = t  # local t and not account for scr refresh
        hold_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hold_text, 'tStartRefresh')  # time at next scr refresh
        hold_text.setAutoDraw(True)
    
    # *hs_key_resp* updates
    waitOnFlip = False
    if hs_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hs_key_resp.frameNStart = frameN  # exact frame index
        hs_key_resp.tStart = t  # local t and not account for scr refresh
        hs_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hs_key_resp, 'tStartRefresh')  # time at next scr refresh
        hs_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(hs_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(hs_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if hs_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = hs_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _hs_key_resp_allKeys.extend(theseKeys)
        if len(_hs_key_resp_allKeys):
            hs_key_resp.keys = _hs_key_resp_allKeys[-1].name  # just the last key pressed
            hs_key_resp.rt = _hs_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Hold_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Hold_Screen"-------
for thisComponent in Hold_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('hold_text.started', hold_text.tStartRefresh)
thisExp.addData('hold_text.stopped', hold_text.tStopRefresh)
# check responses
if hs_key_resp.keys in ['', [], None]:  # No response was made
    hs_key_resp.keys = None
thisExp.addData('hs_key_resp.keys',hs_key_resp.keys)
if hs_key_resp.keys != None:  # we had a response
    thisExp.addData('hs_key_resp.rt', hs_key_resp.rt)
thisExp.addData('hs_key_resp.started', hs_key_resp.tStartRefresh)
thisExp.addData('hs_key_resp.stopped', hs_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Hold_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
instruc_key_resp.keys = []
instruc_key_resp.rt = []
_instruc_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [instructions_text, instruc_key_resp]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_text* updates
    if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.tStart = t  # local t and not account for scr refresh
        instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
        instructions_text.setAutoDraw(True)
    
    # *instruc_key_resp* updates
    waitOnFlip = False
    if instruc_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruc_key_resp.frameNStart = frameN  # exact frame index
        instruc_key_resp.tStart = t  # local t and not account for scr refresh
        instruc_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruc_key_resp, 'tStartRefresh')  # time at next scr refresh
        instruc_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instruc_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instruc_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruc_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = instruc_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _instruc_key_resp_allKeys.extend(theseKeys)
        if len(_instruc_key_resp_allKeys):
            instruc_key_resp.keys = _instruc_key_resp_allKeys[-1].name  # just the last key pressed
            instruc_key_resp.rt = _instruc_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_text.started', instructions_text.tStartRefresh)
thisExp.addData('instructions_text.stopped', instructions_text.tStopRefresh)
# check responses
if instruc_key_resp.keys in ['', [], None]:  # No response was made
    instruc_key_resp.keys = None
thisExp.addData('instruc_key_resp.keys',instruc_key_resp.keys)
if instruc_key_resp.keys != None:  # we had a response
    thisExp.addData('instruc_key_resp.rt', instruc_key_resp.rt)
thisExp.addData('instruc_key_resp.started', instruc_key_resp.tStartRefresh)
thisExp.addData('instruc_key_resp.stopped', instruc_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('experimental_stim_list.xlsx', selection='54:65'),
    seed=None, name='practice_loop')
thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop:
        exec('{} = thisPractice_loop[paramName]'.format(paramName))

for thisPractice_loop in practice_loop:
    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "focus"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    focusComponents = [text]
    for thisComponent in focusComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    focusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "focus"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = focusClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=focusClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in focusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "focus"-------
    for thisComponent in focusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_loop.addData('text.started', text.tStartRefresh)
    practice_loop.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "images"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(left_pic)
    image_2.setImage(right_pic)
    image_key_resp.keys = []
    image_key_resp.rt = []
    _image_key_resp_allKeys = []
    # keep track of which components have finished
    imagesComponents = [image, image_2, left_image_text, center_text, right_image_text, image_key_resp]
    for thisComponent in imagesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    imagesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "images"-------
    while continueRoutine:
        # get current time
        t = imagesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=imagesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        
        # *left_image_text* updates
        if left_image_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_image_text.frameNStart = frameN  # exact frame index
            left_image_text.tStart = t  # local t and not account for scr refresh
            left_image_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_image_text, 'tStartRefresh')  # time at next scr refresh
            left_image_text.setAutoDraw(True)
        
        # *center_text* updates
        if center_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            center_text.frameNStart = frameN  # exact frame index
            center_text.tStart = t  # local t and not account for scr refresh
            center_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(center_text, 'tStartRefresh')  # time at next scr refresh
            center_text.setAutoDraw(True)
        
        # *right_image_text* updates
        if right_image_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_image_text.frameNStart = frameN  # exact frame index
            right_image_text.tStart = t  # local t and not account for scr refresh
            right_image_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_image_text, 'tStartRefresh')  # time at next scr refresh
            right_image_text.setAutoDraw(True)
        
        # *image_key_resp* updates
        waitOnFlip = False
        if image_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_key_resp.frameNStart = frameN  # exact frame index
            image_key_resp.tStart = t  # local t and not account for scr refresh
            image_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_key_resp, 'tStartRefresh')  # time at next scr refresh
            image_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(image_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(image_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if image_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = image_key_resp.getKeys(keyList=['space', 'f', 'k'], waitRelease=False)
            _image_key_resp_allKeys.extend(theseKeys)
            if len(_image_key_resp_allKeys):
                image_key_resp.keys = _image_key_resp_allKeys[-1].name  # just the last key pressed
                image_key_resp.rt = _image_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in imagesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "images"-------
    for thisComponent in imagesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_loop.addData('image.started', image.tStartRefresh)
    practice_loop.addData('image.stopped', image.tStopRefresh)
    practice_loop.addData('image_2.started', image_2.tStartRefresh)
    practice_loop.addData('image_2.stopped', image_2.tStopRefresh)
    practice_loop.addData('left_image_text.started', left_image_text.tStartRefresh)
    practice_loop.addData('left_image_text.stopped', left_image_text.tStopRefresh)
    practice_loop.addData('center_text.started', center_text.tStartRefresh)
    practice_loop.addData('center_text.stopped', center_text.tStopRefresh)
    practice_loop.addData('right_image_text.started', right_image_text.tStartRefresh)
    practice_loop.addData('right_image_text.stopped', right_image_text.tStopRefresh)
    # check responses
    if image_key_resp.keys in ['', [], None]:  # No response was made
        image_key_resp.keys = None
    practice_loop.addData('image_key_resp.keys',image_key_resp.keys)
    if image_key_resp.keys != None:  # we had a response
        practice_loop.addData('image_key_resp.rt', image_key_resp.rt)
    practice_loop.addData('image_key_resp.started', image_key_resp.tStartRefresh)
    practice_loop.addData('image_key_resp.stopped', image_key_resp.tStopRefresh)
    # the Routine "images" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_loop'


# ------Prepare to start Routine "transition_screen"-------
continueRoutine = True
# update component parameters for each repeat
trans_key.keys = []
trans_key.rt = []
_trans_key_allKeys = []
# keep track of which components have finished
transition_screenComponents = [transition_text, trans_key]
for thisComponent in transition_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
transition_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "transition_screen"-------
while continueRoutine:
    # get current time
    t = transition_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=transition_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *transition_text* updates
    if transition_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        transition_text.frameNStart = frameN  # exact frame index
        transition_text.tStart = t  # local t and not account for scr refresh
        transition_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(transition_text, 'tStartRefresh')  # time at next scr refresh
        transition_text.setAutoDraw(True)
    
    # *trans_key* updates
    waitOnFlip = False
    if trans_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trans_key.frameNStart = frameN  # exact frame index
        trans_key.tStart = t  # local t and not account for scr refresh
        trans_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trans_key, 'tStartRefresh')  # time at next scr refresh
        trans_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trans_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trans_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trans_key.status == STARTED and not waitOnFlip:
        theseKeys = trans_key.getKeys(keyList=['space'], waitRelease=False)
        _trans_key_allKeys.extend(theseKeys)
        if len(_trans_key_allKeys):
            trans_key.keys = _trans_key_allKeys[-1].name  # just the last key pressed
            trans_key.rt = _trans_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in transition_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "transition_screen"-------
for thisComponent in transition_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('transition_text.started', transition_text.tStartRefresh)
thisExp.addData('transition_text.stopped', transition_text.tStopRefresh)
# check responses
if trans_key.keys in ['', [], None]:  # No response was made
    trans_key.keys = None
thisExp.addData('trans_key.keys',trans_key.keys)
if trans_key.keys != None:  # we had a response
    thisExp.addData('trans_key.rt', trans_key.rt)
thisExp.addData('trans_key.started', trans_key.tStartRefresh)
thisExp.addData('trans_key.stopped', trans_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "transition_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
experimental_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('experimental_stim_list.xlsx'),
    seed=None, name='experimental_loop')
thisExp.addLoop(experimental_loop)  # add the loop to the experiment
thisExperimental_loop = experimental_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExperimental_loop.rgb)
if thisExperimental_loop != None:
    for paramName in thisExperimental_loop:
        exec('{} = thisExperimental_loop[paramName]'.format(paramName))

for thisExperimental_loop in experimental_loop:
    currentLoop = experimental_loop
    # abbreviate parameter names if possible (e.g. rgb = thisExperimental_loop.rgb)
    if thisExperimental_loop != None:
        for paramName in thisExperimental_loop:
            exec('{} = thisExperimental_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "focus"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    focusComponents = [text]
    for thisComponent in focusComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    focusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "focus"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = focusClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=focusClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in focusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "focus"-------
    for thisComponent in focusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experimental_loop.addData('text.started', text.tStartRefresh)
    experimental_loop.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "images"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(left_pic)
    image_2.setImage(right_pic)
    image_key_resp.keys = []
    image_key_resp.rt = []
    _image_key_resp_allKeys = []
    # keep track of which components have finished
    imagesComponents = [image, image_2, left_image_text, center_text, right_image_text, image_key_resp]
    for thisComponent in imagesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    imagesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "images"-------
    while continueRoutine:
        # get current time
        t = imagesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=imagesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        
        # *left_image_text* updates
        if left_image_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_image_text.frameNStart = frameN  # exact frame index
            left_image_text.tStart = t  # local t and not account for scr refresh
            left_image_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_image_text, 'tStartRefresh')  # time at next scr refresh
            left_image_text.setAutoDraw(True)
        
        # *center_text* updates
        if center_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            center_text.frameNStart = frameN  # exact frame index
            center_text.tStart = t  # local t and not account for scr refresh
            center_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(center_text, 'tStartRefresh')  # time at next scr refresh
            center_text.setAutoDraw(True)
        
        # *right_image_text* updates
        if right_image_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_image_text.frameNStart = frameN  # exact frame index
            right_image_text.tStart = t  # local t and not account for scr refresh
            right_image_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_image_text, 'tStartRefresh')  # time at next scr refresh
            right_image_text.setAutoDraw(True)
        
        # *image_key_resp* updates
        waitOnFlip = False
        if image_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_key_resp.frameNStart = frameN  # exact frame index
            image_key_resp.tStart = t  # local t and not account for scr refresh
            image_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_key_resp, 'tStartRefresh')  # time at next scr refresh
            image_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(image_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(image_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if image_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = image_key_resp.getKeys(keyList=['space', 'f', 'k'], waitRelease=False)
            _image_key_resp_allKeys.extend(theseKeys)
            if len(_image_key_resp_allKeys):
                image_key_resp.keys = _image_key_resp_allKeys[-1].name  # just the last key pressed
                image_key_resp.rt = _image_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in imagesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "images"-------
    for thisComponent in imagesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experimental_loop.addData('image.started', image.tStartRefresh)
    experimental_loop.addData('image.stopped', image.tStopRefresh)
    experimental_loop.addData('image_2.started', image_2.tStartRefresh)
    experimental_loop.addData('image_2.stopped', image_2.tStopRefresh)
    experimental_loop.addData('left_image_text.started', left_image_text.tStartRefresh)
    experimental_loop.addData('left_image_text.stopped', left_image_text.tStopRefresh)
    experimental_loop.addData('center_text.started', center_text.tStartRefresh)
    experimental_loop.addData('center_text.stopped', center_text.tStopRefresh)
    experimental_loop.addData('right_image_text.started', right_image_text.tStartRefresh)
    experimental_loop.addData('right_image_text.stopped', right_image_text.tStopRefresh)
    # check responses
    if image_key_resp.keys in ['', [], None]:  # No response was made
        image_key_resp.keys = None
    experimental_loop.addData('image_key_resp.keys',image_key_resp.keys)
    if image_key_resp.keys != None:  # we had a response
        experimental_loop.addData('image_key_resp.rt', image_key_resp.rt)
    experimental_loop.addData('image_key_resp.started', image_key_resp.tStartRefresh)
    experimental_loop.addData('image_key_resp.stopped', image_key_resp.tStopRefresh)
    # the Routine "images" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'experimental_loop'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [end_text]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

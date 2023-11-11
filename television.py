"""
Filename: television.py
Author: Talieisn Reese
Version: 1.2
Date: 11/10/2023
Purpose: Go outside
"""
class Television:
  """
  A class that represents a television. Far less interesting than the real thing.
  """
  __MIN_VOLUME = 0
  __MAX_VOLUME = 2
  __MIN_CHANNEL = 0
  __MAX_CHANNEL = 3
  def __init__(self):
    """ If you want a Television, you must first BEND REALITY TO YOUR WHIMS AND CREATE IT EX NIHILO"""
    self.__status = False
    self.__muted = False
    self.__volume = Television.__MIN_VOLUME
    self.__channel = Television.__MIN_CHANNEL
  def power(self):
    """Turn the TV off or on."""
    if self.__status:
      self.__status = False
    else:
      self.__status = True
  def mute(self):
    """Stop the volume. Only works if TV is ON"""
    if self.__status == True:
      if self.__muted:
        self.__muted = False
      else:
        self.__muted = True
  def channel_up(self):
    """Iterate channel up by one. If channel is at maximum, loop back to minimum. Only works if TV is ON"""
    if self.__status == True:
      if self.__channel == Television.__MAX_CHANNEL:
        self.__channel = Television.__MIN_CHANNEL
      else:
        self.__channel += 1
  def channel_down(self):
    """Iterate channel down by one. If channel is at minimum, loop back to maximum. Only works if TV is ON"""
    if self.__status == True:
      if self.__channel == Television.__MIN_CHANNEL:
        self.__channel = Television.__MAX_CHANNEL
      else:
        self.__channel -= 1
  def volume_up(self):
    """Iterate volume up by one. If volume is at maximum, don't iterate any longer. Automatically un-mutes the TV. Only works if TV is ON"""
    if self.__status == True:
      if self.__volume < Television.__MAX_VOLUME:
        self.__volume += 1
        self.__muted = False
  def volume_down(self):
    """Iterate volume down by one. If volume is at minimum, don't iterate any longer. Automatically un-mutes the TV. Only works if TV is ON"""
    if self.__status == True:
      if self.__volume > Television.__MIN_VOLUME:
        self.__volume -= 1
        self.__muted = False
  def __str__(self):
    """Display stats of the TV"""
    if self.__muted == False:
      return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
    else:
      return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {0}"
